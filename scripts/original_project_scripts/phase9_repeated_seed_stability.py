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
    logger = logging.getLogger("phase9_seed_stability")
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
    torch.backends.cudnn.deterministic = True


def validate_scope(cfg: dict) -> None:
    task = cfg["task"]
    if task["model"] != "TCN":
        raise ValueError("Phase 9 is restricted to TCN.")
    if task["input_feature_group"] != "speed_only" or task["input_features"] != ["current_speed"]:
        raise ValueError("Phase 9 is restricted to speed_only input.")
    if task["target_variable"] != "speed" or task["target_column"] != "current_speed":
        raise ValueError("Phase 9 is restricted to speed/current_speed.")
    if sorted(task["horizons_hours"]) != [1, 3, 6]:
        raise ValueError("Phase 9 horizons must be [1, 3, 6].")
    if sorted(int(seed) for seed in cfg["training"]["seeds"]) != [42, 2025, 20260623]:
        raise ValueError("Phase 9 seeds must be [42, 2025, 20260623].")


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
    required = {"point_id", "timestamp", cfg["task"]["target_column"], *cfg["task"]["input_features"]}
    missing = required - set(panel.columns)
    if missing:
        raise ValueError(f"Panel file is missing columns after standardization: {sorted(missing)}")
    return panel.sort_values(["point_id", "timestamp"]).reset_index(drop=True)


def build_point_arrays(panel: pd.DataFrame, cfg: dict) -> dict[str, dict[str, np.ndarray]]:
    target_col = cfg["task"]["target_column"]
    feature = cfg["task"]["input_features"][0]
    global_target_mean = float(panel[target_col].mean())
    out: dict[str, dict[str, np.ndarray]] = {}
    for point_id, g in panel.groupby("point_id", sort=True):
        g = g.sort_values("timestamp").reset_index(drop=True)
        point_id = str(point_id)
        point_target_mean = float(g[target_col].mean()) if g[target_col].notna().any() else global_target_mean
        feature_values = pd.to_numeric(g[feature], errors="coerce").to_numpy(dtype=float)
        feature_values = np.where(np.isfinite(feature_values), feature_values, point_target_mean)
        out[point_id] = {
            "timestamp": g["timestamp"].to_numpy(),
            "target": pd.to_numeric(g[target_col], errors="coerce").to_numpy(dtype=float),
            feature: feature_values.astype(np.float32),
        }
    return out


def time_to_index(times: np.ndarray, timestamp: pd.Timestamp) -> int:
    idx = np.searchsorted(times, np.datetime64(timestamp), side="left")
    if idx >= len(times) or times[idx] != np.datetime64(timestamp):
        raise KeyError(f"Timestamp {timestamp} not found in point timeline")
    return int(idx)


