from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize feasible Phase 2 horizon-history combinations.")
    parser.add_argument("--feasibility", default="outputs/tables/window_feasibility_by_horizon.csv")
    parser.add_argument("--missingness", default="outputs/tables/window_missingness_summary.csv")
    parser.add_argument("--target-summary", default="outputs/tables/target_variable_summary.csv")
    parser.add_argument("--min-valid-ratio", type=float, default=0.80)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    feasibility = pd.read_csv(Path(args.feasibility))
    missingness = pd.read_csv(Path(args.missingness))
    targets = pd.read_csv(Path(args.target_summary))

    print("Available targets")
    print(targets.to_string(index=False))

    combo = (
        feasibility.groupby(["history_hours", "horizon_hours", "is_main_forecast", "is_extended_horizon"], as_index=False)
        .agg(
            target_variables=("target_variable", "nunique"),
            candidate_windows=("candidate_windows", "sum"),
            valid_windows_min_80pct_observed=("valid_windows_min_80pct_observed", "sum"),
            min_valid_window_ratio=("valid_window_ratio", "min"),
            max_valid_window_ratio=("valid_window_ratio", "max"),
        )
        .sort_values(["history_hours", "horizon_hours"])
    )
    combo["recommended_status"] = combo.apply(
        lambda r: "extended_stress_test"
        if int(r["is_extended_horizon"]) == 1
        else ("main_feasible" if float(r["min_valid_window_ratio"]) >= args.min_valid_ratio else "review"),
        axis=1,
    )

    miss = (
        missingness.groupby(["history_hours", "horizon_hours"], as_index=False)
        .agg(
            mean_input_observed_ratio=("mean_input_observed_ratio", "mean"),
            mean_target_observed_ratio=("mean_target_observed_ratio", "mean"),
            mean_input_missing_mask_ratio=("mean_input_missing_mask_ratio", "mean"),
        )
        .sort_values(["history_hours", "horizon_hours"])
    )
    out = combo.merge(miss, on=["history_hours", "horizon_hours"], how="left")

    print("\nFeasible horizon-history summary")
    print(out.to_string(index=False))

    review = out[out["recommended_status"].eq("review")]
    print("\nCombinations needing review")
    if review.empty:
        print("none")
    else:
        print(review.to_string(index=False))


if __name__ == "__main__":
    main()
