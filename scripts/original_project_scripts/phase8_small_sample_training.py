from __future__ import annotations

import argparse
import json
import logging
import math
import random
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

import phase7_history_sensitivity as p7


EXPERIMENT = "phase8_small_sample_training"
SUPPORTED_HORIZONS = {1, 3, 6}
REQUIRED_METRIC_COLUMNS = [
    "experiment",
    "model",
    "feature_group",
    "target",
    "target_column",
    "history_hours",
    "horizon_hours",
    "train_ratio",
    "seed",
    "mae",
    "rmse",
    "smape",
    "n_train_windows",
    "n_val_windows",
    "n_test_windows",
    "best_epoch",
    "best_val_mae",
    "train_start",
    "train_end_selected",
    "val_start",
    "val_end",
    "test_start",
    "test_end",
]


def read_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(EXPERIMENT)
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
    if task["target"] != "speed" or task["target_variable"] != "speed" or task["target_column"] != "current_speed":
        raise ValueError("Phase 8 small-sample training is restricted to speed/current_speed.")
    if task["target_definition"] != "future_window_mean_speed":
        raise ValueError("Prediction target must be future_window_mean_speed.")
    if task["model"] != "TCN":
        raise ValueError("Phase 8 small-sample training is restricted to the TCN model.")
    if task["feature_group"] != "speed_only" or task["input_feature_group"] != "speed_only" or task["input_features"] != ["current_speed"]:
        raise ValueError("Phase 8 small-sample training is restricted to speed_only/current_speed input.")
    if int(task["history_hours"]) != 168:
        raise ValueError("Phase 8 small-sample training must use history_hours=168.")
    horizons = {int(h) for h in task["horizons_hours"]}
    if horizons != SUPPORTED_HORIZONS:
        raise ValueError(f"Unsupported horizons {sorted(horizons)}. Expected [1, 3, 6].")
    ratios = [float(r) for r in task["train_ratios"]]
    if ratios != [0.20, 0.40, 0.60, 0.80, 1.00]:
        raise ValueError("train_ratios must be [0.20, 0.40, 0.60, 0.80, 1.00].")
    if [int(s) for s in task["seeds"]] != [1, 2, 3, 4, 5]:
        raise ValueError("seeds must be [1, 2, 3, 4, 5].")


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
    logger.info("Loaded candidate windows for history=%sh horizon=%sh: %s", history, horizon, kept)
    return pd.concat(frames, ignore_index=True).sort_values(["split", "target_start_time", "point_id", "window_id"]).reset_index(drop=True)


def selected_training_windows(windows: pd.DataFrame, ratio: float) -> tuple[pd.DataFrame, pd.Timestamp, pd.Timestamp]:
    train = windows[windows["split"].eq("train")].sort_values(["target_start_time", "point_id", "window_id"]).copy()
    if train.empty:
        raise ValueError("Original training windows are zero.")
    train_times = pd.Series(train["target_start_time"].drop_duplicates().sort_values().to_numpy())
    n_times = max(1, int(math.ceil(len(train_times) * float(ratio))))
    cutoff = pd.Timestamp(train_times.iloc[n_times - 1])
    selected = train[train["target_start_time"].le(cutoff)].copy()
    return selected, pd.Timestamp(train_times.iloc[0]), cutoff


def combined_windows_for_ratio(windows: pd.DataFrame, ratio: float) -> tuple[pd.DataFrame, dict[str, str]]:
    train_selected, train_start, train_end_selected = selected_training_windows(windows, ratio)
    val = windows[windows["split"].eq("val")].copy()
    test = windows[windows["split"].eq("test")].copy()
    if train_selected.empty:
        raise ValueError(f"Selected training windows are zero for train_ratio={ratio}.")
    if val.empty:
        raise ValueError("Validation windows are zero.")
    if test.empty:
        raise ValueError("Test windows are zero.")
    combined = pd.concat([train_selected, val, test], ignore_index=True)
    periods = {
        "train_start": str(train_start),
        "train_end_selected": str(train_end_selected),
        "val_start": str(pd.Timestamp(val["target_start_time"].min())),
        "val_end": str(pd.Timestamp(val["target_end_time"].max())),
        "test_start": str(pd.Timestamp(test["target_start_time"].min())),
        "test_end": str(pd.Timestamp(test["target_end_time"].max())),
    }
    if pd.Timestamp(periods["train_end_selected"]) >= pd.Timestamp(periods["val_start"]):
        raise ValueError("Selected training period overlaps or reaches validation period.")
    if pd.Timestamp(periods["val_end"]) >= pd.Timestamp(periods["test_start"]):
        raise ValueError("Validation period overlaps or reaches test period.")
    return combined, periods


