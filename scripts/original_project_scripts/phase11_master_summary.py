from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


TABLES = Path("outputs/tables")
REPORTS = Path("reports")


def read_table(name: str) -> pd.DataFrame:
    return pd.read_csv(TABLES / name)


def fmt(value: float, digits: int = 4) -> str:
    if pd.isna(value):
        return ""
    return f"{float(value):.{digits}f}"


def seed_source() -> tuple[str, pd.DataFrame, pd.DataFrame]:
    p9b_summary = TABLES / "phase9b_five_seed_summary_by_horizon.csv"
    p9b_metrics = TABLES / "phase9b_five_seed_metrics.csv"
    p9b_vs = TABLES / "phase9b_five_seed_vs_seasonal.csv"
    if p9b_summary.exists() and p9b_metrics.exists() and p9b_vs.exists():
        return "Phase 9B", pd.read_csv(p9b_summary), pd.read_csv(p9b_metrics)
    return "Phase 9", read_table("phase9_seed_summary_by_horizon.csv"), read_table("phase9_seed_metrics.csv")


def phase10_source() -> tuple[bool, pd.DataFrame]:
    summary_path = TABLES / "phase10_benchmark_summary_by_horizon.csv"
    vs_path = TABLES / "phase10_benchmark_vs_baseline.csv"
    metrics_path = TABLES / "phase10_benchmark_seed_metrics.csv"
    if not (summary_path.exists() and vs_path.exists() and metrics_path.exists()):
        return False, pd.DataFrame()

    summary = pd.read_csv(summary_path)
    vs = pd.read_csv(vs_path)
    rows = []
    for _, row in summary.iterrows():
        dataset = row["dataset"]
        horizon = int(row["horizon_steps"])
        g = vs[(vs["dataset"] == dataset) & (vs["horizon_steps"] == horizon)]
        historical = g[g["baseline"].eq("HistoricalAverage")]
        persistence = g[g["baseline"].eq("Persistence")]
        rows.append(
            {
                "dataset": dataset,
                "model": row["model"],
                "feature_group": row["feature_group"],
                "seed_count": int(row["seed_count"]),
                "history_steps": int(row["history_steps"]),
                "horizon_steps": horizon,
                "MAE_mean": row["MAE_mean"],
                "MAE_std": row["MAE_std"],
                "MAE_cv": row["MAE_cv"],
                "RMSE_mean": row["RMSE_mean"],
                "sMAPE_mean": row["sMAPE_mean"],
                "outperforms_historical_average_all_seeds": bool(historical["outperforms_baseline"].all()) if not historical.empty else False,
                "outperforms_persistence_all_seeds": bool(persistence["outperforms_baseline"].all()) if not persistence.empty else False,
                "interpretation": "Valid supplementary public benchmark sanity check: pipeline runs on public data; supports portability, not benchmark superiority.",
            }
        )
    out = pd.DataFrame(rows)
    out.to_csv(TABLES / "final_public_benchmark_summary.csv", index=False)
    return True, out


