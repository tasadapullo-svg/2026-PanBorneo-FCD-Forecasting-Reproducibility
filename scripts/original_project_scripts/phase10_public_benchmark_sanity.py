from __future__ import annotations

import argparse
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
    logger = logging.getLogger("phase10_public_benchmark_sanity")
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
    training = cfg["training"]
    if training["model"] != "TCN":
        raise ValueError("Phase 10 is restricted to TCN.")
    if cfg["task"]["input_feature_group"] != "speed_only":
        raise ValueError("Phase 10 is restricted to speed_only input.")
    if training["baselines"] != ["Persistence", "HistoricalAverage"]:
        raise ValueError("Phase 10 baselines must be Persistence and HistoricalAverage only.")
    if sorted(int(s) for s in training["seeds"]) != [42, 1234, 2025, 3407, 20260623]:
        raise ValueError("Phase 10 seeds must be [42, 2025, 20260623, 1234, 3407].")


def candidate_files(root: Path) -> list[Path]:
    patterns = ["*.csv", "*.csv.gz", "*.npz", "*.h5"]
    files: list[Path] = []
    for pattern in patterns:
        files.extend(root.glob(pattern))
    return sorted(files)


def find_dataset(cfg: dict) -> tuple[str, Path]:
    for candidate in cfg["paths"]["dataset_candidates"]:
        root = Path(candidate)
        if not root.exists():
            continue
        files = candidate_files(root)
        if files:
            return root.name, files[0]
    raise FileNotFoundError(
        "No METR-LA-mini or PEMS-BAY-mini benchmark file found. "
        "Place METR-LA.csv, METR-LA.csv.gz, an NPZ file, or an HDF5 file under data/benchmark/METR-LA-mini."
    )


def load_csv_matrix(path: Path) -> tuple[np.ndarray, dict]:
    df = pd.read_csv(path)
    first_col = df.columns[0] if len(df.columns) else None
    first_is_time = False
    if first_col is not None:
        parsed_time = pd.to_datetime(df[first_col], errors="coerce")
        first_is_time = bool(parsed_time.notna().mean() > 0.95)
    if first_is_time:
        feature_df = df.drop(columns=[first_col])
    else:
        feature_df = df
    numeric = feature_df.select_dtypes(include=[np.number]).copy()
    if numeric.empty:
        for col in feature_df.columns:
            parsed = pd.to_numeric(feature_df[col], errors="coerce")
            if parsed.notna().mean() > 0.8:
                numeric[col] = parsed
    if numeric.empty:
        raise ValueError(f"No numeric sensor-speed columns found in {path}")
    meta = {
        "source_file": str(path),
        "file_format": path.suffix,
        "raw_shape": tuple(df.shape),
        "timestamp_column": str(first_col) if first_is_time else "",
        "sensor_count": int(numeric.shape[1]),
    }
    return numeric.to_numpy(dtype=np.float32), meta


def load_npz_matrix(path: Path) -> tuple[np.ndarray, dict]:
    data = np.load(path)
    key = "data" if "data" in data.files else data.files[0]
    arr = data[key]
    if arr.ndim == 3:
        arr = arr[:, :, 0]
    if arr.ndim != 2:
        raise ValueError(f"Expected NPZ array with 2 or 3 dimensions, got shape={arr.shape}")
    meta = {"source_file": str(path), "file_format": ".npz", "raw_shape": tuple(arr.shape), "timestamp_column": "", "sensor_count": int(arr.shape[1])}
    return arr.astype(np.float32), meta


def load_hdf_matrix(path: Path) -> tuple[np.ndarray, dict]:
    df = pd.read_hdf(path)
    numeric = df.select_dtypes(include=[np.number])
    if numeric.empty:
        raise ValueError(f"No numeric columns found in HDF5 DataFrame {path}")
    meta = {
        "source_file": str(path),
        "file_format": ".h5",
        "raw_shape": tuple(df.shape),
        "timestamp_column": "index" if isinstance(df.index, pd.DatetimeIndex) else "",
        "sensor_count": int(numeric.shape[1]),
    }
    return numeric.to_numpy(dtype=np.float32), meta


