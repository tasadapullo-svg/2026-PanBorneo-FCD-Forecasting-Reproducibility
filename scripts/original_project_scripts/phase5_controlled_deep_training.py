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
    logger = logging.getLogger("phase5_controlled_deep_training")
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
    histories = task["history_hours"] if isinstance(task["history_hours"], list) else [task["history_hours"]]
    if task["target_variable"] != "speed" or task["target_column"] != "current_speed":
        raise ValueError("Phase 5A is restricted to speed/current_speed.")
    if histories != [24]:
        raise ValueError("Phase 5A is restricted to 24h history.")
    if sorted(task["horizons_hours"]) != [1, 3, 6, 12, 24]:
        raise ValueError("Phase 5A horizons must be [1, 3, 6, 12, 24].")
    if sorted(cfg["training"]["models"]) != ["LSTM", "TCN"]:
        raise ValueError("Phase 5A is restricted to LSTM and TCN.")


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
    required = {"point_id", "timestamp", cfg["task"]["target_column"], *cfg["data"]["input_features"]}
    missing = required - set(panel.columns)
    if missing:
        raise ValueError(f"Panel file is missing columns after standardization: {sorted(missing)}")
    return panel.sort_values(["point_id", "timestamp"]).reset_index(drop=True)


def build_point_arrays(panel: pd.DataFrame, cfg: dict) -> dict[str, dict[str, np.ndarray]]:
    target_col = cfg["task"]["target_column"]
    features = cfg["data"]["input_features"]
    global_target_mean = float(panel[target_col].mean())
    out: dict[str, dict[str, np.ndarray]] = {}
    for point_id, g in panel.groupby("point_id", sort=True):
        g = g.sort_values("timestamp").reset_index(drop=True)
        point_id = str(point_id)
        point_target_mean = float(g[target_col].mean()) if g[target_col].notna().any() else global_target_mean
        arrays = {
            "timestamp": g["timestamp"].to_numpy(),
            "target": pd.to_numeric(g[target_col], errors="coerce").to_numpy(dtype=float),
        }
        for col in features:
            values = pd.to_numeric(g[col], errors="coerce").to_numpy(dtype=float)
            if col == target_col:
                values = np.where(np.isfinite(values), values, point_target_mean)
            elif col == "missing_mask":
                values = np.where(np.isfinite(values), values, 1.0)
            elif col in {"coverage_ratio_24h", "volatility_tti_6h", "weekend_flag"}:
                values = np.where(np.isfinite(values), values, 0.0)
            elif col == "hour_of_day":
                values = np.where(np.isfinite(values), values, 0.0) / 23.0
            elif col == "day_of_week":
                values = np.where(np.isfinite(values), values, 0.0) / 6.0
            arrays[col] = values.astype(np.float32)
        out[point_id] = arrays
    return out


def time_to_index(times: np.ndarray, timestamp: pd.Timestamp) -> int:
    idx = np.searchsorted(times, np.datetime64(timestamp), side="left")
    if idx >= len(times) or times[idx] != np.datetime64(timestamp):
        raise KeyError(f"Timestamp {timestamp} not found in point timeline")
    return int(idx)


def load_windows_for_horizon(cfg: dict, horizon: int, logger: logging.Logger) -> pd.DataFrame:
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
            & chunk["history_hours"].eq(24)
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
        raise ValueError(f"No windows found for horizon={horizon}")
    logger.info("Loaded windows for horizon=%sh: %s", horizon, kept)
    return pd.concat(frames, ignore_index=True)


@dataclass
class SampleSet:
    x: np.ndarray
    y: np.ndarray
    split: np.ndarray
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


def build_samples(windows: pd.DataFrame, point_arrays: dict[str, dict[str, np.ndarray]], cfg: dict, horizon: int) -> SampleSet:
    features = cfg["data"]["input_features"]
    xs, ys, splits = [], [], []
    for row in windows.itertuples(index=False):
        point_id = str(row.point_id)
        arrays = point_arrays[point_id]
        times = arrays["timestamp"]
        input_start = time_to_index(times, row.input_start_time)
        input_end = time_to_index(times, row.input_end_time)
        target_start = time_to_index(times, row.target_start_time)
        target_end = time_to_index(times, row.target_end_time)
        if input_end - input_start + 1 != 24:
            continue
        x = np.stack([arrays[col][input_start : input_end + 1] for col in features], axis=1)
        target = arrays["target"][target_start : target_end + 1]
        target = target[np.isfinite(target)]
        if len(target) == 0:
            continue
        xs.append(x.astype(np.float32))
        ys.append(float(target.mean()))
        splits.append(str(row.split))
    if not xs:
        raise ValueError(f"No samples could be built for horizon={horizon}")
    return SampleSet(np.stack(xs).astype(np.float32), np.asarray(ys, dtype=np.float32), np.asarray(splits), horizon)