def write_phase_status(seed_label: str, phase10_done: bool) -> None:
    phase9_status = "completed, accepted, locked" if seed_label == "Phase 9" else "completed with five-seed extension available"
    phase9_scope = (
        "Three-seed TCN speed-only stability for 1h, 3h and 6h best history settings"
        if seed_label == "Phase 9"
        else "Five-seed TCN speed-only stability for 1h, 3h and 6h best history settings"
    )
    phase9_conclusion = (
        "All seeds outperform SeasonalHistoricalAverage for 1h, 3h and 6h; 6h is the most stable."
        if seed_label == "Phase 9"
        else "Five-seed summary is used when available; all five seeds outperform SeasonalHistoricalAverage only where the summary flag is true."
    )
    phase10_status = "completed; supplementary sanity check" if phase10_done else "prepared but not executed"
    phase10_scope = (
        "METR-LA-mini five-seed TCN speed-only supplementary public benchmark sanity check"
        if phase10_done
        else "METR-LA-mini or PEMS-BAY-mini sanity check code only"
    )
    phase10_outputs = (
        "phase10_benchmark_seed_metrics.csv; phase10_benchmark_summary_by_horizon.csv; phase10_benchmark_vs_baseline.csv; phase10_public_benchmark_sanity_report.md"
        if phase10_done
        else "phase10_public_benchmark_sanity.py; phase10_public_benchmark_sanity.yaml; run_phase10_public_benchmark_sanity.bat"
    )
    phase10_conclusion = (
        "The TCN speed-only pipeline completed on METR-LA-mini with five seeds; it outperforms HistoricalAverage but not Persistence, so it supports pipeline portability rather than benchmark superiority."
        if phase10_done
        else "Prepared but not executed because no METR-LA-mini or PEMS-BAY-mini data files were available locally."
    )
    phase10_usable = "supplementary/appendix only" if phase10_done else "not yet"
    rows = [
        ["Phase 1", "Project audit and data inventory", "completed and accepted", "Raw TomTom FCD audit, missingness, point coverage, continuity, quality groups", "data_inventory.csv; missing_summary.csv; coverage_by_point.csv; phase1_data_audit_report.md", "The 1h panel is sufficiently covered for forecasting; 7-day horizon should be stress-test rather than main task.", "yes"],
        ["Phase 2", "Forecasting window construction", "completed and accepted", "Leakage-free chronological windows for 24h/72h/168h histories and multiple horizons", "window_index_all.csv; phase2_panel_1h_model_ready.csv.gz; window_feasibility_by_horizon.csv", "Leakage-free window index and train/validation/test split were constructed for main horizons.", "yes"],
        ["Phase 3", "Baseline forecasting", "completed, accepted, locked", "Persistence, HistoricalAverage, SeasonalHistoricalAverage, Ridge baselines for speed", "phase3_baseline_metrics.csv; phase3_baseline_metrics_by_horizon.csv; phase3_baseline_report.md", "SeasonalHistoricalAverage is a strong periodic baseline and the main comparator.", "yes"],
        ["Phase 4", "Deep learning smoke test", "completed, accepted, locked", "Small LSTM/TCN smoke test for data pipeline, shapes, logging and checkpoints", "phase4_smoke_metrics.csv; phase4_deep_smoke_test_report.md", "Deep learning pipeline, validation loop, logging and checkpoint saving were verified; smoke-test accuracy was not used as final evidence.", "methods appendix only"],
        ["Phase 5", "Controlled deep training", "completed, accepted, locked", "TCN and LSTM with 24h history across 1h, 3h, 6h, 12h, 24h horizons", "phase5_deep_vs_baseline_comparison.csv; phase5_deep_metrics_by_horizon.csv", "Deep models improve over the strong seasonal baseline at 1h, 3h and 6h, but not at 12h or 24h.", "yes"],
        ["Phase 6", "Reliability-aware ablation", "completed, accepted, locked", "TCN ablation over speed, time, reliability, volatility and full feature groups", "phase6_ablation_metrics_by_group.csv; phase6_ablation_vs_speed_only.csv; phase6_ablation_vs_seasonal.csv", "Speed-only is strongest overall; reliability indicators are more useful for diagnosis than direct accuracy gains in this high-coverage dataset.", "yes"],
        ["Phase 7", "History-length sensitivity", "completed, accepted, locked", "TCN speed-only with 24h, 72h and 168h histories for 1h, 3h and 6h horizons", "phase7_history_best_by_horizon.csv; phase7_history_vs_seasonal.csv", "Best history is horizon-dependent: 72h for 1h, 168h for 3h, and 24h for 6h.", "yes"],
        ["Phase 8", "Robustness and difficult-sample diagnosis", "completed, accepted, locked", "Evaluation-only robustness diagnostics for Phase 7 best checkpoints", "phase8_robustness_metrics.csv; phase8_error_by_volatility.csv; phase8_noise_stress_metrics.csv; phase8_missingness_stress_metrics.csv", "High volatility is the dominant difficult-sample source; noise and missingness cause gradual degradation.", "yes"],
        ["Phase 9", "Repeated-seed stability", phase9_status, phase9_scope, "phase9_seed_summary_by_horizon.csv; phase9_seed_vs_seasonal.csv; phase9b_five_seed_summary_by_horizon.csv if available", phase9_conclusion, "yes"],
        ["Phase 10", "Public benchmark sanity check", phase10_status, phase10_scope, phase10_outputs, phase10_conclusion, phase10_usable],
    ]
    pd.DataFrame(
        rows,
        columns=["phase", "experiment_name", "status", "main_scope", "key_outputs", "main_conclusion", "usable_for_paper"],
    ).to_csv(TABLES / "final_phase_status_summary.csv", index=False)


