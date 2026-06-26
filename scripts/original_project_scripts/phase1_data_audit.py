from __future__ import annotations

import argparse
import gzip
import json
import logging
import math
import shutil
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def setup_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("phase1_data_audit")
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


def read_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_package_extracted(package_zip: Path, extracted_root: Path, logger: logging.Logger) -> None:
    marker = extracted_root / "README.md"
    if marker.exists():
        logger.info("Package already extracted at %s", extracted_root)
        return
    extracted_root.mkdir(parents=True, exist_ok=True)
    logger.info("Extracting %s to %s", package_zip, extracted_root)
    with zipfile.ZipFile(package_zip, "r") as zf:
        zf.extractall(extracted_root)


def list_inventory(extracted_root: Path) -> pd.DataFrame:
    rows = []
    for p in sorted(extracted_root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(extracted_root).as_posix()
        rows.append(
            {
                "relative_path": rel,
                "absolute_path": str(p.resolve()),
                "file_name": p.name,
                "extension": "".join(p.suffixes),
                "size_bytes": p.stat().st_size,
                "role_in_project": infer_role(rel),
                "row_count": np.nan,
                "column_count": np.nan,
                "columns": "",
            }
        )
    return pd.DataFrame(rows)


def infer_role(rel: str) -> str:
    low = rel.lower()
    if "panel_1h" in low:
        return "primary regular hourly panel candidate"
    if "panel_30min" in low:
        return "regular 30-minute panel candidate"
    if "panel_15min" in low:
        return "observed-only 15-minute panel"
    if "cleaned_records" in low:
        return "cleaned raw observation records"
    if "nodes" in low:
        return "monitoring point metadata"
    if "adjacency" in low:
        return "spatial graph metadata"
    if "audit" in low:
        return "previous audit artifact"
    if "documentation" in low or "readme" in low:
        return "documentation"
    return "raw/source artifact"


def read_table(path: Path, parse_dates: list[str] | None = None) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=parse_dates)


def csv_header_and_count(path: Path) -> tuple[int, int, str]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", errors="replace", newline="") as f:
        header = f.readline().rstrip("\n").split(",")
        count = 0
        for count, _ in enumerate(f, start=1):
            pass
    return count, len(header), "|".join(header)


def enrich_inventory(inv: pd.DataFrame, extracted_root: Path, logger: logging.Logger) -> pd.DataFrame:
    csv_mask = inv["extension"].isin([".csv", ".csv.gz"])
    for idx, row in inv[csv_mask].iterrows():
        p = extracted_root / row["relative_path"]
        try:
            nrows, ncols, cols = csv_header_and_count(p)
            inv.loc[idx, ["row_count", "column_count", "columns"]] = [nrows, ncols, cols]
        except Exception as exc:
            logger.warning("Could not scan %s: %s", p, exc)
    return inv


def infer_fields(df: pd.DataFrame) -> dict:
    cols = list(df.columns)
    lower = {c.lower(): c for c in cols}

    def first(candidates: list[str]) -> str | None:
        for cand in candidates:
            if cand in lower:
                return lower[cand]
        for c in cols:
            lc = c.lower()
            if any(cand in lc for cand in candidates):
                return c
        return None

    return {
        "point_id": first(["node_id", "point_id", "monitoring_point", "station_id", "sensor_id"]),
        "timestamp": first(["time_bin", "event_time", "timestamp", "datetime", "time"]),
        "speed": first(["current_speed", "speed"]),
        "free_flow_speed": first(["free_flow_speed"]),
        "travel_time": first(["current_travel_time", "travel_time"]),
        "free_flow_travel_time": first(["free_flow_travel_time"]),
        "congestion": first(["tti", "congestion", "congestion_index", "speed_deficit_ratio"]),
        "has_observation": first(["has_observation", "observed"]),
        "missing_mask": first(["missing_mask", "missing"]),
        "observed_count": first(["observed_count"]),
    }


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    n = len(df)
    for col in df.columns:
        missing = int(df[col].isna().sum())
        rows.append(
            {
                "column": col,
                "dtype": str(df[col].dtype),
                "missing_count": missing,
                "missing_rate": missing / n if n else np.nan,
                "unique_count": int(df[col].nunique(dropna=True)),
            }
        )
    return pd.DataFrame(rows)