def fit_standardizer(samples: SampleSet) -> Standardizer:
    train = samples.split == "train"
    x_train = samples.x[train]
    y_train = samples.y[train]
    x_mean = x_train.reshape(-1, x_train.shape[-1]).mean(axis=0)
    x_std = x_train.reshape(-1, x_train.shape[-1]).std(axis=0)
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


def build_lstm(input_size: int, cfg: dict):
    import torch.nn as nn

    class Model(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            mcfg = cfg["models"]["lstm"]
            self.lstm = nn.LSTM(
                input_size=input_size,
                hidden_size=int(mcfg["hidden_size"]),
                num_layers=int(mcfg["num_layers"]),
                dropout=float(mcfg["dropout"]) if int(mcfg["num_layers"]) > 1 else 0.0,
                batch_first=True,
            )
            self.head = nn.Linear(int(mcfg["hidden_size"]), 1)

        def forward(self, x):
            out, _ = self.lstm(x)
            return self.head(out[:, -1, :])

    return Model()


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

    allocated = torch.cuda.memory_allocated() / (1024**2)
    reserved = torch.cuda.memory_reserved() / (1024**2)
    return f"allocated_mb={allocated:.1f},reserved_mb={reserved:.1f}"


def train_model(model_name: str, samples: SampleSet, scaler: Standardizer, cfg: dict, logger: logging.Logger, checkpoint_dir: Path):
    import torch
    import torch.nn as nn

    device_cfg = cfg["training"]["device"]
    device = "cuda" if device_cfg == "auto" and torch.cuda.is_available() else ("cpu" if device_cfg == "auto" else device_cfg)
    x_scaled = scaler.transform_x(samples.x)
    y_scaled = scaler.transform_y(samples.y)
    train = samples.split == "train"
    val = samples.split == "val"
    test = samples.split == "test"
    batch_size = int(cfg["training"]["batch_size"])
    train_loader = make_loader(x_scaled[train], y_scaled[train], batch_size, True)
    val_loader = make_loader(x_scaled[val], y_scaled[val], batch_size, False)
    test_loader = make_loader(x_scaled[test], y_scaled[test], batch_size, False)
    model = build_tcn(x_scaled.shape[2], cfg) if model_name == "TCN" else build_lstm(x_scaled.shape[2], cfg)
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=float(cfg["training"]["learning_rate"]), weight_decay=float(cfg["training"]["weight_decay"]))
    criterion = nn.MSELoss()
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = checkpoint_dir / f"phase5_{model_name.lower()}_h24_y{samples.horizon_hours}.pt"
    scaler_path = checkpoint_dir / f"phase5_{model_name.lower()}_h24_y{samples.horizon_hours}_scaler.json"

    best_val_mae = float("inf")
    best_epoch = 0
    stale_epochs = 0
    rows = []
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
        improved = val_metrics["MAE"] < best_val_mae
        if improved:
            best_val_mae = val_metrics["MAE"]
            best_epoch = epoch
            stale_epochs = 0
            torch.save(
                {
                    "model_name": model_name,
                    "history_hours": 24,
                    "horizon_hours": samples.horizon_hours,
                    "state_dict": model.state_dict(),
                    "input_features": cfg["data"]["input_features"],
                    "scaler": scaler.to_jsonable(cfg["data"]["input_features"]),
                    "config": cfg,
                },
                checkpoint_path,
            )
            scaler_path.write_text(json.dumps(scaler.to_jsonable(cfg["data"]["input_features"]), indent=2), encoding="utf-8")
        else:
            stale_epochs += 1
        elapsed = time.perf_counter() - start
        message = (
            f"model={model_name} horizon={samples.horizon_hours}h epoch={epoch}/{cfg['training']['epochs']} "
            f"train_loss={train_loss:.6f} val_MAE={val_metrics['MAE']:.6f} val_RMSE={val_metrics['RMSE']:.6f} "
            f"best_val_MAE={best_val_mae:.6f} elapsed_sec={elapsed:.2f} device={device} "
            f"gpu_memory={cuda_memory_text(device)} checkpoint={checkpoint_path}"
        )
        logger.info(message)
        rows.append(
            {
                "model": model_name,
                "history_hours": 24,
                "horizon_hours": samples.horizon_hours,
                "epoch": epoch,
                "split": "val",
                "train_loss": train_loss,
                "MAE": val_metrics["MAE"],
                "RMSE": val_metrics["RMSE"],
                "sMAPE": val_metrics["sMAPE"],
                "best_val_MAE": best_val_mae,
                "best_epoch": best_epoch,
                "elapsed_seconds": elapsed,
            }
        )
        if stale_epochs >= int(cfg["training"]["early_stopping_patience"]):
            logger.info("Early stopping: model=%s horizon=%sh epoch=%s", model_name, samples.horizon_hours, epoch)
            break

    state = torch.load(checkpoint_path, map_location=device, weights_only=False)
    model.load_state_dict(state["state_dict"])
    test_true, test_pred = predict_original_units(model, test_loader, device, scaler)
    test_metrics = metric_dict(test_true, test_pred)
    rows.append(
        {
            "model": model_name,
            "history_hours": 24,
            "horizon_hours": samples.horizon_hours,
            "epoch": best_epoch,
            "split": "test",
            "train_loss": np.nan,
            "MAE": test_metrics["MAE"],
            "RMSE": test_metrics["RMSE"],
            "sMAPE": test_metrics["sMAPE"],
            "best_val_MAE": best_val_mae,
            "best_epoch": best_epoch,
            "elapsed_seconds": time.perf_counter() - start,
        }
    )
    runtime = {
        "model": model_name,
        "history_hours": 24,
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
    return rows, runtime


def load_seasonal_baseline(cfg: dict) -> pd.DataFrame:
    path = Path(cfg["paths"]["phase3_baseline_metrics_by_horizon"])
    if path.exists():
        base = pd.read_csv(path)
        base = base[(base["model"] == "SeasonalHistoricalAverage") & (base["split"] == "test")]
        return base[["horizon_hours", "MAE", "RMSE", "sMAPE"]].rename(
            columns={
                "MAE": "SeasonalHistoricalAverage_MAE",
                "RMSE": "SeasonalHistoricalAverage_RMSE",
                "sMAPE": "SeasonalHistoricalAverage_sMAPE",
            }
        )
    base = pd.read_csv(cfg["paths"]["phase3_baseline_metrics"])
    base = base[(base["model"] == "SeasonalHistoricalAverage") & (base["split"] == "test")].copy()
    rows = []
    for horizon in cfg["task"]["horizons_hours"]:
        row = base.iloc[0]
        rows.append(
            {
                "horizon_hours": horizon,
                "SeasonalHistoricalAverage_MAE": row["MAE"],
                "SeasonalHistoricalAverage_RMSE": row["RMSE"],
                "SeasonalHistoricalAverage_sMAPE": row["sMAPE"],
            }
        )
    return pd.DataFrame(rows)


def write_outputs(metrics: pd.DataFrame, runtime: pd.DataFrame, cfg: dict) -> None:
    out_tables = Path(cfg["paths"]["output_tables"])
    out_tables.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(out_tables / "phase5_deep_metrics.csv", index=False, encoding="utf-8-sig")
    metrics.groupby(["model", "history_hours", "horizon_hours", "split"], as_index=False).agg(
        n=("MAE", "size"),
        best_epoch=("best_epoch", "max"),
        MAE=("MAE", "last"),
        RMSE=("RMSE", "last"),
        sMAPE=("sMAPE", "last"),
    ).to_csv(out_tables / "phase5_deep_metrics_by_horizon.csv", index=False, encoding="utf-8-sig")
    metrics.groupby(["model", "split"], as_index=False).agg(
        n=("MAE", "size"),
        MAE=("MAE", "mean"),
        RMSE=("RMSE", "mean"),
        sMAPE=("sMAPE", "mean"),
    ).to_csv(out_tables / "phase5_deep_metrics_by_model.csv", index=False, encoding="utf-8-sig")
    runtime.to_csv(out_tables / "phase5_deep_runtime_summary.csv", index=False, encoding="utf-8-sig")

    test_metrics = metrics[metrics["split"] == "test"].copy()
    baseline = load_seasonal_baseline(cfg)
    comparison = test_metrics.merge(baseline, on="horizon_hours", how="left")
    comparison["delta_MAE_vs_seasonal"] = comparison["SeasonalHistoricalAverage_MAE"] - comparison["MAE"]
    comparison["improvement_percent_vs_seasonal"] = 100.0 * comparison["delta_MAE_vs_seasonal"] / comparison["SeasonalHistoricalAverage_MAE"]
    comparison[
        [
            "model",
            "history_hours",
            "horizon_hours",
            "MAE",
            "RMSE",
            "sMAPE",
            "SeasonalHistoricalAverage_MAE",
            "delta_MAE_vs_seasonal",
            "improvement_percent_vs_seasonal",
        ]
    ].to_csv(out_tables / "phase5_deep_vs_baseline_comparison.csv", index=False, encoding="utf-8-sig")


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
    out_tables = Path(cfg["paths"]["output_tables"])
    report_path = Path(cfg["paths"]["reports"]) / "phase5_controlled_deep_training_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    metrics = pd.read_csv(out_tables / "phase5_deep_metrics.csv")
    comparison = pd.read_csv(out_tables / "phase5_deep_vs_baseline_comparison.csv")
    runtime = pd.read_csv(out_tables / "phase5_deep_runtime_summary.csv")
    lines = [
        "# Phase 5 Controlled Deep Training Report",
        "",
        "Phase 5A tests whether TCN and LSTM can compete with the strongest Phase 3 periodic baseline under a larger but still controlled setting.",
        "",
        "## Scope",
        "- Target: future-window mean speed",
        "- History: 24h only",
        "- Horizons: 1h, 3h, 6h, 12h, 24h",
        "- Models: TCN and LSTM only",
        "- Training budget: 20 epochs with early stopping patience 5",
        "- Feature and target scaling are fitted on the train split only.",
        "",
        "## Metrics",
        dataframe_to_markdown(metrics),
        "",
        "## Deep Models vs Seasonal Historical Average",
        dataframe_to_markdown(comparison),
        "",
        "## Runtime",
        dataframe_to_markdown(runtime),
        "",
        "## Data Controls",
        "- Chronological Phase 2 splits are used.",
        "- Input tensors are built only from the input window.",
        "- Target-window values are used only for loss and evaluation.",
        "- Best checkpoints are selected by validation MAE.",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase5_controlled_deep_training.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    validate_scope(cfg)

    out_logs = Path(cfg["paths"]["output_logs"])
    checkpoints = Path(cfg["paths"]["checkpoints"])
    Path(cfg["paths"]["output_tables"]).mkdir(parents=True, exist_ok=True)
    out_logs.mkdir(parents=True, exist_ok=True)
    checkpoints.mkdir(parents=True, exist_ok=True)
    Path(cfg["paths"]["reports"]).mkdir(parents=True, exist_ok=True)
    logger = setup_logger(out_logs / "phase5_controlled_deep_training.log")
    logger.info("Starting Phase 5 controlled deep training")

    try:
        import torch

        logger.info("PyTorch version: %s", torch.__version__)
    except ImportError as exc:
        raise ImportError("Phase 5 requires PyTorch in the configured environment.") from exc

    set_seed(int(cfg["project"]["random_seed"]))
    panel = load_panel(Path(cfg["paths"]["panel_1h"]), cfg)
    point_arrays = build_point_arrays(panel, cfg)
    all_metric_rows = []
    runtime_rows = []
    for horizon in [int(h) for h in cfg["task"]["horizons_hours"]]:
        windows = load_windows_for_horizon(cfg, horizon, logger)
        samples = build_samples(windows, point_arrays, cfg, horizon)
        scaler = fit_standardizer(samples)
        logger.info("Built samples for horizon=%sh X=%s y=%s", horizon, samples.x.shape, samples.y.shape)
        for model_name in cfg["training"]["models"]:
            metric_rows, runtime = train_model(model_name, samples, scaler, cfg, logger, checkpoints)
            all_metric_rows.extend(metric_rows)
            runtime_rows.append(runtime)
    metrics = pd.DataFrame(all_metric_rows)
    runtime = pd.DataFrame(runtime_rows)
    write_outputs(metrics, runtime, cfg)
    write_report(cfg)
    logger.info("Phase 5 controlled deep training completed")


if __name__ == "__main__":
    main()