def write_main_results(seed_label: str, seed_summary: pd.DataFrame, seed_metrics: pd.DataFrame) -> None:
    phase3_h = read_table("phase3_baseline_metrics_by_horizon.csv")
    phase5_cmp = read_table("phase5_deep_vs_baseline_comparison.csv")
    phase7_best = read_table("phase7_history_best_by_horizon.csv")
    phase7_vs = read_table("phase7_history_vs_seasonal.csv")
    rows = []
    seasonal = phase3_h[(phase3_h["model"] == "SeasonalHistoricalAverage") & (phase3_h["split"] == "test") & (phase3_h["horizon_hours"].isin([1, 3, 6, 12, 24]))]
    for _, r in seasonal.iterrows():
        rows.append(["Phase 3", "SeasonalHistoricalAverage", "seasonal_hour_day_point", "train historical table", int(r["horizon_hours"]), "test", r["MAE"], r["RMSE"], r["sMAPE"], "self", 0.0, "Strong periodic baseline used as the main comparator."])
    for _, r in phase5_cmp.iterrows():
        interp = "Deep model improves over SeasonalHistoricalAverage at short/medium horizon." if r["improvement_percent_vs_seasonal"] > 0 else "SeasonalHistoricalAverage remains stronger for this longer aggregated horizon."
        rows.append(["Phase 5", r["model"], "full_features", int(r["history_hours"]), int(r["horizon_hours"]), "test", r["MAE"], r["RMSE"], r["sMAPE"], "SeasonalHistoricalAverage", r["improvement_percent_vs_seasonal"], interp])
    for _, r in phase7_best.iterrows():
        match = phase7_vs[(phase7_vs["split"] == r["split"]) & (phase7_vs["history_hours"] == r["history_hours"]) & (phase7_vs["horizon_hours"] == r["horizon_hours"])]
        imp = match["improvement_percent_vs_seasonal"].iloc[0] if not match.empty else np.nan
        rows.append(["Phase 7", r["model"], r["input_feature_group"], int(r["history_hours"]), int(r["horizon_hours"]), r["split"], r["MAE"], r["RMSE"], r["sMAPE"], "SeasonalHistoricalAverage", imp, "Best TCN speed-only history setting for this horizon."])
    for _, r in seed_summary.iterrows():
        g = seed_metrics[(seed_metrics["history_hours"] == r["history_hours"]) & (seed_metrics["horizon_hours"] == r["horizon_hours"]) & (seed_metrics["split"] == "test")]
        rows.append([
            seed_label,
            "TCN",
            "speed_only_seed_mean",
            int(r["history_hours"]),
            int(r["horizon_hours"]),
            "test",
            r["MAE_mean"],
            g["RMSE"].mean() if not g.empty else np.nan,
            g["sMAPE"].mean() if not g.empty else np.nan,
            "SeasonalHistoricalAverage",
            r["mean_improvement_percent_vs_seasonal"],
            f"Seed-stability mean using {int(r['seed_count'])} seeds; MAE_std={fmt(r['MAE_std'])}; all seeds outperform seasonal={r['all_seeds_outperform_seasonal']}",
        ])
    pd.DataFrame(
        rows,
        columns=["source_phase", "model", "feature_group", "history_hours", "horizon_hours", "split", "MAE", "RMSE", "sMAPE", "comparison_baseline", "improvement_percent_vs_seasonal", "interpretation"],
    ).to_csv(TABLES / "final_main_forecasting_results.csv", index=False)