def fit_standardizer_selected_train(samples: p7.SampleSet) -> p7.Standardizer:
    split_names = set(str(s) for s in np.unique(samples.split))
    if not {"train", "val", "test"}.issubset(split_names):
        raise ValueError(f"Expected train/val/test splits before scaling, found {sorted(split_names)}.")
    train = samples.split == "train"
    val = samples.split == "val"
    test = samples.split == "test"
    if int(train.sum()) == 0:
        raise ValueError("Scaler fit blocked: selected training windows are zero.")
    if int(val.sum()) == 0 or int(test.sum()) == 0:
        raise ValueError("Scaler fit blocked: validation or test windows are zero.")
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
    scaler = p7.Standardizer(x_mean.astype(np.float32), x_std.astype(np.float32), y_mean, y_std)
    if np.shares_memory(x_train, samples.x[val]) or np.shares_memory(x_train, samples.x[test]):
        raise ValueError("Scaler fit check failed: training array shares memory with validation or test arrays.")
    return scaler


def assert_metric_finite(metrics: dict, context: str) -> None:
    for name in ["MAE", "RMSE", "sMAPE"]:
        value = float(metrics[name])
        if not np.isfinite(value):
            raise ValueError(f"{context}: metric {name} is NaN or infinite.")


def train_once(samples: p7.SampleSet, cfg: dict, seed: int, train_ratio: float, periods: dict[str, str], logger: logging.Logger, checkpoint_dir: Path) -> dict:
    import torch
    import torch.nn as nn

    set_seed(seed)
    scaler = fit_standardizer_selected_train(samples)
    x_scaled = scaler.transform_x(samples.x)
    y_scaled = scaler.transform_y(samples.y)
    train_mask = samples.split == "train"
    val_mask = samples.split == "val"
    test_mask = samples.split == "test"
    if int(train_mask.sum()) == 0:
        raise ValueError(f"Selected training windows are zero for train_ratio={train_ratio}.")
    if int(val_mask.sum()) == 0:
        raise ValueError("Validation windows are zero.")
    if int(test_mask.sum()) == 0:
        raise ValueError("Test windows are zero.")

    device_cfg = cfg["training"]["device"]
    device = "cuda" if device_cfg == "auto" and torch.cuda.is_available() else ("cpu" if device_cfg == "auto" else device_cfg)
    batch_size = int(cfg["training"]["batch_size"])
    train_loader = p7.make_loader(x_scaled[train_mask], y_scaled[train_mask], batch_size, True)
    val_loader = p7.make_loader(x_scaled[val_mask], y_scaled[val_mask], batch_size, False)
    test_loader = p7.make_loader(x_scaled[test_mask], y_scaled[test_mask], batch_size, False)
    model = p7.build_tcn(x_scaled.shape[2], cfg).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(cfg["training"]["learning_rate"]),
        weight_decay=float(cfg["training"]["weight_decay"]),
    )
    criterion = nn.MSELoss()
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    ratio_label = f"{int(round(train_ratio * 100)):03d}"
    base = f"phase8_small_sample_tcn_speed_only_ratio{ratio_label}_seed{seed}_h{samples.history_hours}_y{samples.horizon_hours}"
    checkpoint_path = checkpoint_dir / f"{base}.pt"
    scaler_path = checkpoint_dir / f"{base}_scaler.json"

    best_val_mae = float("inf")
    best_epoch = 0
    stale = 0
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
        val_true, val_pred = p7.predict_original_units(model, val_loader, device, scaler)
        val_metrics = p7.metric_dict(val_true, val_pred)
        assert_metric_finite(val_metrics, f"validation ratio={train_ratio} seed={seed} horizon={samples.horizon_hours}")
        if val_metrics["MAE"] < best_val_mae:
            best_val_mae = val_metrics["MAE"]
            best_epoch = epoch
            stale = 0
            torch.save(
                {
                    "model_name": "TCN",
                    "experiment": EXPERIMENT,
                    "seed": seed,
                    "train_ratio": train_ratio,
                    "history_hours": samples.history_hours,
                    "horizon_hours": samples.horizon_hours,
                    "state_dict": model.state_dict(),
                    "input_features": cfg["task"]["input_features"],
                    "scaler_fit_split": "selected_train_only",
                    "scaler": scaler.to_jsonable(cfg["task"]["input_features"]),
                    "periods": periods,
                    "config": cfg,
                },
                checkpoint_path,
            )
            scaler_meta = scaler.to_jsonable(cfg["task"]["input_features"])
            scaler_meta.update({"scaler_fit_split": "selected_train_only", "train_ratio": train_ratio, "seed": seed, "periods": periods})
            scaler_path.write_text(json.dumps(scaler_meta, indent=2), encoding="utf-8")
        else:
            stale += 1
        logger.info(
            "ratio=%.2f seed=%s history=%sh horizon=%sh epoch=%s/%s train_loss=%.6f val_MAE=%.6f best_val_MAE=%.6f elapsed_sec=%.2f device=%s checkpoint=%s",
            train_ratio,
            seed,
            samples.history_hours,
            samples.horizon_hours,
            epoch,
            cfg["training"]["epochs"],
            train_loss,
            val_metrics["MAE"],
            best_val_mae,
            time.perf_counter() - start,
            device,
            checkpoint_path,
        )
        if stale >= int(cfg["training"]["early_stopping_patience"]):
            logger.info("Early stopping: ratio=%.2f seed=%s history=%sh horizon=%sh epoch=%s", train_ratio, seed, samples.history_hours, samples.horizon_hours, epoch)
            break

    state = torch.load(checkpoint_path, map_location=device, weights_only=False)
    if state.get("scaler_fit_split") != "selected_train_only":
        raise ValueError("Scaler metadata check failed: scaler was not marked as selected_train_only.")
    model.load_state_dict(state["state_dict"])
    test_true, test_pred = p7.predict_original_units(model, test_loader, device, scaler)
    test_metrics = p7.metric_dict(test_true, test_pred)
    assert_metric_finite(test_metrics, f"test ratio={train_ratio} seed={seed} horizon={samples.horizon_hours}")

    return {
        "experiment": EXPERIMENT,
        "model": "TCN",
        "feature_group": cfg["task"]["feature_group"],
        "target": cfg["task"]["target"],
        "target_column": cfg["task"]["target_column"],
        "history_hours": int(samples.history_hours),
        "horizon_hours": int(samples.horizon_hours),
        "train_ratio": float(train_ratio),
        "seed": int(seed),
        "mae": float(test_metrics["MAE"]),
        "rmse": float(test_metrics["RMSE"]),
        "smape": float(test_metrics["sMAPE"]),
        "n_train_windows": int(train_mask.sum()),
        "n_val_windows": int(val_mask.sum()),
        "n_test_windows": int(test_mask.sum()),
        "best_epoch": int(best_epoch),
        "best_val_mae": float(best_val_mae),
        **periods,
    }


