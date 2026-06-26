from __future__ import annotations

import argparse
import json
import logging
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def read_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("phase8_robustness_diagnosis")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    import torch

    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def validate_scope(cfg: dict) -> None:
    task = cfg["task"]
    if task["target_variable"] != "speed" or task["target_column"] != "current_speed":
        raise ValueError("Phase 8 is restricted to speed/current_speed.")
    if task["input_feature_group"] != "speed_only" or task["input_features"] != ["current_speed"]:
        raise ValueError("Phase 8 is restricted to speed_only input.")
    if sorted(task["horizons_hours"]) != [1, 3, 6]:
        raise ValueError("Phase 8 horizons must be [1, 3, 6].")
    if cfg["model"]["name"] != "TCN":
        raise ValueError("Phase 8 evaluates TCN checkpoints only.")


def standardize_panel_columns(panel: pd.DataFrame) -> pd.DataFrame:
    panel = panel.copy()
    if "point_id" not in panel.columns and "node_id" in panel.columns:
        panel["point_id"] = panel["node_id"]
    if "timestamp" not in panel.columns and "time_bin" in panel.columns:
        panel["timestamp"] = pd.to_datetime(panel["time_bin"])
    elif "timestamp" in panel.columns:
        panel["timestamp"] = pd.to_datetime(panel["timestamp"])
    if "hour_of_day" not in panel.columns and "hour" in panel.columns:
        panel["hour_of_day"] = panel["hour"]
    if "weekend_flag" not in panel.columns and "day_of_week" in panel.columns:
        panel["weekend_flag"] = (pd.to_numeric(panel["day_of_week"], errors="coerce").fillna(0) >= 5).astype(int)
    return panel


def load_panel(path: Path, cfg: dict) -> pd.DataFrame:
    panel = pd.read_csv(path)
    panel = standardize_panel_columns(panel)
    required = {
        "point_id",
        "timestamp",
        cfg["task"]["target_column"],
        "volatility_tti_6h",
        "hour_of_day",
        *cfg["task"]["input_features"],
    }
    missing = required - set(panel.columns)
    if missing:
        raise ValueError(f"Panel file is missing columns after standardization: {sorted(missing)}")
    return panel.sort_values(["point_id", "timestamp"]).reset_index(drop=True)


def build_point_arrays(panel: pd.DataFrame, cfg: dict) -> dict[str, dict[str, np.ndarray]]:
    target_col = cfg["task"]["target_column"]
    feature = cfg["task"]["input_features"][0]
    global_mean = float(panel[target_col].mean())
    out: dict[str, dict[str, np.ndarray]] = {}
    for point_id, g in panel.groupby("point_id", sort=True):
        g = g.sort_values("timestamp").reset_index(drop=True)
        point_id = str(point_id)
        point_mean = float(g[target_col].mean()) if g[target_col].notna().any() else global_mean
        speed = pd.to_numeric(g[feature], errors="coerce").to_numpy(dtype=float)
        speed = np.where(np.isfinite(speed), speed, point_mean)
        out[point_id] = {
            "timestamp": g["timestamp"].to_numpy(),
            "speed": speed.astype(np.float32),
            "target": pd.to_numeric(g[target_col], errors="coerce").to_numpy(dtype=float),
            "volatility_tti_6h": pd.to_numeric(g["volatility_tti_6h"], errors="coerce").fillna(0).to_numpy(dtype=float),
            "hour_of_day": pd.to_numeric(g["hour_of_day"], errors="coerce").fillna(0).to_numpy(dtype=int),
        }
    return out


def time_to_index(times: np.ndarray, timestamp: pd.Timestamp) -> int:
    idx = np.searchsorted(times, np.datetime64(timestamp), side="left")
    if idx >= len(times) or times[idx] != np.datetime64(timestamp):
        raise KeyError(f"Timestamp {timestamp} not found in point timeline")
    return int(idx)


def checkpoint_paths(cfg: dict, history: int, horizon: int) -> tuple[Path, Path]:
    root = Path(cfg["paths"]["checkpoints"])
    base = f"phase7_tcn_speed_only_h{history}_y{horizon}"
    return root / f"{base}.pt", root / f"{base}_scaler.json"


