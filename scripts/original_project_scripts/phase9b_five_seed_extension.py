from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd

import phase9_repeated_seed_stability as p9


REQUIRED_PHASE9_FILES = [
    "phase9_seed_metrics",
    "phase9_seed_runtime_summary",
    "phase9_seed_vs_seasonal",
    "phase9_seed_summary_by_horizon",
]


def validate_scope(cfg: dict) -> None:
    task = cfg["task"]
    if task["model"] != "TCN":
        raise ValueError("Phase 9B is restricted to TCN.")
    if task["input_feature_group"] != "speed_only" or task["input_features"] != ["current_speed"]:
        raise ValueError("Phase 9B is restricted to speed_only input.")
    if task["target_variable"] != "speed" or task["target_column"] != "current_speed":
        raise ValueError("Phase 9B is restricted to speed/current_speed.")
    if task["target_definition"] != "future_window_mean_speed":
        raise ValueError("Phase 9B target must be future_window_mean_speed.")
    if sorted(int(h) for h in task["horizons_hours"]) != [1, 3, 6]:
        raise ValueError("Phase 9B horizons must be [1, 3, 6].")
    if {int(k): int(v) for k, v in task["best_history_by_horizon"].items()} != {1: 72, 3: 168, 6: 24}:
        raise ValueError("Phase 9B must use Phase 7 best histories: 1->72, 3->168, 6->24.")
    if sorted(int(s) for s in cfg["training"]["existing_seeds"]) != [42, 2025, 20260623]:
        raise ValueError("Existing Phase 9 seeds must be [42, 2025, 20260623].")
    if sorted(int(s) for s in cfg["training"]["additional_seeds"]) != [1234, 3407]:
        raise ValueError("Additional Phase 9B seeds must be [1234, 3407].")


def require_existing_phase9_outputs(cfg: dict) -> None:
    missing = [cfg["paths"][key] for key in REQUIRED_PHASE9_FILES if not Path(cfg["paths"][key]).exists()]
    if missing:
        raise FileNotFoundError(
            "Phase 9B requires existing Phase 9 output files and will not rerun old seeds. "
            f"Missing files: {missing}"
        )
    metrics = pd.read_csv(cfg["paths"]["phase9_seed_metrics"])
    expected = set(int(s) for s in cfg["training"]["existing_seeds"])
    found = set(int(s) for s in metrics["seed"].dropna().unique())
    if not expected.issubset(found):
        raise ValueError(f"Existing Phase 9 metrics do not contain all required seeds. expected={sorted(expected)} found={sorted(found)}")