def choose_frequency(timestamps: pd.Series) -> tuple[pd.Timedelta, str]:
    ordered = pd.Series(pd.to_datetime(timestamps.dropna().sort_values().unique()))
    diffs = ordered.diff().dropna()
    if diffs.empty:
        return pd.Timedelta(hours=1), "1h"
    mode = diffs.mode().iloc[0]
    seconds = int(mode.total_seconds())
    if seconds % 3600 == 0:
        return mode, f"{seconds // 3600}h"
    if seconds % 60 == 0:
        return mode, f"{seconds // 60}min"
    return mode, f"{seconds}s"


def coverage_by_point(df: pd.DataFrame, fields: dict, cfg: dict) -> pd.DataFrame:
    point_col = fields["point_id"]
    time_col = fields["timestamp"]
    has_col = fields["has_observation"]
    speed_col = fields["speed"]
    tt_col = fields["travel_time"]
    cong_col = fields["congestion"]
    freq_delta, _ = choose_frequency(df[time_col])
    rows = []
    global_start = df[time_col].min()
    global_end = df[time_col].max()
    global_expected = int(((global_end - global_start) / freq_delta) + 1)
    for point, g in df.groupby(point_col, sort=True):
        g = g.sort_values(time_col)
        duplicates = int(g.duplicated([point_col, time_col]).sum())
        first_time = g[time_col].min()
        last_time = g[time_col].max()
        expected = int(((last_time - first_time) / freq_delta) + 1) if pd.notna(first_time) else 0
        observed_steps = int(g[has_col].fillna(0).astype(int).sum()) if has_col else len(g)
        row_count = int(len(g))
        speed_anom = anomaly_count(g, speed_col, cfg["audit"]["speed_min_kmh"], cfg["audit"]["speed_max_kmh"])
        tt_anom = anomaly_count(g, tt_col, cfg["audit"]["travel_time_min_seconds"], cfg["audit"]["travel_time_max_seconds"])
        cong_anom = anomaly_count(g, cong_col, cfg["audit"]["tti_min"], cfg["audit"]["tti_max"])
        coverage = observed_steps / expected if expected else np.nan
        rows.append(
            {
                "point_id": point,
                "record_rows": row_count,
                "first_time": first_time,
                "last_time": last_time,
                "global_expected_steps": global_expected,
                "point_expected_steps": expected,
                "observed_steps": observed_steps,
                "coverage_ratio": coverage,
                "duplicate_timestamp_rows": duplicates,
                "speed_anomaly_count": speed_anom,
                "travel_time_anomaly_count": tt_anom,
                "congestion_anomaly_count": cong_anom,
                "coverage_group": coverage_group(coverage),
                "max_consecutive_missing_steps": max_consecutive_missing(g, has_col),
            }
        )
    out = pd.DataFrame(rows)
    return out.sort_values("point_id")


def anomaly_count(df: pd.DataFrame, col: str | None, low: float, high: float) -> int:
    if not col or col not in df.columns:
        return 0
    s = pd.to_numeric(df[col], errors="coerce")
    return int(((s < low) | (s > high)).fillna(False).sum())


def max_consecutive_missing(g: pd.DataFrame, has_col: str | None) -> int:
    if not has_col or has_col not in g.columns:
        return 0
    vals = g[has_col].fillna(0).astype(int).to_numpy()
    max_run = run = 0
    for v in vals:
        if v == 0:
            run += 1
            max_run = max(max_run, run)
        else:
            run = 0
    return int(max_run)


def coverage_group(x: float) -> str:
    if pd.isna(x):
        return "unknown"
    if x >= 0.80:
        return "high"
    if x >= 0.50:
        return "medium"
    return "low"


def time_coverage_summary(df: pd.DataFrame, fields: dict) -> pd.DataFrame:
    point_col = fields["point_id"]
    time_col = fields["timestamp"]
    has_col = fields["has_observation"]
    total_points = df[point_col].nunique()
    if has_col:
        out = (
            df.groupby(time_col)
            .agg(total_panel_rows=(point_col, "size"), observed_points=(has_col, lambda x: int(pd.to_numeric(x, errors="coerce").fillna(0).sum())))
            .reset_index()
        )
    else:
        out = df.groupby(time_col).agg(total_panel_rows=(point_col, "size"), observed_points=(point_col, "nunique")).reset_index()
    out["total_points"] = total_points
    out["coverage_ratio"] = out["observed_points"] / total_points
    out["date"] = out[time_col].dt.date.astype(str)
    return out