def load_speed_matrix(path: Path) -> tuple[np.ndarray, dict]:
    name = path.name.lower()
    if name.endswith(".csv") or name.endswith(".csv.gz"):
        return load_csv_matrix(path)
    if name.endswith(".npz"):
        return load_npz_matrix(path)
    if name.endswith(".h5"):
        return load_hdf_matrix(path)
    raise ValueError(f"Unsupported benchmark file format: {path}")


def split_indices(n_time: int, ratios: list[float]) -> dict[str, tuple[int, int]]:
    train_end = int(np.floor(n_time * ratios[0]))
    val_end = int(np.floor(n_time * (ratios[0] + ratios[1])))
    return {"train": (0, train_end), "val": (train_end, val_end), "test": (val_end, n_time)}


def fill_missing_by_train_mean(arr: np.ndarray, train_end: int) -> np.ndarray:
    train = arr[:train_end]
    means = np.nanmean(train, axis=0)
    global_mean = float(np.nanmean(train))
    means = np.where(np.isfinite(means), means, global_mean)
    out = arr.copy()
    missing = np.where(~np.isfinite(out))
    out[missing] = np.take(means, missing[1])
    return out.astype(np.float32)


@dataclass
class SampleSet:
    x: np.ndarray
    y: np.ndarray
    split: np.ndarray
    sensor_id: np.ndarray
    horizon_steps: int
    history_steps: int


@dataclass
class Standardizer:
    x_mean: float
    x_std: float
    y_mean: float
    y_std: float

    def transform_x(self, x: np.ndarray) -> np.ndarray:
        return ((x - self.x_mean) / self.x_std).astype(np.float32)

    def transform_y(self, y: np.ndarray) -> np.ndarray:
        return ((y - self.y_mean) / self.y_std).astype(np.float32)

    def inverse_y(self, y_scaled: np.ndarray) -> np.ndarray:
        return y_scaled * self.y_std + self.y_mean


def make_samples(arr: np.ndarray, cfg: dict) -> SampleSet:
    history = int(cfg["data"]["history_steps"])
    horizon = int(cfg["data"]["horizon_steps"])
    splits = split_indices(arr.shape[0], cfg["data"]["split_ratios"])
    caps = {
        "train": int(cfg["data"]["max_train_samples"]),
        "val": int(cfg["data"]["max_val_samples"]),
        "test": int(cfg["data"]["max_test_samples"]),
    }
    counts = {split: 0 for split in caps}
    x_rows, y_rows, split_rows, sensor_rows = [], [], [], []
    for split, (start, end) in splits.items():
        last_start = end - history - horizon + 1
        if last_start <= start:
            continue
        for t in range(start, last_start):
            if counts[split] >= caps[split]:
                break
            target_index = t + history + horizon - 1
            for sensor in range(arr.shape[1]):
                if counts[split] >= caps[split]:
                    break
                x_rows.append(arr[t : t + history, sensor].reshape(-1, 1).astype(np.float32))
                y_rows.append(float(arr[target_index, sensor]))
                split_rows.append(split)
                sensor_rows.append(sensor)
                counts[split] += 1
    if not x_rows:
        raise ValueError("No samples generated. Check benchmark length, history_steps and horizon_steps.")
    return SampleSet(
        x=np.stack(x_rows).astype(np.float32),
        y=np.asarray(y_rows, dtype=np.float32),
        split=np.asarray(split_rows),
        sensor_id=np.asarray(sensor_rows),
        horizon_steps=horizon,
        history_steps=history,
    )