def train_once_phase9b(samples: p9.SampleSet, cfg: dict, seed: int, logger, checkpoint_dir: Path):
    import torch
    import torch.nn as nn

    p9.set_seed(seed)
    scaler = p9.fit_standardizer(samples)
    x_scaled = scaler.transform_x(samples.x)
    y_scaled = scaler.transform_y(samples.y)
    train_mask = samples.split == "train"
    val_mask = samples.split == "val"
    test_mask = samples.split == "test"
    device_cfg = cfg["training"]["device"]
    device = "cuda" if device_cfg == "auto" and torch.cuda.is_available() else ("cpu" if device_cfg == "auto" else device_cfg)
    batch_size = int(cfg["training"]["batch_size"])
    train_loader = p9.make_loader(x_scaled[train_mask], y_scaled[train_mask], batch_size, True)
    val_loader = p9.make_loader(x_scaled[val_mask], y_scaled[val_mask], batch_size, False)
    test_loader = p9.make_loader(x_scaled[test_mask], y_scaled[test_mask], batch_size, False)
    model = p9.build_tcn(x_scaled.shape[2], cfg).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(cfg["training"]["learning_rate"]),
        weight_decay=float(cfg["training"]["weight_decay"]),
    )
    criterion = nn.MSELoss()
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = checkpoint_dir / f"phase9b_tcn_speed_only_seed{seed}_h{samples.history_hours}_y{samples.horizon_hours}.pt"
    scaler_path = checkpoint_dir / f"phase9b_tcn_speed_only_seed{seed}_h{samples.history_hours}_y{samples.horizon_hours}_scaler.json"

    best_val_mae = float("inf")
    best_epoch = 0
    stale = 0
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
        val_true, val_pred = p9.predict_original_units(model, val_loader, device, scaler)
        val_metrics = p9.metric_dict(val_true, val_pred)
        if val_metrics["MAE"] < best_val_mae:
            best_val_mae = val_metrics["MAE"]
            best_epoch = step
            stale = 0
            torch.save(
                {
                    "model_name": "TCN",
                    "phase": "Phase 9B",
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
            stale += 1
        elapsed = time.perf_counter() - start
        logger.info(
            "seed=%s history=%sh horizon=%sh step=%s/%s train_loss=%.6f val_MAE=%.6f val_RMSE=%.6f "
            "best_val_MAE=%.6f elapsed_sec=%.2f device=%s gpu_memory=%s checkpoint=%s",
            seed,
            samples.history_hours,
            samples.horizon_hours,
            step,
            cfg["training"]["epochs"],
            train_loss,
            val_metrics["MAE"],
            val_metrics["RMSE"],
            best_val_mae,
            elapsed,
            device,
            p9.cuda_memory_text(device),
            checkpoint_path,
        )
        if stale >= int(cfg["training"]["early_stopping_patience"]):
            logger.info("Early stopping: seed=%s history=%sh horizon=%sh step=%s", seed, samples.history_hours, samples.horizon_hours, step)
            break

    state = torch.load(checkpoint_path, map_location=device, weights_only=False)
    model.load_state_dict(state["state_dict"])
    test_true, test_pred = p9.predict_original_units(model, test_loader, device, scaler)
    test_metrics = p9.metric_dict(test_true, test_pred)
    metric_row = {
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
    runtime_row = {
        "seed": seed,
        "history_hours": samples.history_hours,
        "horizon_hours": samples.horizon_hours,
        "device": device,
        "train_samples": int(train_mask.sum()),
        "val_samples": int(val_mask.sum()),
        "test_samples": int(test_mask.sum()),
        "best_epoch": best_epoch,
        "best_val_MAE": best_val_mae,
        "seconds": time.perf_counter() - start,
        "checkpoint": str(checkpoint_path),
        "scaler_metadata": str(scaler_path),
    }
    return metric_row, runtime_row


def load_seasonal_baseline(cfg: dict) -> pd.DataFrame:
    base = pd.read_csv(cfg["paths"]["phase7_history_vs_seasonal"])
    return base[
        ["horizon_hours", "SeasonalHistoricalAverage_MAE", "SeasonalHistoricalAverage_RMSE", "SeasonalHistoricalAverage_sMAPE"]
    ].drop_duplicates("horizon_hours")


def merge_and_write_outputs(new_metrics: pd.DataFrame, new_runtime: pd.DataFrame, cfg: dict) -> None:
    out = Path(cfg["paths"]["output_tables"])
    out.mkdir(parents=True, exist_ok=True)
    new_metrics.to_csv(out / "phase9b_new_seed_metrics.csv", index=False, encoding="utf-8-sig")
    new_runtime.to_csv(out / "phase9b_new_seed_runtime_summary.csv", index=False, encoding="utf-8-sig")

    old_metrics = pd.read_csv(cfg["paths"]["phase9_seed_metrics"])
    all_metrics = pd.concat([old_metrics, new_metrics], ignore_index=True)
    expected = sorted(int(s) for s in cfg["training"]["all_expected_seeds"])
    found = sorted(int(s) for s in all_metrics["seed"].dropna().unique())
    if found != expected:
        raise ValueError(f"Five-seed merge failed. expected={expected} found={found}")
    all_metrics.to_csv(out / "phase9b_five_seed_metrics.csv", index=False, encoding="utf-8-sig")

    seasonal = load_seasonal_baseline(cfg)
    vs = all_metrics.merge(seasonal, on="horizon_hours", how="left")
    vs["delta_MAE_vs_seasonal"] = vs["SeasonalHistoricalAverage_MAE"] - vs["MAE"]
    vs["improvement_percent_vs_seasonal"] = 100.0 * vs["delta_MAE_vs_seasonal"] / vs["SeasonalHistoricalAverage_MAE"]
    vs["outperforms_seasonal"] = vs["MAE"] < vs["SeasonalHistoricalAverage_MAE"]
    vs.to_csv(out / "phase9b_five_seed_vs_seasonal.csv", index=False, encoding="utf-8-sig")

    rows = []
    for horizon, g in vs.groupby("horizon_hours", sort=True):
        mae = g["MAE"].to_numpy(dtype=float)
        rows.append(
            {
                "horizon_hours": int(horizon),
                "history_hours": int(g["history_hours"].iloc[0]),
                "seed_count": int(len(g)),
                "MAE_mean": float(mae.mean()),
                "MAE_std": float(mae.std(ddof=1)),
                "MAE_min": float(mae.min()),
                "MAE_max": float(mae.max()),
                "MAE_cv": float(mae.std(ddof=1) / mae.mean()) if mae.mean() != 0 else 0.0,
                "best_seed": int(g.loc[g["MAE"].idxmin(), "seed"]),
                "worst_seed": int(g.loc[g["MAE"].idxmax(), "seed"]),
                "SeasonalHistoricalAverage_MAE": float(g["SeasonalHistoricalAverage_MAE"].iloc[0]),
                "all_seeds_outperform_seasonal": bool(g["outperforms_seasonal"].all()),
                "mean_improvement_percent_vs_seasonal": float(g["improvement_percent_vs_seasonal"].mean()),
            }
        )
    summary = pd.DataFrame(rows)
    summary.to_csv(out / "phase9b_five_seed_summary_by_horizon.csv", index=False, encoding="utf-8-sig")

    summary[["horizon_hours", "history_hours", "MAE_mean", "MAE_std", "MAE_cv", "SeasonalHistoricalAverage_MAE"]].to_csv(
        out / "phase9b_figure_mae_mean_std.csv", index=False, encoding="utf-8-sig"
    )
    vs[["seed", "horizon_hours", "history_hours", "MAE", "RMSE", "sMAPE", "outperforms_seasonal"]].to_csv(
        out / "phase9b_figure_seed_scatter.csv", index=False, encoding="utf-8-sig"
    )
    vs[["seed", "horizon_hours", "history_hours", "improvement_percent_vs_seasonal"]].to_csv(
        out / "phase9b_figure_improvement_boxplot.csv", index=False, encoding="utf-8-sig"
    )


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows._"
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)


def write_report(cfg: dict) -> None:
    out = Path(cfg["paths"]["output_tables"])
    report_path = Path(cfg["paths"]["reports"]) / "phase9b_five_seed_extension_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    new_metrics = pd.read_csv(out / "phase9b_new_seed_metrics.csv")
    summary = pd.read_csv(out / "phase9b_five_seed_summary_by_horizon.csv")
    vs = pd.read_csv(out / "phase9b_five_seed_vs_seasonal.csv")
    text = [
        "# Phase 9B Five-Seed Extension Report",
        "",
        "Phase 9B trains only the two additional seeds 1234 and 3407, then merges them with the locked Phase 9 seeds 42, 2025 and 20260623.",
        "",
        "## New Seed Metrics",
        dataframe_to_markdown(new_metrics),
        "",
        "## Five-Seed Summary By Horizon",
        dataframe_to_markdown(summary),
        "",
        "## Five-Seed Comparison With SeasonalHistoricalAverage",
        dataframe_to_markdown(vs),
        "",
        "The locked Phase 9 output files are read only and are not modified by this extension.",
        "",
    ]
    report_path.write_text("\n".join(text), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase9b_five_seed_extension.yaml")
    args = parser.parse_args()
    cfg = p9.read_config(Path(args.config))
    validate_scope(cfg)
    require_existing_phase9_outputs(cfg)

    for key in ["output_tables", "output_logs", "checkpoints", "reports"]:
        Path(cfg["paths"][key]).mkdir(parents=True, exist_ok=True)
    logger = p9.setup_logger(Path(cfg["paths"]["output_logs"]) / "phase9b_five_seed_extension.log")
    logger.info("Starting Phase 9B five-seed extension. Existing seeds are read from Phase 9; only seeds 1234 and 3407 are trained.")

    panel = p9.load_panel(Path(cfg["paths"]["panel_1h"]), cfg)
    point_arrays = p9.build_point_arrays(panel, cfg)
    metric_rows = []
    runtime_rows = []
    for horizon in [int(h) for h in cfg["task"]["horizons_hours"]]:
        history = int(cfg["task"]["best_history_by_horizon"][horizon])
        windows = p9.load_windows(cfg, history, horizon, logger)
        samples = p9.build_samples(windows, point_arrays, cfg, history, horizon)
        logger.info("Built samples for history=%sh horizon=%sh X=%s y=%s", history, horizon, samples.x.shape, samples.y.shape)
        for seed in [int(s) for s in cfg["training"]["additional_seeds"]]:
            row, runtime = train_once_phase9b(samples, cfg, seed, logger, Path(cfg["paths"]["checkpoints"]))
            metric_rows.append(row)
            runtime_rows.append(runtime)

    merge_and_write_outputs(pd.DataFrame(metric_rows), pd.DataFrame(runtime_rows), cfg)
    write_report(cfg)
    logger.info("Phase 9B five-seed extension completed")


if __name__ == "__main__":
    main()