def continuity_check(df: pd.DataFrame, fields: dict) -> pd.DataFrame:
    point_col = fields["point_id"]
    time_col = fields["timestamp"]
    freq_delta, freq_label = choose_frequency(df[time_col])
    rows = []
    for point, g in df.groupby(point_col, sort=True):
        times = pd.Series(pd.to_datetime(g[time_col].dropna().sort_values().unique()))
        diffs = times.diff().dropna()
        rows.append(
            {
                "point_id": point,
                "inferred_frequency": freq_label,
                "unique_timestamps": int(len(times)),
                "gap_count_larger_than_frequency": int((diffs > freq_delta).sum()),
                "max_gap_hours": float(diffs.max().total_seconds() / 3600) if not diffs.empty else 0.0,
                "duplicate_timestamp_rows": int(g.duplicated([point_col, time_col]).sum()),
            }
        )
    return pd.DataFrame(rows)


def split_summary(df: pd.DataFrame, fields: dict, ratios: list[float]) -> pd.DataFrame:
    time_col = fields["timestamp"]
    point_col = fields["point_id"]
    times = pd.Series(pd.to_datetime(sorted(df[time_col].dropna().unique())))
    n = len(times)
    train_end_idx = max(0, int(math.floor(n * ratios[0])) - 1)
    val_end_idx = max(train_end_idx + 1, int(math.floor(n * (ratios[0] + ratios[1]))) - 1)
    splits = [
        ("train", 0, train_end_idx),
        ("val", train_end_idx + 1, val_end_idx),
        ("test", val_end_idx + 1, n - 1),
    ]
    rows = []
    for name, start_i, end_i in splits:
        if start_i > end_i or start_i >= n:
            rows.append({"split": name, "start_time": pd.NaT, "end_time": pd.NaT, "time_steps": 0, "rows": 0, "points": 0})
            continue
        start_t, end_t = times.iloc[start_i], times.iloc[end_i]
        mask = (df[time_col] >= start_t) & (df[time_col] <= end_t)
        rows.append(
            {
                "split": name,
                "start_time": start_t,
                "end_time": end_t,
                "time_steps": int(end_i - start_i + 1),
                "rows": int(mask.sum()),
                "points": int(df.loc[mask, point_col].nunique()),
            }
        )
    return pd.DataFrame(rows)


def window_feasibility(df: pd.DataFrame, fields: dict, cfg: dict) -> pd.DataFrame:
    point_col = fields["point_id"]
    time_col = fields["timestamp"]
    has_col = fields["has_observation"]
    horizons = cfg["audit"]["forecast_horizons_hours"]
    histories = cfg["audit"]["history_windows_hours"]
    freq_delta, freq_label = choose_frequency(df[time_col])
    step_hours = freq_delta.total_seconds() / 3600
    rows = []
    for history_h in histories:
        history_steps = int(round(history_h / step_hours))
        for horizon_h in horizons:
            horizon_steps = int(round(horizon_h / step_hours))
            valid_total = 0
            candidate_total = 0
            for _, g in df.groupby(point_col, sort=False):
                g = g.sort_values(time_col)
                obs = g[has_col].fillna(0).astype(int).to_numpy() if has_col else np.ones(len(g), dtype=int)
                n = len(obs)
                candidates = max(0, n - history_steps - horizon_steps + 1)
                candidate_total += candidates
                if candidates == 0:
                    continue
                csum = np.r_[0, np.cumsum(obs)]
                for i in range(candidates):
                    target_obs = csum[i + history_steps + horizon_steps] - csum[i + history_steps]
                    if target_obs == horizon_steps:
                        valid_total += 1
            rows.append(
                {
                    "history_hours": history_h,
                    "horizon_hours": horizon_h,
                    "frequency": freq_label,
                    "candidate_windows": int(candidate_total),
                    "fully_observed_target_windows": int(valid_total),
                    "fully_observed_target_window_ratio": valid_total / candidate_total if candidate_total else np.nan,
                }
            )
    return pd.DataFrame(rows)