def fit_standardizer(samples: SampleSet) -> Standardizer:
    train = samples.split == "train"
    x_train = samples.x[train]
    y_train = samples.y[train]
    x_mean = float(x_train.mean())
    x_std = float(x_train.std())
    y_mean = float(y_train.mean())
    y_std = float(y_train.std())
    return Standardizer(x_mean, x_std if x_std > 1e-8 else 1.0, y_mean, y_std if y_std > 1e-8 else 1.0)


def make_loader(x: np.ndarray, y: np.ndarray, batch_size: int, use_order_permutation: bool):
    import torch
    from torch.utils.data import DataLoader, TensorDataset

    dataset = TensorDataset(torch.from_numpy(x), torch.from_numpy(y.reshape(-1, 1)))
    return DataLoader(dataset, batch_size=batch_size, shuffle=use_order_permutation, num_workers=0)


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

    return f"allocated_mb={torch.cuda.memory_allocated() / 1048576:.1f},reserved_mb={torch.cuda.memory_reserved() / 1048576:.1f}"


def train_tcn_for_seed(samples: SampleSet, scaler: Standardizer, cfg: dict, seed: int, logger: logging.Logger, checkpoint_path: Path) -> tuple[dict, dict]:
    import torch
    import torch.nn as nn

    set_seed(seed)
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
    model = build_tcn(x_scaled.shape[2], cfg).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(cfg["training"]["learning_rate"]),
        weight_decay=float(cfg["training"]["weight_decay"]),
    )
    criterion = nn.MSELoss()
    best_val_mae = float("inf")
    best_step = 0
    stale_steps = 0
    start = time.perf_counter()
    for step in range(1, int(cfg["training"]["epochs"]) + 1):
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
            best_step = step
            stale_steps = 0
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            torch.save(
                {
                    "state_dict": model.state_dict(),
                    "seed": seed,
                    "history_steps": samples.history_steps,
                    "horizon_steps": samples.horizon_steps,
                    "config": cfg,
                    "scaler": scaler.__dict__,
                },
                checkpoint_path,
            )
        else:
            stale_steps += 1
        elapsed = time.perf_counter() - start
        logger.info(
            "dataset_public_sanity model=TCN seed=%s history_steps=%s horizon_steps=%s step=%s/%s train_loss=%.6f "
            "val_MAE=%.6f val_RMSE=%.6f best_val_MAE=%.6f elapsed_sec=%.2f device=%s gpu_memory=%s checkpoint=%s",
            seed,
            samples.history_steps,
            samples.horizon_steps,
            step,
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
        if stale_steps >= int(cfg["training"]["early_stopping_patience"]):
            logger.info("Early stopping: seed=%s step=%s", seed, step)
            break
    state = torch.load(checkpoint_path, map_location=device, weights_only=False)
    model.load_state_dict(state["state_dict"])
    test_true, test_pred = predict_original_units(model, test_loader, device, scaler)
    metrics = metric_dict(test_true, test_pred)
    metric_row = {
        "dataset": cfg["runtime"]["dataset_name"],
        "model": "TCN",
        "feature_group": cfg["task"]["input_feature_group"],
        "seed": seed,
        "history_steps": samples.history_steps,
        "horizon_steps": samples.horizon_steps,
        "split": "test",
        "best_step": best_step,
        "best_val_MAE": best_val_mae,
        **metrics,
        "checkpoint": str(checkpoint_path),
    }
    runtime_row = {
        "dataset": cfg["runtime"]["dataset_name"],
        "seed": seed,
        "device": device,
        "history_steps": samples.history_steps,
        "horizon_steps": samples.horizon_steps,
        "train_samples": int(train.sum()),
        "val_samples": int(val.sum()),
        "test_samples": int(test.sum()),
        "best_step": best_step,
        "best_val_MAE": best_val_mae,
        "seconds": time.perf_counter() - start,
        "checkpoint": str(checkpoint_path),
    }
    return metric_row, runtime_row


def baseline_metrics(samples: SampleSet, dataset_name: str) -> pd.DataFrame:
    test = samples.split == "test"
    train = samples.split == "train"
    preds = {
        "Persistence": samples.x[:, -1, 0].astype(np.float32),
        "HistoricalAverage": np.full_like(samples.y, float(samples.y[train].mean()), dtype=np.float32),
    }
    rows = []
    for model, pred in preds.items():
        rows.append(
            {
                "dataset": dataset_name,
                "model": model,
                "feature_group": "baseline",
                "seed": "",
                "history_steps": samples.history_steps,
                "horizon_steps": samples.horizon_steps,
                "split": "test",
                "best_step": "",
                "best_val_MAE": np.nan,
                **metric_dict(samples.y[test], pred[test]),
                "checkpoint": "",
            }
        )
    return pd.DataFrame(rows)


def write_outputs(seed_metrics: pd.DataFrame, baseline_df: pd.DataFrame, runtime_df: pd.DataFrame, cfg: dict) -> None:
    out = Path(cfg["paths"]["output_tables"])
    out.mkdir(parents=True, exist_ok=True)
    seed_metrics.to_csv(out / "phase10_benchmark_seed_metrics.csv", index=False, encoding="utf-8-sig")
    runtime_df.to_csv(out / "phase10_benchmark_runtime_summary.csv", index=False, encoding="utf-8-sig")

    summary_rows = []
    for (dataset, horizon), g in seed_metrics.groupby(["dataset", "horizon_steps"], sort=True):
        mae = g["MAE"].to_numpy(dtype=float)
        summary_rows.append(
            {
                "dataset": dataset,
                "model": "TCN",
                "feature_group": "speed_only",
                "history_steps": int(g["history_steps"].iloc[0]),
                "horizon_steps": int(horizon),
                "seed_count": int(len(g)),
                "MAE_mean": float(mae.mean()),
                "MAE_std": float(mae.std(ddof=1)),
                "MAE_min": float(mae.min()),
                "MAE_max": float(mae.max()),
                "MAE_cv": float(mae.std(ddof=1) / mae.mean()) if mae.mean() != 0 else 0.0,
                "RMSE_mean": float(g["RMSE"].mean()),
                "sMAPE_mean": float(g["sMAPE"].mean()),
            }
        )
    summary = pd.DataFrame(summary_rows)
    summary.to_csv(out / "phase10_benchmark_summary_by_horizon.csv", index=False, encoding="utf-8-sig")

    baseline_rows = []
    for _, base in baseline_df.iterrows():
        for _, seed_row in seed_metrics.iterrows():
            baseline_rows.append(
                {
                    "dataset": seed_row["dataset"],
                    "baseline": base["model"],
                    "seed": int(seed_row["seed"]),
                    "history_steps": int(seed_row["history_steps"]),
                    "horizon_steps": int(seed_row["horizon_steps"]),
                    "baseline_MAE": base["MAE"],
                    "TCN_MAE": seed_row["MAE"],
                    "delta_MAE_vs_baseline": base["MAE"] - seed_row["MAE"],
                    "improvement_percent_vs_baseline": 100.0 * (base["MAE"] - seed_row["MAE"]) / base["MAE"],
                    "outperforms_baseline": bool(seed_row["MAE"] < base["MAE"]),
                }
            )
    vs = pd.DataFrame(baseline_rows)
    vs.to_csv(out / "phase10_benchmark_vs_baseline.csv", index=False, encoding="utf-8-sig")

    seed_metrics[["dataset", "seed", "history_steps", "horizon_steps", "MAE", "RMSE", "sMAPE"]].to_csv(
        out / "phase10_figure_seed_scatter.csv", index=False, encoding="utf-8-sig"
    )
    summary[["dataset", "history_steps", "horizon_steps", "MAE_mean", "MAE_std", "MAE_cv"]].to_csv(
        out / "phase10_figure_mae_mean_std.csv", index=False, encoding="utf-8-sig"
    )


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows._"
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)