def validate_test_period_stable(periods_seen: dict[int, tuple[str, str]], horizon: int, periods: dict[str, str]) -> None:
    signature = (periods["test_start"], periods["test_end"])
    if horizon not in periods_seen:
        periods_seen[horizon] = signature
    elif periods_seen[horizon] != signature:
        raise ValueError(
            f"Test period changed for horizon={horizon}: expected={periods_seen[horizon]} observed={signature}"
        )


def dataframe_to_markdown(df: pd.DataFrame, max_rows: int = 100) -> str:
    if df.empty:
        return "_No rows._"
    view = df.head(max_rows).copy()
    cols = list(view.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[c]).replace("|", "/") for c in cols) + " |")
    if len(df) > max_rows:
        lines.append(f"\n_Showing first {max_rows} of {len(df)} rows._")
    return "\n".join(lines)


def write_report(cfg: dict, metrics: pd.DataFrame, warnings: list[str]) -> None:
    report_path = Path(cfg["paths"]["reports"]) / "phase8_small_sample_training_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    output_files = [
        Path(cfg["paths"]["output_tables"]) / "phase8_small_sample_metrics.csv",
        Path("outputs/plot_data/Fig07_small_sample_training_data.csv"),
    ]
    rows = [{"file": str(path).replace("\\", "/"), "exists_now": path.exists(), "rows": int(len(pd.read_csv(path))) if path.exists() else 0} for path in output_files]
    summary = metrics.groupby(["horizon_hours", "train_ratio"], as_index=False).agg(
        seed_count=("seed", "nunique"),
        n_train_windows_mean=("n_train_windows", "mean"),
        mae_mean=("mae", "mean"),
        mae_std=("mae", "std"),
    )
    lines = [
        "# Phase 8 Small-Sample Training Report",
        "",
        "## Purpose",
        "This experiment measures TCN speed-only robustness when the chronological training period is reduced while validation and test periods remain unchanged.",
        "",
        "## Data Split Design",
        "- Chronological train/validation/test split is read from the existing Phase 2 window index.",
        "- For each training ratio, only the earliest share of original train-period target timestamps is retained.",
        "- Validation and test windows are unchanged across all ratios and seeds.",
        "",
        "## Leakage Control",
        "- Raw data are not modified.",
        "- Selected training windows are defined before sample tensors are built.",
        "- Feature and target scalers are fitted only on the selected training samples.",
        "- Validation and test tensors are transformed using the selected-training scaler.",
        "",
        "## Design",
        f"- Training ratios: {cfg['task']['train_ratios']}",
        f"- Horizons: {cfg['task']['horizons_hours']}",
        f"- Seeds: {cfg['task']['seeds']}",
        f"- History length: {cfg['task']['history_hours']}h",
        "",
        "## Output Files",
        dataframe_to_markdown(pd.DataFrame(rows)),
        "",
        "## Metric Summary",
        dataframe_to_markdown(summary),
        "",
        "## Warnings",
        dataframe_to_markdown(pd.DataFrame({"warning": warnings or ["none"]})),
        "",
        "## Manuscript Interpretation Template",
        "Small-sample sensitivity can be reported as the percentage MAE degradation of the 20% chronological-training model relative to the full-training model for the same forecast horizon. Stable degradation across seeds supports robustness under limited labelled history; sharp degradation identifies horizons that require longer training coverage.",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def write_placeholder_report() -> None:
    report_path = Path("reports/phase8_small_sample_training_report.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    if report_path.exists():
        return
    report_path.write_text(
        "\n".join(
            [
                "# Phase 8 Small-Sample Training Report",
                "",
                "Status: code and runner prepared; long training has not been run yet.",
                "",
                "Run `run_phase8_small_sample_training.bat` to generate `outputs/tables/phase8_small_sample_metrics.csv`, then run `run_phase12a_prepare_plot_data.bat` to generate `outputs/plot_data/Fig07_small_sample_training_data.csv` and refresh the plot-data manifest.",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase8_small_sample_training.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    validate_scope(cfg)

    for key in ["output_tables", "output_logs", "checkpoints", "reports"]:
        Path(cfg["paths"][key]).mkdir(parents=True, exist_ok=True)
    logger = setup_logger(Path(cfg["paths"]["output_logs"]) / "phase8_small_sample_training.log")
    logger.info("Starting %s", EXPERIMENT)

    try:
        import torch

        logger.info("PyTorch version: %s", torch.__version__)
    except ImportError as exc:
        raise ImportError("Phase 8 small-sample training requires PyTorch in the configured environment.") from exc

    set_seed(int(cfg["project"]["random_seed"]))
    panel = p7.load_panel(Path(cfg["paths"]["panel_1h"]), cfg)
    point_arrays = p7.build_point_arrays(panel, cfg)
    history = int(cfg["task"]["history_hours"])
    metric_rows = []
    warnings: list[str] = []
    periods_seen: dict[int, tuple[str, str]] = {}

    for horizon in [int(h) for h in cfg["task"]["horizons_hours"]]:
        if horizon not in SUPPORTED_HORIZONS:
            raise ValueError(f"Unsupported horizon: {horizon}")
        windows = load_windows(cfg, history, horizon, logger)
        for train_ratio in [float(r) for r in cfg["task"]["train_ratios"]]:
            ratio_windows, periods = combined_windows_for_ratio(windows, train_ratio)
            validate_test_period_stable(periods_seen, horizon, periods)
            samples = p7.build_samples(ratio_windows, point_arrays, cfg, history, horizon)
            split_counts = pd.Series(samples.split).value_counts().to_dict()
            logger.info(
                "Built samples horizon=%sh ratio=%.2f X=%s y=%s split_counts=%s selected_train_end=%s",
                horizon,
                train_ratio,
                samples.x.shape,
                samples.y.shape,
                split_counts,
                periods["train_end_selected"],
            )
            if int((samples.split == "train").sum()) == 0:
                raise ValueError(f"Selected training windows are zero after sample construction for horizon={horizon} ratio={train_ratio}.")
            if int((samples.split == "val").sum()) == 0:
                raise ValueError(f"Validation windows are zero after sample construction for horizon={horizon} ratio={train_ratio}.")
            if int((samples.split == "test").sum()) == 0:
                raise ValueError(f"Test windows are zero after sample construction for horizon={horizon} ratio={train_ratio}.")
            for seed in [int(s) for s in cfg["task"]["seeds"]]:
                row = train_once(samples, cfg, seed, train_ratio, periods, logger, Path(cfg["paths"]["checkpoints"]))
                metric_rows.append(row)

    metrics = pd.DataFrame(metric_rows)
    metrics = metrics[REQUIRED_METRIC_COLUMNS]
    numeric_cols = ["mae", "rmse", "smape", "best_val_mae"]
    if not np.isfinite(metrics[numeric_cols].to_numpy(dtype=float)).all():
        raise ValueError("At least one output metric is NaN or infinite.")
    out_path = Path(cfg["paths"]["output_tables"]) / "phase8_small_sample_metrics.csv"
    metrics.to_csv(out_path, index=False, encoding="utf-8-sig")
    write_report(cfg, metrics, warnings)
    logger.info("Completed %s. Metrics: %s", EXPERIMENT, out_path)


if __name__ == "__main__":
    main()