def write_ablation_summary() -> None:
    group = read_table("phase6_ablation_metrics_by_group.csv")
    horizon = read_table("phase6_ablation_metrics_by_horizon.csv")
    speed = read_table("phase6_ablation_vs_speed_only.csv")
    seasonal = read_table("phase6_ablation_vs_seasonal.csv")
    interpretations = {
        "speed_only": "Strongest group overall; recent speed history is the dominant predictive signal.",
        "speed_time": "Time features do not improve overall accuracy relative to speed-only in this setting.",
        "speed_reliability": "Reliability features do not consistently improve direct accuracy in this high-coverage dataset.",
        "speed_volatility": "Volatility helps slightly at 1h but is not stable across horizons.",
        "full_features": "Full features underperform speed-only, suggesting feature redundancy or overfitting risk.",
    }
    rows = []
    for name in ["speed_only", "speed_time", "speed_reliability", "speed_volatility", "full_features"]:
        g = group[(group["split"] == "test") & (group["ablation_group"] == name)]
        h = horizon[(horizon["split"] == "test") & (horizon["ablation_group"] == name)]
        best = h.loc[h["MAE"].idxmin()]
        s = speed[(speed["split"] == "test") & (speed["ablation_group"] == name)]
        se = seasonal[(seasonal["split"] == "test") & (seasonal["ablation_group"] == name)]
        rows.append([name, "TCN", 24, "1,3,6", g["MAE"].iloc[0], g["RMSE"].iloc[0], g["sMAPE"].iloc[0], int(best["horizon_hours"]), best["MAE"], s["improvement_percent_vs_speed_only"].mean(), se["improvement_percent_vs_seasonal"].mean(), interpretations[name]])
    pd.DataFrame(
        rows,
        columns=["ablation_group", "model", "history_hours", "horizons", "test_MAE_mean_across_horizons", "test_RMSE_mean_across_horizons", "test_sMAPE_mean_across_horizons", "best_horizon_hours", "best_horizon_MAE", "mean_improvement_percent_vs_speed_only", "mean_improvement_percent_vs_seasonal", "interpretation"],
    ).to_csv(TABLES / "final_ablation_summary.csv", index=False)


def write_history_summary() -> None:
    best = read_table("phase7_history_best_by_horizon.csv")
    hist = read_table("phase7_history_metrics_by_history.csv")
    vs = read_table("phase7_history_vs_seasonal.csv")
    rows = []
    for _, r in best.iterrows():
        imp = vs[(vs["history_hours"] == r["history_hours"]) & (vs["horizon_hours"] == r["horizon_hours"]) & (vs["split"] == "test")]["improvement_percent_vs_seasonal"].iloc[0]
        text = {1: "1h best history is 72h, indicating medium memory helps very short-horizon correction.", 3: "3h best history is 168h, indicating weekly input context can help this horizon.", 6: "6h best history is 24h, indicating recent dynamics dominate this horizon."}[int(r["horizon_hours"])]
        rows.append(["best_history_per_horizon", int(r["history_hours"]), int(r["horizon_hours"]), r["MAE"], r["RMSE"], r["sMAPE"], imp, True, text])
    for _, r in hist[hist["split"] == "test"].iterrows():
        text = "168h is slightly best overall, but optimal memory length is horizon-dependent." if int(r["history_hours"]) == 168 else "Overall history-level summary; do not interpret as universally best for every horizon."
        rows.append(["overall_by_history", int(r["history_hours"]), "all_1_3_6", r["MAE"], r["RMSE"], r["sMAPE"], np.nan, False, text])
    pd.DataFrame(
        rows,
        columns=["summary_type", "history_hours", "horizon_hours", "MAE", "RMSE", "sMAPE", "improvement_percent_vs_seasonal", "is_best_history_for_horizon", "interpretation"],
    ).to_csv(TABLES / "final_history_sensitivity_summary.csv", index=False)


