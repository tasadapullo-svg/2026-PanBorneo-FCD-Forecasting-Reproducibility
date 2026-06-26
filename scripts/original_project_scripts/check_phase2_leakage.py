from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


DEFAULT_SPLITS = {
    "train": ("2025-12-08 13:00:00", "2026-02-04 06:00:00"),
    "val": ("2026-02-04 07:00:00", "2026-02-16 15:00:00"),
    "test": ("2026-02-16 16:00:00", "2026-03-01 00:00:00"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Phase 2 leakage and chronological split boundaries.")
    parser.add_argument("--window-index", default="outputs/tables/window_index_all.csv")
    parser.add_argument("--split-summary", default="outputs/tables/train_val_test_split_summary.csv")
    parser.add_argument("--chunksize", type=int, default=500_000)
    return parser.parse_args()


def load_split_ranges(path: Path) -> dict[str, tuple[pd.Timestamp, pd.Timestamp]]:
    if not path.exists():
        return {k: (pd.Timestamp(v[0]), pd.Timestamp(v[1])) for k, v in DEFAULT_SPLITS.items()}
    df = pd.read_csv(path)
    return {
        str(row["split"]).strip(): (pd.Timestamp(row["start_time"]), pd.Timestamp(row["end_time"]))
        for _, row in df.iterrows()
    }


def main() -> None:
    args = parse_args()
    window_path = Path(args.window_index)
    split_ranges = load_split_ranges(Path(args.split_summary))

    usecols = [
        "input_start_time",
        "input_end_time",
        "target_start_time",
        "target_end_time",
        "split",
        "horizon_hours",
        "is_main_forecast",
        "is_extended_horizon",
        "leakage_check_passed",
    ]
    parse_dates = ["input_start_time", "input_end_time", "target_start_time", "target_end_time"]

    checked = 0
    temporal_leaks = 0
    boundary_failures = 0
    flag_failures = 0
    horizon_flag_failures = 0
    split_counts: dict[str, int] = {}

    for chunk in pd.read_csv(window_path, usecols=usecols, parse_dates=parse_dates, chunksize=args.chunksize):
        checked += len(chunk)
        temporal_leaks += int((chunk["input_end_time"] >= chunk["target_start_time"]).sum())
        flag_failures += int((chunk["leakage_check_passed"] != 1).sum())
        horizon_flag_failures += int(((chunk["horizon_hours"] == 168) & (chunk["is_extended_horizon"] != 1)).sum())
        horizon_flag_failures += int(((chunk["horizon_hours"] == 168) & (chunk["is_main_forecast"] != 0)).sum())
        horizon_flag_failures += int(((chunk["horizon_hours"] != 168) & (chunk["is_main_forecast"] != 1)).sum())

        for split, (start, end) in split_ranges.items():
            mask = chunk["split"].eq(split)
            if not mask.any():
                continue
            bad = (
                (chunk.loc[mask, "input_start_time"] < start)
                | (chunk.loc[mask, "target_end_time"] > end)
            )
            boundary_failures += int(bad.sum())
            split_counts[split] = split_counts.get(split, 0) + int(mask.sum())

    print("Phase 2 leakage and split-boundary check")
    print(f"- checked rows: {checked:,}")
    print(f"- split counts: {split_counts}")
    print(f"- input_end_time >= target_start_time: {temporal_leaks}")
    print(f"- split boundary failures: {boundary_failures}")
    print(f"- leakage_check_passed flag failures: {flag_failures}")
    print(f"- main/extended horizon flag failures: {horizon_flag_failures}")

    if temporal_leaks or boundary_failures or flag_failures or horizon_flag_failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
