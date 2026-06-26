from __future__ import annotations

import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd


TABLES = Path("outputs/tables")
PLOT = Path("outputs/plot_data")
LOGS = Path("outputs/logs")
REPORTS = Path("reports")


def setup_logger() -> logging.Logger:
    LOGS.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("phase12a_prepare_plot_data")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler = logging.FileHandler(LOGS / "phase12a_prepare_plot_data.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def read_source(name: str) -> tuple[pd.DataFrame | None, str]:
    path = TABLES / name
    if not path.exists():
        return None, "missing_source"
    return pd.read_csv(path), "ok"


def write_csv(name: str, df: pd.DataFrame, manifest: list[dict], meta: dict) -> None:
    PLOT.mkdir(parents=True, exist_ok=True)
    path = PLOT / name
    df.to_csv(path, index=False, encoding="utf-8-sig")
    manifest.append({**meta, "csv_file": str(path).replace("\\", "/"), "status": "ok" if "missing_source" not in set(df.get("status", [])) else "missing_source"})


def to_markdown_simple(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows._"
    cols = list(df.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.iterrows():
        lines.append("| " + " | ".join(str(row[c]).replace("|", "/") for c in cols) + " |")
    return "\n".join(lines)


def missing_csv(name: str, manifest: list[dict], meta: dict, missing_sources: str) -> None:
    df = pd.DataFrame([{"status": "missing_source", "missing_sources": missing_sources}])
    write_csv(name, df, manifest, meta)


def horizon_label(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce").astype("Int64").astype(str) + "h"


def short_phase_label(phase: str) -> str:
    return str(phase).replace("Phase ", "P")


def add_zero_delta(df: pd.DataFrame, value_col: str, group_cols: list[str], level_col: str) -> pd.DataFrame:
    out = df.copy()
    out["baseline_MAE_at_zero"] = np.nan
    for _, g in out.groupby(group_cols, dropna=False):
        zero = g[pd.to_numeric(g[level_col], errors="coerce").eq(0)]
        if zero.empty:
            continue
        base = float(zero[value_col].iloc[0])
        out.loc[g.index, "baseline_MAE_at_zero"] = base
    out["MAE_increase_vs_zero"] = out["MAE"] - out["baseline_MAE_at_zero"]
    out["MAE_increase_percent_vs_zero"] = 100.0 * out["MAE_increase_vs_zero"] / out["baseline_MAE_at_zero"]
    return out


def main() -> None:
    logger = setup_logger()
    PLOT.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    manifest: list[dict] = []
    output_summaries: list[dict] = []

    def record(name: str) -> None:
        df = pd.read_csv(PLOT / name)
        output_summaries.append({"csv_file": name, "rows": len(df), "columns": len(df.columns), "column_names": ", ".join(df.columns)})
        logger.info("Created %s rows=%s cols=%s", name, len(df), len(df.columns))

    # Fig01
    df, status = read_source("final_phase_status_summary.csv")
    meta = {
        "figure_id": "Fig01",
        "figure_title": "Overall experimental workflow",
        "source_files": "final_phase_status_summary.csv",
        "required_columns": "phase; experiment_name; status; main_scope; main_conclusion; usable_for_paper",
        "plot_type": "workflow/table timeline",
        "recommended_location": "main text",
        "main_message": "Complete reproducible workflow from audit to final summaries.",
    }
    if df is None:
        missing_csv("Fig01_workflow_data.csv", manifest, meta, "final_phase_status_summary.csv")
    else:
        out = df.copy()
        out["phase_order"] = out["phase"].str.extract(r"(\d+)").astype(int)
        out["short_label"] = out["phase"].map(short_phase_label)
        out["figure_group"] = np.where(out["usable_for_paper"].str.contains("appendix|supplementary", case=False, na=False), "supplementary", "main")
        out["include_in_main_workflow"] = True
        write_csv("Fig01_workflow_data.csv", out, manifest, meta)
    record("Fig01_workflow_data.csv")

    # Fig02
    df, status = read_source("final_main_forecasting_results.csv")
    meta = {
        "figure_id": "Fig02",
        "figure_title": "Main forecasting performance",
        "source_files": "final_main_forecasting_results.csv; final_seed_stability_summary.csv",
        "required_columns": "source_phase; model; feature_group; history_hours; horizon_hours; MAE; RMSE; sMAPE",
        "plot_type": "line/bar comparison",
        "recommended_location": "main text",
        "main_message": "Deep models improve short/medium horizons but do not dominate all horizons.",
    }
    if df is None:
        missing_csv("Fig02_main_forecasting_performance.csv", manifest, meta, "final_main_forecasting_results.csv")
    else:
        out = df.copy()
        seed, _ = read_source("final_seed_stability_summary.csv")
        out["MAE_std"] = np.nan
        if seed is not None:
            for _, r in seed.iterrows():
                mask = out["source_phase"].eq("Phase 9B") & pd.to_numeric(out["horizon_hours"], errors="coerce").eq(r["horizon_hours"])
                out.loc[mask, "MAE_std"] = r["MAE_std"]
        out["plot_model_label"] = out["source_phase"].astype(str) + " " + out["model"].astype(str)
        out["plot_group"] = np.select(
            [out["model"].eq("SeasonalHistoricalAverage"), out["source_phase"].eq("Phase 5"), out["source_phase"].eq("Phase 9B")],
            ["strong_baseline", "controlled_deep", "final_five_seed"],
            default="other",
        )
        out["is_final_five_seed"] = out["source_phase"].eq("Phase 9B")
        out["has_errorbar"] = out["MAE_std"].notna()
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        write_csv("Fig02_main_forecasting_performance.csv", out, manifest, meta)
    record("Fig02_main_forecasting_performance.csv")

    # Fig03 mean/std
    df, status = read_source("final_seed_stability_summary.csv")
    phase9b, _ = read_source("phase9b_five_seed_summary_by_horizon.csv")
    meta = {
        "figure_id": "Fig03a",
        "figure_title": "Five-seed Pan Borneo TCN stability",
        "source_files": "final_seed_stability_summary.csv; phase9b_five_seed_summary_by_horizon.csv",
        "required_columns": "horizon_hours; history_hours; seed_count; MAE_mean; MAE_std; MAE_cv",
        "plot_type": "bar with error bars",
        "recommended_location": "main text",
        "main_message": "Pan Borneo core model is stable across five seeds.",
    }
    if df is None:
        missing_csv("Fig03_five_seed_stability_mean_std.csv", manifest, meta, "final_seed_stability_summary.csv")
    else:
        out = df.copy()
        if phase9b is not None and "SeasonalHistoricalAverage_MAE" in phase9b.columns:
            out = out.merge(phase9b[["horizon_hours", "SeasonalHistoricalAverage_MAE"]], on="horizon_hours", how="left")
        else:
            out["SeasonalHistoricalAverage_MAE"] = np.nan
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        out["model_label"] = "TCN speed-only five-seed"
        out["baseline_label"] = "SeasonalHistoricalAverage"
        out["yerr_low"] = out["MAE_std"]
        out["yerr_high"] = out["MAE_std"]
        write_csv("Fig03_five_seed_stability_mean_std.csv", out, manifest, meta)
    record("Fig03_five_seed_stability_mean_std.csv")

    # Fig03 scatter
    df, status = read_source("phase9b_five_seed_vs_seasonal.csv")
    meta = {
        "figure_id": "Fig03b",
        "figure_title": "Seed-level Pan Borneo MAE scatter",
        "source_files": "phase9b_five_seed_vs_seasonal.csv",
        "required_columns": "seed; horizon_hours; history_hours; MAE; RMSE; sMAPE; SeasonalHistoricalAverage_MAE",
        "plot_type": "scatter",
        "recommended_location": "main text",
        "main_message": "Every Pan Borneo seed outperforms the strong seasonal baseline.",
    }
    if df is None:
        missing_csv("Fig03_seed_scatter.csv", manifest, meta, "phase9b_five_seed_vs_seasonal.csv")
    else:
        out = df.copy()
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        out["seed_label"] = "seed " + out["seed"].astype(str)
        out["jitter_group"] = out.groupby("horizon_hours").cumcount()
        write_csv("Fig03_seed_scatter.csv", out, manifest, meta)
    record("Fig03_seed_scatter.csv")

    # Fig03 improvement
    df, status = read_source("phase9b_five_seed_vs_seasonal.csv")
    meta = {
        "figure_id": "Fig03c",
        "figure_title": "Improvement percent distribution",
        "source_files": "phase9b_five_seed_vs_seasonal.csv",
        "required_columns": "seed; horizon_hours; history_hours; improvement_percent_vs_seasonal; outperforms_seasonal",
        "plot_type": "box/strip plot",
        "recommended_location": "main text",
        "main_message": "Improvement over seasonal baseline is positive for all core horizons and seeds.",
    }
    if df is None:
        missing_csv("Fig03_improvement_boxplot.csv", manifest, meta, "phase9b_five_seed_vs_seasonal.csv")
    else:
        out = df[["seed", "horizon_hours", "history_hours", "improvement_percent_vs_seasonal", "outperforms_seasonal"]].copy()
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        out["zero_reference"] = 0.0
        write_csv("Fig03_improvement_boxplot.csv", out, manifest, meta)
    record("Fig03_improvement_boxplot.csv")

    # Fig04 ablation
    df, status = read_source("phase6_ablation_vs_speed_only.csv")
    seasonal, _ = read_source("phase6_ablation_vs_seasonal.csv")
    meta = {
        "figure_id": "Fig04",
        "figure_title": "Feature ablation results",
        "source_files": "phase6_ablation_vs_speed_only.csv; phase6_ablation_vs_seasonal.csv",
        "required_columns": "ablation_group; horizon_hours; MAE; RMSE; sMAPE",
        "plot_type": "grouped bar/line",
        "recommended_location": "main text",
        "main_message": "Speed-only is strongest overall; reliability features are diagnostic rather than direct accuracy boosters.",
    }
    if df is None:
        missing_csv("Fig04_ablation_data.csv", manifest, meta, "phase6_ablation_vs_speed_only.csv")
    else:
        out = df[df["split"].eq("test")].copy()
        if seasonal is not None:
            cols = ["ablation_group", "horizon_hours", "improvement_percent_vs_seasonal"]
            out = out.merge(seasonal[seasonal["split"].eq("test")][cols], on=["ablation_group", "horizon_hours"], how="left")
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        labels = {
            "speed_only": "Speed only",
            "speed_time": "Speed + time",
            "speed_reliability": "Speed + reliability",
            "speed_volatility": "Speed + volatility",
            "full_features": "Full features",
        }
        out["ablation_label"] = out["ablation_group"].map(labels).fillna(out["ablation_group"])
        out["is_speed_only"] = out["ablation_group"].eq("speed_only")
        out["recommended_color_group"] = np.where(out["is_speed_only"], "reference", "ablation")
        out["interpretation_short"] = np.where(out["is_speed_only"], "strongest direct input", "not consistently better than speed-only")
        write_csv("Fig04_ablation_data.csv", out, manifest, meta)
    record("Fig04_ablation_data.csv")

    # Fig05 history
    df, status = read_source("phase7_history_vs_seasonal.csv")
    meta = {
        "figure_id": "Fig05",
        "figure_title": "History-length sensitivity",
        "source_files": "phase7_history_vs_seasonal.csv",
        "required_columns": "history_hours; horizon_hours; MAE; RMSE; sMAPE; is_best_history_for_horizon",
        "plot_type": "line/small multiples",
        "recommended_location": "main text",
        "main_message": "Optimal history length is horizon-dependent.",
    }
    if df is None:
        missing_csv("Fig05_history_sensitivity_data.csv", manifest, meta, "phase7_history_vs_seasonal.csv")
    else:
        out = df[df["split"].eq("test")].copy()
        out["history_label"] = horizon_label(out["history_hours"])
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        out["best_marker"] = np.where(out["is_best_history_for_horizon"], "best", "")
        order = {24: 1, 72: 2, 168: 3}
        out["plot_order"] = pd.to_numeric(out["history_hours"], errors="coerce").map(order)
        write_csv("Fig05_history_sensitivity_data.csv", out, manifest, meta)
    record("Fig05_history_sensitivity_data.csv")

    # Fig06 volatility
    df, status = read_source("phase8_error_by_volatility.csv")
    meta = {
        "figure_id": "Fig06",
        "figure_title": "Volatility-stratified prediction error",
        "source_files": "phase8_error_by_volatility.csv",
        "required_columns": "horizon_hours; volatility_bin; n; MAE; RMSE; sMAPE",
        "plot_type": "grouped bar",
        "recommended_location": "main text",
        "main_message": "High volatility is the dominant difficult-sample source.",
    }
    if df is None:
        missing_csv("Fig06_volatility_error_data.csv", manifest, meta, "phase8_error_by_volatility.csv")
    else:
        out = df.copy()
        out["horizon_label"] = horizon_label(out["horizon_hours"])
        order_map = {"q1_low": 1, "q2_mid_low": 2, "q3_mid_high": 3, "q4_high": 4}
        out["volatility_label"] = out["volatility_bin"].astype(str)
        out["volatility_order"] = out["volatility_bin"].map(order_map)
        out["high_vs_low_flag"] = np.where(out["volatility_bin"].astype(str).str.contains("q4"), "high", np.where(out["volatility_bin"].astype(str).str.contains("q1"), "low", "middle"))
        write_csv("Fig06_volatility_error_data.csv", out, manifest, meta)
    record("Fig06_volatility_error_data.csv")

    # Fig07 missingness
    df, status = read_source("phase8_missingness_stress_metrics.csv")
    meta = {
        "figure_id": "Fig07a",
        "figure_title": "Missingness stress test",
        "source_files": "phase8_missingness_stress_metrics.csv",
        "required_columns": "history_hours; horizon_hours; missing_level; n; MAE; RMSE; sMAPE",
        "plot_type": "line",
        "recommended_location": "main text",
        "main_message": "Missingness stress causes gradual degradation.",
    }
    miss_out = None
    if df is None:
        missing_csv("Fig07_missingness_stress_data.csv", manifest, meta, "phase8_missingness_stress_metrics.csv")
    else:
        miss_out = df.copy()
        miss_out["horizon_label"] = horizon_label(miss_out["horizon_hours"])
        miss_out["perturbation_type"] = "missingness"
        miss_out["perturbation_level"] = miss_out["missing_level"]
        miss_out = add_zero_delta(miss_out, "MAE", ["horizon_hours"], "perturbation_level")
        write_csv("Fig07_missingness_stress_data.csv", miss_out, manifest, meta)
    record("Fig07_missingness_stress_data.csv")

    # Fig07 noise
    df, status = read_source("phase8_noise_stress_metrics.csv")
    meta = {
        "figure_id": "Fig07b",
        "figure_title": "Noise stress test",
        "source_files": "phase8_noise_stress_metrics.csv",
        "required_columns": "history_hours; horizon_hours; noise_level; n; MAE; RMSE; sMAPE",
        "plot_type": "line",
        "recommended_location": "main text",
        "main_message": "Noise stress causes gradual degradation.",
    }
    noise_out = None
    if df is None:
        missing_csv("Fig07_noise_stress_data.csv", manifest, meta, "phase8_noise_stress_metrics.csv")
    else:
        noise_out = df.copy()
        noise_out["horizon_label"] = horizon_label(noise_out["horizon_hours"])
        noise_out["perturbation_type"] = "noise"
        noise_out["perturbation_level"] = noise_out["noise_level"]
        noise_out = add_zero_delta(noise_out, "MAE", ["horizon_hours"], "perturbation_level")
        write_csv("Fig07_noise_stress_data.csv", noise_out, manifest, meta)
    record("Fig07_noise_stress_data.csv")

    # Fig07 small-sample training
    df, status = read_source("phase8_small_sample_metrics.csv")
    meta = {
        "figure_id": "Fig07c",
        "figure_title": "Small-sample training sensitivity",
        "source_files": "phase8_small_sample_metrics.csv",
        "required_columns": "train_ratio; horizon_hours; model; feature_group; mae; rmse; smape; n_train_windows; n_test_windows",
        "plot_type": "line with seed standard-deviation bands",
        "recommended_location": "main text",
        "main_message": "Limited chronological training samples test robustness beyond input perturbations.",
    }
    if df is None:
        small_out = None
        missing_csv("Fig07_small_sample_training_data.csv", manifest, meta, "phase8_small_sample_metrics.csv")
    else:
        required = {
            "train_ratio",
            "horizon_hours",
            "model",
            "feature_group",
            "mae",
            "rmse",
            "smape",
            "n_train_windows",
            "n_test_windows",
        }
        missing = required - set(df.columns)
        if missing:
            raise ValueError(f"phase8_small_sample_metrics.csv is missing columns: {sorted(missing)}")
        small_out = (
            df.groupby(["train_ratio", "horizon_hours", "model", "feature_group"], as_index=False)
            .agg(
                mae_mean=("mae", "mean"),
                mae_std=("mae", "std"),
                rmse_mean=("rmse", "mean"),
                rmse_std=("rmse", "std"),
                smape_mean=("smape", "mean"),
                smape_std=("smape", "std"),
                n_train_windows_mean=("n_train_windows", "mean"),
                n_test_windows_mean=("n_test_windows", "mean"),
            )
            .sort_values(["horizon_hours", "train_ratio"])
        )
        small_out["train_ratio_percent"] = (pd.to_numeric(small_out["train_ratio"], errors="coerce") * 100.0).round(6)
        full = small_out[pd.to_numeric(small_out["train_ratio"], errors="coerce").eq(1.0)][
            ["horizon_hours", "mae_mean"]
        ].rename(columns={"mae_mean": "mae_full_train_mean"})
        if full.empty:
            raise ValueError("phase8_small_sample_metrics.csv must include train_ratio=1.00 for full-training degradation.")
        small_out = small_out.merge(full, on="horizon_hours", how="left")
        if small_out["mae_full_train_mean"].isna().any():
            raise ValueError("Full-training MAE is missing for at least one small-sample horizon.")
        small_out["mae_degradation_vs_full_pct"] = (
            (small_out["mae_mean"] - small_out["mae_full_train_mean"]) / small_out["mae_full_train_mean"] * 100.0
        )
        small_out = small_out[
            [
                "train_ratio",
                "train_ratio_percent",
                "horizon_hours",
                "model",
                "feature_group",
                "mae_mean",
                "mae_std",
                "rmse_mean",
                "rmse_std",
                "smape_mean",
                "smape_std",
                "mae_full_train_mean",
                "mae_degradation_vs_full_pct",
                "n_train_windows_mean",
                "n_test_windows_mean",
            ]
        ]
        write_csv("Fig07_small_sample_training_data.csv", small_out, manifest, meta)
    record("Fig07_small_sample_training_data.csv")

    # Fig07 degradation summary
    meta = {
        "figure_id": "Fig07d",
        "figure_title": "Overall degradation summary",
        "source_files": "phase8_missingness_stress_metrics.csv; phase8_noise_stress_metrics.csv; phase8_small_sample_metrics.csv",
        "required_columns": "stress_type; worst_case_mae_increase_pct",
        "plot_type": "compact bar",
        "recommended_location": "main text",
        "main_message": "Worst-case degradation summarizes missingness, noise, and limited-training robustness.",
    }
    summary_rows = []
    if miss_out is not None:
        row = miss_out.loc[pd.to_numeric(miss_out["MAE_increase_percent_vs_zero"], errors="coerce").idxmax()]
        summary_rows.append(
            {
                "stress_type": "missingness",
                "worst_case_mae_increase_pct": float(row["MAE_increase_percent_vs_zero"]),
                "horizon_hours": int(row["horizon_hours"]),
                "level": float(row["missing_level"]),
                "source_csv": "Fig07_missingness_stress_data.csv",
            }
        )
    if noise_out is not None:
        row = noise_out.loc[pd.to_numeric(noise_out["MAE_increase_percent_vs_zero"], errors="coerce").idxmax()]
        summary_rows.append(
            {
                "stress_type": "noise",
                "worst_case_mae_increase_pct": float(row["MAE_increase_percent_vs_zero"]),
                "horizon_hours": int(row["horizon_hours"]),
                "level": float(row["noise_level"]),
                "source_csv": "Fig07_noise_stress_data.csv",
            }
        )
    if small_out is not None:
        row = small_out.loc[pd.to_numeric(small_out["mae_degradation_vs_full_pct"], errors="coerce").idxmax()]
        summary_rows.append(
            {
                "stress_type": "small_sample_training",
                "worst_case_mae_increase_pct": float(row["mae_degradation_vs_full_pct"]),
                "horizon_hours": int(row["horizon_hours"]),
                "level": float(row["train_ratio"]),
                "source_csv": "Fig07_small_sample_training_data.csv",
            }
        )
    if not summary_rows:
        missing_csv("Fig07_degradation_summary_data.csv", manifest, meta, "phase8_missingness_stress_metrics.csv; phase8_noise_stress_metrics.csv; phase8_small_sample_metrics.csv")
    else:
        write_csv("Fig07_degradation_summary_data.csv", pd.DataFrame(summary_rows), manifest, meta)
    record("Fig07_degradation_summary_data.csv")

    # Fig07 combined support file retained for backward compatibility with existing plotting notebooks.
    meta = {
        "figure_id": "Fig07_support",
        "figure_title": "Combined noise and missingness support data",
        "source_files": "phase8_noise_stress_metrics.csv; phase8_missingness_stress_metrics.csv",
        "required_columns": "perturbation_type; perturbation_level; horizon_hours; horizon_label; MAE; RMSE; sMAPE",
        "plot_type": "supporting line/facet",
        "recommended_location": "supporting data",
        "main_message": "Backward-compatible combined perturbation data.",
    }
    if noise_out is None and miss_out is None:
        missing_csv("Fig07_noise_missingness_combined_data.csv", manifest, meta, "phase8_noise_stress_metrics.csv; phase8_missingness_stress_metrics.csv")
    else:
        frames = []
        for frame in [noise_out, miss_out]:
            if frame is not None:
                cols = ["perturbation_type", "perturbation_level", "horizon_hours", "horizon_label", "MAE", "RMSE", "sMAPE", "MAE_increase_vs_zero", "MAE_increase_percent_vs_zero"]
                frames.append(frame[cols].copy())
        write_csv("Fig07_noise_missingness_combined_data.csv", pd.concat(frames, ignore_index=True), manifest, meta)
    record("Fig07_noise_missingness_combined_data.csv")

    # FigA1 public benchmark
    final_pub, _ = read_source("final_public_benchmark_summary.csv")
    phase10_vs, _ = read_source("phase10_benchmark_vs_baseline.csv")
    phase10_seed, _ = read_source("phase10_figure_seed_scatter.csv")
    meta = {
        "figure_id": "FigA1",
        "figure_title": "Supplementary public benchmark sanity check",
        "source_files": "final_public_benchmark_summary.csv; phase10_benchmark_vs_baseline.csv; phase10_figure_seed_scatter.csv",
        "required_columns": "dataset; model; seed_count; MAE_mean; MAE_std; MAE_cv; baseline_name; baseline_MAE; seed; MAE",
        "plot_type": "appendix summary/scatter",
        "recommended_location": "appendix",
        "main_message": "Public benchmark supports pipeline portability, not benchmark superiority.",
    }
    if final_pub is None:
        missing_csv("FigA1_public_benchmark_sanity_data.csv", manifest, meta, "final_public_benchmark_summary.csv")
    else:
        summary_part = final_pub.copy()
        summary_part["baseline_name"] = ""
        summary_part["baseline_MAE"] = np.nan
        summary_part["seed"] = np.nan
        summary_part["MAE"] = summary_part["MAE_mean"]
        if phase10_vs is not None:
            base_part = phase10_vs.rename(columns={"baseline": "baseline_name"})[["dataset", "baseline_name", "baseline_MAE", "seed", "TCN_MAE"]].copy()
            base_part["model"] = "TCN"
            base_part["feature_group"] = "speed_only"
            base_part["seed_count"] = np.nan
            base_part["history_steps"] = np.nan
            base_part["horizon_steps"] = np.nan
            base_part["MAE_mean"] = np.nan
            base_part["MAE_std"] = np.nan
            base_part["MAE_cv"] = np.nan
            base_part["RMSE_mean"] = np.nan
            base_part["sMAPE_mean"] = np.nan
            base_part["outperforms_historical_average_all_seeds"] = np.nan
            base_part["outperforms_persistence_all_seeds"] = np.nan
            base_part["interpretation"] = "baseline comparison row"
            base_part = base_part.rename(columns={"TCN_MAE": "MAE"})
            out = pd.concat([summary_part, base_part], ignore_index=True, sort=False)
        else:
            out = summary_part
        out["outperforms_HA"] = out.get("outperforms_historical_average_all_seeds", np.nan)
        out["outperforms_Persistence"] = out.get("outperforms_persistence_all_seeds", np.nan)
        out["dataset_label"] = out["dataset"]
        out["benchmark_role"] = "supplementary_sanity_check"
        out["claim_boundary"] = "pipeline_portability_not_sota"
        out["recommended_location"] = "appendix"
        write_csv("FigA1_public_benchmark_sanity_data.csv", out, manifest, meta)
    record("FigA1_public_benchmark_sanity_data.csv")

    # Main table
    df, status = read_source("final_main_forecasting_results.csv")
    seed, _ = read_source("final_seed_stability_summary.csv")
    meta = {
        "figure_id": "Table1",
        "figure_title": "Paper-ready main forecasting results",
        "source_files": "final_main_forecasting_results.csv; final_seed_stability_summary.csv",
        "required_columns": "result_group; model; history_hours; horizon_hours; MAE; MAE_std; RMSE; sMAPE",
        "plot_type": "paper table",
        "recommended_location": "main text",
        "main_message": "Compact main results table.",
    }
    if df is None:
        missing_csv("Table_main_results_for_paper.csv", manifest, meta, "final_main_forecasting_results.csv")
    else:
        out = df[
            df["model"].eq("SeasonalHistoricalAverage")
            | df["source_phase"].eq("Phase 9B")
            | (df["source_phase"].eq("Phase 5") & pd.to_numeric(df["horizon_hours"], errors="coerce").isin([1, 3, 6, 12, 24]))
        ].copy()
        out["MAE_std"] = np.nan
        if seed is not None:
            for _, r in seed.iterrows():
                mask = out["source_phase"].eq("Phase 9B") & pd.to_numeric(out["horizon_hours"], errors="coerce").eq(r["horizon_hours"])
                out.loc[mask, "MAE_std"] = r["MAE_std"]
        out["result_group"] = np.select(
            [out["model"].eq("SeasonalHistoricalAverage"), out["source_phase"].eq("Phase 9B"), out["source_phase"].eq("Phase 5")],
            ["strong_baseline", "final_five_seed_tcn", "controlled_deep"],
            default="other",
        )
        cols = ["result_group", "model", "feature_group", "history_hours", "horizon_hours", "MAE", "MAE_std", "RMSE", "sMAPE", "improvement_percent_vs_seasonal", "interpretation"]
        write_csv("Table_main_results_for_paper.csv", out[cols], manifest, meta)
    record("Table_main_results_for_paper.csv")

    # Findings table
    df, status = read_source("final_empirical_findings_summary.csv")
    meta = {
        "figure_id": "Table2",
        "figure_title": "Paper-ready empirical findings",
        "source_files": "final_empirical_findings_summary.csv",
        "required_columns": "finding_id; finding; supporting_phase; supporting_metric; paper_interpretation; caution_or_limitation",
        "plot_type": "paper table",
        "recommended_location": "main text or discussion",
        "main_message": "Concise paper-level findings and limitations.",
    }
    if df is None:
        missing_csv("Table_key_findings_for_paper.csv", manifest, meta, "final_empirical_findings_summary.csv")
    else:
        write_csv("Table_key_findings_for_paper.csv", df.copy(), manifest, meta)
    record("Table_key_findings_for_paper.csv")

    pd.DataFrame(manifest).to_csv(PLOT / "plot_data_manifest.csv", index=False, encoding="utf-8-sig")
    record("plot_data_manifest.csv")

    report = ["# Phase 12A Plot Data Preparation Report", "", "No figures were generated. No training was run. Previous phase outputs and locked folders were not modified.", "", "## Output CSV Summary", ""]
    summary_df = pd.DataFrame(output_summaries)
    report.append(to_markdown_simple(summary_df))
    report.extend(
        [
            "",
            "## Interpretation Constraints",
            "- Reliability features are not claimed to directly improve forecasting accuracy.",
            "- Deep learning is not claimed to dominate all horizons.",
            "- Longer history is not claimed to always be better.",
            "- Phase 10 is labelled as supplementary sanity check only.",
            "- Pan Borneo Phase 9B five-seed results remain the main evidence.",
        ]
    )
    (REPORTS / "phase12a_plot_data_preparation_report.md").write_text("\n".join(report), encoding="utf-8")
    logger.info("Phase 12A plot-data package completed")


if __name__ == "__main__":
    main()
