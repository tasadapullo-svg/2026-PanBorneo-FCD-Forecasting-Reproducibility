from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


REQUIRED_OUTPUTS = [
    "window_index_all.csv",
    "window_feasibility_by_horizon.csv",
    "window_count_by_split.csv",
    "window_count_by_point.csv",
    "window_missingness_summary.csv",
    "target_variable_summary.csv",
]

REQUIRED_WINDOW_COLUMNS = [
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect Phase 2 outputs without fully loading window_index_all.csv.")
    parser.add_argument("--tables-dir", default="outputs/tables")
    parser.add_argument("--chunksize", type=int, default=500_000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tables_dir = Path(args.tables_dir)
    window_path = tables_dir / "window_index_all.csv"

    print("Phase 2 output presence")
    for name in REQUIRED_OUTPUTS:
        path = tables_dir / name
        status = "OK" if path.exists() else "MISSING"
        size_mb = path.stat().st_size / (1024 * 1024) if path.exists() else 0
        print(f"- {name}: {status}, {size_mb:.2f} MB")

    if not window_path.exists():
        raise FileNotFoundError(window_path)

    header = pd.read_csv(window_path, nrows=0)
    missing_cols = [c for c in REQUIRED_WINDOW_COLUMNS if c not in header.columns]
    print("\nwindow_index_all.csv schema")
    print(f"- columns: {len(header.columns)}")
    print(f"- missing required columns: {missing_cols if missing_cols else 'none'}")

    total_rows = 0
    split_counts: dict[str, int] = {}
    target_counts: dict[str, int] = {}
    combo_counts: dict[tuple[int, int], int] = {}
    min_window_id = None
    max_window_id = None

    usecols = ["window_id", "split", "target_variable", "history_hours", "horizon_hours"]
    for chunk in pd.read_csv(window_path, usecols=usecols, chunksize=args.chunksize):
        total_rows += len(chunk)
        min_id = int(chunk["window_id"].min())
        max_id = int(chunk["window_id"].max())
        min_window_id = min_id if min_window_id is None else min(min_window_id, min_id)
        max_window_id = max_id if max_window_id is None else max(max_window_id, max_id)

        for key, value in chunk["split"].value_counts().items():
            split_counts[str(key)] = split_counts.get(str(key), 0) + int(value)
        for key, value in chunk["target_variable"].value_counts().items():
            target_counts[str(key)] = target_counts.get(str(key), 0) + int(value)
        grouped = chunk.groupby(["history_hours", "horizon_hours"]).size()
        for key, value in grouped.items():
            combo_counts[(int(key[0]), int(key[1]))] = combo_counts.get((int(key[0]), int(key[1])), 0) + int(value)

    print("\nwindow_index_all.csv streaming summary")
    print(f"- rows: {total_rows:,}")
    print(f"- window_id range: {min_window_id} to {max_window_id}")
    print(f"- split counts: {split_counts}")
    print(f"- target counts: {target_counts}")
    print("- history-horizon counts:")
    for (history, horizon), count in sorted(combo_counts.items()):
        print(f"  {history}h -> {horizon}h: {count:,}")


if __name__ == "__main__":
    main()
