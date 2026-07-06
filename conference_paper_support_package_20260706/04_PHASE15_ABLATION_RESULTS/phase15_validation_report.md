# Phase 15 Validation Report

**Status: PASS**

Checks: 685; failures: 0

## Failures

- None.

## Check Results

| Check | Passed | Detail |
| --- | --- | --- |
| metrics_exists | True | D:\2026_PD\outputs\tables\phase15_feature_ablation_metrics.csv |
| metrics_rows | True | found 75 |
| required_metrics_columns | True | missing=[] |
| feature_groups | True | ['full_features', 'speed_only', 'speed_reliability', 'speed_time', 'speed_volatility'] |
| horizons | True | [1, 3, 6] |
| seeds | True | [42, 2024, 2025, 2026, 3407] |
| five_seeds_per_group_horizon | True | {('full_features', 1): 5, ('full_features', 3): 5, ('full_features', 6): 5, ('speed_only', 1): 5, ('speed_only', 3): 5, ('speed_only', 6): 5, ('speed_reliability', 1): 5, ('speed_reliability', 3): 5, ('speed_reliability', 6): 5, ('speed_time', 1): 5, ('speed_time', 3): 5, ('speed_time', 6): 5, ('speed_volatility', 1): 5, ('speed_volatility', 3): 5, ('speed_volatility', 6): 5} |
| speed_only_relative_zero | True | non-zero speed_only relative MAE |
| prediction_files | True | found 75 |
| nonempty:full_features_h1_seed2024.parquet | True | rows=12265 |
| columns:full_features_h1_seed2024.parquet | True | missing=[] |
| key:full_features_h1_seed2024.parquet | True | {'full_features'}/{1}/{2024} |
| filename:full_features_h1_seed2024.parquet | True | full_features_h1_seed2024.parquet |
| sample_ids:full_features_h1_seed2024.parquet | True | expected=12265, found=12265 |
| finite:full_features_h1_seed2024.parquet | True | contains NaN/inf |
| nonempty:full_features_h1_seed2025.parquet | True | rows=12265 |
| columns:full_features_h1_seed2025.parquet | True | missing=[] |
| key:full_features_h1_seed2025.parquet | True | {'full_features'}/{1}/{2025} |
| filename:full_features_h1_seed2025.parquet | True | full_features_h1_seed2025.parquet |
| sample_ids:full_features_h1_seed2025.parquet | True | expected=12265, found=12265 |
| finite:full_features_h1_seed2025.parquet | True | contains NaN/inf |
| nonempty:full_features_h1_seed2026.parquet | True | rows=12265 |
| columns:full_features_h1_seed2026.parquet | True | missing=[] |
| key:full_features_h1_seed2026.parquet | True | {'full_features'}/{1}/{2026} |
| filename:full_features_h1_seed2026.parquet | True | full_features_h1_seed2026.parquet |
| sample_ids:full_features_h1_seed2026.parquet | True | expected=12265, found=12265 |
| finite:full_features_h1_seed2026.parquet | True | contains NaN/inf |
| nonempty:full_features_h1_seed3407.parquet | True | rows=12265 |
| columns:full_features_h1_seed3407.parquet | True | missing=[] |
| key:full_features_h1_seed3407.parquet | True | {'full_features'}/{1}/{3407} |
| filename:full_features_h1_seed3407.parquet | True | full_features_h1_seed3407.parquet |
| sample_ids:full_features_h1_seed3407.parquet | True | expected=12265, found=12265 |
| finite:full_features_h1_seed3407.parquet | True | contains NaN/inf |
| nonempty:full_features_h1_seed42.parquet | True | rows=12265 |
| columns:full_features_h1_seed42.parquet | True | missing=[] |
| key:full_features_h1_seed42.parquet | True | {'full_features'}/{1}/{42} |
| filename:full_features_h1_seed42.parquet | True | full_features_h1_seed42.parquet |
| sample_ids:full_features_h1_seed42.parquet | True | expected=12265, found=12265 |
| finite:full_features_h1_seed42.parquet | True | contains NaN/inf |
| nonempty:full_features_h3_seed2024.parquet | True | rows=11878 |
| columns:full_features_h3_seed2024.parquet | True | missing=[] |
| key:full_features_h3_seed2024.parquet | True | {'full_features'}/{3}/{2024} |
| filename:full_features_h3_seed2024.parquet | True | full_features_h3_seed2024.parquet |
| sample_ids:full_features_h3_seed2024.parquet | True | expected=11878, found=11878 |
| finite:full_features_h3_seed2024.parquet | True | contains NaN/inf |
| nonempty:full_features_h3_seed2025.parquet | True | rows=11878 |
| columns:full_features_h3_seed2025.parquet | True | missing=[] |
| key:full_features_h3_seed2025.parquet | True | {'full_features'}/{3}/{2025} |
| filename:full_features_h3_seed2025.parquet | True | full_features_h3_seed2025.parquet |
| sample_ids:full_features_h3_seed2025.parquet | True | expected=11878, found=11878 |
| finite:full_features_h3_seed2025.parquet | True | contains NaN/inf |
| nonempty:full_features_h3_seed2026.parquet | True | rows=11878 |
| columns:full_features_h3_seed2026.parquet | True | missing=[] |
| key:full_features_h3_seed2026.parquet | True | {'full_features'}/{3}/{2026} |
| filename:full_features_h3_seed2026.parquet | True | full_features_h3_seed2026.parquet |
| sample_ids:full_features_h3_seed2026.parquet | True | expected=11878, found=11878 |
| finite:full_features_h3_seed2026.parquet | True | contains NaN/inf |
| nonempty:full_features_h3_seed3407.parquet | True | rows=11878 |
| columns:full_features_h3_seed3407.parquet | True | missing=[] |
| key:full_features_h3_seed3407.parquet | True | {'full_features'}/{3}/{3407} |
| filename:full_features_h3_seed3407.parquet | True | full_features_h3_seed3407.parquet |
| sample_ids:full_features_h3_seed3407.parquet | True | expected=11878, found=11878 |
| finite:full_features_h3_seed3407.parquet | True | contains NaN/inf |
| nonempty:full_features_h3_seed42.parquet | True | rows=11878 |
| columns:full_features_h3_seed42.parquet | True | missing=[] |
| key:full_features_h3_seed42.parquet | True | {'full_features'}/{3}/{42} |
| filename:full_features_h3_seed42.parquet | True | full_features_h3_seed42.parquet |
| sample_ids:full_features_h3_seed42.parquet | True | expected=11878, found=11878 |
| finite:full_features_h3_seed42.parquet | True | contains NaN/inf |
| nonempty:full_features_h6_seed2024.parquet | True | rows=12166 |
| columns:full_features_h6_seed2024.parquet | True | missing=[] |
| key:full_features_h6_seed2024.parquet | True | {'full_features'}/{6}/{2024} |
| filename:full_features_h6_seed2024.parquet | True | full_features_h6_seed2024.parquet |
| sample_ids:full_features_h6_seed2024.parquet | True | expected=12166, found=12166 |
| finite:full_features_h6_seed2024.parquet | True | contains NaN/inf |
| nonempty:full_features_h6_seed2025.parquet | True | rows=12166 |
| columns:full_features_h6_seed2025.parquet | True | missing=[] |
| key:full_features_h6_seed2025.parquet | True | {'full_features'}/{6}/{2025} |
| filename:full_features_h6_seed2025.parquet | True | full_features_h6_seed2025.parquet |
| sample_ids:full_features_h6_seed2025.parquet | True | expected=12166, found=12166 |
| finite:full_features_h6_seed2025.parquet | True | contains NaN/inf |
| nonempty:full_features_h6_seed2026.parquet | True | rows=12166 |
| columns:full_features_h6_seed2026.parquet | True | missing=[] |
| key:full_features_h6_seed2026.parquet | True | {'full_features'}/{6}/{2026} |
| filename:full_features_h6_seed2026.parquet | True | full_features_h6_seed2026.parquet |
| sample_ids:full_features_h6_seed2026.parquet | True | expected=12166, found=12166 |
| finite:full_features_h6_seed2026.parquet | True | contains NaN/inf |
| nonempty:full_features_h6_seed3407.parquet | True | rows=12166 |
| columns:full_features_h6_seed3407.parquet | True | missing=[] |
| key:full_features_h6_seed3407.parquet | True | {'full_features'}/{6}/{3407} |
| filename:full_features_h6_seed3407.parquet | True | full_features_h6_seed3407.parquet |
| sample_ids:full_features_h6_seed3407.parquet | True | expected=12166, found=12166 |
| finite:full_features_h6_seed3407.parquet | True | contains NaN/inf |
| nonempty:full_features_h6_seed42.parquet | True | rows=12166 |
| columns:full_features_h6_seed42.parquet | True | missing=[] |
| key:full_features_h6_seed42.parquet | True | {'full_features'}/{6}/{42} |
| filename:full_features_h6_seed42.parquet | True | full_features_h6_seed42.parquet |
| sample_ids:full_features_h6_seed42.parquet | True | expected=12166, found=12166 |
| finite:full_features_h6_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_only_h1_seed2024.parquet | True | rows=12265 |
| columns:speed_only_h1_seed2024.parquet | True | missing=[] |
| key:speed_only_h1_seed2024.parquet | True | {'speed_only'}/{1}/{2024} |
| filename:speed_only_h1_seed2024.parquet | True | speed_only_h1_seed2024.parquet |
| sample_ids:speed_only_h1_seed2024.parquet | True | expected=12265, found=12265 |
| finite:speed_only_h1_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_only_h1_seed2025.parquet | True | rows=12265 |
| columns:speed_only_h1_seed2025.parquet | True | missing=[] |
| key:speed_only_h1_seed2025.parquet | True | {'speed_only'}/{1}/{2025} |
| filename:speed_only_h1_seed2025.parquet | True | speed_only_h1_seed2025.parquet |
| sample_ids:speed_only_h1_seed2025.parquet | True | expected=12265, found=12265 |
| finite:speed_only_h1_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_only_h1_seed2026.parquet | True | rows=12265 |
| columns:speed_only_h1_seed2026.parquet | True | missing=[] |
| key:speed_only_h1_seed2026.parquet | True | {'speed_only'}/{1}/{2026} |
| filename:speed_only_h1_seed2026.parquet | True | speed_only_h1_seed2026.parquet |
| sample_ids:speed_only_h1_seed2026.parquet | True | expected=12265, found=12265 |
| finite:speed_only_h1_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_only_h1_seed3407.parquet | True | rows=12265 |
| columns:speed_only_h1_seed3407.parquet | True | missing=[] |
| key:speed_only_h1_seed3407.parquet | True | {'speed_only'}/{1}/{3407} |
| filename:speed_only_h1_seed3407.parquet | True | speed_only_h1_seed3407.parquet |
| sample_ids:speed_only_h1_seed3407.parquet | True | expected=12265, found=12265 |
| finite:speed_only_h1_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_only_h1_seed42.parquet | True | rows=12265 |
| columns:speed_only_h1_seed42.parquet | True | missing=[] |
| key:speed_only_h1_seed42.parquet | True | {'speed_only'}/{1}/{42} |
| filename:speed_only_h1_seed42.parquet | True | speed_only_h1_seed42.parquet |
| sample_ids:speed_only_h1_seed42.parquet | True | expected=12265, found=12265 |
| finite:speed_only_h1_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_only_h3_seed2024.parquet | True | rows=11878 |
| columns:speed_only_h3_seed2024.parquet | True | missing=[] |
| key:speed_only_h3_seed2024.parquet | True | {'speed_only'}/{3}/{2024} |
| filename:speed_only_h3_seed2024.parquet | True | speed_only_h3_seed2024.parquet |
| sample_ids:speed_only_h3_seed2024.parquet | True | expected=11878, found=11878 |
| finite:speed_only_h3_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_only_h3_seed2025.parquet | True | rows=11878 |
| columns:speed_only_h3_seed2025.parquet | True | missing=[] |
| key:speed_only_h3_seed2025.parquet | True | {'speed_only'}/{3}/{2025} |
| filename:speed_only_h3_seed2025.parquet | True | speed_only_h3_seed2025.parquet |
| sample_ids:speed_only_h3_seed2025.parquet | True | expected=11878, found=11878 |
| finite:speed_only_h3_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_only_h3_seed2026.parquet | True | rows=11878 |
| columns:speed_only_h3_seed2026.parquet | True | missing=[] |
| key:speed_only_h3_seed2026.parquet | True | {'speed_only'}/{3}/{2026} |
| filename:speed_only_h3_seed2026.parquet | True | speed_only_h3_seed2026.parquet |
| sample_ids:speed_only_h3_seed2026.parquet | True | expected=11878, found=11878 |
| finite:speed_only_h3_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_only_h3_seed3407.parquet | True | rows=11878 |
| columns:speed_only_h3_seed3407.parquet | True | missing=[] |
| key:speed_only_h3_seed3407.parquet | True | {'speed_only'}/{3}/{3407} |
| filename:speed_only_h3_seed3407.parquet | True | speed_only_h3_seed3407.parquet |
| sample_ids:speed_only_h3_seed3407.parquet | True | expected=11878, found=11878 |
| finite:speed_only_h3_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_only_h3_seed42.parquet | True | rows=11878 |
| columns:speed_only_h3_seed42.parquet | True | missing=[] |
| key:speed_only_h3_seed42.parquet | True | {'speed_only'}/{3}/{42} |
| filename:speed_only_h3_seed42.parquet | True | speed_only_h3_seed42.parquet |
| sample_ids:speed_only_h3_seed42.parquet | True | expected=11878, found=11878 |
| finite:speed_only_h3_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_only_h6_seed2024.parquet | True | rows=12166 |
| columns:speed_only_h6_seed2024.parquet | True | missing=[] |
| key:speed_only_h6_seed2024.parquet | True | {'speed_only'}/{6}/{2024} |
| filename:speed_only_h6_seed2024.parquet | True | speed_only_h6_seed2024.parquet |
| sample_ids:speed_only_h6_seed2024.parquet | True | expected=12166, found=12166 |
| finite:speed_only_h6_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_only_h6_seed2025.parquet | True | rows=12166 |
| columns:speed_only_h6_seed2025.parquet | True | missing=[] |
| key:speed_only_h6_seed2025.parquet | True | {'speed_only'}/{6}/{2025} |
| filename:speed_only_h6_seed2025.parquet | True | speed_only_h6_seed2025.parquet |
| sample_ids:speed_only_h6_seed2025.parquet | True | expected=12166, found=12166 |
| finite:speed_only_h6_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_only_h6_seed2026.parquet | True | rows=12166 |
| columns:speed_only_h6_seed2026.parquet | True | missing=[] |
| key:speed_only_h6_seed2026.parquet | True | {'speed_only'}/{6}/{2026} |
| filename:speed_only_h6_seed2026.parquet | True | speed_only_h6_seed2026.parquet |
| sample_ids:speed_only_h6_seed2026.parquet | True | expected=12166, found=12166 |
| finite:speed_only_h6_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_only_h6_seed3407.parquet | True | rows=12166 |
| columns:speed_only_h6_seed3407.parquet | True | missing=[] |
| key:speed_only_h6_seed3407.parquet | True | {'speed_only'}/{6}/{3407} |
| filename:speed_only_h6_seed3407.parquet | True | speed_only_h6_seed3407.parquet |
| sample_ids:speed_only_h6_seed3407.parquet | True | expected=12166, found=12166 |
| finite:speed_only_h6_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_only_h6_seed42.parquet | True | rows=12166 |
| columns:speed_only_h6_seed42.parquet | True | missing=[] |
| key:speed_only_h6_seed42.parquet | True | {'speed_only'}/{6}/{42} |
| filename:speed_only_h6_seed42.parquet | True | speed_only_h6_seed42.parquet |
| sample_ids:speed_only_h6_seed42.parquet | True | expected=12166, found=12166 |
| finite:speed_only_h6_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h1_seed2024.parquet | True | rows=12265 |
| columns:speed_reliability_h1_seed2024.parquet | True | missing=[] |
| key:speed_reliability_h1_seed2024.parquet | True | {'speed_reliability'}/{1}/{2024} |
| filename:speed_reliability_h1_seed2024.parquet | True | speed_reliability_h1_seed2024.parquet |
| sample_ids:speed_reliability_h1_seed2024.parquet | True | expected=12265, found=12265 |
| finite:speed_reliability_h1_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h1_seed2025.parquet | True | rows=12265 |
| columns:speed_reliability_h1_seed2025.parquet | True | missing=[] |
| key:speed_reliability_h1_seed2025.parquet | True | {'speed_reliability'}/{1}/{2025} |
| filename:speed_reliability_h1_seed2025.parquet | True | speed_reliability_h1_seed2025.parquet |
| sample_ids:speed_reliability_h1_seed2025.parquet | True | expected=12265, found=12265 |
| finite:speed_reliability_h1_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h1_seed2026.parquet | True | rows=12265 |
| columns:speed_reliability_h1_seed2026.parquet | True | missing=[] |
| key:speed_reliability_h1_seed2026.parquet | True | {'speed_reliability'}/{1}/{2026} |
| filename:speed_reliability_h1_seed2026.parquet | True | speed_reliability_h1_seed2026.parquet |
| sample_ids:speed_reliability_h1_seed2026.parquet | True | expected=12265, found=12265 |
| finite:speed_reliability_h1_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h1_seed3407.parquet | True | rows=12265 |
| columns:speed_reliability_h1_seed3407.parquet | True | missing=[] |
| key:speed_reliability_h1_seed3407.parquet | True | {'speed_reliability'}/{1}/{3407} |
| filename:speed_reliability_h1_seed3407.parquet | True | speed_reliability_h1_seed3407.parquet |
| sample_ids:speed_reliability_h1_seed3407.parquet | True | expected=12265, found=12265 |
| finite:speed_reliability_h1_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h1_seed42.parquet | True | rows=12265 |
| columns:speed_reliability_h1_seed42.parquet | True | missing=[] |
| key:speed_reliability_h1_seed42.parquet | True | {'speed_reliability'}/{1}/{42} |
| filename:speed_reliability_h1_seed42.parquet | True | speed_reliability_h1_seed42.parquet |
| sample_ids:speed_reliability_h1_seed42.parquet | True | expected=12265, found=12265 |
| finite:speed_reliability_h1_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h3_seed2024.parquet | True | rows=11878 |
| columns:speed_reliability_h3_seed2024.parquet | True | missing=[] |
| key:speed_reliability_h3_seed2024.parquet | True | {'speed_reliability'}/{3}/{2024} |
| filename:speed_reliability_h3_seed2024.parquet | True | speed_reliability_h3_seed2024.parquet |
| sample_ids:speed_reliability_h3_seed2024.parquet | True | expected=11878, found=11878 |
| finite:speed_reliability_h3_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h3_seed2025.parquet | True | rows=11878 |
| columns:speed_reliability_h3_seed2025.parquet | True | missing=[] |
| key:speed_reliability_h3_seed2025.parquet | True | {'speed_reliability'}/{3}/{2025} |
| filename:speed_reliability_h3_seed2025.parquet | True | speed_reliability_h3_seed2025.parquet |
| sample_ids:speed_reliability_h3_seed2025.parquet | True | expected=11878, found=11878 |
| finite:speed_reliability_h3_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h3_seed2026.parquet | True | rows=11878 |
| columns:speed_reliability_h3_seed2026.parquet | True | missing=[] |
| key:speed_reliability_h3_seed2026.parquet | True | {'speed_reliability'}/{3}/{2026} |
| filename:speed_reliability_h3_seed2026.parquet | True | speed_reliability_h3_seed2026.parquet |
| sample_ids:speed_reliability_h3_seed2026.parquet | True | expected=11878, found=11878 |
| finite:speed_reliability_h3_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h3_seed3407.parquet | True | rows=11878 |
| columns:speed_reliability_h3_seed3407.parquet | True | missing=[] |
| key:speed_reliability_h3_seed3407.parquet | True | {'speed_reliability'}/{3}/{3407} |
| filename:speed_reliability_h3_seed3407.parquet | True | speed_reliability_h3_seed3407.parquet |
| sample_ids:speed_reliability_h3_seed3407.parquet | True | expected=11878, found=11878 |
| finite:speed_reliability_h3_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h3_seed42.parquet | True | rows=11878 |
| columns:speed_reliability_h3_seed42.parquet | True | missing=[] |
| key:speed_reliability_h3_seed42.parquet | True | {'speed_reliability'}/{3}/{42} |
| filename:speed_reliability_h3_seed42.parquet | True | speed_reliability_h3_seed42.parquet |
| sample_ids:speed_reliability_h3_seed42.parquet | True | expected=11878, found=11878 |
| finite:speed_reliability_h3_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h6_seed2024.parquet | True | rows=12166 |
| columns:speed_reliability_h6_seed2024.parquet | True | missing=[] |
| key:speed_reliability_h6_seed2024.parquet | True | {'speed_reliability'}/{6}/{2024} |
| filename:speed_reliability_h6_seed2024.parquet | True | speed_reliability_h6_seed2024.parquet |
| sample_ids:speed_reliability_h6_seed2024.parquet | True | expected=12166, found=12166 |
| finite:speed_reliability_h6_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h6_seed2025.parquet | True | rows=12166 |
| columns:speed_reliability_h6_seed2025.parquet | True | missing=[] |
| key:speed_reliability_h6_seed2025.parquet | True | {'speed_reliability'}/{6}/{2025} |
| filename:speed_reliability_h6_seed2025.parquet | True | speed_reliability_h6_seed2025.parquet |
| sample_ids:speed_reliability_h6_seed2025.parquet | True | expected=12166, found=12166 |
| finite:speed_reliability_h6_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h6_seed2026.parquet | True | rows=12166 |
| columns:speed_reliability_h6_seed2026.parquet | True | missing=[] |
| key:speed_reliability_h6_seed2026.parquet | True | {'speed_reliability'}/{6}/{2026} |
| filename:speed_reliability_h6_seed2026.parquet | True | speed_reliability_h6_seed2026.parquet |
| sample_ids:speed_reliability_h6_seed2026.parquet | True | expected=12166, found=12166 |
| finite:speed_reliability_h6_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h6_seed3407.parquet | True | rows=12166 |
| columns:speed_reliability_h6_seed3407.parquet | True | missing=[] |
| key:speed_reliability_h6_seed3407.parquet | True | {'speed_reliability'}/{6}/{3407} |
| filename:speed_reliability_h6_seed3407.parquet | True | speed_reliability_h6_seed3407.parquet |
| sample_ids:speed_reliability_h6_seed3407.parquet | True | expected=12166, found=12166 |
| finite:speed_reliability_h6_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_reliability_h6_seed42.parquet | True | rows=12166 |
| columns:speed_reliability_h6_seed42.parquet | True | missing=[] |
| key:speed_reliability_h6_seed42.parquet | True | {'speed_reliability'}/{6}/{42} |
| filename:speed_reliability_h6_seed42.parquet | True | speed_reliability_h6_seed42.parquet |
| sample_ids:speed_reliability_h6_seed42.parquet | True | expected=12166, found=12166 |
| finite:speed_reliability_h6_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_time_h1_seed2024.parquet | True | rows=12265 |
| columns:speed_time_h1_seed2024.parquet | True | missing=[] |
| key:speed_time_h1_seed2024.parquet | True | {'speed_time'}/{1}/{2024} |
| filename:speed_time_h1_seed2024.parquet | True | speed_time_h1_seed2024.parquet |
| sample_ids:speed_time_h1_seed2024.parquet | True | expected=12265, found=12265 |
| finite:speed_time_h1_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_time_h1_seed2025.parquet | True | rows=12265 |
| columns:speed_time_h1_seed2025.parquet | True | missing=[] |
| key:speed_time_h1_seed2025.parquet | True | {'speed_time'}/{1}/{2025} |
| filename:speed_time_h1_seed2025.parquet | True | speed_time_h1_seed2025.parquet |
| sample_ids:speed_time_h1_seed2025.parquet | True | expected=12265, found=12265 |
| finite:speed_time_h1_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_time_h1_seed2026.parquet | True | rows=12265 |
| columns:speed_time_h1_seed2026.parquet | True | missing=[] |
| key:speed_time_h1_seed2026.parquet | True | {'speed_time'}/{1}/{2026} |
| filename:speed_time_h1_seed2026.parquet | True | speed_time_h1_seed2026.parquet |
| sample_ids:speed_time_h1_seed2026.parquet | True | expected=12265, found=12265 |
| finite:speed_time_h1_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_time_h1_seed3407.parquet | True | rows=12265 |
| columns:speed_time_h1_seed3407.parquet | True | missing=[] |
| key:speed_time_h1_seed3407.parquet | True | {'speed_time'}/{1}/{3407} |
| filename:speed_time_h1_seed3407.parquet | True | speed_time_h1_seed3407.parquet |
| sample_ids:speed_time_h1_seed3407.parquet | True | expected=12265, found=12265 |
| finite:speed_time_h1_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_time_h1_seed42.parquet | True | rows=12265 |
| columns:speed_time_h1_seed42.parquet | True | missing=[] |
| key:speed_time_h1_seed42.parquet | True | {'speed_time'}/{1}/{42} |
| filename:speed_time_h1_seed42.parquet | True | speed_time_h1_seed42.parquet |
| sample_ids:speed_time_h1_seed42.parquet | True | expected=12265, found=12265 |
| finite:speed_time_h1_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_time_h3_seed2024.parquet | True | rows=11878 |
| columns:speed_time_h3_seed2024.parquet | True | missing=[] |
| key:speed_time_h3_seed2024.parquet | True | {'speed_time'}/{3}/{2024} |
| filename:speed_time_h3_seed2024.parquet | True | speed_time_h3_seed2024.parquet |
| sample_ids:speed_time_h3_seed2024.parquet | True | expected=11878, found=11878 |
| finite:speed_time_h3_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_time_h3_seed2025.parquet | True | rows=11878 |
| columns:speed_time_h3_seed2025.parquet | True | missing=[] |
| key:speed_time_h3_seed2025.parquet | True | {'speed_time'}/{3}/{2025} |
| filename:speed_time_h3_seed2025.parquet | True | speed_time_h3_seed2025.parquet |
| sample_ids:speed_time_h3_seed2025.parquet | True | expected=11878, found=11878 |
| finite:speed_time_h3_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_time_h3_seed2026.parquet | True | rows=11878 |
| columns:speed_time_h3_seed2026.parquet | True | missing=[] |
| key:speed_time_h3_seed2026.parquet | True | {'speed_time'}/{3}/{2026} |
| filename:speed_time_h3_seed2026.parquet | True | speed_time_h3_seed2026.parquet |
| sample_ids:speed_time_h3_seed2026.parquet | True | expected=11878, found=11878 |
| finite:speed_time_h3_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_time_h3_seed3407.parquet | True | rows=11878 |
| columns:speed_time_h3_seed3407.parquet | True | missing=[] |
| key:speed_time_h3_seed3407.parquet | True | {'speed_time'}/{3}/{3407} |
| filename:speed_time_h3_seed3407.parquet | True | speed_time_h3_seed3407.parquet |
| sample_ids:speed_time_h3_seed3407.parquet | True | expected=11878, found=11878 |
| finite:speed_time_h3_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_time_h3_seed42.parquet | True | rows=11878 |
| columns:speed_time_h3_seed42.parquet | True | missing=[] |
| key:speed_time_h3_seed42.parquet | True | {'speed_time'}/{3}/{42} |
| filename:speed_time_h3_seed42.parquet | True | speed_time_h3_seed42.parquet |
| sample_ids:speed_time_h3_seed42.parquet | True | expected=11878, found=11878 |
| finite:speed_time_h3_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_time_h6_seed2024.parquet | True | rows=12166 |
| columns:speed_time_h6_seed2024.parquet | True | missing=[] |
| key:speed_time_h6_seed2024.parquet | True | {'speed_time'}/{6}/{2024} |
| filename:speed_time_h6_seed2024.parquet | True | speed_time_h6_seed2024.parquet |
| sample_ids:speed_time_h6_seed2024.parquet | True | expected=12166, found=12166 |
| finite:speed_time_h6_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_time_h6_seed2025.parquet | True | rows=12166 |
| columns:speed_time_h6_seed2025.parquet | True | missing=[] |
| key:speed_time_h6_seed2025.parquet | True | {'speed_time'}/{6}/{2025} |
| filename:speed_time_h6_seed2025.parquet | True | speed_time_h6_seed2025.parquet |
| sample_ids:speed_time_h6_seed2025.parquet | True | expected=12166, found=12166 |
| finite:speed_time_h6_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_time_h6_seed2026.parquet | True | rows=12166 |
| columns:speed_time_h6_seed2026.parquet | True | missing=[] |
| key:speed_time_h6_seed2026.parquet | True | {'speed_time'}/{6}/{2026} |
| filename:speed_time_h6_seed2026.parquet | True | speed_time_h6_seed2026.parquet |
| sample_ids:speed_time_h6_seed2026.parquet | True | expected=12166, found=12166 |
| finite:speed_time_h6_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_time_h6_seed3407.parquet | True | rows=12166 |
| columns:speed_time_h6_seed3407.parquet | True | missing=[] |
| key:speed_time_h6_seed3407.parquet | True | {'speed_time'}/{6}/{3407} |
| filename:speed_time_h6_seed3407.parquet | True | speed_time_h6_seed3407.parquet |
| sample_ids:speed_time_h6_seed3407.parquet | True | expected=12166, found=12166 |
| finite:speed_time_h6_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_time_h6_seed42.parquet | True | rows=12166 |
| columns:speed_time_h6_seed42.parquet | True | missing=[] |
| key:speed_time_h6_seed42.parquet | True | {'speed_time'}/{6}/{42} |
| filename:speed_time_h6_seed42.parquet | True | speed_time_h6_seed42.parquet |
| sample_ids:speed_time_h6_seed42.parquet | True | expected=12166, found=12166 |
| finite:speed_time_h6_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h1_seed2024.parquet | True | rows=12265 |
| columns:speed_volatility_h1_seed2024.parquet | True | missing=[] |
| key:speed_volatility_h1_seed2024.parquet | True | {'speed_volatility'}/{1}/{2024} |
| filename:speed_volatility_h1_seed2024.parquet | True | speed_volatility_h1_seed2024.parquet |
| sample_ids:speed_volatility_h1_seed2024.parquet | True | expected=12265, found=12265 |
| finite:speed_volatility_h1_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h1_seed2025.parquet | True | rows=12265 |
| columns:speed_volatility_h1_seed2025.parquet | True | missing=[] |
| key:speed_volatility_h1_seed2025.parquet | True | {'speed_volatility'}/{1}/{2025} |
| filename:speed_volatility_h1_seed2025.parquet | True | speed_volatility_h1_seed2025.parquet |
| sample_ids:speed_volatility_h1_seed2025.parquet | True | expected=12265, found=12265 |
| finite:speed_volatility_h1_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h1_seed2026.parquet | True | rows=12265 |
| columns:speed_volatility_h1_seed2026.parquet | True | missing=[] |
| key:speed_volatility_h1_seed2026.parquet | True | {'speed_volatility'}/{1}/{2026} |
| filename:speed_volatility_h1_seed2026.parquet | True | speed_volatility_h1_seed2026.parquet |
| sample_ids:speed_volatility_h1_seed2026.parquet | True | expected=12265, found=12265 |
| finite:speed_volatility_h1_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h1_seed3407.parquet | True | rows=12265 |
| columns:speed_volatility_h1_seed3407.parquet | True | missing=[] |
| key:speed_volatility_h1_seed3407.parquet | True | {'speed_volatility'}/{1}/{3407} |
| filename:speed_volatility_h1_seed3407.parquet | True | speed_volatility_h1_seed3407.parquet |
| sample_ids:speed_volatility_h1_seed3407.parquet | True | expected=12265, found=12265 |
| finite:speed_volatility_h1_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h1_seed42.parquet | True | rows=12265 |
| columns:speed_volatility_h1_seed42.parquet | True | missing=[] |
| key:speed_volatility_h1_seed42.parquet | True | {'speed_volatility'}/{1}/{42} |
| filename:speed_volatility_h1_seed42.parquet | True | speed_volatility_h1_seed42.parquet |
| sample_ids:speed_volatility_h1_seed42.parquet | True | expected=12265, found=12265 |
| finite:speed_volatility_h1_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h3_seed2024.parquet | True | rows=11878 |
| columns:speed_volatility_h3_seed2024.parquet | True | missing=[] |
| key:speed_volatility_h3_seed2024.parquet | True | {'speed_volatility'}/{3}/{2024} |
| filename:speed_volatility_h3_seed2024.parquet | True | speed_volatility_h3_seed2024.parquet |
| sample_ids:speed_volatility_h3_seed2024.parquet | True | expected=11878, found=11878 |
| finite:speed_volatility_h3_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h3_seed2025.parquet | True | rows=11878 |
| columns:speed_volatility_h3_seed2025.parquet | True | missing=[] |
| key:speed_volatility_h3_seed2025.parquet | True | {'speed_volatility'}/{3}/{2025} |
| filename:speed_volatility_h3_seed2025.parquet | True | speed_volatility_h3_seed2025.parquet |
| sample_ids:speed_volatility_h3_seed2025.parquet | True | expected=11878, found=11878 |
| finite:speed_volatility_h3_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h3_seed2026.parquet | True | rows=11878 |
| columns:speed_volatility_h3_seed2026.parquet | True | missing=[] |
| key:speed_volatility_h3_seed2026.parquet | True | {'speed_volatility'}/{3}/{2026} |
| filename:speed_volatility_h3_seed2026.parquet | True | speed_volatility_h3_seed2026.parquet |
| sample_ids:speed_volatility_h3_seed2026.parquet | True | expected=11878, found=11878 |
| finite:speed_volatility_h3_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h3_seed3407.parquet | True | rows=11878 |
| columns:speed_volatility_h3_seed3407.parquet | True | missing=[] |
| key:speed_volatility_h3_seed3407.parquet | True | {'speed_volatility'}/{3}/{3407} |
| filename:speed_volatility_h3_seed3407.parquet | True | speed_volatility_h3_seed3407.parquet |
| sample_ids:speed_volatility_h3_seed3407.parquet | True | expected=11878, found=11878 |
| finite:speed_volatility_h3_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h3_seed42.parquet | True | rows=11878 |
| columns:speed_volatility_h3_seed42.parquet | True | missing=[] |
| key:speed_volatility_h3_seed42.parquet | True | {'speed_volatility'}/{3}/{42} |
| filename:speed_volatility_h3_seed42.parquet | True | speed_volatility_h3_seed42.parquet |
| sample_ids:speed_volatility_h3_seed42.parquet | True | expected=11878, found=11878 |
| finite:speed_volatility_h3_seed42.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h6_seed2024.parquet | True | rows=12166 |
| columns:speed_volatility_h6_seed2024.parquet | True | missing=[] |
| key:speed_volatility_h6_seed2024.parquet | True | {'speed_volatility'}/{6}/{2024} |
| filename:speed_volatility_h6_seed2024.parquet | True | speed_volatility_h6_seed2024.parquet |
| sample_ids:speed_volatility_h6_seed2024.parquet | True | expected=12166, found=12166 |
| finite:speed_volatility_h6_seed2024.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h6_seed2025.parquet | True | rows=12166 |
| columns:speed_volatility_h6_seed2025.parquet | True | missing=[] |
| key:speed_volatility_h6_seed2025.parquet | True | {'speed_volatility'}/{6}/{2025} |
| filename:speed_volatility_h6_seed2025.parquet | True | speed_volatility_h6_seed2025.parquet |
| sample_ids:speed_volatility_h6_seed2025.parquet | True | expected=12166, found=12166 |
| finite:speed_volatility_h6_seed2025.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h6_seed2026.parquet | True | rows=12166 |
| columns:speed_volatility_h6_seed2026.parquet | True | missing=[] |
| key:speed_volatility_h6_seed2026.parquet | True | {'speed_volatility'}/{6}/{2026} |
| filename:speed_volatility_h6_seed2026.parquet | True | speed_volatility_h6_seed2026.parquet |
| sample_ids:speed_volatility_h6_seed2026.parquet | True | expected=12166, found=12166 |
| finite:speed_volatility_h6_seed2026.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h6_seed3407.parquet | True | rows=12166 |
| columns:speed_volatility_h6_seed3407.parquet | True | missing=[] |
| key:speed_volatility_h6_seed3407.parquet | True | {'speed_volatility'}/{6}/{3407} |
| filename:speed_volatility_h6_seed3407.parquet | True | speed_volatility_h6_seed3407.parquet |
| sample_ids:speed_volatility_h6_seed3407.parquet | True | expected=12166, found=12166 |
| finite:speed_volatility_h6_seed3407.parquet | True | contains NaN/inf |
| nonempty:speed_volatility_h6_seed42.parquet | True | rows=12166 |
| columns:speed_volatility_h6_seed42.parquet | True | missing=[] |
| key:speed_volatility_h6_seed42.parquet | True | {'speed_volatility'}/{6}/{42} |
| filename:speed_volatility_h6_seed42.parquet | True | speed_volatility_h6_seed42.parquet |
| sample_ids:speed_volatility_h6_seed42.parquet | True | expected=12166, found=12166 |
| finite:speed_volatility_h6_seed42.parquet | True | contains NaN/inf |
| exact_prediction_keys | True | missing=[] |
| test_n:('speed_only', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('speed_only', 1, 42) | True | metrics=0.906022549336461, computed=0.906022549336461 |
| rmse:('speed_only', 1, 42) | True | metrics=2.429039396511718, computed=2.429039396511718 |
| test_n:('speed_only', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('speed_only', 1, 2024) | True | metrics=0.9251396566422871, computed=0.9251396566422871 |
| rmse:('speed_only', 1, 2024) | True | metrics=2.453934800807006, computed=2.453934800807006 |
| test_n:('speed_only', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('speed_only', 1, 2025) | True | metrics=0.9084905082432048, computed=0.9084905082432047 |
| rmse:('speed_only', 1, 2025) | True | metrics=2.414344404308656, computed=2.414344404308656 |
| test_n:('speed_only', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('speed_only', 1, 2026) | True | metrics=0.9828015614761122, computed=0.9828015614761122 |
| rmse:('speed_only', 1, 2026) | True | metrics=2.526369192106773, computed=2.526369192106773 |
| test_n:('speed_only', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('speed_only', 1, 3407) | True | metrics=1.1055805200078368, computed=1.1055805200078368 |
| rmse:('speed_only', 1, 3407) | True | metrics=2.54654767527361, computed=2.54654767527361 |
| test_n:('speed_time', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('speed_time', 1, 42) | True | metrics=1.1662308745417262, computed=1.1662308745417262 |
| rmse:('speed_time', 1, 42) | True | metrics=2.460402032681061, computed=2.460402032681061 |
| test_n:('speed_time', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('speed_time', 1, 2024) | True | metrics=1.1536623941165691, computed=1.1536623941165693 |
| rmse:('speed_time', 1, 2024) | True | metrics=2.4344063303920334, computed=2.4344063303920334 |
| test_n:('speed_time', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('speed_time', 1, 2025) | True | metrics=1.1714714928932983, computed=1.1714714928932983 |
| rmse:('speed_time', 1, 2025) | True | metrics=2.485897134325068, computed=2.485897134325068 |
| test_n:('speed_time', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('speed_time', 1, 2026) | True | metrics=1.1293472182736122, computed=1.1293472182736122 |
| rmse:('speed_time', 1, 2026) | True | metrics=2.4370496007171503, computed=2.4370496007171503 |
| test_n:('speed_time', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('speed_time', 1, 3407) | True | metrics=1.1539159736679954, computed=1.1539159736679954 |
| rmse:('speed_time', 1, 3407) | True | metrics=2.450467717929436, computed=2.4504677179294356 |
| test_n:('speed_reliability', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('speed_reliability', 1, 42) | True | metrics=1.2682172451027065, computed=1.2682172451027063 |
| rmse:('speed_reliability', 1, 42) | True | metrics=2.712672733974059, computed=2.712672733974059 |
| test_n:('speed_reliability', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('speed_reliability', 1, 2024) | True | metrics=1.087687025136283, computed=1.087687025136283 |
| rmse:('speed_reliability', 1, 2024) | True | metrics=2.519773505387315, computed=2.519773505387315 |
| test_n:('speed_reliability', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('speed_reliability', 1, 2025) | True | metrics=1.2220928036627166, computed=1.2220928036627166 |
| rmse:('speed_reliability', 1, 2025) | True | metrics=2.60459842615331, computed=2.60459842615331 |
| test_n:('speed_reliability', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('speed_reliability', 1, 2026) | True | metrics=1.1584966102037146, computed=1.1584966102037146 |
| rmse:('speed_reliability', 1, 2026) | True | metrics=2.5448924401753223, computed=2.5448924401753223 |
| test_n:('speed_reliability', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('speed_reliability', 1, 3407) | True | metrics=1.1048356920468578, computed=1.1048356920468578 |
| rmse:('speed_reliability', 1, 3407) | True | metrics=2.574119088184078, computed=2.574119088184078 |
| test_n:('speed_volatility', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('speed_volatility', 1, 42) | True | metrics=1.0654062082171682, computed=1.0654062082171682 |
| rmse:('speed_volatility', 1, 42) | True | metrics=2.53535332842458, computed=2.53535332842458 |
| test_n:('speed_volatility', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('speed_volatility', 1, 2024) | True | metrics=1.202566486176694, computed=1.202566486176694 |
| rmse:('speed_volatility', 1, 2024) | True | metrics=2.653051575756161, computed=2.653051575756161 |
| test_n:('speed_volatility', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('speed_volatility', 1, 2025) | True | metrics=1.014876095615889, computed=1.0148760956158893 |
| rmse:('speed_volatility', 1, 2025) | True | metrics=2.4725495033283678, computed=2.4725495033283673 |
| test_n:('speed_volatility', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('speed_volatility', 1, 2026) | True | metrics=1.031352468864606, computed=1.0313524688646059 |
| rmse:('speed_volatility', 1, 2026) | True | metrics=2.457094040451174, computed=2.457094040451174 |
| test_n:('speed_volatility', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('speed_volatility', 1, 3407) | True | metrics=1.065334844919695, computed=1.0653348449196953 |
| rmse:('speed_volatility', 1, 3407) | True | metrics=2.5014049076921148, computed=2.5014049076921148 |
| test_n:('full_features', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('full_features', 1, 42) | True | metrics=1.1306425526148924, computed=1.1306425526148924 |
| rmse:('full_features', 1, 42) | True | metrics=2.459456107874222, computed=2.459456107874222 |
| test_n:('full_features', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('full_features', 1, 2024) | True | metrics=1.152644129339841, computed=1.152644129339841 |
| rmse:('full_features', 1, 2024) | True | metrics=2.482148689164527, computed=2.482148689164527 |
| test_n:('full_features', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('full_features', 1, 2025) | True | metrics=1.27193466059004, computed=1.2719346605900401 |
| rmse:('full_features', 1, 2025) | True | metrics=2.6342993241397368, computed=2.6342993241397368 |
| test_n:('full_features', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('full_features', 1, 2026) | True | metrics=1.1632968047274603, computed=1.1632968047274603 |
| rmse:('full_features', 1, 2026) | True | metrics=2.4694179885160925, computed=2.4694179885160925 |
| test_n:('full_features', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('full_features', 1, 3407) | True | metrics=1.3894647571052088, computed=1.3894647571052088 |
| rmse:('full_features', 1, 3407) | True | metrics=2.705622092972387, computed=2.705622092972387 |
| test_n:('speed_only', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('speed_only', 3, 42) | True | metrics=1.030488510729187, computed=1.030488510729187 |
| rmse:('speed_only', 3, 42) | True | metrics=1.8904786185711384, computed=1.8904786185711382 |
| test_n:('speed_only', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('speed_only', 3, 2024) | True | metrics=1.0353786012784745, computed=1.0353786012784743 |
| rmse:('speed_only', 3, 2024) | True | metrics=1.890078967947356, computed=1.8900789679473557 |
| test_n:('speed_only', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('speed_only', 3, 2025) | True | metrics=1.0656143581251, computed=1.0656143581250999 |
| rmse:('speed_only', 3, 2025) | True | metrics=1.838615813073456, computed=1.8386158130734562 |
| test_n:('speed_only', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('speed_only', 3, 2026) | True | metrics=1.0748662550374302, computed=1.0748662550374302 |
| rmse:('speed_only', 3, 2026) | True | metrics=2.1272069725708747, computed=2.1272069725708747 |
| test_n:('speed_only', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('speed_only', 3, 3407) | True | metrics=1.0046011034658329, computed=1.0046011034658329 |
| rmse:('speed_only', 3, 3407) | True | metrics=1.8211394600005493, computed=1.8211394600005495 |
| test_n:('speed_time', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('speed_time', 3, 42) | True | metrics=1.086942267269373, computed=1.086942267269373 |
| rmse:('speed_time', 3, 42) | True | metrics=1.8409952720907767, computed=1.8409952720907772 |
| test_n:('speed_time', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('speed_time', 3, 2024) | True | metrics=1.0694351531897637, computed=1.0694351531897637 |
| rmse:('speed_time', 3, 2024) | True | metrics=1.8251628862715092, computed=1.8251628862715095 |
| test_n:('speed_time', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('speed_time', 3, 2025) | True | metrics=1.050852872884159, computed=1.050852872884159 |
| rmse:('speed_time', 3, 2025) | True | metrics=1.821460481556543, computed=1.821460481556543 |
| test_n:('speed_time', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('speed_time', 3, 2026) | True | metrics=1.0465170275303908, computed=1.0465170275303908 |
| rmse:('speed_time', 3, 2026) | True | metrics=1.8362290125041472, computed=1.8362290125041472 |
| test_n:('speed_time', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('speed_time', 3, 3407) | True | metrics=1.084591706888225, computed=1.084591706888225 |
| rmse:('speed_time', 3, 3407) | True | metrics=1.8427666540982957, computed=1.8427666540982954 |
| test_n:('speed_reliability', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('speed_reliability', 3, 42) | True | metrics=1.2121916799999723, computed=1.2121916799999723 |
| rmse:('speed_reliability', 3, 42) | True | metrics=2.160600888923826, computed=2.160600888923826 |
| test_n:('speed_reliability', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('speed_reliability', 3, 2024) | True | metrics=1.110817974756655, computed=1.110817974756655 |
| rmse:('speed_reliability', 3, 2024) | True | metrics=2.0084507694691687, computed=2.0084507694691687 |
| test_n:('speed_reliability', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('speed_reliability', 3, 2025) | True | metrics=1.138494004864427, computed=1.138494004864427 |
| rmse:('speed_reliability', 3, 2025) | True | metrics=1.9965326391227325, computed=1.9965326391227323 |
| test_n:('speed_reliability', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('speed_reliability', 3, 2026) | True | metrics=1.0385738592152645, computed=1.0385738592152645 |
| rmse:('speed_reliability', 3, 2026) | True | metrics=1.93000556942556, computed=1.9300055694255598 |
| test_n:('speed_reliability', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('speed_reliability', 3, 3407) | True | metrics=1.0696521345704748, computed=1.0696521345704748 |
| rmse:('speed_reliability', 3, 3407) | True | metrics=1.955334582939994, computed=1.955334582939994 |
| test_n:('speed_volatility', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('speed_volatility', 3, 42) | True | metrics=1.081836074023641, computed=1.081836074023641 |
| rmse:('speed_volatility', 3, 42) | True | metrics=2.0253350859806627, computed=2.0253350859806627 |
| test_n:('speed_volatility', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('speed_volatility', 3, 2024) | True | metrics=0.9751874925632994, computed=0.9751874925632994 |
| rmse:('speed_volatility', 3, 2024) | True | metrics=1.858459994864704, computed=1.8584599948647038 |
| test_n:('speed_volatility', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('speed_volatility', 3, 2025) | True | metrics=1.0101323936258146, computed=1.0101323936258146 |
| rmse:('speed_volatility', 3, 2025) | True | metrics=1.872543101336878, computed=1.872543101336878 |
| test_n:('speed_volatility', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('speed_volatility', 3, 2026) | True | metrics=0.958706561594544, computed=0.9587065615945441 |
| rmse:('speed_volatility', 3, 2026) | True | metrics=1.836219501074231, computed=1.836219501074231 |
| test_n:('speed_volatility', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('speed_volatility', 3, 3407) | True | metrics=1.037559008433735, computed=1.037559008433735 |
| rmse:('speed_volatility', 3, 3407) | True | metrics=1.873660677466121, computed=1.873660677466121 |
| test_n:('full_features', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('full_features', 3, 42) | True | metrics=1.1280393443097168, computed=1.1280393443097168 |
| rmse:('full_features', 3, 42) | True | metrics=1.889791028370647, computed=1.889791028370647 |
| test_n:('full_features', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('full_features', 3, 2024) | True | metrics=1.0965016664208578, computed=1.0965016664208578 |
| rmse:('full_features', 3, 2024) | True | metrics=1.8306693949955424, computed=1.8306693949955422 |
| test_n:('full_features', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('full_features', 3, 2025) | True | metrics=1.172280978305429, computed=1.1722809783054293 |
| rmse:('full_features', 3, 2025) | True | metrics=1.969541169142211, computed=1.9695411691422107 |
| test_n:('full_features', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('full_features', 3, 2026) | True | metrics=1.1904330604464584, computed=1.1904330604464584 |
| rmse:('full_features', 3, 2026) | True | metrics=1.9599611912233368, computed=1.9599611912233372 |
| test_n:('full_features', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('full_features', 3, 3407) | True | metrics=1.1555155800496475, computed=1.1555155800496475 |
| rmse:('full_features', 3, 3407) | True | metrics=1.9527490259612643, computed=1.9527490259612643 |
| test_n:('speed_only', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('speed_only', 6, 42) | True | metrics=0.9146507908477608, computed=0.9146507908477608 |
| rmse:('speed_only', 6, 42) | True | metrics=1.467171637986396, computed=1.467171637986396 |
| test_n:('speed_only', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('speed_only', 6, 2024) | True | metrics=0.9207800947167696, computed=0.9207800947167696 |
| rmse:('speed_only', 6, 2024) | True | metrics=1.535266968555516, computed=1.535266968555516 |
| test_n:('speed_only', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('speed_only', 6, 2025) | True | metrics=0.974629830945661, computed=0.974629830945661 |
| rmse:('speed_only', 6, 2025) | True | metrics=1.4869337761502883, computed=1.4869337761502885 |
| test_n:('speed_only', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('speed_only', 6, 2026) | True | metrics=0.920632612111438, computed=0.920632612111438 |
| rmse:('speed_only', 6, 2026) | True | metrics=1.5361016667114955, computed=1.5361016667114957 |
| test_n:('speed_only', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('speed_only', 6, 3407) | True | metrics=0.9182315483388004, computed=0.9182315483388003 |
| rmse:('speed_only', 6, 3407) | True | metrics=1.498190665170002, computed=1.498190665170002 |
| test_n:('speed_time', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('speed_time', 6, 42) | True | metrics=1.0261092573997126, computed=1.0261092573997126 |
| rmse:('speed_time', 6, 42) | True | metrics=1.5860830118152038, computed=1.5860830118152038 |
| test_n:('speed_time', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('speed_time', 6, 2024) | True | metrics=0.9999631044211288, computed=0.9999631044211287 |
| rmse:('speed_time', 6, 2024) | True | metrics=1.551969686676018, computed=1.551969686676018 |
| test_n:('speed_time', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('speed_time', 6, 2025) | True | metrics=0.9765841568572612, computed=0.9765841568572612 |
| rmse:('speed_time', 6, 2025) | True | metrics=1.5386157699305212, computed=1.5386157699305212 |
| test_n:('speed_time', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('speed_time', 6, 2026) | True | metrics=0.9475405697914284, computed=0.9475405697914285 |
| rmse:('speed_time', 6, 2026) | True | metrics=1.5091449350530677, computed=1.5091449350530677 |
| test_n:('speed_time', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('speed_time', 6, 3407) | True | metrics=0.9764561657056632, computed=0.9764561657056632 |
| rmse:('speed_time', 6, 3407) | True | metrics=1.5313411538099446, computed=1.5313411538099446 |
| test_n:('speed_reliability', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('speed_reliability', 6, 42) | True | metrics=1.1226995970766618, computed=1.1226995970766618 |
| rmse:('speed_reliability', 6, 42) | True | metrics=1.933276329314527, computed=1.933276329314527 |
| test_n:('speed_reliability', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('speed_reliability', 6, 2024) | True | metrics=1.2038960360430306, computed=1.2038960360430306 |
| rmse:('speed_reliability', 6, 2024) | True | metrics=2.0316146338899133, computed=2.0316146338899133 |
| test_n:('speed_reliability', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('speed_reliability', 6, 2025) | True | metrics=0.9495766467411582, computed=0.9495766467411582 |
| rmse:('speed_reliability', 6, 2025) | True | metrics=1.536786049950351, computed=1.536786049950351 |
| test_n:('speed_reliability', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('speed_reliability', 6, 2026) | True | metrics=1.0018471547417904, computed=1.0018471547417904 |
| rmse:('speed_reliability', 6, 2026) | True | metrics=1.6737745374200532, computed=1.6737745374200532 |
| test_n:('speed_reliability', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('speed_reliability', 6, 3407) | True | metrics=0.998397441477088, computed=0.9983974414770881 |
| rmse:('speed_reliability', 6, 3407) | True | metrics=1.6674287038713669, computed=1.6674287038713669 |
| test_n:('speed_volatility', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('speed_volatility', 6, 42) | True | metrics=0.9848327749598168, computed=0.9848327749598169 |
| rmse:('speed_volatility', 6, 42) | True | metrics=1.636229796522543, computed=1.636229796522543 |
| test_n:('speed_volatility', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('speed_volatility', 6, 2024) | True | metrics=0.9859345019226224, computed=0.9859345019226224 |
| rmse:('speed_volatility', 6, 2024) | True | metrics=1.5373252700818134, computed=1.5373252700818134 |
| test_n:('speed_volatility', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('speed_volatility', 6, 2025) | True | metrics=0.8786726375757306, computed=0.8786726375757306 |
| rmse:('speed_volatility', 6, 2025) | True | metrics=1.4834792781630084, computed=1.4834792781630084 |
| test_n:('speed_volatility', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('speed_volatility', 6, 2026) | True | metrics=0.9566516964015808, computed=0.9566516964015807 |
| rmse:('speed_volatility', 6, 2026) | True | metrics=1.5502795312302018, computed=1.5502795312302018 |
| test_n:('speed_volatility', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('speed_volatility', 6, 3407) | True | metrics=0.945357398729702, computed=0.9453573987297021 |
| rmse:('speed_volatility', 6, 3407) | True | metrics=1.4898181988692345, computed=1.4898181988692345 |
| test_n:('full_features', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('full_features', 6, 42) | True | metrics=1.0392762719849975, computed=1.0392762719849977 |
| rmse:('full_features', 6, 42) | True | metrics=1.5850672160967356, computed=1.5850672160967356 |
| test_n:('full_features', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('full_features', 6, 2024) | True | metrics=1.0143020851879003, computed=1.0143020851879003 |
| rmse:('full_features', 6, 2024) | True | metrics=1.5467639131350026, computed=1.5467639131350026 |
| test_n:('full_features', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('full_features', 6, 2025) | True | metrics=1.1314962272010665, computed=1.1314962272010665 |
| rmse:('full_features', 6, 2025) | True | metrics=1.73935893124201, computed=1.7393589312420101 |
| test_n:('full_features', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('full_features', 6, 2026) | True | metrics=1.1326843643000344, computed=1.1326843643000344 |
| rmse:('full_features', 6, 2026) | True | metrics=1.697791532674226, computed=1.6977915326742261 |
| test_n:('full_features', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('full_features', 6, 3407) | True | metrics=1.0855548328109308, computed=1.0855548328109308 |
| rmse:('full_features', 6, 3407) | True | metrics=1.7019167208761412, computed=1.7019167208761412 |