def load_windows(cfg: dict, history: int, horizon: int, logger: logging.Logger) -> pd.DataFrame:
    limit = int(cfg["task"]["max_test_samples"])
    frames = []
    kept = 0
    usecols = [
        "window_id",
        "point_id",
        "input_start_time",
        "input_end_time",
        "target_start_time",
        "target_end_time",
        "history_hours",
        "horizon_hours",
        "split",
        "target_variable",
        "input_observed_ratio",
        "target_observed_ratio",
        "is_main_forecast",
        "is_extended_horizon",
    ]
    parse_dates = ["input_start_time", "input_end_time", "target_start_time", "target_end_time"]
    for chunk in pd.read_csv(
        cfg["paths"]["window_index"],
        usecols=usecols,
        parse_dates=parse_dates,
        chunksize=int(cfg["task"]["window_chunksize"]),
    ):
        mask = (
            chunk["split"].eq(cfg["task"]["test_split"])
            & chunk["target_variable"].eq(cfg["task"]["target_variable"])
            & chunk["history_hours"].eq(int(history))
            & chunk["horizon_hours"].eq(int(horizon))
            & chunk["is_main_forecast"].eq(1)
            & chunk["is_extended_horizon"].eq(0)
            & (chunk["input_observed_ratio"] >= float(cfg["task"]["min_input_observed_ratio"]))
            & (chunk["target_observed_ratio"] >= float(cfg["task"]["min_target_observed_ratio"]))
        )
        filtered = chunk.loc[mask].copy()
        if filtered.empty:
            continue
        take = filtered.head(limit - kept)
        kept += len(take)
        frames.append(take)
        if kept >= limit:
            break
    if not frames:
        raise ValueError(f"No test windows found for history={history}, horizon={horizon}")
    logger.info("Loaded test windows for history=%sh horizon=%sh samples=%s", history, horizon, kept)
    return pd.concat(frames, ignore_index=True)


@dataclass
class EvalSet:
    x: np.ndarray
    y: np.ndarray
    meta: pd.DataFrame
    history_hours: int
    horizon_hours: int


@dataclass
class Scaler:
    x_mean: float
    x_std: float
    y_mean: float
    y_std: float

    def transform_x(self, x: np.ndarray) -> np.ndarray:
        return ((x - self.x_mean) / self.x_std).astype(np.float32)

    def inverse_y(self, y_scaled: np.ndarray) -> np.ndarray:
        return y_scaled * self.y_std + self.y_mean


def load_scaler(path: Path) -> Scaler:
    data = json.loads(path.read_text(encoding="utf-8"))
    return Scaler(
        x_mean=float(data["x_mean"][0]),
        x_std=float(data["x_std"][0]) if float(data["x_std"][0]) > 1e-8 else 1.0,
        y_mean=float(data["y_mean"]),
        y_std=float(data["y_std"]) if float(data["y_std"]) > 1e-8 else 1.0,
    )


def hour_group(hour: int, cfg: dict) -> str:
    if hour in set(cfg["diagnostics"]["am_peak_hours"]):
        return "am_peak"
    if hour in set(cfg["diagnostics"]["pm_peak_hours"]):
        return "pm_peak"
    return "off_peak"


def build_eval_set(windows: pd.DataFrame, point_arrays: dict[str, dict[str, np.ndarray]], cfg: dict, history: int, horizon: int) -> EvalSet:
    xs, ys, rows = [], [], []
    for row in windows.itertuples(index=False):
        point_id = str(row.point_id)
        arrays = point_arrays[point_id]
        times = arrays["timestamp"]
        input_start = time_to_index(times, row.input_start_time)
        input_end = time_to_index(times, row.input_end_time)
        target_start = time_to_index(times, row.target_start_time)
        target_end = time_to_index(times, row.target_end_time)
        if input_end - input_start + 1 != history:
            continue
        x = arrays["speed"][input_start : input_end + 1].reshape(-1, 1)
        target = arrays["target"][target_start : target_end + 1]
        target = target[np.isfinite(target)]
        if len(target) == 0:
            continue
        input_hour = int(arrays["hour_of_day"][input_end])
        input_volatility = float(np.nanmean(arrays["volatility_tti_6h"][input_start : input_end + 1]))
        xs.append(x.astype(np.float32))
        ys.append(float(target.mean()))
        rows.append(
            {
                "window_id": int(row.window_id),
                "point_id": point_id,
                "input_start_time": row.input_start_time,
                "input_end_time": row.input_end_time,
                "target_start_time": row.target_start_time,
                "target_end_time": row.target_end_time,
                "history_hours": history,
                "horizon_hours": horizon,
                "input_observed_ratio": float(row.input_observed_ratio),
                "target_observed_ratio": float(row.target_observed_ratio),
                "input_volatility_tti_6h": input_volatility,
                "input_end_hour": input_hour,
                "hour_group": hour_group(input_hour, cfg),
            }
        )
    if not xs:
        raise ValueError(f"No eval samples could be built for history={history}, horizon={horizon}")
    return EvalSet(np.stack(xs).astype(np.float32), np.asarray(ys, dtype=np.float32), pd.DataFrame(rows), history, horizon)


