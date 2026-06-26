from __future__ import annotations

import argparse
import csv
import logging
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def read_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("phase2_window_construction")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def split_ranges(times: pd.Series, ratios: list[float]) -> dict[str, tuple[pd.Timestamp, pd.Timestamp]]:
    n = len(times)
    train_end_idx = max(0, int(np.floor(n * ratios[0])) - 1)
    val_end_idx = max(train_end_idx + 1, int(np.floor(n * (ratios[0] + ratios[1]))) - 1)
    return {
        "train": (times.iloc[0], times.iloc[train_end_idx]),
        "val": (times.iloc[train_end_idx + 1], times.iloc[val_end_idx]),
        "test": (times.iloc[val_end_idx + 1], times.iloc[-1]),
    }


def assign_split(
    input_start: pd.Timestamp,
    target_end: pd.Timestamp,
    ranges: dict[str, tuple[pd.Timestamp, pd.Timestamp]],
) -> str | None:
    for split, (start, end) in ranges.items():
        if input_start >= start and target_end <= end:
            return split
    return None


def available_targets(df: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    rows = []
    for target_name, column in cfg["targets"]["preferred"].items():
        if column not in df.columns:
            rows.append(
                {
                    "target_variable": target_name,
                    "source_column": column,
                    "available": False,
                    "non_missing_count": 0,
                    "missing_rate": np.nan,
                    "mean": np.nan,
                    "std": np.nan,
                    "min": np.nan,
                    "max": np.nan,
                    "recommended_main_target": False,
                }
            )
            continue
        s = pd.to_numeric(df[column], errors="coerce")
        rows.append(
            {
                "target_variable": target_name,
                "source_column": column,
                "available": True,
                "non_missing_count": int(s.notna().sum()),
                "missing_rate": float(s.isna().mean()),
                "mean": float(s.mean()),
                "std": float(s.std()),
                "min": float(s.min()),
                "max": float(s.max()),
                "recommended_main_target": target_name == "speed",
            }
        )
    return pd.DataFrame(rows)


def weekend_flag(day_of_week: int) -> int:
    return int(day_of_week >= 5)


def safe_ratio(values: np.ndarray) -> float:
    if len(values) == 0:
        return np.nan
    return float(np.nanmean(values))


def std_or_zero(values: np.ndarray) -> float:
    values = values[~np.isnan(values)]
    if len(values) <= 1:
        return 0.0
    return float(np.std(values, ddof=1))


def build_windows(cfg: dict, logger: logging.Logger) -> None:
    paths = cfg["paths"]
    out_tables = Path(paths["output_tables"])
    processed = Path(paths["processed"])
    reports = Path(paths["reports"])
    out_tables.mkdir(parents=True, exist_ok=True)
    processed.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(paths["primary_panel"], parse_dates=["time_bin"])
    df = df.sort_values(["node_id", "time_bin"]).reset_index(drop=True)
    logger.info("Loaded primary panel with %s rows and %s points", len(df), df["node_id"].nunique())

    quality = pd.read_csv(paths["point_quality"])
    quality_map = dict(zip(quality["point_id"], quality["coverage_group"]))
    point_code_map = {point: idx for idx, point in enumerate(sorted(df["node_id"].unique()))}
    point_meta = pd.DataFrame(
        {
            "point_id": list(point_code_map.keys()),
            "point_code": list(point_code_map.values()),
            "point_quality_group": [quality_map.get(p, "unknown") for p in point_code_map.keys()],
        }
    )
    point_meta.to_csv(processed / "point_metadata.csv", index=False, encoding="utf-8-sig")

    target_summary = available_targets(df, cfg)
    target_summary.to_csv(out_tables / "target_variable_summary.csv", index=False, encoding="utf-8-sig")
    targets = target_summary[target_summary["available"]].copy()
    if targets.empty:
        raise ValueError("No configured target variables were found in the primary panel.")
    logger.info("Available targets: %s", targets["target_variable"].tolist())

    all_times = pd.Series(pd.to_datetime(sorted(df["time_bin"].unique())))
    ranges = split_ranges(all_times, cfg["windowing"]["split_ratios"])
    logger.info("Chronological split ranges: %s", ranges)

    histories = cfg["windowing"]["histories_hours"]
    main_horizons = cfg["windowing"]["main_horizons_hours"]
    extended_horizons = cfg["windowing"]["extended_horizons_hours"]
    combos = []
    for history in histories:
        horizons = list(main_horizons)
        if history == 168:
            horizons += list(extended_horizons)
        for horizon in horizons:
            combos.append((int(history), int(horizon)))

    output_path = out_tables / "window_index_all.csv"
    columns = [
        "window_id",
        "point_id",
        "point_code",
        "input_start_time",
        "input_end_time",
        "target_start_time",
        "target_end_time",
        "history_hours",
        "horizon_hours",
        "split",
        "target_variable",
        "target_source_column",
        "input_observed_ratio",
        "target_observed_ratio",
        "is_main_forecast",
        "is_extended_horizon",
        "missing_mask_ratio",
        "coverage_ratio_24h",
        "coverage_ratio_72h",
        "recent_volatility_24h",
        "hour_of_day",
        "day_of_week",
        "weekend_flag",
        "point_quality_group",
        "leakage_check_passed",
    ]

    feasibility = defaultdict(lambda: {"candidate_windows": 0, "valid_windows": 0})
    split_counts = defaultdict(int)
    point_counts = defaultdict(int)
    missingness = defaultdict(lambda: {"count": 0, "input_ratio_sum": 0.0, "target_ratio_sum": 0.0, "missing_ratio_sum": 0.0})
    leakage_failures = 0
    total_rows = 0
    min_input_ratio = float(cfg["windowing"]["minimum_input_observed_ratio_for_feasible"])
    min_target_ratio = float(cfg["windowing"]["minimum_target_observed_ratio_for_feasible"])

    with output_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        window_id = 0

        for point_id, g in df.groupby("node_id", sort=True):
            g = g.sort_values("time_bin").reset_index(drop=True)
            times = g["time_bin"].to_numpy()
            obs = pd.to_numeric(g["has_observation"], errors="coerce").fillna(0).to_numpy(dtype=float)
            missing_mask = pd.to_numeric(g["missing_mask"], errors="coerce").fillna(1).to_numpy(dtype=float)
            tti_input = pd.to_numeric(g.get("tti_input", g.get("tti")), errors="coerce").to_numpy(dtype=float)
            point_quality = quality_map.get(point_id, "unknown")
            point_code = point_code_map[point_id]

            target_arrays = {
                row["target_variable"]: pd.to_numeric(g[row["source_column"]], errors="coerce").to_numpy(dtype=float)
                for _, row in targets.iterrows()
            }
            target_source_cols = dict(zip(targets["target_variable"], targets["source_column"]))

            n = len(g)
            obs_csum = np.r_[0.0, np.cumsum(obs)]
            missing_csum = np.r_[0.0, np.cumsum(missing_mask)]

            for history_hours, horizon_hours in combos:
                history_steps = history_hours
                horizon_steps = horizon_hours
                max_start = n - history_steps - horizon_steps + 1
                if max_start <= 0:
                    continue
                is_extended = int(horizon_hours in extended_horizons)
                is_main = int(not is_extended)

                for start_idx in range(max_start):
                    input_start_idx = start_idx
                    input_end_idx = start_idx + history_steps - 1
                    target_start_idx = start_idx + history_steps
                    target_end_idx = target_start_idx + horizon_steps - 1

                    input_start = pd.Timestamp(times[input_start_idx])
                    input_end = pd.Timestamp(times[input_end_idx])
                    target_start = pd.Timestamp(times[target_start_idx])
                    target_end = pd.Timestamp(times[target_end_idx])
                    split = assign_split(input_start, target_end, ranges)
                    if split is None:
                        continue

                    leakage_ok = input_end < target_start
                    if not leakage_ok:
                        leakage_failures += len(target_arrays)

                    input_obs_ratio = (obs_csum[input_end_idx + 1] - obs_csum[input_start_idx]) / history_steps
                    input_missing_ratio = (missing_csum[input_end_idx + 1] - missing_csum[input_start_idx]) / history_steps
                    last_24_start = max(input_start_idx, input_end_idx - 24 + 1)
                    last_72_start = max(input_start_idx, input_end_idx - 72 + 1)
                    cov_24 = (obs_csum[input_end_idx + 1] - obs_csum[last_24_start]) / (input_end_idx - last_24_start + 1)
                    cov_72 = (obs_csum[input_end_idx + 1] - obs_csum[last_72_start]) / (input_end_idx - last_72_start + 1)
                    vol_24 = std_or_zero(tti_input[last_24_start : input_end_idx + 1])
                    hod = int(input_end.hour)
                    dow = int(input_end.dayofweek)

                    for target_name, target_values in target_arrays.items():
                        target_slice = target_values[target_start_idx : target_end_idx + 1]
                        target_obs_ratio = float(np.isfinite(target_slice).mean())
                        row = {
                            "window_id": window_id,
                            "point_id": point_id,
                            "point_code": point_code,
                            "input_start_time": input_start,
                            "input_end_time": input_end,
                            "target_start_time": target_start,
                            "target_end_time": target_end,
                            "history_hours": history_hours,
                            "horizon_hours": horizon_hours,
                            "split": split,
                            "target_variable": target_name,
                            "target_source_column": target_source_cols[target_name],
                            "input_observed_ratio": round(float(input_obs_ratio), 6),
                            "target_observed_ratio": round(target_obs_ratio, 6),
                            "is_main_forecast": is_main,
                            "is_extended_horizon": is_extended,
                            "missing_mask_ratio": round(float(input_missing_ratio), 6),
                            "coverage_ratio_24h": round(float(cov_24), 6),
                            "coverage_ratio_72h": round(float(cov_72), 6),
                            "recent_volatility_24h": round(float(vol_24), 6),
                            "hour_of_day": hod,
                            "day_of_week": dow,
                            "weekend_flag": weekend_flag(dow),
                            "point_quality_group": point_quality,
                            "leakage_check_passed": int(leakage_ok),
                        }
                        writer.writerow(row)

                        key = (history_hours, horizon_hours, target_name, is_main, is_extended)
                        feasibility[key]["candidate_windows"] += 1
                        if input_obs_ratio >= min_input_ratio and target_obs_ratio >= min_target_ratio:
                            feasibility[key]["valid_windows"] += 1
                        split_counts[(split, history_hours, horizon_hours, target_name)] += 1
                        point_counts[(point_id, history_hours, horizon_hours, target_name)] += 1
                        miss_key = (history_hours, horizon_hours, target_name)
                        missingness[miss_key]["count"] += 1
                        missingness[miss_key]["input_ratio_sum"] += float(input_obs_ratio)
                        missingness[miss_key]["target_ratio_sum"] += float(target_obs_ratio)
                        missingness[miss_key]["missing_ratio_sum"] += float(input_missing_ratio)
                        window_id += 1
                        total_rows += 1

            logger.info("Processed point %s; cumulative window rows=%s", point_id, total_rows)

    feasibility_rows = []
    for (history, horizon, target, is_main, is_extended), vals in sorted(feasibility.items()):
        cand = vals["candidate_windows"]
        valid = vals["valid_windows"]
        feasibility_rows.append(
            {
                "history_hours": history,
                "horizon_hours": horizon,
                "target_variable": target,
                "is_main_forecast": is_main,
                "is_extended_horizon": is_extended,
                "candidate_windows": cand,
                "valid_windows_min_80pct_observed": valid,
                "valid_window_ratio": valid / cand if cand else np.nan,
                "feasible_as_main_experiment": bool(is_main and valid >= 1000 and valid / cand >= 0.50) if cand else False,
            }
        )
    feasibility_df = pd.DataFrame(feasibility_rows)
    feasibility_df.to_csv(out_tables / "window_feasibility_by_horizon.csv", index=False, encoding="utf-8-sig")

    split_rows = [
        {
            "split": split,
            "history_hours": history,
            "horizon_hours": horizon,
            "target_variable": target,
            "window_count": count,
        }
        for (split, history, horizon, target), count in sorted(split_counts.items())
    ]
    pd.DataFrame(split_rows).to_csv(out_tables / "window_count_by_split.csv", index=False, encoding="utf-8-sig")

    point_rows = [
        {
            "point_id": point,
            "history_hours": history,
            "horizon_hours": horizon,
            "target_variable": target,
            "window_count": count,
            "point_quality_group": quality_map.get(point, "unknown"),
        }
        for (point, history, horizon, target), count in sorted(point_counts.items())
    ]
    point_df = pd.DataFrame(point_rows)
    point_df.to_csv(out_tables / "window_count_by_point.csv", index=False, encoding="utf-8-sig")

    missing_rows = []
    for (history, horizon, target), vals in sorted(missingness.items()):
        count = vals["count"]
        missing_rows.append(
            {
                "history_hours": history,
                "horizon_hours": horizon,
                "target_variable": target,
                "window_count": count,
                "mean_input_observed_ratio": vals["input_ratio_sum"] / count if count else np.nan,
                "mean_target_observed_ratio": vals["target_ratio_sum"] / count if count else np.nan,
                "mean_input_missing_mask_ratio": vals["missing_ratio_sum"] / count if count else np.nan,
            }
        )
    pd.DataFrame(missing_rows).to_csv(out_tables / "window_missingness_summary.csv", index=False, encoding="utf-8-sig")

    model_ready_cols = [
        "node_id",
        "time_bin",
        "current_speed",
        "current_travel_time",
        "tti",
        "travel_time_delay",
        "missing_mask",
        "coverage_ratio_24h",
        "volatility_tti_6h",
        "hour",
        "day_of_week",
    ]
    existing_cols = [c for c in model_ready_cols if c in df.columns]
    df[existing_cols].to_csv(processed / "phase2_panel_1h_model_ready.csv.gz", index=False, compression="gzip")

    write_report(
        reports / "phase2_window_construction_report.md",
        target_summary,
        feasibility_df,
        pd.DataFrame(split_rows),
        point_df,
        leakage_failures,
        total_rows,
        ranges,
        logger,
    )
    logger.info("Wrote %s rows to %s", total_rows, output_path)


def dataframe_to_markdown(df: pd.DataFrame, max_rows: int = 30) -> str:
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


def write_report(
    path: Path,
    target_summary: pd.DataFrame,
    feasibility: pd.DataFrame,
    split_counts: pd.DataFrame,
    point_counts: pd.DataFrame,
    leakage_failures: int,
    total_rows: int,
    ranges: dict[str, tuple[pd.Timestamp, pd.Timestamp]],
    logger: logging.Logger,
) -> None:
    target_available = target_summary[target_summary["available"]]
    recommended = target_summary[target_summary["recommended_main_target"] & target_summary["available"]]
    recommended_name = recommended["target_variable"].iloc[0] if not recommended.empty else target_available["target_variable"].iloc[0]
    main_feas = feasibility[feasibility["is_main_forecast"] == 1]
    extended = feasibility[feasibility["is_extended_horizon"] == 1]
    low_valid = feasibility[feasibility["valid_window_ratio"] < 0.50]
    excluded_points = []
    if not point_counts.empty:
        totals = point_counts.groupby("point_id")["window_count"].sum()
        excluded_points = totals[totals == 0].index.tolist()

    split_total = split_counts.groupby("split", as_index=False)["window_count"].sum() if not split_counts.empty else pd.DataFrame()
    combo_total = feasibility.groupby(["history_hours", "horizon_hours", "is_main_forecast", "is_extended_horizon"], as_index=False).agg(
        candidate_windows=("candidate_windows", "sum"),
        valid_windows_min_80pct_observed=("valid_windows_min_80pct_observed", "sum"),
    )

    lines = [
        "# Phase 2 Window Construction Report",
        "",
        "## Scope",
        "Phase 2 constructed leakage-free sliding-window indices only. No model training was run.",
        "",
        "## Target Variables",
        dataframe_to_markdown(target_summary),
        "",
        f"Recommended main prediction target: `{recommended_name}`. It is preferred because speed is directly available, interpretable, and has the same missing rate as the primary traffic fields.",
        "",
        "## Chronological Split",
        *[f"- {name}: {start} to {end}" for name, (start, end) in ranges.items()],
        "",
        "The strict Phase 2 rule requires input and target timestamps to be fully contained inside the assigned split.",
        "",
        "## Window Counts by History-Horizon",
        dataframe_to_markdown(combo_total),
        "",
        "## Window Counts by Split",
        dataframe_to_markdown(split_total),
        "",
        "## Horizon Feasibility",
        f"- Main horizons 1h, 3h, 6h, 12h, and 24h are feasible when judged by the 80% input/target observed-ratio rule: {bool(main_feas['feasible_as_main_experiment'].all())}.",
        f"- 168h is retained as extended stress-test only: {not extended.empty}.",
        f"- Horizon/target combinations below 50% valid ratio: {len(low_valid)}.",
        f"- Points excluded: {excluded_points if excluded_points else 'none'}.",
        f"- Leakage failures detected: {leakage_failures}.",
        f"- Total rows in `window_index_all.csv`: {total_rows:,}.",
        "",
        "## Leakage Controls",
        "- `input_end_time < target_start_time` for every emitted window.",
        "- Train, validation, and test samples are assigned only when both input and target stay within the same chronological split.",
        "- Reliability fields such as coverage ratios and recent volatility are computed from the input window only.",
        "",
        "## Phase 3 Recommendation",
        "Run baseline models only: Persistence, Historical Average, and optionally ARIMA/Random Forest after verifying the baseline feature matrix. Use `speed` as the first target, then repeat for `travel_time` and `tti` if baseline logs are clean.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Wrote report to %s", path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase2_window_construction.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    logger = setup_logger(Path(cfg["paths"]["output_logs"]) / "phase2_window_construction.log")
    logger.info("Starting Phase 2 window construction")
    build_windows(cfg, logger)
    logger.info("Phase 2 window construction completed")


if __name__ == "__main__":
    main()