def load_windows(cfg: dict, history: int, horizon: int, logger: logging.Logger) -> pd.DataFrame:
    limits = {
        "train": int(cfg["data"]["max_train_samples"]),
        "val": int(cfg["data"]["max_val_samples"]),
        "test": int(cfg["data"]["max_test_samples"]),
    }
    kept = {split: 0 for split in limits}
    frames = []
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
        chunksize=int(cfg["data"]["window_chunksize"]),
    ):
        mask = (
            chunk["target_variable"].eq(cfg["task"]["target_variable"])
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
        for split, limit in limits.items():
            if kept[split] >= limit:
                continue
            part = filtered[filtered["split"].eq(split)]
            if part.empty:
                continue
            take = part.head(limit - kept[split])
            kept[split] += len(take)
            frames.append(take)
        if all(kept[s] >= limits[s] for s in limits):
            break
    if not frames:
        raise ValueError(f"No windows found for history={history}, horizon={horizon}")
    logger.info("Loaded windows for history=%sh horizon=%sh: %s", history, horizon, kept)
    return pd.concat(frames, ignore_index=True)


@dataclass
class SampleSet:
    x: np.ndarray
    y: np.ndarray
    split: np.ndarray
    history_hours: int
    horizon_hours: int


@dataclass
class Standardizer:
    x_mean: np.ndarray
    x_std: np.ndarray
    y_mean: float
    y_std: float

    def transform_x(self, x: np.ndarray) -> np.ndarray:
        return ((x - self.x_mean.reshape(1, 1, -1)) / self.x_std.reshape(1, 1, -1)).astype(np.float32)

    def transform_y(self, y: np.ndarray) -> np.ndarray:
        return ((y - self.y_mean) / self.y_std).astype(np.float32)

    def inverse_y(self, y_scaled: np.ndarray) -> np.ndarray:
        return y_scaled * self.y_std + self.y_mean

    def to_jsonable(self, features: list[str]) -> dict:
        return {
            "features": features,
            "x_mean": self.x_mean.tolist(),
            "x_std": self.x_std.tolist(),
            "y_mean": self.y_mean,
            "y_std": self.y_std,
        }


def build_samples(windows: pd.DataFrame, point_arrays: dict[str, dict[str, np.ndarray]], cfg: dict, history: int, horizon: int) -> SampleSet:
    feature = cfg["task"]["input_features"][0]
    xs, ys, splits = [], [], []
    for row in windows.itertuples(index=False):
        point_id = str(row.point_id)
        arrays = point_arrays[point_id]
        times = arrays["timestamp"]
        input_start = time_to_index(times, row.input_start_time)
        input_end = time_to_index(times, row.input_end_time)
        target_start = time_to_index(times, row.target_start_time)
        target_end = time_to_index(times, row.target_end_time)
        if input_end - input_start + 1 != int(history):
            continue
        target = arrays["target"][target_start : target_end + 1]
        target = target[np.isfinite(target)]
        if len(target) == 0:
            continue
        xs.append(arrays[feature][input_start : input_end + 1].reshape(-1, 1).astype(np.float32))
        ys.append(float(target.mean()))
        splits.append(str(row.split))
    if not xs:
        raise ValueError(f"No samples could be built for history={history}, horizon={horizon}")
    return SampleSet(np.stack(xs).astype(np.float32), np.asarray(ys, dtype=np.float32), np.asarray(splits), history, horizon)


def fit_standardizer(samples: SampleSet) -> Standardizer:
    train = samples.split == "train"
    x_train = samples.x[train]
    y_train = samples.y[train]
    x_flat = x_train.reshape(-1, x_train.shape[-1])
    x_mean = x_flat.mean(axis=0)
    x_std = x_flat.std(axis=0)
    x_std = np.where(x_std < 1e-6, 1.0, x_std)
    y_mean = float(y_train.mean())
    y_std = float(y_train.std())
    if y_std < 1e-6:
        y_std = 1.0
    return Standardizer(x_mean.astype(np.float32), x_std.astype(np.float32), y_mean, y_std)


def make_loader(x: np.ndarray, y: np.ndarray, batch_size: int, use_order_permutation: bool):
    import torch
    from torch.utils.data import DataLoader, TensorDataset

    ds = TensorDataset(torch.from_numpy(x), torch.from_numpy(y.reshape(-1, 1)))
    return DataLoader(ds, batch_size=batch_size, shuffle=use_order_permutation, num_workers=0)


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
            mcfg = cfg["models"]["tcn"]
            layers = []
            in_ch = input_size
            for idx, out_ch in enumerate([int(c) for c in mcfg["channels"]]):
                layers.append(TemporalBlock(in_ch, out_ch, int(mcfg["kernel_size"]), 2**idx, float(mcfg["dropout"])))
                in_ch = out_ch
            self.tcn = nn.Sequential(*layers)
            self.head = nn.Linear(in_ch, 1)

        def forward(self, x):
            x = x.transpose(1, 2)
            out = self.tcn(x)
            return self.head(out[:, :, -1])

    return Model()


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


def predict_original_units(model, loader, device: str, scaler: Standardizer) -> tuple[np.ndarray, np.ndarray]:
    import torch

    model.eval()
    preds, truths = [], []
    with torch.no_grad():
        for xb, yb in loader:
            pred = model(xb.to(device)).detach().cpu().numpy().reshape(-1)
            preds.append(scaler.inverse_y(pred))
            truths.append(scaler.inverse_y(yb.numpy().reshape(-1)))
    return np.concatenate(truths), np.concatenate(preds)


def cuda_memory_text(device: str) -> str:
    if device != "cuda":
        return "NA"
    import torch

    allocated = torch.cuda.memory_allocated() / 1048576
    reserved = torch.cuda.memory_reserved() / 1048576
    return f"allocated_mb={allocated:.1f},reserved_mb={reserved:.1f}"


def train_once(samples: SampleSet, cfg: dict, seed: int, logger: logging.Logger, checkpoint_dir: Path):
    import torch
    import torch.nn as nn

    set_seed(seed)
    scaler = fit_standardizer(samples)
    x_scaled = scaler.transform_x(samples.x)
    y_scaled = scaler.transform_y(samples.y)
    train = samples.split == "train"
    val = samples.split == "val"
    test = samples.split == "test"
    device_cfg = cfg["training"]["device"]
    device = "cuda" if device_cfg == "auto" and torch.cuda.is_available() else ("cpu" if device_cfg == "auto" else device_cfg)
    batch_size = int(cfg["training"]["batch_size"])
    train_loader = make_loader(x_scaled[train], y_scaled[train], batch_size, True)
    val_loader = make_loader(x_scaled[val], y_scaled[val], batch_size, False)
    test_loader = make_loader(x_scaled[test], y_scaled[test], batch_size, False)
    model = build_tcn(x_scaled.shape[2], cfg).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(cfg["training"]["learning_rate"]), weight_decay=float(cfg["training"]["weight_decay"]))
    criterion = nn.MSELoss()
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = checkpoint_dir / f"phase9_tcn_speed_only_seed{seed}_h{samples.history_hours}_y{samples.horizon_hours}.pt"
    scaler_path = checkpoint_dir / f"phase9_tcn_speed_only_seed{seed}_h{samples.history_hours}_y{samples.horizon_hours}_scaler.json"

    best_val_mae = float("inf")
    best_epoch = 0
    stale_epochs = 0
    start = time.perf_counter()
    for epoch in range(1, int(cfg["training"]["epochs"]) + 1):
        model.train()
        loss_sum = 0.0
        seen = 0
        for xb, yb in train_loader:
            xb = xb.to(device)
            yb = yb.to(device)
            optimizer.zero_grad(set_to_none=True)
            pred = model(xb)
            loss = criterion(pred, yb)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), float(cfg["training"]["gradient_clip_norm"]))
            optimizer.step()
            loss_sum += float(loss.item()) * len(xb)
            seen += len(xb)
        train_loss = loss_sum / max(seen, 1)
        val_true, val_pred = predict_original_units(model, val_loader, device, scaler)
        val_metrics = metric_dict(val_true, val_pred)
        if val_metrics["MAE"] < best_val_mae:
            best_val_mae = val_metrics["MAE"]
            best_epoch = epoch
            stale_epochs = 0
            torch.save(
                {
                    "model_name": "TCN",
                    "seed": seed,
                    "history_hours": samples.history_hours,
                    "horizon_hours": samples.horizon_hours,
                    "state_dict": model.state_dict(),
                    "input_features": cfg["task"]["input_features"],
                    "scaler": scaler.to_jsonable(cfg["task"]["input_features"]),
                    "config": cfg,
                },
                checkpoint_path,
            )
            scaler_path.write_text(json.dumps(scaler.to_jsonable(cfg["task"]["input_features"]), indent=2), encoding="utf-8")
        else:
            stale_epochs += 1
        elapsed = time.perf_counter() - start
        logger.info(
            "seed=%s history=%sh horizon=%sh epoch=%s/%s train_loss=%.6f val_MAE=%.6f val_RMSE=%.6f "
            "best_val_MAE=%.6f elapsed_sec=%.2f device=%s gpu_memory=%s checkpoint=%s",
            seed,
            samples.history_hours,
            samples.horizon_hours,
            epoch,
            cfg["training"]["epochs"],
            train_loss,
            val_metrics["MAE"],
            val_metrics["RMSE"],
            best_val_mae,
            elapsed,
            device,
            cuda_memory_text(device),
            checkpoint_path,
        )
        if stale_epochs >= int(cfg["training"]["early_stopping_patience"]):
            logger.info("Early stopping: seed=%s history=%sh horizon=%sh epoch=%s", seed, samples.history_hours, samples.horizon_hours, epoch)
            break

    state = torch.load(checkpoint_path, map_location=device, weights_only=False)
    model.load_state_dict(state["state_dict"])
    test_true, test_pred = predict_original_units(model, test_loader, device, scaler)
    test_metrics = metric_dict(test_true, test_pred)
    row = {
        "model": "TCN",
        "input_feature_group": cfg["task"]["input_feature_group"],
        "seed": seed,
        "history_hours": samples.history_hours,
        "horizon_hours": samples.horizon_hours,
        "split": "test",
        "best_epoch": best_epoch,
        "best_val_MAE": best_val_mae,
        **test_metrics,
        "checkpoint": str(checkpoint_path),
    }
    runtime = {
        "seed": seed,
        "history_hours": samples.history_hours,
        "horizon_hours": samples.horizon_hours,
        "device": device,
        "train_samples": int(train.sum()),
        "val_samples": int(val.sum()),
        "test_samples": int(test.sum()),
        "best_epoch": best_epoch,
        "best_val_MAE": best_val_mae,
        "seconds": time.perf_counter() - start,
        "checkpoint": str(checkpoint_path),
        "scaler_metadata": str(scaler_path),
    }
    return row, runtime