def write_robustness_summary() -> None:
    base = read_table("phase8_robustness_metrics.csv")
    vol = read_table("phase8_error_by_volatility.csv")
    noise = read_table("phase8_noise_stress_metrics.csv")
    miss = read_table("phase8_missingness_stress_metrics.csv")
    rows = []
    for _, r in base.iterrows():
        rows.append(["base_metric", int(r["history_hours"]), int(r["horizon_hours"]), "clean_test", "base", int(r["n"]), r["MAE"], r["RMSE"], r["sMAPE"], "Base robustness evaluation using the Phase 7 best checkpoint."])
    for h, g in vol.groupby("horizon_hours"):
        low = g[g["volatility_bin"].astype(str).str.contains("q1")]
        high = g[g["volatility_bin"].astype(str).str.contains("q4")]
        rows.append(["volatility_stratification", "best_for_horizon", int(h), "input_volatility", "q4_high_vs_q1_low", int(high["n"].iloc[0]), high["MAE"].iloc[0], high["RMSE"].iloc[0], high["sMAPE"].iloc[0], f"High-volatility samples are dominant difficult cases; q4 MAE exceeds q1 by {fmt(high['MAE'].iloc[0] - low['MAE'].iloc[0])}."])
    for h, g in noise.groupby("horizon_hours"):
        b = g[g["noise_level"] == 0.0]
        high = g[g["noise_level"] == g["noise_level"].max()]
        rows.append(["noise_stress", int(high["history_hours"].iloc[0]), int(h), "noise_level", float(high["noise_level"].iloc[0]), int(high["n"].iloc[0]), high["MAE"].iloc[0], high["RMSE"].iloc[0], high["sMAPE"].iloc[0], f"Noise stress causes gradual degradation, not catastrophic failure; MAE change from base is {fmt(high['MAE'].iloc[0] - b['MAE'].iloc[0])}."])
    for h, g in miss.groupby("horizon_hours"):
        b = g[g["missing_level"] == 0.0]
        high = g[g["missing_level"] == g["missing_level"].max()]
        rows.append(["missingness_stress", int(high["history_hours"].iloc[0]), int(h), "missing_level", float(high["missing_level"].iloc[0]), int(high["n"].iloc[0]), high["MAE"].iloc[0], high["RMSE"].iloc[0], high["sMAPE"].iloc[0], f"Missingness stress causes gradual but milder degradation than noise; MAE change from base is {fmt(high['MAE'].iloc[0] - b['MAE'].iloc[0])}."])
    pd.DataFrame(
        rows,
        columns=["summary_type", "history_hours", "horizon_hours", "condition", "level", "n", "MAE", "RMSE", "sMAPE", "interpretation"],
    ).to_csv(TABLES / "final_robustness_summary.csv", index=False)


def write_seed_summary(seed_label: str, summary: pd.DataFrame) -> None:
    rows = []
    for _, r in summary.iterrows():
        if int(r["horizon_hours"]) == 6:
            text = "6h is the most stable horizon among the repeated-seed runs."
        elif int(r["horizon_hours"]) == 1:
            text = "1h has slightly larger seed variation but remains consistently better than the strong baseline."
        else:
            text = "3h remains consistently better than the strong baseline with moderate seed variation."
        rows.append([int(r["horizon_hours"]), int(r["history_hours"]), int(r["seed_count"]), r["MAE_mean"], r["MAE_std"], r["MAE_cv"], bool(r["all_seeds_outperform_seasonal"]), r["mean_improvement_percent_vs_seasonal"], seed_label, text])
    pd.DataFrame(
        rows,
        columns=["horizon_hours", "history_hours", "seed_count", "MAE_mean", "MAE_std", "MAE_cv", "all_seeds_outperform_seasonal", "mean_improvement_percent_vs_seasonal", "source_phase", "interpretation"],
    ).to_csv(TABLES / "final_seed_stability_summary.csv", index=False)