def write_report(cfg: dict, meta: dict) -> None:
    out = Path(cfg["paths"]["output_tables"])
    report_path = Path(cfg["paths"]["reports"]) / "phase10_public_benchmark_sanity_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    seed_metrics = pd.read_csv(out / "phase10_benchmark_seed_metrics.csv")
    summary = pd.read_csv(out / "phase10_benchmark_summary_by_horizon.csv")
    vs = pd.read_csv(out / "phase10_benchmark_vs_baseline.csv")
    runtime = pd.read_csv(out / "phase10_benchmark_runtime_summary.csv")
    lines = [
        "# Phase 10 Public Benchmark Sanity Check Report",
        "",
        "Phase 10 is a supplementary public benchmark sanity check only. It verifies that the speed-only TCN pipeline can run on a public traffic speed matrix.",
        "",
        "It is not a comprehensive public benchmark study and should not be described as a competitive benchmark claim.",
        "",
        "## Dataset",
        f"- Dataset folder: `{cfg['runtime']['dataset_name']}`",
        f"- Source file: `{meta['source_file']}`",
        f"- File format: `{meta['file_format']}`",
        f"- Raw shape: `{meta['raw_shape']}`",
        f"- Sensor columns: `{meta['sensor_count']}`",
        f"- Timestamp column: `{meta['timestamp_column']}`",
        "",
        "## Five-Seed TCN Metrics",
        dataframe_to_markdown(seed_metrics),
        "",
        "## Summary By Horizon",
        dataframe_to_markdown(summary),
        "",
        "## Versus Simple Baselines",
        dataframe_to_markdown(vs),
        "",
        "## Runtime",
        dataframe_to_markdown(runtime),
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase10_public_benchmark_sanity.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    validate_scope(cfg)

    for key in ["output_tables", "output_logs", "checkpoints", "reports"]:
        Path(cfg["paths"][key]).mkdir(parents=True, exist_ok=True)
    logger = setup_logger(Path(cfg["paths"]["output_logs"]) / "phase10_public_benchmark_sanity.log")
    logger.info("Starting Phase 10 supplementary public benchmark sanity check")

    dataset_name, dataset_path = find_dataset(cfg)
    cfg["runtime"] = {"dataset_name": dataset_name, "dataset_path": str(dataset_path)}
    logger.info("Using dataset=%s file=%s", dataset_name, dataset_path)
    raw, meta = load_speed_matrix(dataset_path)
    splits = split_indices(raw.shape[0], cfg["data"]["split_ratios"])
    filled = fill_missing_by_train_mean(raw, splits["train"][1])
    samples = make_samples(filled, cfg)
    scaler = fit_standardizer(samples)
    logger.info("Prepared samples: X=%s y=%s train=%s val=%s test=%s", samples.x.shape, samples.y.shape, int((samples.split == "train").sum()), int((samples.split == "val").sum()), int((samples.split == "test").sum()))

    baseline_df = baseline_metrics(samples, dataset_name)
    metric_rows = []
    runtime_rows = []
    for seed in [int(s) for s in cfg["training"]["seeds"]]:
        checkpoint = Path(cfg["paths"]["checkpoints"]) / f"phase10_tcn_speed_only_{dataset_name.lower()}_seed{seed}_h{samples.history_steps}_y{samples.horizon_steps}.pt"
        metric_row, runtime_row = train_tcn_for_seed(samples, scaler, cfg, seed, logger, checkpoint)
        metric_rows.append(metric_row)
        runtime_rows.append(runtime_row)

    seed_metrics = pd.DataFrame(metric_rows)
    runtime_df = pd.DataFrame(runtime_rows)
    write_outputs(seed_metrics, baseline_df, runtime_df, cfg)
    write_report(cfg, meta)
    logger.info("Phase 10 supplementary public benchmark sanity check completed")


if __name__ == "__main__":
    main()