def load_seasonal_baseline(cfg: dict) -> pd.DataFrame:
    base = pd.read_csv(cfg["paths"]["phase7_history_vs_seasonal"])
    base = base[["horizon_hours", "SeasonalHistoricalAverage_MAE", "SeasonalHistoricalAverage_RMSE", "SeasonalHistoricalAverage_sMAPE"]].drop_duplicates("horizon_hours")
    return base


def write_outputs(metrics: pd.DataFrame, runtime: pd.DataFrame, cfg: dict) -> None:
    out = Path(cfg["paths"]["output_tables"])
    out.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(out / "phase9_seed_metrics.csv", index=False, encoding="utf-8-sig")
    runtime.to_csv(out / "phase9_seed_runtime_summary.csv", index=False, encoding="utf-8-sig")
    seasonal = load_seasonal_baseline(cfg)
    vs = metrics.merge(seasonal, on="horizon_hours", how="left")
    vs["delta_MAE_vs_seasonal"] = vs["SeasonalHistoricalAverage_MAE"] - vs["MAE"]
    vs["improvement_percent_vs_seasonal"] = 100.0 * vs["delta_MAE_vs_seasonal"] / vs["SeasonalHistoricalAverage_MAE"]
    vs["outperforms_seasonal"] = vs["MAE"] < vs["SeasonalHistoricalAverage_MAE"]
    vs.to_csv(out / "phase9_seed_vs_seasonal.csv", index=False, encoding="utf-8-sig")
    rows = []
    for horizon, g in vs.groupby("horizon_hours"):
        mae = g["MAE"].to_numpy(dtype=float)
        seasonal_mae = float(g["SeasonalHistoricalAverage_MAE"].iloc[0])
        rows.append(
            {
                "horizon_hours": horizon,
                "history_hours": int(g["history_hours"].iloc[0]),
                "seed_count": len(g),
                "MAE_mean": float(mae.mean()),
                "MAE_std": float(mae.std(ddof=1)) if len(mae) > 1 else 0.0,
                "MAE_min": float(mae.min()),
                "MAE_max": float(mae.max()),
                "MAE_cv": float(mae.std(ddof=1) / mae.mean()) if len(mae) > 1 and mae.mean() != 0 else 0.0,
                "best_seed": int(g.loc[g["MAE"].idxmin(), "seed"]),
                "worst_seed": int(g.loc[g["MAE"].idxmax(), "seed"]),
                "SeasonalHistoricalAverage_MAE": seasonal_mae,
                "all_seeds_outperform_seasonal": bool(g["outperforms_seasonal"].all()),
                "mean_improvement_percent_vs_seasonal": float(g["improvement_percent_vs_seasonal"].mean()),
            }
        )
    pd.DataFrame(rows).to_csv(out / "phase9_seed_summary_by_horizon.csv", index=False, encoding="utf-8-sig")


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
    report_path = Path(cfg["paths"]["reports"]) / "phase9_repeated_seed_stability_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    metrics = pd.read_csv(out / "phase9_seed_metrics.csv")
    summary = pd.read_csv(out / "phase9_seed_summary_by_horizon.csv")
    vs = pd.read_csv(out / "phase9_seed_vs_seasonal.csv")
    lines = [
        "# Phase 9 Repeated-Seed Stability Report",
        "",
        "Phase 9 repeats the core TCN speed-only configurations across three random seeds. It is descriptive stability testing only.",
        "",
        "## Seed-Level Metrics",
        dataframe_to_markdown(metrics),
        "",
        "## Summary By Horizon",
        dataframe_to_markdown(summary),
        "",
        "## Versus Seasonal Historical Average",
        dataframe_to_markdown(vs),
        "",
        "No statistical significance test is reported because per-sample baseline predictions are not available.",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase9_repeated_seed_stability.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    validate_scope(cfg)

    for key in ["output_tables", "output_logs", "checkpoints", "reports"]:
        Path(cfg["paths"][key]).mkdir(parents=True, exist_ok=True)
    logger = setup_logger(Path(cfg["paths"]["output_logs"]) / "phase9_repeated_seed_stability.log")
    logger.info("Starting Phase 9 repeated-seed stability")

    try:
        import torch

        logger.info("PyTorch version: %s", torch.__version__)
    except ImportError as exc:
        raise ImportError("Phase 9 requires PyTorch in the configured environment.") from exc

    panel = load_panel(Path(cfg["paths"]["panel_1h"]), cfg)
    point_arrays = build_point_arrays(panel, cfg)
    metric_rows = []
    runtime_rows = []
    for horizon in [int(h) for h in cfg["task"]["horizons_hours"]]:
        history = int(cfg["task"]["best_history_by_horizon"][horizon])
        windows = load_windows(cfg, history, horizon, logger)
        samples = build_samples(windows, point_arrays, cfg, history, horizon)
        logger.info("Built samples for history=%sh horizon=%sh X=%s y=%s", history, horizon, samples.x.shape, samples.y.shape)
        for seed in [int(s) for s in cfg["training"]["seeds"]]:
            row, runtime = train_once(samples, cfg, seed, logger, Path(cfg["paths"]["checkpoints"]))
            metric_rows.append(row)
            runtime_rows.append(runtime)
    metrics = pd.DataFrame(metric_rows)
    runtime = pd.DataFrame(runtime_rows)
    write_outputs(metrics, runtime, cfg)
    write_report(cfg)
    logger.info("Phase 9 repeated-seed stability completed")


if __name__ == "__main__":
    main()