def write_findings(seed_label: str, seed_summary: pd.DataFrame, phase10_done: bool) -> None:
    seed_count = int(seed_summary["seed_count"].max())
    all_flag = bool(seed_summary["all_seeds_outperform_seasonal"].all())
    phase10_metric = (
        "METR-LA-mini five-seed sanity check completed; TCN outperforms HistoricalAverage but not Persistence."
        if phase10_done
        else "Phase 10 code was prepared but not executed."
    )
    phase10_interpretation = "Supports pipeline portability, not public benchmark superiority." if phase10_done else "No public-data empirical claim is made."
    rows = [
        ["F1", "The Pan Borneo 1h forecasting panel and leakage-free windows are feasible for short/medium horizon forecasting.", "Phase 1; Phase 2", "51 monitoring points; high 1h coverage; leakage-free chronological windows", "The dataset supports a reproducible corridor-scale forecasting experiment.", "The 168h prediction horizon remains a stress test, not the main task."],
        ["F2", "SeasonalHistoricalAverage is a strong baseline.", "Phase 3", "SeasonalHistoricalAverage test MAE is substantially lower than Persistence and HistoricalAverage overall.", "Periodic point-hour-day structure is strong and must be treated as a serious comparator.", "Do not compare deep models only against weak baselines."],
        ["F3", "Controlled deep models improve short/medium horizons but do not dominate all horizons.", "Phase 5", "TCN/LSTM improve over seasonal baseline at 1h, 3h and 6h; 12h and 24h are worse.", "Deep models add dynamic correction for short/medium horizons.", "Do not claim universal deep learning dominance."],
        ["F4", "TCN speed-only is the strongest direct forecasting feature configuration.", "Phase 6", "speed_only mean MAE 0.8951 across 1h/3h/6h, best among ablation groups.", "Recent speed history is the dominant predictive signal.", "Reliability features did not consistently improve direct accuracy."],
        ["F5", "Reliability indicators are useful for diagnosis and robustness interpretation.", "Phase 6; Phase 8", "Ablation does not improve direct accuracy; robustness strata expose volatility and coverage-related error patterns.", "Reliability-aware analysis is valuable as diagnostic evidence under sparse FCD conditions.", "Frame reliability-aware contribution as diagnosis/robustness, not guaranteed accuracy improvement."],
        ["F6", "Optimal history length is horizon-dependent.", "Phase 7", "Best histories: 72h for 1h, 168h for 3h, 24h for 6h.", "Memory length should be tuned by horizon rather than fixed as longest available context.", "Do not claim longer history is always better."],
        ["F7", "High volatility is the main difficult-sample source.", "Phase 8", "High-volatility bins have much higher MAE than low-volatility bins across horizons.", "Traffic state instability, rather than only missingness, drives hard cases.", "Volatility is diagnostic and should not be computed from the target window."],
        ["F8", "The core TCN advantage is stable across random seeds.", seed_label, f"{seed_count} seeds evaluated; all seeds outperform SeasonalHistoricalAverage for all core horizons is {all_flag}.", "The main predictive claim is not an artifact of a single random initialization.", "Seed stability is evidence for robustness, not exhaustive uncertainty quantification."],
        ["F9", "The public benchmark check supports pipeline portability only.", "Phase 10", phase10_metric, phase10_interpretation, "Do not claim SOTA performance or public benchmark dominance."],
    ]
    pd.DataFrame(rows, columns=["finding_id", "finding", "supporting_phase", "supporting_metric", "paper_interpretation", "caution_or_limitation"]).to_csv(TABLES / "final_empirical_findings_summary.csv", index=False)