def point_quality_summary(cov: pd.DataFrame, windows: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    out = cov.copy()
    threshold = cfg["audit"]["direct_1week_min_point_coverage"]
    out["meets_coverage_threshold_for_direct_1week"] = out["coverage_ratio"] >= threshold
    return out


def write_report(
    path: Path,
    inventory: pd.DataFrame,
    df: pd.DataFrame,
    fields: dict,
    cov: pd.DataFrame,
    missing: pd.DataFrame,
    time_cov: pd.DataFrame,
    continuity: pd.DataFrame,
    windows: pd.DataFrame,
    split: pd.DataFrame,
    logger: logging.Logger,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    direct = windows[(windows["history_hours"] == 168) & (windows["horizon_hours"] == 168)]
    direct_ratio = float(direct["fully_observed_target_window_ratio"].iloc[0]) if not direct.empty else np.nan
    direct_windows = int(direct["fully_observed_target_windows"].iloc[0]) if not direct.empty else 0
    one_day = windows[(windows["history_hours"] == 72) & (windows["horizon_hours"] == 24)]
    one_day_windows = int(one_day["fully_observed_target_windows"].iloc[0]) if not one_day.empty else 0
    suitable = direct_windows >= 100 and direct_ratio >= 0.05
    recommendation = "direct 7-day forecasting can be retained as a stress-test target, but it should not be the only task." if suitable else "use multi-horizon forecasting first, with 1h/3h/6h/12h/24h as primary horizons and 7-day as an extended sparse-data stress test."

    split_markdown = dataframe_to_markdown(split)
    lines = [
        "# Phase 1 Data Audit Report",
        "",
        "## Data Source",
        f"- Primary panel: `04_panels/panel_1h.csv.gz`",
        f"- Rows in primary panel: {len(df):,}",
        f"- Monitoring points: {df[fields['point_id']].nunique():,}",
        f"- Time range: {df[fields['timestamp']].min()} to {df[fields['timestamp']].max()}",
        f"- Inferred fields: `{json.dumps(fields, ensure_ascii=False)}`",
        "",
        "## Inventory",
        f"- Files scanned: {len(inventory):,}",
        f"- CSV/GZ files scanned with row counts: {inventory['row_count'].notna().sum():,}",
        "",
        "## Missingness and Coverage",
        f"- Median point coverage ratio: {cov['coverage_ratio'].median():.3f}",
        f"- Mean point coverage ratio: {cov['coverage_ratio'].mean():.3f}",
        f"- High/medium/low coverage points: {cov['coverage_group'].value_counts().to_dict()}",
        f"- Worst max consecutive missing steps: {int(cov['max_consecutive_missing_steps'].max())}",
        f"- Mean timestamp coverage ratio: {time_cov['coverage_ratio'].mean():.3f}",
        "",
        "## Continuity and Validity",
        f"- Duplicate point-timestamp rows in primary panel: {int(cov['duplicate_timestamp_rows'].sum())}",
        f"- Points with timeline gaps larger than inferred frequency: {int((continuity['gap_count_larger_than_frequency'] > 0).sum())}",
        f"- Speed anomaly rows: {int(cov['speed_anomaly_count'].sum())}",
        f"- Travel-time anomaly rows: {int(cov['travel_time_anomaly_count'].sum())}",
        f"- Congestion anomaly rows: {int(cov['congestion_anomaly_count'].sum())}",
        "",
        "## Train/Val/Test Split",
        split_markdown,
        "",
        "## One-Week Forecasting Feasibility",
        f"- Fully observed target windows for 168h history -> 168h horizon: {direct_windows:,}",
        f"- Ratio among candidate windows: {direct_ratio:.4f}",
        f"- Fully observed target windows for 72h history -> 24h horizon: {one_day_windows:,}",
        f"- Direct 1-week recommendation: {recommendation}",
        "",
        "## Required Output Files",
        "- `outputs/tables/data_inventory.csv`",
        "- `outputs/tables/missing_summary.csv`",
        "- `outputs/tables/coverage_by_point.csv`",
        "- `outputs/tables/time_coverage_summary.csv`",
        "- `outputs/tables/coverage_by_time.csv`",
        "- `outputs/tables/time_continuity_check.csv`",
        "- `outputs/tables/point_quality_summary.csv`",
        "- `outputs/tables/train_val_test_split_summary.csv`",
        "- `outputs/tables/window_feasibility_summary.csv`",
        "- `outputs/logs/phase1_data_audit.log`",
        "",
        "## Next Phase",
        "Build leakage-free rolling-window indices from the time-ordered split, retain missing masks and coverage/reliability variables, and begin with Persistence and Historical Average baselines before adding tree and neural models.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Wrote report to %s", path)


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_No rows._"
    cols = list(df.columns)
    lines = [
        "| " + " | ".join(cols) + " |",
        "| " + " | ".join(["---"] * len(cols)) + " |",
    ]
    for _, row in df.iterrows():
        vals = [str(row[col]) for col in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase1_data_audit.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))

    out_tables = Path(cfg["paths"]["output_tables"])
    out_logs = Path(cfg["paths"]["output_logs"])
    reports = Path(cfg["paths"]["reports"])
    for p in [out_tables, out_logs, reports]:
        p.mkdir(parents=True, exist_ok=True)
    logger = setup_logger(out_logs / "phase1_data_audit.log")
    logger.info("Starting Phase 1 data audit")

    package_zip = Path(cfg["paths"]["package_zip"])
    extracted_root = Path(cfg["paths"]["extracted_root"])
    ensure_package_extracted(package_zip, extracted_root, logger)

    inventory = enrich_inventory(list_inventory(extracted_root), extracted_root, logger)
    inventory.to_csv(out_tables / "data_inventory.csv", index=False, encoding="utf-8-sig")
    logger.info("Wrote data inventory")

    primary_panel = Path(cfg["paths"]["primary_panel"])
    df = read_table(primary_panel, parse_dates=["time_bin"])
    fields = infer_fields(df)
    logger.info("Inferred fields: %s", fields)
    if not fields["point_id"] or not fields["timestamp"]:
        raise ValueError("Could not infer point id or timestamp field from primary panel.")

    missing = missing_summary(df)
    missing.to_csv(out_tables / "missing_summary.csv", index=False, encoding="utf-8-sig")

    cov = coverage_by_point(df, fields, cfg)
    cov.to_csv(out_tables / "coverage_by_point.csv", index=False, encoding="utf-8-sig")

    time_cov = time_coverage_summary(df, fields)
    time_cov.to_csv(out_tables / "time_coverage_summary.csv", index=False, encoding="utf-8-sig")
    time_cov.to_csv(out_tables / "coverage_by_time.csv", index=False, encoding="utf-8-sig")

    continuity = continuity_check(df, fields)
    continuity.to_csv(out_tables / "time_continuity_check.csv", index=False, encoding="utf-8-sig")

    windows = window_feasibility(df, fields, cfg)
    windows.to_csv(out_tables / "window_feasibility_summary.csv", index=False, encoding="utf-8-sig")

    quality = point_quality_summary(cov, windows, cfg)
    quality.to_csv(out_tables / "point_quality_summary.csv", index=False, encoding="utf-8-sig")

    split = split_summary(df, fields, cfg["audit"]["split_ratios"])
    split.to_csv(out_tables / "train_val_test_split_summary.csv", index=False, encoding="utf-8-sig")

    dictionary_rows = [{"field": k, "inferred_column": v or "", "source": "auto_inference"} for k, v in fields.items()]
    dictionary = pd.DataFrame(dictionary_rows)
    existing_dictionary = Path(cfg["paths"]["existing_dictionary"])
    if existing_dictionary.exists():
        source_dict = pd.read_csv(existing_dictionary)
        source_dict.to_csv(out_tables / "data_dictionary_source.csv", index=False, encoding="utf-8-sig")
    dictionary.to_csv(out_tables / "data_dictionary.csv", index=False, encoding="utf-8-sig")

    write_report(
        reports / "phase1_data_audit_report.md",
        inventory,
        df,
        fields,
        cov,
        missing,
        time_cov,
        continuity,
        windows,
        split,
        logger,
    )
    logger.info("Phase 1 data audit completed")


if __name__ == "__main__":
    main()