def build_tcn(input_size: int, cfg: dict):
    import torch
    import torch.nn as nn

    class Chomp1d(nn.Module):
        def __init__(self, chomp_size: int) -> None:
            super().__init__()
            self.chomp_size = chomp_size

        def forward(self, x):
            return x[:, :, : -self.chomp_size].contiguous() if self.chomp_size > 0 else x

    class TemporalBlock(nn.Module):
        def __init__(self, in_channels: int, out_channels: int, kernel_size: int, dilation: int, dropout: float) -> None:
            super().__init__()
            padding = (kernel_size - 1) * dilation
            self.net = nn.Sequential(
                nn.Conv1d(in_channels, out_channels, kernel_size, padding=padding, dilation=dilation),
                Chomp1d(padding),
                nn.ReLU(),
                nn.Dropout(dropout),
                nn.Conv1d(out_channels, out_channels, kernel_size, padding=padding, dilation=dilation),
                Chomp1d(padding),
                nn.ReLU(),
                nn.Dropout(dropout),
            )
            self.downsample = nn.Conv1d(in_channels, out_channels, 1) if in_channels != out_channels else nn.Identity()

        def forward(self, x):
            return torch.relu(self.net(x) + self.downsample(x))

    class Model(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            channels = [int(c) for c in cfg["model"]["channels"]]
            kernel_size = int(cfg["model"]["kernel_size"])
            dropout = float(cfg["model"]["dropout"])
            layers = []
            in_ch = input_size
            for idx, out_ch in enumerate(channels):
                layers.append(TemporalBlock(in_ch, out_ch, kernel_size, 2**idx, dropout))
                in_ch = out_ch
            self.tcn = nn.Sequential(*layers)
            self.head = nn.Linear(in_ch, 1)

        def forward(self, x):
            x = x.transpose(1, 2)
            out = self.tcn(x)
            return self.head(out[:, :, -1])

    return Model()


def load_model(path: Path, cfg: dict, device: str):
    import torch

    model = build_tcn(1, cfg).to(device)
    state = torch.load(path, map_location=device, weights_only=False)
    model.load_state_dict(state["state_dict"])
    model.eval()
    return model


def device_name(cfg: dict) -> str:
    import torch

    device_cfg = cfg["model"]["device"]
    return "cuda" if device_cfg == "auto" and torch.cuda.is_available() else ("cpu" if device_cfg == "auto" else device_cfg)


def predict(model, x_original: np.ndarray, scaler: Scaler, device: str, batch_size: int = 512) -> np.ndarray:
    import torch

    x_scaled = scaler.transform_x(x_original)
    preds = []
    with torch.no_grad():
        for start in range(0, len(x_scaled), batch_size):
            xb = torch.from_numpy(x_scaled[start : start + batch_size]).to(device)
            pred = model(xb).detach().cpu().numpy().reshape(-1)
            preds.append(scaler.inverse_y(pred))
    return np.concatenate(preds)


def metric_dict(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    mask = np.isfinite(y_true) & np.isfinite(y_pred)
    yt = y_true[mask].astype(float)
    yp = y_pred[mask].astype(float)
    err = yp - yt
    denom = np.abs(yt) + np.abs(yp)
    safe = denom > 1e-8
    return {
        "n": int(len(yt)),
        "MAE": float(np.abs(err).mean()),
        "RMSE": float(np.sqrt(np.square(err).mean())),
        "sMAPE": float((2 * np.abs(err[safe]) / denom[safe]).mean()) if safe.any() else np.nan,
    }


def attach_errors(eval_set: EvalSet, y_pred: np.ndarray) -> pd.DataFrame:
    out = eval_set.meta.copy()
    out["y_true"] = eval_set.y
    out["y_pred"] = y_pred
    out["error"] = out["y_pred"] - out["y_true"]
    out["absolute_error"] = out["error"].abs()
    return out


def summarize_group(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    rows = []
    for key, g in df.groupby(group_cols, dropna=False):
        values = key if isinstance(key, tuple) else (key,)
        row = {col: value for col, value in zip(group_cols, values)}
        row.update(metric_dict(g["y_true"].to_numpy(), g["y_pred"].to_numpy()))
        rows.append(row)
    return pd.DataFrame(rows)


def add_rank_bins(df: pd.DataFrame, column: str, out_col: str) -> pd.Series:
    ranked = df[column].rank(method="first")
    try:
        return pd.qcut(ranked, q=4, labels=["q1_low", "q2_mid_low", "q3_mid_high", "q4_high"])
    except ValueError:
        return pd.Series(["single_bin"] * len(df), index=df.index)


def apply_noise(x: np.ndarray, level: float, scaler: Scaler, seed: int) -> np.ndarray:
    if level == 0:
        return x.copy()
    rng = np.random.default_rng(seed)
    return (x + rng.normal(0.0, level * scaler.x_std, size=x.shape)).astype(np.float32)


def forward_fill_rows(x: np.ndarray, fallback: float) -> np.ndarray:
    out = x.copy()
    for i in range(out.shape[0]):
        last = fallback
        for t in range(out.shape[1]):
            if np.isfinite(out[i, t, 0]):
                last = out[i, t, 0]
            else:
                out[i, t, 0] = last
    return out.astype(np.float32)


def apply_missingness(x: np.ndarray, level: float, fallback: float, seed: int) -> np.ndarray:
    if level == 0:
        return x.copy()
    rng = np.random.default_rng(seed)
    out = x.copy()
    mask = rng.random(size=out.shape[:2]) < level
    out[mask, 0] = np.nan
    return forward_fill_rows(out, fallback)


def dataframe_to_markdown(df: pd.DataFrame, max_rows: int = 100) -> str:
    if df.empty:
        return "_No rows._"
    view = df.head(max_rows).copy()
    cols = list(view.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    if len(df) > max_rows:
        lines.append(f"\n_Showing first {max_rows} of {len(df)} rows._")
    return "\n".join(lines)


def write_report(cfg: dict) -> None:
    out = Path(cfg["paths"]["output_tables"])
    report_path = Path(cfg["paths"]["reports"]) / "phase8_robustness_diagnosis_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    metrics = pd.read_csv(out / "phase8_robustness_metrics.csv")
    input_bins = pd.read_csv(out / "phase8_error_by_input_observed_ratio.csv")
    volatility = pd.read_csv(out / "phase8_error_by_volatility.csv")
    noise = pd.read_csv(out / "phase8_noise_stress_metrics.csv")
    missing = pd.read_csv(out / "phase8_missingness_stress_metrics.csv")
    lines = [
        "# Phase 8 Robustness And Difficult-Sample Diagnosis Report",
        "",
        "Phase 8 evaluates existing Phase 7 TCN speed-only checkpoints. No model parameters are updated.",
        "",
        "## Base Robustness Metrics",
        dataframe_to_markdown(metrics),
        "",
        "## Input Observed Ratio Stratification",
        dataframe_to_markdown(input_bins),
        "",
        "## Volatility Stratification",
        dataframe_to_markdown(volatility),
        "",
        "## Noise Stress Test",
        dataframe_to_markdown(noise),
        "",
        "## Missingness Stress Test",
        dataframe_to_markdown(missing),
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase8_robustness_diagnosis.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    validate_scope(cfg)
    set_seed(int(cfg["project"]["random_seed"]))

    for path_key in ["output_tables", "output_logs", "reports"]:
        Path(cfg["paths"][path_key]).mkdir(parents=True, exist_ok=True)
    logger = setup_logger(Path(cfg["paths"]["output_logs"]) / "phase8_robustness_diagnosis.log")
    logger.info("Starting Phase 8 robustness diagnosis")

    try:
        import torch

        logger.info("PyTorch version: %s", torch.__version__)
    except ImportError as exc:
        raise ImportError("Phase 8 requires PyTorch in the configured environment.") from exc

    device = device_name(cfg)
    panel = load_panel(Path(cfg["paths"]["panel_1h"]), cfg)
    point_arrays = build_point_arrays(panel, cfg)
    out_tables = Path(cfg["paths"]["output_tables"])

    base_rows = []
    all_errors = []
    noise_rows = []
    missing_rows = []
    runtime_rows = []
    for horizon in [int(h) for h in cfg["task"]["horizons_hours"]]:
        history = int(cfg["task"]["best_history_by_horizon"][horizon])
        ckpt_path, scaler_path = checkpoint_paths(cfg, history, horizon)
        start_time = time.perf_counter()
        scaler = load_scaler(scaler_path)
        model = load_model(ckpt_path, cfg, device)
        windows = load_windows(cfg, history, horizon, logger)
        eval_set = build_eval_set(windows, point_arrays, cfg, history, horizon)

        pred = predict(model, eval_set.x, scaler, device)
        metrics = metric_dict(eval_set.y, pred)
        base_rows.append(
            {
                "history_hours": history,
                "horizon_hours": horizon,
                "checkpoint": str(ckpt_path),
                **metrics,
            }
        )
        errors = attach_errors(eval_set, pred)
        all_errors.append(errors)
        logger.info(
            "base_eval history=%sh horizon=%sh checkpoint=%s samples=%s MAE=%.6f RMSE=%.6f sMAPE=%.6f elapsed_sec=%.2f device=%s",
            history,
            horizon,
            ckpt_path,
            metrics["n"],
            metrics["MAE"],
            metrics["RMSE"],
            metrics["sMAPE"],
            time.perf_counter() - start_time,
            device,
        )

        for level in [float(v) for v in cfg["stress_tests"]["noise_levels"]]:
            noisy_x = apply_noise(eval_set.x, level, scaler, int(cfg["project"]["random_seed"]) + horizon + int(level * 1000))
            noisy_pred = predict(model, noisy_x, scaler, device)
            m = metric_dict(eval_set.y, noisy_pred)
            noise_rows.append({"history_hours": history, "horizon_hours": horizon, "noise_level": level, **m})
            logger.info("noise_eval history=%sh horizon=%sh level=%.3f MAE=%.6f RMSE=%.6f sMAPE=%.6f", history, horizon, level, m["MAE"], m["RMSE"], m["sMAPE"])

        for level in [float(v) for v in cfg["stress_tests"]["missing_levels"]]:
            masked_x = apply_missingness(eval_set.x, level, scaler.x_mean, int(cfg["project"]["random_seed"]) + 10000 + horizon + int(level * 1000))
            masked_pred = predict(model, masked_x, scaler, device)
            m = metric_dict(eval_set.y, masked_pred)
            missing_rows.append({"history_hours": history, "horizon_hours": horizon, "missing_level": level, **m})
            logger.info("missing_eval history=%sh horizon=%sh level=%.3f MAE=%.6f RMSE=%.6f sMAPE=%.6f", history, horizon, level, m["MAE"], m["RMSE"], m["sMAPE"])

        runtime_rows.append(
            {
                "history_hours": history,
                "horizon_hours": horizon,
                "checkpoint": str(ckpt_path),
                "scaler_metadata": str(scaler_path),
                "samples": len(eval_set.y),
                "seconds": time.perf_counter() - start_time,
                "device": device,
            }
        )

    base = pd.DataFrame(base_rows)
    err = pd.concat(all_errors, ignore_index=True)
    err["input_observed_ratio_bin"] = add_rank_bins(err, "input_observed_ratio", "input_observed_ratio_bin")
    err["target_observed_ratio_bin"] = add_rank_bins(err, "target_observed_ratio", "target_observed_ratio_bin")
    err["volatility_bin"] = add_rank_bins(err, "input_volatility_tti_6h", "volatility_bin")

    base.to_csv(out_tables / "phase8_robustness_metrics.csv", index=False, encoding="utf-8-sig")
    summarize_group(err, ["horizon_hours", "input_observed_ratio_bin"]).to_csv(out_tables / "phase8_error_by_input_observed_ratio.csv", index=False, encoding="utf-8-sig")
    summarize_group(err, ["horizon_hours", "target_observed_ratio_bin"]).to_csv(out_tables / "phase8_error_by_target_observed_ratio.csv", index=False, encoding="utf-8-sig")
    summarize_group(err, ["horizon_hours", "volatility_bin"]).to_csv(out_tables / "phase8_error_by_volatility.csv", index=False, encoding="utf-8-sig")
    summarize_group(err, ["horizon_hours", "hour_group"]).to_csv(out_tables / "phase8_error_by_hour_group.csv", index=False, encoding="utf-8-sig")
    summarize_group(err, ["horizon_hours", "point_id"]).to_csv(out_tables / "phase8_error_by_point.csv", index=False, encoding="utf-8-sig")
    err.sort_values("absolute_error", ascending=False).head(int(cfg["diagnostics"]["top_difficult_samples"])).to_csv(out_tables / "phase8_top_difficult_samples.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(noise_rows).to_csv(out_tables / "phase8_noise_stress_metrics.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(missing_rows).to_csv(out_tables / "phase8_missingness_stress_metrics.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(runtime_rows).to_csv(out_tables / "phase8_runtime_summary.csv", index=False, encoding="utf-8-sig")
    write_report(cfg)
    logger.info("Phase 8 robustness diagnosis completed")


if __name__ == "__main__":
    main()