def phase10_report_text(phase10_done: bool, phase10_summary: pd.DataFrame) -> str:
    if not phase10_done or phase10_summary.empty:
        return "Phase 10 was prepared but not executed because public benchmark mini data were unavailable."
    row = phase10_summary.iloc[0]
    return (
        f"Phase 10 completed as a supplementary public benchmark sanity check on {row['dataset']} with "
        f"{int(row['seed_count'])} seeds. TCN speed-only achieved MAE_mean={fmt(row['MAE_mean'])}, "
        f"MAE_std={fmt(row['MAE_std'])}, and MAE_cv={fmt(row['MAE_cv'])}. It outperformed HistoricalAverage "
        f"for all seeds ({row['outperforms_historical_average_all_seeds']}) but did not outperform Persistence "
        f"for all seeds ({row['outperforms_persistence_all_seeds']}). This supports pipeline portability, not "
        "public benchmark superiority."
    )


def write_reports(seed_label: str, seed_summary: pd.DataFrame, phase10_done: bool, phase10_summary: pd.DataFrame) -> None:
    seed_count = int(seed_summary["seed_count"].max())
    all_flag = bool(seed_summary["all_seeds_outperform_seasonal"].all())
    seed_lines = [
        f"- {int(r['horizon_hours'])}h horizon, {int(r['history_hours'])}h history: MAE_mean={fmt(r['MAE_mean'])}, MAE_std={fmt(r['MAE_std'])}, MAE_cv={fmt(r['MAE_cv'])}, all seeds outperform seasonal={r['all_seeds_outperform_seasonal']}."
        for _, r in seed_summary.iterrows()
    ]
    master = f"""# Experiment Master Summary

## Scope
This summary consolidates the locked Pan Borneo FCD forecasting experiment. Phase 10 is treated as a supplementary public benchmark sanity check only.

## Main Findings
- The 1h panel and leakage-free windows support short/medium-horizon forecasting.
- SeasonalHistoricalAverage is a strong periodic baseline.
- Deep models improve 1h, 3h and 6h horizons, but not 12h and 24h.
- TCN speed-only is the strongest direct forecasting configuration.
- Reliability indicators are useful for diagnosis and robustness interpretation, not direct accuracy improvement in this high-coverage dataset.
- Optimal history length is horizon-dependent.
- High volatility is the main difficult-sample source.

## Seed Stability
The seed-stability summary uses {seed_label} results with {seed_count} seeds.
All seeds outperform SeasonalHistoricalAverage for every core horizon: {all_flag}.
{chr(10).join(seed_lines)}

## Phase 10 Status
{phase10_report_text(phase10_done, phase10_summary)}
"""
    (REPORTS / "experiment_master_summary.md").write_text(master, encoding="utf-8")

    figure_plan = """# Final Figure Plan

No image files are generated in Phase 11. This is a plotting plan only.

## Fig. 1 Overall experimental workflow
- Source CSV file: `outputs/tables/final_phase_status_summary.csv`
- Variables to plot: phase, experiment_name, status, main_scope
- Expected message: complete reproducible workflow from audit to stability testing.
- Placement: main text

## Fig. 2 Data coverage and window feasibility
- Source CSV file: `outputs/tables/coverage_by_point.csv`, `outputs/tables/window_feasibility_by_horizon.csv`
- Variables to plot: coverage ratio and feasible window counts
- Expected message: main horizons are feasible; 168h horizon is a stress test.
- Placement: main text or appendix

## Fig. 3 Baseline vs deep model performance
- Source CSV file: `outputs/tables/final_main_forecasting_results.csv`
- Variables to plot: model, horizon_hours, MAE, improvement_percent_vs_seasonal
- Expected message: deep models improve 1h/3h/6h but not 12h/24h.
- Placement: main text

## Fig. 4 Feature ablation results
- Source CSV file: `outputs/tables/final_ablation_summary.csv`
- Variables to plot: ablation_group, MAE
- Expected message: speed-only is strongest overall.
- Placement: main text

## Fig. 5 History-length sensitivity
- Source CSV file: `outputs/tables/final_history_sensitivity_summary.csv`
- Variables to plot: history_hours, horizon_hours, MAE
- Expected message: optimal memory length is horizon-dependent.
- Placement: main text

## Fig. 6 Volatility-stratified prediction error
- Source CSV file: `outputs/tables/phase8_error_by_volatility.csv`
- Variables to plot: horizon_hours, volatility_bin, MAE
- Expected message: high-volatility windows are the dominant difficult cases.
- Placement: main text

## Fig. 7 Noise and missingness robustness
- Source CSV file: `outputs/tables/phase8_noise_stress_metrics.csv`, `outputs/tables/phase8_missingness_stress_metrics.csv`
- Variables to plot: perturbation level, horizon_hours, MAE
- Expected message: perturbations cause gradual degradation.
- Placement: main text or appendix

## Fig. 8 Repeated-seed stability
- Source CSV file: `outputs/tables/final_seed_stability_summary.csv`
- Variables to plot: horizon_hours, MAE_mean, MAE_std
- Expected message: seed-stability conclusion uses Phase 9B five-seed results when available.
- Placement: main text

## Fig. 9 Supplementary public benchmark sanity check
- Source CSV file: `outputs/tables/final_public_benchmark_summary.csv`
- Variables to plot: dataset, MAE_mean, MAE_std, outperforms_historical_average_all_seeds, outperforms_persistence_all_seeds
- Expected message: the TCN speed-only pipeline runs on public traffic data, but this is portability evidence rather than public benchmark superiority.
- Placement: appendix or supplementary material
"""
    (REPORTS / "final_figure_plan.md").write_text(figure_plan, encoding="utf-8")

    outline = """# Final Results Section Outline

## 4.1 Data Audit and Forecasting-Window Feasibility
Report audit and leakage-free window construction.

## 4.2 Strong Baseline Performance
Present SeasonalHistoricalAverage as the strong comparator.

## 4.3 Controlled Deep Learning Performance
State that deep models improve 1h, 3h and 6h, but do not dominate all horizons.

## 4.4 Feature Ablation
State that TCN speed-only is strongest for direct forecasting. Reliability indicators are diagnostic.

## 4.5 History-Length Sensitivity
State that the best history length is horizon-dependent.

## 4.6 Robustness and Difficult-Sample Diagnosis
State that high volatility is the main difficult-sample source.

## 4.7 Repeated-Seed Stability
Use Phase 9B five-seed results if available; otherwise use Phase 9 three-seed results. Claim that all seeds outperform SeasonalHistoricalAverage only if the table flag is true.

## 4.8 Summary of Empirical Findings
Summarize the reproducible workflow, short/medium-horizon TCN speed-only advantage, diagnostic role of reliability indicators, horizon-dependent memory, and Phase 10 status.

## Appendix: Supplementary Public Benchmark Sanity Check
If Phase 10 outputs exist, report METR-LA-mini as a supplementary sanity check only. State that TCN speed-only completed five-seed runs and outperformed HistoricalAverage, but did not outperform Persistence. Do not claim SOTA or benchmark dominance.
"""
    (REPORTS / "final_results_section_outline.md").write_text(outline, encoding="utf-8")


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    seed_label, seed_summary, seed_metrics = seed_source()
    phase10_done, phase10_summary = phase10_source()
    write_phase_status(seed_label, phase10_done)
    write_main_results(seed_label, seed_summary, seed_metrics)
    write_ablation_summary()
    write_history_summary()
    write_robustness_summary()
    write_seed_summary(seed_label, seed_summary)
    write_findings(seed_label, seed_summary, phase10_done)
    write_reports(seed_label, seed_summary, phase10_done, phase10_summary)
    print(f"Phase 11 summary files updated using {seed_label} seed-stability results.")


if __name__ == "__main__":
    main()
