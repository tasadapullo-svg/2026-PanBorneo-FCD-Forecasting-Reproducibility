# Phase 13 Full Output Validation

**Status: PASS**

- Metrics: `outputs\tables\phase13_strong_baseline_metrics.csv`
- Predictions: `outputs\predictions\phase13`
- Tolerance: `1e-06`

## Summary

- Checks run: 954
- Failed checks: 0

## Failures

- None.

## Check Results

| Check | Passed | Detail |
| --- | --- | --- |
| metrics_exists | True | D:\2026_PD\outputs\tables\phase13_strong_baseline_metrics.csv |
| metrics_rows | True | found 105, expected 105 |
| metrics_required_columns | True | missing [] |
| models | True | found ['GRU', 'HA', 'Persistence', 'ST-Transformer-lite', 'SeasonalHA', 'TCN', 'XGBoost'] |
| horizons | True | found [1, 3, 6] |
| seeds | True | found [42, 2024, 2025, 2026, 3407] |
| five_rows_per_model_horizon | True | counts={('GRU', 1): 5, ('GRU', 3): 5, ('GRU', 6): 5, ('HA', 1): 5, ('HA', 3): 5, ('HA', 6): 5, ('Persistence', 1): 5, ('Persistence', 3): 5, ('Persistence', 6): 5, ('ST-Transformer-lite', 1): 5, ('ST-Transformer-lite', 3): 5, ('ST-Transformer-lite', 6): 5, ('SeasonalHA', 1): 5, ('SeasonalHA', 3): 5, ('SeasonalHA', 6): 5, ('TCN', 1): 5, ('TCN', 3): 5, ('TCN', 6): 5, ('XGBoost', 1): 5, ('XGBoost', 3): 5, ('XGBoost', 6): 5} |
| unique_metric_keys | True | duplicate model/horizon/seed metric keys |
| prediction_directory_exists | True | D:\2026_PD\outputs\predictions\phase13 |
| prediction_file_count | True | found 105, expected 105 |
| nonempty:GRU_h1_seed2024.parquet | True | rows=12265 |
| columns:GRU_h1_seed2024.parquet | True | missing=[] |
| single_key:GRU_h1_seed2024.parquet | True | models={'GRU'}, horizons={1}, seeds={2024} |
| filename:GRU_h1_seed2024.parquet | True | expected GRU_h1_seed2024.parquet |
| finite_values:GRU_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h1_seed2025.parquet | True | rows=12265 |
| columns:GRU_h1_seed2025.parquet | True | missing=[] |
| single_key:GRU_h1_seed2025.parquet | True | models={'GRU'}, horizons={1}, seeds={2025} |
| filename:GRU_h1_seed2025.parquet | True | expected GRU_h1_seed2025.parquet |
| identical_samples:h1:GRU_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:GRU_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h1_seed2026.parquet | True | rows=12265 |
| columns:GRU_h1_seed2026.parquet | True | missing=[] |
| single_key:GRU_h1_seed2026.parquet | True | models={'GRU'}, horizons={1}, seeds={2026} |
| filename:GRU_h1_seed2026.parquet | True | expected GRU_h1_seed2026.parquet |
| identical_samples:h1:GRU_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:GRU_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h1_seed3407.parquet | True | rows=12265 |
| columns:GRU_h1_seed3407.parquet | True | missing=[] |
| single_key:GRU_h1_seed3407.parquet | True | models={'GRU'}, horizons={1}, seeds={3407} |
| filename:GRU_h1_seed3407.parquet | True | expected GRU_h1_seed3407.parquet |
| identical_samples:h1:GRU_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:GRU_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h1_seed42.parquet | True | rows=12265 |
| columns:GRU_h1_seed42.parquet | True | missing=[] |
| single_key:GRU_h1_seed42.parquet | True | models={'GRU'}, horizons={1}, seeds={42} |
| filename:GRU_h1_seed42.parquet | True | expected GRU_h1_seed42.parquet |
| identical_samples:h1:GRU_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:GRU_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h3_seed2024.parquet | True | rows=11878 |
| columns:GRU_h3_seed2024.parquet | True | missing=[] |
| single_key:GRU_h3_seed2024.parquet | True | models={'GRU'}, horizons={3}, seeds={2024} |
| filename:GRU_h3_seed2024.parquet | True | expected GRU_h3_seed2024.parquet |
| finite_values:GRU_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h3_seed2025.parquet | True | rows=11878 |
| columns:GRU_h3_seed2025.parquet | True | missing=[] |
| single_key:GRU_h3_seed2025.parquet | True | models={'GRU'}, horizons={3}, seeds={2025} |
| filename:GRU_h3_seed2025.parquet | True | expected GRU_h3_seed2025.parquet |
| identical_samples:h3:GRU_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:GRU_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h3_seed2026.parquet | True | rows=11878 |
| columns:GRU_h3_seed2026.parquet | True | missing=[] |
| single_key:GRU_h3_seed2026.parquet | True | models={'GRU'}, horizons={3}, seeds={2026} |
| filename:GRU_h3_seed2026.parquet | True | expected GRU_h3_seed2026.parquet |
| identical_samples:h3:GRU_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:GRU_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h3_seed3407.parquet | True | rows=11878 |
| columns:GRU_h3_seed3407.parquet | True | missing=[] |
| single_key:GRU_h3_seed3407.parquet | True | models={'GRU'}, horizons={3}, seeds={3407} |
| filename:GRU_h3_seed3407.parquet | True | expected GRU_h3_seed3407.parquet |
| identical_samples:h3:GRU_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:GRU_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h3_seed42.parquet | True | rows=11878 |
| columns:GRU_h3_seed42.parquet | True | missing=[] |
| single_key:GRU_h3_seed42.parquet | True | models={'GRU'}, horizons={3}, seeds={42} |
| filename:GRU_h3_seed42.parquet | True | expected GRU_h3_seed42.parquet |
| identical_samples:h3:GRU_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:GRU_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h6_seed2024.parquet | True | rows=12166 |
| columns:GRU_h6_seed2024.parquet | True | missing=[] |
| single_key:GRU_h6_seed2024.parquet | True | models={'GRU'}, horizons={6}, seeds={2024} |
| filename:GRU_h6_seed2024.parquet | True | expected GRU_h6_seed2024.parquet |
| finite_values:GRU_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h6_seed2025.parquet | True | rows=12166 |
| columns:GRU_h6_seed2025.parquet | True | missing=[] |
| single_key:GRU_h6_seed2025.parquet | True | models={'GRU'}, horizons={6}, seeds={2025} |
| filename:GRU_h6_seed2025.parquet | True | expected GRU_h6_seed2025.parquet |
| identical_samples:h6:GRU_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:GRU_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h6_seed2026.parquet | True | rows=12166 |
| columns:GRU_h6_seed2026.parquet | True | missing=[] |
| single_key:GRU_h6_seed2026.parquet | True | models={'GRU'}, horizons={6}, seeds={2026} |
| filename:GRU_h6_seed2026.parquet | True | expected GRU_h6_seed2026.parquet |
| identical_samples:h6:GRU_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:GRU_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h6_seed3407.parquet | True | rows=12166 |
| columns:GRU_h6_seed3407.parquet | True | missing=[] |
| single_key:GRU_h6_seed3407.parquet | True | models={'GRU'}, horizons={6}, seeds={3407} |
| filename:GRU_h6_seed3407.parquet | True | expected GRU_h6_seed3407.parquet |
| identical_samples:h6:GRU_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:GRU_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:GRU_h6_seed42.parquet | True | rows=12166 |
| columns:GRU_h6_seed42.parquet | True | missing=[] |
| single_key:GRU_h6_seed42.parquet | True | models={'GRU'}, horizons={6}, seeds={42} |
| filename:GRU_h6_seed42.parquet | True | expected GRU_h6_seed42.parquet |
| identical_samples:h6:GRU_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:GRU_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h1_seed2024.parquet | True | rows=12265 |
| columns:HA_h1_seed2024.parquet | True | missing=[] |
| single_key:HA_h1_seed2024.parquet | True | models={'HA'}, horizons={1}, seeds={2024} |
| filename:HA_h1_seed2024.parquet | True | expected HA_h1_seed2024.parquet |
| identical_samples:h1:HA_h1_seed2024.parquet | True | expected 12265 ids, found 12265 |
| finite_values:HA_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h1_seed2025.parquet | True | rows=12265 |
| columns:HA_h1_seed2025.parquet | True | missing=[] |
| single_key:HA_h1_seed2025.parquet | True | models={'HA'}, horizons={1}, seeds={2025} |
| filename:HA_h1_seed2025.parquet | True | expected HA_h1_seed2025.parquet |
| identical_samples:h1:HA_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:HA_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h1_seed2026.parquet | True | rows=12265 |
| columns:HA_h1_seed2026.parquet | True | missing=[] |
| single_key:HA_h1_seed2026.parquet | True | models={'HA'}, horizons={1}, seeds={2026} |
| filename:HA_h1_seed2026.parquet | True | expected HA_h1_seed2026.parquet |
| identical_samples:h1:HA_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:HA_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h1_seed3407.parquet | True | rows=12265 |
| columns:HA_h1_seed3407.parquet | True | missing=[] |
| single_key:HA_h1_seed3407.parquet | True | models={'HA'}, horizons={1}, seeds={3407} |
| filename:HA_h1_seed3407.parquet | True | expected HA_h1_seed3407.parquet |
| identical_samples:h1:HA_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:HA_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h1_seed42.parquet | True | rows=12265 |
| columns:HA_h1_seed42.parquet | True | missing=[] |
| single_key:HA_h1_seed42.parquet | True | models={'HA'}, horizons={1}, seeds={42} |
| filename:HA_h1_seed42.parquet | True | expected HA_h1_seed42.parquet |
| identical_samples:h1:HA_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:HA_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h3_seed2024.parquet | True | rows=11878 |
| columns:HA_h3_seed2024.parquet | True | missing=[] |
| single_key:HA_h3_seed2024.parquet | True | models={'HA'}, horizons={3}, seeds={2024} |
| filename:HA_h3_seed2024.parquet | True | expected HA_h3_seed2024.parquet |
| identical_samples:h3:HA_h3_seed2024.parquet | True | expected 11878 ids, found 11878 |
| finite_values:HA_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h3_seed2025.parquet | True | rows=11878 |
| columns:HA_h3_seed2025.parquet | True | missing=[] |
| single_key:HA_h3_seed2025.parquet | True | models={'HA'}, horizons={3}, seeds={2025} |
| filename:HA_h3_seed2025.parquet | True | expected HA_h3_seed2025.parquet |
| identical_samples:h3:HA_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:HA_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h3_seed2026.parquet | True | rows=11878 |
| columns:HA_h3_seed2026.parquet | True | missing=[] |
| single_key:HA_h3_seed2026.parquet | True | models={'HA'}, horizons={3}, seeds={2026} |
| filename:HA_h3_seed2026.parquet | True | expected HA_h3_seed2026.parquet |
| identical_samples:h3:HA_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:HA_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h3_seed3407.parquet | True | rows=11878 |
| columns:HA_h3_seed3407.parquet | True | missing=[] |
| single_key:HA_h3_seed3407.parquet | True | models={'HA'}, horizons={3}, seeds={3407} |
| filename:HA_h3_seed3407.parquet | True | expected HA_h3_seed3407.parquet |
| identical_samples:h3:HA_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:HA_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h3_seed42.parquet | True | rows=11878 |
| columns:HA_h3_seed42.parquet | True | missing=[] |
| single_key:HA_h3_seed42.parquet | True | models={'HA'}, horizons={3}, seeds={42} |
| filename:HA_h3_seed42.parquet | True | expected HA_h3_seed42.parquet |
| identical_samples:h3:HA_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:HA_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h6_seed2024.parquet | True | rows=12166 |
| columns:HA_h6_seed2024.parquet | True | missing=[] |
| single_key:HA_h6_seed2024.parquet | True | models={'HA'}, horizons={6}, seeds={2024} |
| filename:HA_h6_seed2024.parquet | True | expected HA_h6_seed2024.parquet |
| identical_samples:h6:HA_h6_seed2024.parquet | True | expected 12166 ids, found 12166 |
| finite_values:HA_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h6_seed2025.parquet | True | rows=12166 |
| columns:HA_h6_seed2025.parquet | True | missing=[] |
| single_key:HA_h6_seed2025.parquet | True | models={'HA'}, horizons={6}, seeds={2025} |
| filename:HA_h6_seed2025.parquet | True | expected HA_h6_seed2025.parquet |
| identical_samples:h6:HA_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:HA_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h6_seed2026.parquet | True | rows=12166 |
| columns:HA_h6_seed2026.parquet | True | missing=[] |
| single_key:HA_h6_seed2026.parquet | True | models={'HA'}, horizons={6}, seeds={2026} |
| filename:HA_h6_seed2026.parquet | True | expected HA_h6_seed2026.parquet |
| identical_samples:h6:HA_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:HA_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h6_seed3407.parquet | True | rows=12166 |
| columns:HA_h6_seed3407.parquet | True | missing=[] |
| single_key:HA_h6_seed3407.parquet | True | models={'HA'}, horizons={6}, seeds={3407} |
| filename:HA_h6_seed3407.parquet | True | expected HA_h6_seed3407.parquet |
| identical_samples:h6:HA_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:HA_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:HA_h6_seed42.parquet | True | rows=12166 |
| columns:HA_h6_seed42.parquet | True | missing=[] |
| single_key:HA_h6_seed42.parquet | True | models={'HA'}, horizons={6}, seeds={42} |
| filename:HA_h6_seed42.parquet | True | expected HA_h6_seed42.parquet |
| identical_samples:h6:HA_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:HA_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h1_seed2024.parquet | True | rows=12265 |
| columns:Persistence_h1_seed2024.parquet | True | missing=[] |
| single_key:Persistence_h1_seed2024.parquet | True | models={'Persistence'}, horizons={1}, seeds={2024} |
| filename:Persistence_h1_seed2024.parquet | True | expected Persistence_h1_seed2024.parquet |
| identical_samples:h1:Persistence_h1_seed2024.parquet | True | expected 12265 ids, found 12265 |
| finite_values:Persistence_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h1_seed2025.parquet | True | rows=12265 |
| columns:Persistence_h1_seed2025.parquet | True | missing=[] |
| single_key:Persistence_h1_seed2025.parquet | True | models={'Persistence'}, horizons={1}, seeds={2025} |
| filename:Persistence_h1_seed2025.parquet | True | expected Persistence_h1_seed2025.parquet |
| identical_samples:h1:Persistence_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:Persistence_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h1_seed2026.parquet | True | rows=12265 |
| columns:Persistence_h1_seed2026.parquet | True | missing=[] |
| single_key:Persistence_h1_seed2026.parquet | True | models={'Persistence'}, horizons={1}, seeds={2026} |
| filename:Persistence_h1_seed2026.parquet | True | expected Persistence_h1_seed2026.parquet |
| identical_samples:h1:Persistence_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:Persistence_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h1_seed3407.parquet | True | rows=12265 |
| columns:Persistence_h1_seed3407.parquet | True | missing=[] |
| single_key:Persistence_h1_seed3407.parquet | True | models={'Persistence'}, horizons={1}, seeds={3407} |
| filename:Persistence_h1_seed3407.parquet | True | expected Persistence_h1_seed3407.parquet |
| identical_samples:h1:Persistence_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:Persistence_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h1_seed42.parquet | True | rows=12265 |
| columns:Persistence_h1_seed42.parquet | True | missing=[] |
| single_key:Persistence_h1_seed42.parquet | True | models={'Persistence'}, horizons={1}, seeds={42} |
| filename:Persistence_h1_seed42.parquet | True | expected Persistence_h1_seed42.parquet |
| identical_samples:h1:Persistence_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:Persistence_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h3_seed2024.parquet | True | rows=11878 |
| columns:Persistence_h3_seed2024.parquet | True | missing=[] |
| single_key:Persistence_h3_seed2024.parquet | True | models={'Persistence'}, horizons={3}, seeds={2024} |
| filename:Persistence_h3_seed2024.parquet | True | expected Persistence_h3_seed2024.parquet |
| identical_samples:h3:Persistence_h3_seed2024.parquet | True | expected 11878 ids, found 11878 |
| finite_values:Persistence_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h3_seed2025.parquet | True | rows=11878 |
| columns:Persistence_h3_seed2025.parquet | True | missing=[] |
| single_key:Persistence_h3_seed2025.parquet | True | models={'Persistence'}, horizons={3}, seeds={2025} |
| filename:Persistence_h3_seed2025.parquet | True | expected Persistence_h3_seed2025.parquet |
| identical_samples:h3:Persistence_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:Persistence_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h3_seed2026.parquet | True | rows=11878 |
| columns:Persistence_h3_seed2026.parquet | True | missing=[] |
| single_key:Persistence_h3_seed2026.parquet | True | models={'Persistence'}, horizons={3}, seeds={2026} |
| filename:Persistence_h3_seed2026.parquet | True | expected Persistence_h3_seed2026.parquet |
| identical_samples:h3:Persistence_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:Persistence_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h3_seed3407.parquet | True | rows=11878 |
| columns:Persistence_h3_seed3407.parquet | True | missing=[] |
| single_key:Persistence_h3_seed3407.parquet | True | models={'Persistence'}, horizons={3}, seeds={3407} |
| filename:Persistence_h3_seed3407.parquet | True | expected Persistence_h3_seed3407.parquet |
| identical_samples:h3:Persistence_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:Persistence_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h3_seed42.parquet | True | rows=11878 |
| columns:Persistence_h3_seed42.parquet | True | missing=[] |
| single_key:Persistence_h3_seed42.parquet | True | models={'Persistence'}, horizons={3}, seeds={42} |
| filename:Persistence_h3_seed42.parquet | True | expected Persistence_h3_seed42.parquet |
| identical_samples:h3:Persistence_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:Persistence_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h6_seed2024.parquet | True | rows=12166 |
| columns:Persistence_h6_seed2024.parquet | True | missing=[] |
| single_key:Persistence_h6_seed2024.parquet | True | models={'Persistence'}, horizons={6}, seeds={2024} |
| filename:Persistence_h6_seed2024.parquet | True | expected Persistence_h6_seed2024.parquet |
| identical_samples:h6:Persistence_h6_seed2024.parquet | True | expected 12166 ids, found 12166 |
| finite_values:Persistence_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h6_seed2025.parquet | True | rows=12166 |
| columns:Persistence_h6_seed2025.parquet | True | missing=[] |
| single_key:Persistence_h6_seed2025.parquet | True | models={'Persistence'}, horizons={6}, seeds={2025} |
| filename:Persistence_h6_seed2025.parquet | True | expected Persistence_h6_seed2025.parquet |
| identical_samples:h6:Persistence_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:Persistence_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h6_seed2026.parquet | True | rows=12166 |
| columns:Persistence_h6_seed2026.parquet | True | missing=[] |
| single_key:Persistence_h6_seed2026.parquet | True | models={'Persistence'}, horizons={6}, seeds={2026} |
| filename:Persistence_h6_seed2026.parquet | True | expected Persistence_h6_seed2026.parquet |
| identical_samples:h6:Persistence_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:Persistence_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h6_seed3407.parquet | True | rows=12166 |
| columns:Persistence_h6_seed3407.parquet | True | missing=[] |
| single_key:Persistence_h6_seed3407.parquet | True | models={'Persistence'}, horizons={6}, seeds={3407} |
| filename:Persistence_h6_seed3407.parquet | True | expected Persistence_h6_seed3407.parquet |
| identical_samples:h6:Persistence_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:Persistence_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:Persistence_h6_seed42.parquet | True | rows=12166 |
| columns:Persistence_h6_seed42.parquet | True | missing=[] |
| single_key:Persistence_h6_seed42.parquet | True | models={'Persistence'}, horizons={6}, seeds={42} |
| filename:Persistence_h6_seed42.parquet | True | expected Persistence_h6_seed42.parquet |
| identical_samples:h6:Persistence_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:Persistence_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h1_seed2024.parquet | True | rows=12265 |
| columns:SeasonalHA_h1_seed2024.parquet | True | missing=[] |
| single_key:SeasonalHA_h1_seed2024.parquet | True | models={'SeasonalHA'}, horizons={1}, seeds={2024} |
| filename:SeasonalHA_h1_seed2024.parquet | True | expected SeasonalHA_h1_seed2024.parquet |
| identical_samples:h1:SeasonalHA_h1_seed2024.parquet | True | expected 12265 ids, found 12265 |
| finite_values:SeasonalHA_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h1_seed2025.parquet | True | rows=12265 |
| columns:SeasonalHA_h1_seed2025.parquet | True | missing=[] |
| single_key:SeasonalHA_h1_seed2025.parquet | True | models={'SeasonalHA'}, horizons={1}, seeds={2025} |
| filename:SeasonalHA_h1_seed2025.parquet | True | expected SeasonalHA_h1_seed2025.parquet |
| identical_samples:h1:SeasonalHA_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:SeasonalHA_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h1_seed2026.parquet | True | rows=12265 |
| columns:SeasonalHA_h1_seed2026.parquet | True | missing=[] |
| single_key:SeasonalHA_h1_seed2026.parquet | True | models={'SeasonalHA'}, horizons={1}, seeds={2026} |
| filename:SeasonalHA_h1_seed2026.parquet | True | expected SeasonalHA_h1_seed2026.parquet |
| identical_samples:h1:SeasonalHA_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:SeasonalHA_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h1_seed3407.parquet | True | rows=12265 |
| columns:SeasonalHA_h1_seed3407.parquet | True | missing=[] |
| single_key:SeasonalHA_h1_seed3407.parquet | True | models={'SeasonalHA'}, horizons={1}, seeds={3407} |
| filename:SeasonalHA_h1_seed3407.parquet | True | expected SeasonalHA_h1_seed3407.parquet |
| identical_samples:h1:SeasonalHA_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:SeasonalHA_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h1_seed42.parquet | True | rows=12265 |
| columns:SeasonalHA_h1_seed42.parquet | True | missing=[] |
| single_key:SeasonalHA_h1_seed42.parquet | True | models={'SeasonalHA'}, horizons={1}, seeds={42} |
| filename:SeasonalHA_h1_seed42.parquet | True | expected SeasonalHA_h1_seed42.parquet |
| identical_samples:h1:SeasonalHA_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:SeasonalHA_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h3_seed2024.parquet | True | rows=11878 |
| columns:SeasonalHA_h3_seed2024.parquet | True | missing=[] |
| single_key:SeasonalHA_h3_seed2024.parquet | True | models={'SeasonalHA'}, horizons={3}, seeds={2024} |
| filename:SeasonalHA_h3_seed2024.parquet | True | expected SeasonalHA_h3_seed2024.parquet |
| identical_samples:h3:SeasonalHA_h3_seed2024.parquet | True | expected 11878 ids, found 11878 |
| finite_values:SeasonalHA_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h3_seed2025.parquet | True | rows=11878 |
| columns:SeasonalHA_h3_seed2025.parquet | True | missing=[] |
| single_key:SeasonalHA_h3_seed2025.parquet | True | models={'SeasonalHA'}, horizons={3}, seeds={2025} |
| filename:SeasonalHA_h3_seed2025.parquet | True | expected SeasonalHA_h3_seed2025.parquet |
| identical_samples:h3:SeasonalHA_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:SeasonalHA_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h3_seed2026.parquet | True | rows=11878 |
| columns:SeasonalHA_h3_seed2026.parquet | True | missing=[] |
| single_key:SeasonalHA_h3_seed2026.parquet | True | models={'SeasonalHA'}, horizons={3}, seeds={2026} |
| filename:SeasonalHA_h3_seed2026.parquet | True | expected SeasonalHA_h3_seed2026.parquet |
| identical_samples:h3:SeasonalHA_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:SeasonalHA_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h3_seed3407.parquet | True | rows=11878 |
| columns:SeasonalHA_h3_seed3407.parquet | True | missing=[] |
| single_key:SeasonalHA_h3_seed3407.parquet | True | models={'SeasonalHA'}, horizons={3}, seeds={3407} |
| filename:SeasonalHA_h3_seed3407.parquet | True | expected SeasonalHA_h3_seed3407.parquet |
| identical_samples:h3:SeasonalHA_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:SeasonalHA_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h3_seed42.parquet | True | rows=11878 |
| columns:SeasonalHA_h3_seed42.parquet | True | missing=[] |
| single_key:SeasonalHA_h3_seed42.parquet | True | models={'SeasonalHA'}, horizons={3}, seeds={42} |
| filename:SeasonalHA_h3_seed42.parquet | True | expected SeasonalHA_h3_seed42.parquet |
| identical_samples:h3:SeasonalHA_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:SeasonalHA_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h6_seed2024.parquet | True | rows=12166 |
| columns:SeasonalHA_h6_seed2024.parquet | True | missing=[] |
| single_key:SeasonalHA_h6_seed2024.parquet | True | models={'SeasonalHA'}, horizons={6}, seeds={2024} |
| filename:SeasonalHA_h6_seed2024.parquet | True | expected SeasonalHA_h6_seed2024.parquet |
| identical_samples:h6:SeasonalHA_h6_seed2024.parquet | True | expected 12166 ids, found 12166 |
| finite_values:SeasonalHA_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h6_seed2025.parquet | True | rows=12166 |
| columns:SeasonalHA_h6_seed2025.parquet | True | missing=[] |
| single_key:SeasonalHA_h6_seed2025.parquet | True | models={'SeasonalHA'}, horizons={6}, seeds={2025} |
| filename:SeasonalHA_h6_seed2025.parquet | True | expected SeasonalHA_h6_seed2025.parquet |
| identical_samples:h6:SeasonalHA_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:SeasonalHA_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h6_seed2026.parquet | True | rows=12166 |
| columns:SeasonalHA_h6_seed2026.parquet | True | missing=[] |
| single_key:SeasonalHA_h6_seed2026.parquet | True | models={'SeasonalHA'}, horizons={6}, seeds={2026} |
| filename:SeasonalHA_h6_seed2026.parquet | True | expected SeasonalHA_h6_seed2026.parquet |
| identical_samples:h6:SeasonalHA_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:SeasonalHA_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h6_seed3407.parquet | True | rows=12166 |
| columns:SeasonalHA_h6_seed3407.parquet | True | missing=[] |
| single_key:SeasonalHA_h6_seed3407.parquet | True | models={'SeasonalHA'}, horizons={6}, seeds={3407} |
| filename:SeasonalHA_h6_seed3407.parquet | True | expected SeasonalHA_h6_seed3407.parquet |
| identical_samples:h6:SeasonalHA_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:SeasonalHA_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:SeasonalHA_h6_seed42.parquet | True | rows=12166 |
| columns:SeasonalHA_h6_seed42.parquet | True | missing=[] |
| single_key:SeasonalHA_h6_seed42.parquet | True | models={'SeasonalHA'}, horizons={6}, seeds={42} |
| filename:SeasonalHA_h6_seed42.parquet | True | expected SeasonalHA_h6_seed42.parquet |
| identical_samples:h6:SeasonalHA_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:SeasonalHA_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h1_seed2024.parquet | True | rows=12265 |
| columns:ST-Transformer-lite_h1_seed2024.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h1_seed2024.parquet | True | models={'ST-Transformer-lite'}, horizons={1}, seeds={2024} |
| filename:ST-Transformer-lite_h1_seed2024.parquet | True | expected ST-Transformer-lite_h1_seed2024.parquet |
| identical_samples:h1:ST-Transformer-lite_h1_seed2024.parquet | True | expected 12265 ids, found 12265 |
| finite_values:ST-Transformer-lite_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h1_seed2025.parquet | True | rows=12265 |
| columns:ST-Transformer-lite_h1_seed2025.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h1_seed2025.parquet | True | models={'ST-Transformer-lite'}, horizons={1}, seeds={2025} |
| filename:ST-Transformer-lite_h1_seed2025.parquet | True | expected ST-Transformer-lite_h1_seed2025.parquet |
| identical_samples:h1:ST-Transformer-lite_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:ST-Transformer-lite_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h1_seed2026.parquet | True | rows=12265 |
| columns:ST-Transformer-lite_h1_seed2026.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h1_seed2026.parquet | True | models={'ST-Transformer-lite'}, horizons={1}, seeds={2026} |
| filename:ST-Transformer-lite_h1_seed2026.parquet | True | expected ST-Transformer-lite_h1_seed2026.parquet |
| identical_samples:h1:ST-Transformer-lite_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:ST-Transformer-lite_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h1_seed3407.parquet | True | rows=12265 |
| columns:ST-Transformer-lite_h1_seed3407.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h1_seed3407.parquet | True | models={'ST-Transformer-lite'}, horizons={1}, seeds={3407} |
| filename:ST-Transformer-lite_h1_seed3407.parquet | True | expected ST-Transformer-lite_h1_seed3407.parquet |
| identical_samples:h1:ST-Transformer-lite_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:ST-Transformer-lite_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h1_seed42.parquet | True | rows=12265 |
| columns:ST-Transformer-lite_h1_seed42.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h1_seed42.parquet | True | models={'ST-Transformer-lite'}, horizons={1}, seeds={42} |
| filename:ST-Transformer-lite_h1_seed42.parquet | True | expected ST-Transformer-lite_h1_seed42.parquet |
| identical_samples:h1:ST-Transformer-lite_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:ST-Transformer-lite_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h3_seed2024.parquet | True | rows=11878 |
| columns:ST-Transformer-lite_h3_seed2024.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h3_seed2024.parquet | True | models={'ST-Transformer-lite'}, horizons={3}, seeds={2024} |
| filename:ST-Transformer-lite_h3_seed2024.parquet | True | expected ST-Transformer-lite_h3_seed2024.parquet |
| identical_samples:h3:ST-Transformer-lite_h3_seed2024.parquet | True | expected 11878 ids, found 11878 |
| finite_values:ST-Transformer-lite_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h3_seed2025.parquet | True | rows=11878 |
| columns:ST-Transformer-lite_h3_seed2025.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h3_seed2025.parquet | True | models={'ST-Transformer-lite'}, horizons={3}, seeds={2025} |
| filename:ST-Transformer-lite_h3_seed2025.parquet | True | expected ST-Transformer-lite_h3_seed2025.parquet |
| identical_samples:h3:ST-Transformer-lite_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:ST-Transformer-lite_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h3_seed2026.parquet | True | rows=11878 |
| columns:ST-Transformer-lite_h3_seed2026.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h3_seed2026.parquet | True | models={'ST-Transformer-lite'}, horizons={3}, seeds={2026} |
| filename:ST-Transformer-lite_h3_seed2026.parquet | True | expected ST-Transformer-lite_h3_seed2026.parquet |
| identical_samples:h3:ST-Transformer-lite_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:ST-Transformer-lite_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h3_seed3407.parquet | True | rows=11878 |
| columns:ST-Transformer-lite_h3_seed3407.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h3_seed3407.parquet | True | models={'ST-Transformer-lite'}, horizons={3}, seeds={3407} |
| filename:ST-Transformer-lite_h3_seed3407.parquet | True | expected ST-Transformer-lite_h3_seed3407.parquet |
| identical_samples:h3:ST-Transformer-lite_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:ST-Transformer-lite_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h3_seed42.parquet | True | rows=11878 |
| columns:ST-Transformer-lite_h3_seed42.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h3_seed42.parquet | True | models={'ST-Transformer-lite'}, horizons={3}, seeds={42} |
| filename:ST-Transformer-lite_h3_seed42.parquet | True | expected ST-Transformer-lite_h3_seed42.parquet |
| identical_samples:h3:ST-Transformer-lite_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:ST-Transformer-lite_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h6_seed2024.parquet | True | rows=12166 |
| columns:ST-Transformer-lite_h6_seed2024.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h6_seed2024.parquet | True | models={'ST-Transformer-lite'}, horizons={6}, seeds={2024} |
| filename:ST-Transformer-lite_h6_seed2024.parquet | True | expected ST-Transformer-lite_h6_seed2024.parquet |
| identical_samples:h6:ST-Transformer-lite_h6_seed2024.parquet | True | expected 12166 ids, found 12166 |
| finite_values:ST-Transformer-lite_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h6_seed2025.parquet | True | rows=12166 |
| columns:ST-Transformer-lite_h6_seed2025.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h6_seed2025.parquet | True | models={'ST-Transformer-lite'}, horizons={6}, seeds={2025} |
| filename:ST-Transformer-lite_h6_seed2025.parquet | True | expected ST-Transformer-lite_h6_seed2025.parquet |
| identical_samples:h6:ST-Transformer-lite_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:ST-Transformer-lite_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h6_seed2026.parquet | True | rows=12166 |
| columns:ST-Transformer-lite_h6_seed2026.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h6_seed2026.parquet | True | models={'ST-Transformer-lite'}, horizons={6}, seeds={2026} |
| filename:ST-Transformer-lite_h6_seed2026.parquet | True | expected ST-Transformer-lite_h6_seed2026.parquet |
| identical_samples:h6:ST-Transformer-lite_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:ST-Transformer-lite_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h6_seed3407.parquet | True | rows=12166 |
| columns:ST-Transformer-lite_h6_seed3407.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h6_seed3407.parquet | True | models={'ST-Transformer-lite'}, horizons={6}, seeds={3407} |
| filename:ST-Transformer-lite_h6_seed3407.parquet | True | expected ST-Transformer-lite_h6_seed3407.parquet |
| identical_samples:h6:ST-Transformer-lite_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:ST-Transformer-lite_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:ST-Transformer-lite_h6_seed42.parquet | True | rows=12166 |
| columns:ST-Transformer-lite_h6_seed42.parquet | True | missing=[] |
| single_key:ST-Transformer-lite_h6_seed42.parquet | True | models={'ST-Transformer-lite'}, horizons={6}, seeds={42} |
| filename:ST-Transformer-lite_h6_seed42.parquet | True | expected ST-Transformer-lite_h6_seed42.parquet |
| identical_samples:h6:ST-Transformer-lite_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:ST-Transformer-lite_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h1_seed2024.parquet | True | rows=12265 |
| columns:TCN_h1_seed2024.parquet | True | missing=[] |
| single_key:TCN_h1_seed2024.parquet | True | models={'TCN'}, horizons={1}, seeds={2024} |
| filename:TCN_h1_seed2024.parquet | True | expected TCN_h1_seed2024.parquet |
| identical_samples:h1:TCN_h1_seed2024.parquet | True | expected 12265 ids, found 12265 |
| finite_values:TCN_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h1_seed2025.parquet | True | rows=12265 |
| columns:TCN_h1_seed2025.parquet | True | missing=[] |
| single_key:TCN_h1_seed2025.parquet | True | models={'TCN'}, horizons={1}, seeds={2025} |
| filename:TCN_h1_seed2025.parquet | True | expected TCN_h1_seed2025.parquet |
| identical_samples:h1:TCN_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:TCN_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h1_seed2026.parquet | True | rows=12265 |
| columns:TCN_h1_seed2026.parquet | True | missing=[] |
| single_key:TCN_h1_seed2026.parquet | True | models={'TCN'}, horizons={1}, seeds={2026} |
| filename:TCN_h1_seed2026.parquet | True | expected TCN_h1_seed2026.parquet |
| identical_samples:h1:TCN_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:TCN_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h1_seed3407.parquet | True | rows=12265 |
| columns:TCN_h1_seed3407.parquet | True | missing=[] |
| single_key:TCN_h1_seed3407.parquet | True | models={'TCN'}, horizons={1}, seeds={3407} |
| filename:TCN_h1_seed3407.parquet | True | expected TCN_h1_seed3407.parquet |
| identical_samples:h1:TCN_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:TCN_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h1_seed42.parquet | True | rows=12265 |
| columns:TCN_h1_seed42.parquet | True | missing=[] |
| single_key:TCN_h1_seed42.parquet | True | models={'TCN'}, horizons={1}, seeds={42} |
| filename:TCN_h1_seed42.parquet | True | expected TCN_h1_seed42.parquet |
| identical_samples:h1:TCN_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:TCN_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h3_seed2024.parquet | True | rows=11878 |
| columns:TCN_h3_seed2024.parquet | True | missing=[] |
| single_key:TCN_h3_seed2024.parquet | True | models={'TCN'}, horizons={3}, seeds={2024} |
| filename:TCN_h3_seed2024.parquet | True | expected TCN_h3_seed2024.parquet |
| identical_samples:h3:TCN_h3_seed2024.parquet | True | expected 11878 ids, found 11878 |
| finite_values:TCN_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h3_seed2025.parquet | True | rows=11878 |
| columns:TCN_h3_seed2025.parquet | True | missing=[] |
| single_key:TCN_h3_seed2025.parquet | True | models={'TCN'}, horizons={3}, seeds={2025} |
| filename:TCN_h3_seed2025.parquet | True | expected TCN_h3_seed2025.parquet |
| identical_samples:h3:TCN_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:TCN_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h3_seed2026.parquet | True | rows=11878 |
| columns:TCN_h3_seed2026.parquet | True | missing=[] |
| single_key:TCN_h3_seed2026.parquet | True | models={'TCN'}, horizons={3}, seeds={2026} |
| filename:TCN_h3_seed2026.parquet | True | expected TCN_h3_seed2026.parquet |
| identical_samples:h3:TCN_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:TCN_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h3_seed3407.parquet | True | rows=11878 |
| columns:TCN_h3_seed3407.parquet | True | missing=[] |
| single_key:TCN_h3_seed3407.parquet | True | models={'TCN'}, horizons={3}, seeds={3407} |
| filename:TCN_h3_seed3407.parquet | True | expected TCN_h3_seed3407.parquet |
| identical_samples:h3:TCN_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:TCN_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h3_seed42.parquet | True | rows=11878 |
| columns:TCN_h3_seed42.parquet | True | missing=[] |
| single_key:TCN_h3_seed42.parquet | True | models={'TCN'}, horizons={3}, seeds={42} |
| filename:TCN_h3_seed42.parquet | True | expected TCN_h3_seed42.parquet |
| identical_samples:h3:TCN_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:TCN_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h6_seed2024.parquet | True | rows=12166 |
| columns:TCN_h6_seed2024.parquet | True | missing=[] |
| single_key:TCN_h6_seed2024.parquet | True | models={'TCN'}, horizons={6}, seeds={2024} |
| filename:TCN_h6_seed2024.parquet | True | expected TCN_h6_seed2024.parquet |
| identical_samples:h6:TCN_h6_seed2024.parquet | True | expected 12166 ids, found 12166 |
| finite_values:TCN_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h6_seed2025.parquet | True | rows=12166 |
| columns:TCN_h6_seed2025.parquet | True | missing=[] |
| single_key:TCN_h6_seed2025.parquet | True | models={'TCN'}, horizons={6}, seeds={2025} |
| filename:TCN_h6_seed2025.parquet | True | expected TCN_h6_seed2025.parquet |
| identical_samples:h6:TCN_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:TCN_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h6_seed2026.parquet | True | rows=12166 |
| columns:TCN_h6_seed2026.parquet | True | missing=[] |
| single_key:TCN_h6_seed2026.parquet | True | models={'TCN'}, horizons={6}, seeds={2026} |
| filename:TCN_h6_seed2026.parquet | True | expected TCN_h6_seed2026.parquet |
| identical_samples:h6:TCN_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:TCN_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h6_seed3407.parquet | True | rows=12166 |
| columns:TCN_h6_seed3407.parquet | True | missing=[] |
| single_key:TCN_h6_seed3407.parquet | True | models={'TCN'}, horizons={6}, seeds={3407} |
| filename:TCN_h6_seed3407.parquet | True | expected TCN_h6_seed3407.parquet |
| identical_samples:h6:TCN_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:TCN_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:TCN_h6_seed42.parquet | True | rows=12166 |
| columns:TCN_h6_seed42.parquet | True | missing=[] |
| single_key:TCN_h6_seed42.parquet | True | models={'TCN'}, horizons={6}, seeds={42} |
| filename:TCN_h6_seed42.parquet | True | expected TCN_h6_seed42.parquet |
| identical_samples:h6:TCN_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:TCN_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h1_seed2024.parquet | True | rows=12265 |
| columns:XGBoost_h1_seed2024.parquet | True | missing=[] |
| single_key:XGBoost_h1_seed2024.parquet | True | models={'XGBoost'}, horizons={1}, seeds={2024} |
| filename:XGBoost_h1_seed2024.parquet | True | expected XGBoost_h1_seed2024.parquet |
| identical_samples:h1:XGBoost_h1_seed2024.parquet | True | expected 12265 ids, found 12265 |
| finite_values:XGBoost_h1_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h1_seed2025.parquet | True | rows=12265 |
| columns:XGBoost_h1_seed2025.parquet | True | missing=[] |
| single_key:XGBoost_h1_seed2025.parquet | True | models={'XGBoost'}, horizons={1}, seeds={2025} |
| filename:XGBoost_h1_seed2025.parquet | True | expected XGBoost_h1_seed2025.parquet |
| identical_samples:h1:XGBoost_h1_seed2025.parquet | True | expected 12265 ids, found 12265 |
| finite_values:XGBoost_h1_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h1_seed2026.parquet | True | rows=12265 |
| columns:XGBoost_h1_seed2026.parquet | True | missing=[] |
| single_key:XGBoost_h1_seed2026.parquet | True | models={'XGBoost'}, horizons={1}, seeds={2026} |
| filename:XGBoost_h1_seed2026.parquet | True | expected XGBoost_h1_seed2026.parquet |
| identical_samples:h1:XGBoost_h1_seed2026.parquet | True | expected 12265 ids, found 12265 |
| finite_values:XGBoost_h1_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h1_seed3407.parquet | True | rows=12265 |
| columns:XGBoost_h1_seed3407.parquet | True | missing=[] |
| single_key:XGBoost_h1_seed3407.parquet | True | models={'XGBoost'}, horizons={1}, seeds={3407} |
| filename:XGBoost_h1_seed3407.parquet | True | expected XGBoost_h1_seed3407.parquet |
| identical_samples:h1:XGBoost_h1_seed3407.parquet | True | expected 12265 ids, found 12265 |
| finite_values:XGBoost_h1_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h1_seed42.parquet | True | rows=12265 |
| columns:XGBoost_h1_seed42.parquet | True | missing=[] |
| single_key:XGBoost_h1_seed42.parquet | True | models={'XGBoost'}, horizons={1}, seeds={42} |
| filename:XGBoost_h1_seed42.parquet | True | expected XGBoost_h1_seed42.parquet |
| identical_samples:h1:XGBoost_h1_seed42.parquet | True | expected 12265 ids, found 12265 |
| finite_values:XGBoost_h1_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h3_seed2024.parquet | True | rows=11878 |
| columns:XGBoost_h3_seed2024.parquet | True | missing=[] |
| single_key:XGBoost_h3_seed2024.parquet | True | models={'XGBoost'}, horizons={3}, seeds={2024} |
| filename:XGBoost_h3_seed2024.parquet | True | expected XGBoost_h3_seed2024.parquet |
| identical_samples:h3:XGBoost_h3_seed2024.parquet | True | expected 11878 ids, found 11878 |
| finite_values:XGBoost_h3_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h3_seed2025.parquet | True | rows=11878 |
| columns:XGBoost_h3_seed2025.parquet | True | missing=[] |
| single_key:XGBoost_h3_seed2025.parquet | True | models={'XGBoost'}, horizons={3}, seeds={2025} |
| filename:XGBoost_h3_seed2025.parquet | True | expected XGBoost_h3_seed2025.parquet |
| identical_samples:h3:XGBoost_h3_seed2025.parquet | True | expected 11878 ids, found 11878 |
| finite_values:XGBoost_h3_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h3_seed2026.parquet | True | rows=11878 |
| columns:XGBoost_h3_seed2026.parquet | True | missing=[] |
| single_key:XGBoost_h3_seed2026.parquet | True | models={'XGBoost'}, horizons={3}, seeds={2026} |
| filename:XGBoost_h3_seed2026.parquet | True | expected XGBoost_h3_seed2026.parquet |
| identical_samples:h3:XGBoost_h3_seed2026.parquet | True | expected 11878 ids, found 11878 |
| finite_values:XGBoost_h3_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h3_seed3407.parquet | True | rows=11878 |
| columns:XGBoost_h3_seed3407.parquet | True | missing=[] |
| single_key:XGBoost_h3_seed3407.parquet | True | models={'XGBoost'}, horizons={3}, seeds={3407} |
| filename:XGBoost_h3_seed3407.parquet | True | expected XGBoost_h3_seed3407.parquet |
| identical_samples:h3:XGBoost_h3_seed3407.parquet | True | expected 11878 ids, found 11878 |
| finite_values:XGBoost_h3_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h3_seed42.parquet | True | rows=11878 |
| columns:XGBoost_h3_seed42.parquet | True | missing=[] |
| single_key:XGBoost_h3_seed42.parquet | True | models={'XGBoost'}, horizons={3}, seeds={42} |
| filename:XGBoost_h3_seed42.parquet | True | expected XGBoost_h3_seed42.parquet |
| identical_samples:h3:XGBoost_h3_seed42.parquet | True | expected 11878 ids, found 11878 |
| finite_values:XGBoost_h3_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h6_seed2024.parquet | True | rows=12166 |
| columns:XGBoost_h6_seed2024.parquet | True | missing=[] |
| single_key:XGBoost_h6_seed2024.parquet | True | models={'XGBoost'}, horizons={6}, seeds={2024} |
| filename:XGBoost_h6_seed2024.parquet | True | expected XGBoost_h6_seed2024.parquet |
| identical_samples:h6:XGBoost_h6_seed2024.parquet | True | expected 12166 ids, found 12166 |
| finite_values:XGBoost_h6_seed2024.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h6_seed2025.parquet | True | rows=12166 |
| columns:XGBoost_h6_seed2025.parquet | True | missing=[] |
| single_key:XGBoost_h6_seed2025.parquet | True | models={'XGBoost'}, horizons={6}, seeds={2025} |
| filename:XGBoost_h6_seed2025.parquet | True | expected XGBoost_h6_seed2025.parquet |
| identical_samples:h6:XGBoost_h6_seed2025.parquet | True | expected 12166 ids, found 12166 |
| finite_values:XGBoost_h6_seed2025.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h6_seed2026.parquet | True | rows=12166 |
| columns:XGBoost_h6_seed2026.parquet | True | missing=[] |
| single_key:XGBoost_h6_seed2026.parquet | True | models={'XGBoost'}, horizons={6}, seeds={2026} |
| filename:XGBoost_h6_seed2026.parquet | True | expected XGBoost_h6_seed2026.parquet |
| identical_samples:h6:XGBoost_h6_seed2026.parquet | True | expected 12166 ids, found 12166 |
| finite_values:XGBoost_h6_seed2026.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h6_seed3407.parquet | True | rows=12166 |
| columns:XGBoost_h6_seed3407.parquet | True | missing=[] |
| single_key:XGBoost_h6_seed3407.parquet | True | models={'XGBoost'}, horizons={6}, seeds={3407} |
| filename:XGBoost_h6_seed3407.parquet | True | expected XGBoost_h6_seed3407.parquet |
| identical_samples:h6:XGBoost_h6_seed3407.parquet | True | expected 12166 ids, found 12166 |
| finite_values:XGBoost_h6_seed3407.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| nonempty:XGBoost_h6_seed42.parquet | True | rows=12166 |
| columns:XGBoost_h6_seed42.parquet | True | missing=[] |
| single_key:XGBoost_h6_seed42.parquet | True | models={'XGBoost'}, horizons={6}, seeds={42} |
| filename:XGBoost_h6_seed42.parquet | True | expected XGBoost_h6_seed42.parquet |
| identical_samples:h6:XGBoost_h6_seed42.parquet | True | expected 12166 ids, found 12166 |
| finite_values:XGBoost_h6_seed42.parquet | True | non-finite y_true/y_pred/abs_error/squared_error |
| exact_prediction_keys | True | missing=[], extra=[] |
| metric_parquet_key_match | True | metrics=105, parquet=105 |
| test_n:('HA', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('HA', 1, 42) | True | metrics=1.9087225491398945, recomputed=1.9087225491398945 |
| rmse:('HA', 1, 42) | True | metrics=3.7858135633876095, recomputed=3.7858135633876104 |
| test_n:('SeasonalHA', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('SeasonalHA', 1, 42) | True | metrics=1.1484393823112802, recomputed=1.1484393823112802 |
| rmse:('SeasonalHA', 1, 42) | True | metrics=2.689582231267182, recomputed=2.689582231267182 |
| test_n:('Persistence', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('Persistence', 1, 42) | True | metrics=1.0493704965733723, recomputed=1.0493704965733723 |
| rmse:('Persistence', 1, 42) | True | metrics=3.1935336818078524, recomputed=3.1935336818078524 |
| test_n:('XGBoost', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('XGBoost', 1, 42) | True | metrics=0.9754881618171628, recomputed=0.9754881618171627 |
| rmse:('XGBoost', 1, 42) | True | metrics=2.273730045644893, recomputed=2.2737300456448932 |
| test_n:('GRU', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('GRU', 1, 42) | True | metrics=1.0824979600933586, recomputed=1.0824979600933586 |
| rmse:('GRU', 1, 42) | True | metrics=2.4775653740748944, recomputed=2.4775653740748944 |
| test_n:('TCN', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('TCN', 1, 42) | True | metrics=1.0808280047522825, recomputed=1.0808280047522825 |
| rmse:('TCN', 1, 42) | True | metrics=2.410745754110528, recomputed=2.4107457541105277 |
| test_n:('ST-Transformer-lite', 1, 42) | True | metrics=12265, parquet=12265 |
| mae:('ST-Transformer-lite', 1, 42) | True | metrics=1.1339109752793437, recomputed=1.1339109752793435 |
| rmse:('ST-Transformer-lite', 1, 42) | True | metrics=2.493446266319621, recomputed=2.493446266319621 |
| test_n:('HA', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('HA', 1, 2024) | True | metrics=1.9087225491398945, recomputed=1.9087225491398945 |
| rmse:('HA', 1, 2024) | True | metrics=3.7858135633876095, recomputed=3.7858135633876104 |
| test_n:('SeasonalHA', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('SeasonalHA', 1, 2024) | True | metrics=1.1484393823112802, recomputed=1.1484393823112802 |
| rmse:('SeasonalHA', 1, 2024) | True | metrics=2.689582231267182, recomputed=2.689582231267182 |
| test_n:('Persistence', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('Persistence', 1, 2024) | True | metrics=1.0493704965733723, recomputed=1.0493704965733723 |
| rmse:('Persistence', 1, 2024) | True | metrics=3.1935336818078524, recomputed=3.1935336818078524 |
| test_n:('XGBoost', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('XGBoost', 1, 2024) | True | metrics=0.9666126464271468, recomputed=0.9666126464271467 |
| rmse:('XGBoost', 1, 2024) | True | metrics=2.2575673804204706, recomputed=2.2575673804204706 |
| test_n:('GRU', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('GRU', 1, 2024) | True | metrics=1.0536621614713548, recomputed=1.0536621614713548 |
| rmse:('GRU', 1, 2024) | True | metrics=2.440587619557492, recomputed=2.440587619557492 |
| test_n:('TCN', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('TCN', 1, 2024) | True | metrics=1.2894024442664176, recomputed=1.2894024442664176 |
| rmse:('TCN', 1, 2024) | True | metrics=2.550351453703432, recomputed=2.550351453703432 |
| test_n:('ST-Transformer-lite', 1, 2024) | True | metrics=12265, parquet=12265 |
| mae:('ST-Transformer-lite', 1, 2024) | True | metrics=1.0536606097775385, recomputed=1.0536606097775385 |
| rmse:('ST-Transformer-lite', 1, 2024) | True | metrics=2.445787180952758, recomputed=2.445787180952758 |
| test_n:('HA', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('HA', 1, 2025) | True | metrics=1.9087225491398945, recomputed=1.9087225491398945 |
| rmse:('HA', 1, 2025) | True | metrics=3.7858135633876095, recomputed=3.7858135633876104 |
| test_n:('SeasonalHA', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('SeasonalHA', 1, 2025) | True | metrics=1.1484393823112802, recomputed=1.1484393823112802 |
| rmse:('SeasonalHA', 1, 2025) | True | metrics=2.689582231267182, recomputed=2.689582231267182 |
| test_n:('Persistence', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('Persistence', 1, 2025) | True | metrics=1.0493704965733723, recomputed=1.0493704965733723 |
| rmse:('Persistence', 1, 2025) | True | metrics=3.1935336818078524, recomputed=3.1935336818078524 |
| test_n:('XGBoost', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('XGBoost', 1, 2025) | True | metrics=0.9864562109641236, recomputed=0.9864562109641236 |
| rmse:('XGBoost', 1, 2025) | True | metrics=2.300100721195666, recomputed=2.300100721195666 |
| test_n:('GRU', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('GRU', 1, 2025) | True | metrics=1.0672940662817911, recomputed=1.0672940662817911 |
| rmse:('GRU', 1, 2025) | True | metrics=2.440868021947784, recomputed=2.440868021947784 |
| test_n:('TCN', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('TCN', 1, 2025) | True | metrics=1.076335222265257, recomputed=1.0763352222652567 |
| rmse:('TCN', 1, 2025) | True | metrics=2.420085505129536, recomputed=2.4200855051295362 |
| test_n:('ST-Transformer-lite', 1, 2025) | True | metrics=12265, parquet=12265 |
| mae:('ST-Transformer-lite', 1, 2025) | True | metrics=1.0086975192518268, recomputed=1.0086975192518268 |
| rmse:('ST-Transformer-lite', 1, 2025) | True | metrics=2.4265423766830563, recomputed=2.4265423766830563 |
| test_n:('HA', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('HA', 1, 2026) | True | metrics=1.9087225491398945, recomputed=1.9087225491398945 |
| rmse:('HA', 1, 2026) | True | metrics=3.7858135633876095, recomputed=3.7858135633876104 |
| test_n:('SeasonalHA', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('SeasonalHA', 1, 2026) | True | metrics=1.1484393823112802, recomputed=1.1484393823112802 |
| rmse:('SeasonalHA', 1, 2026) | True | metrics=2.689582231267182, recomputed=2.689582231267182 |
| test_n:('Persistence', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('Persistence', 1, 2026) | True | metrics=1.0493704965733723, recomputed=1.0493704965733723 |
| rmse:('Persistence', 1, 2026) | True | metrics=3.1935336818078524, recomputed=3.1935336818078524 |
| test_n:('XGBoost', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('XGBoost', 1, 2026) | True | metrics=0.97194424849649, recomputed=0.9719442484964899 |
| rmse:('XGBoost', 1, 2026) | True | metrics=2.274192934170031, recomputed=2.274192934170031 |
| test_n:('GRU', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('GRU', 1, 2026) | True | metrics=0.9841886541379796, recomputed=0.9841886541379795 |
| rmse:('GRU', 1, 2026) | True | metrics=2.382109834878539, recomputed=2.382109834878539 |
| test_n:('TCN', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('TCN', 1, 2026) | True | metrics=1.1523838764786285, recomputed=1.1523838764786283 |
| rmse:('TCN', 1, 2026) | True | metrics=2.4317375030474984, recomputed=2.4317375030474984 |
| test_n:('ST-Transformer-lite', 1, 2026) | True | metrics=12265, parquet=12265 |
| mae:('ST-Transformer-lite', 1, 2026) | True | metrics=1.1148925384695658, recomputed=1.1148925384695658 |
| rmse:('ST-Transformer-lite', 1, 2026) | True | metrics=2.4751620871113245, recomputed=2.4751620871113245 |
| test_n:('HA', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('HA', 1, 3407) | True | metrics=1.9087225491398945, recomputed=1.9087225491398945 |
| rmse:('HA', 1, 3407) | True | metrics=3.7858135633876095, recomputed=3.7858135633876104 |
| test_n:('SeasonalHA', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('SeasonalHA', 1, 3407) | True | metrics=1.1484393823112802, recomputed=1.1484393823112802 |
| rmse:('SeasonalHA', 1, 3407) | True | metrics=2.689582231267182, recomputed=2.689582231267182 |
| test_n:('Persistence', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('Persistence', 1, 3407) | True | metrics=1.0493704965733723, recomputed=1.0493704965733723 |
| rmse:('Persistence', 1, 3407) | True | metrics=3.1935336818078524, recomputed=3.1935336818078524 |
| test_n:('XGBoost', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('XGBoost', 1, 3407) | True | metrics=0.9674360639943038, recomputed=0.9674360639943038 |
| rmse:('XGBoost', 1, 3407) | True | metrics=2.2658686073388195, recomputed=2.2658686073388195 |
| test_n:('GRU', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('GRU', 1, 3407) | True | metrics=1.0555837347417083, recomputed=1.0555837347417085 |
| rmse:('GRU', 1, 3407) | True | metrics=2.432666746392397, recomputed=2.4326667463923966 |
| test_n:('TCN', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('TCN', 1, 3407) | True | metrics=1.1110538793689029, recomputed=1.1110538793689029 |
| rmse:('TCN', 1, 3407) | True | metrics=2.4104664274849346, recomputed=2.4104664274849346 |
| test_n:('ST-Transformer-lite', 1, 3407) | True | metrics=12265, parquet=12265 |
| mae:('ST-Transformer-lite', 1, 3407) | True | metrics=1.022140058633312, recomputed=1.022140058633312 |
| rmse:('ST-Transformer-lite', 1, 3407) | True | metrics=2.5862653543382703, recomputed=2.5862653543382703 |
| test_n:('HA', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('HA', 3, 42) | True | metrics=1.7670076734430764, recomputed=1.7670076734430764 |
| rmse:('HA', 3, 42) | True | metrics=3.221253620625528, recomputed=3.2212536206255273 |
| test_n:('SeasonalHA', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('SeasonalHA', 3, 42) | True | metrics=1.015958182557622, recomputed=1.015958182557622 |
| rmse:('SeasonalHA', 3, 42) | True | metrics=1.943902548137346, recomputed=1.943902548137346 |
| test_n:('Persistence', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('Persistence', 3, 42) | True | metrics=1.310700671402648, recomputed=1.3107006714026481 |
| rmse:('Persistence', 3, 42) | True | metrics=3.2709789138092544, recomputed=3.2709789138092544 |
| test_n:('XGBoost', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('XGBoost', 3, 42) | True | metrics=0.8652056803063404, recomputed=0.8652056803063404 |
| rmse:('XGBoost', 3, 42) | True | metrics=1.647763616801272, recomputed=1.6477636168012721 |
| test_n:('GRU', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('GRU', 3, 42) | True | metrics=1.0531255454201351, recomputed=1.0531255454201351 |
| rmse:('GRU', 3, 42) | True | metrics=1.9105882193141717, recomputed=1.9105882193141714 |
| test_n:('TCN', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('TCN', 3, 42) | True | metrics=1.0222466029308324, recomputed=1.0222466029308324 |
| rmse:('TCN', 3, 42) | True | metrics=1.8519774583210475, recomputed=1.8519774583210475 |
| test_n:('ST-Transformer-lite', 3, 42) | True | metrics=11878, parquet=11878 |
| mae:('ST-Transformer-lite', 3, 42) | True | metrics=0.9987882171582044, recomputed=0.9987882171582043 |
| rmse:('ST-Transformer-lite', 3, 42) | True | metrics=1.9089679742597876, recomputed=1.9089679742597874 |
| test_n:('HA', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('HA', 3, 2024) | True | metrics=1.7670076734430764, recomputed=1.7670076734430764 |
| rmse:('HA', 3, 2024) | True | metrics=3.221253620625528, recomputed=3.2212536206255273 |
| test_n:('SeasonalHA', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('SeasonalHA', 3, 2024) | True | metrics=1.015958182557622, recomputed=1.015958182557622 |
| rmse:('SeasonalHA', 3, 2024) | True | metrics=1.943902548137346, recomputed=1.943902548137346 |
| test_n:('Persistence', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('Persistence', 3, 2024) | True | metrics=1.310700671402648, recomputed=1.3107006714026481 |
| rmse:('Persistence', 3, 2024) | True | metrics=3.2709789138092544, recomputed=3.2709789138092544 |
| test_n:('XGBoost', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('XGBoost', 3, 2024) | True | metrics=0.8725682599192457, recomputed=0.8725682599192457 |
| rmse:('XGBoost', 3, 2024) | True | metrics=1.6560855864258712, recomputed=1.6560855864258712 |
| test_n:('GRU', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('GRU', 3, 2024) | True | metrics=1.0074605787617326, recomputed=1.0074605787617326 |
| rmse:('GRU', 3, 2024) | True | metrics=1.7862341298931863, recomputed=1.7862341298931863 |
| test_n:('TCN', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('TCN', 3, 2024) | True | metrics=0.9782033187408884, recomputed=0.9782033187408884 |
| rmse:('TCN', 3, 2024) | True | metrics=1.7975557706969278, recomputed=1.7975557706969278 |
| test_n:('ST-Transformer-lite', 3, 2024) | True | metrics=11878, parquet=11878 |
| mae:('ST-Transformer-lite', 3, 2024) | True | metrics=1.0312760931651868, recomputed=1.0312760931651868 |
| rmse:('ST-Transformer-lite', 3, 2024) | True | metrics=1.8740137401174344, recomputed=1.8740137401174344 |
| test_n:('HA', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('HA', 3, 2025) | True | metrics=1.7670076734430764, recomputed=1.7670076734430764 |
| rmse:('HA', 3, 2025) | True | metrics=3.221253620625528, recomputed=3.2212536206255273 |
| test_n:('SeasonalHA', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('SeasonalHA', 3, 2025) | True | metrics=1.015958182557622, recomputed=1.015958182557622 |
| rmse:('SeasonalHA', 3, 2025) | True | metrics=1.943902548137346, recomputed=1.943902548137346 |
| test_n:('Persistence', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('Persistence', 3, 2025) | True | metrics=1.310700671402648, recomputed=1.3107006714026481 |
| rmse:('Persistence', 3, 2025) | True | metrics=3.2709789138092544, recomputed=3.2709789138092544 |
| test_n:('XGBoost', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('XGBoost', 3, 2025) | True | metrics=0.8654067557675807, recomputed=0.8654067557675807 |
| rmse:('XGBoost', 3, 2025) | True | metrics=1.651715349857346, recomputed=1.651715349857346 |
| test_n:('GRU', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('GRU', 3, 2025) | True | metrics=1.0060004685378312, recomputed=1.0060004685378312 |
| rmse:('GRU', 3, 2025) | True | metrics=1.824149725606107, recomputed=1.824149725606107 |
| test_n:('TCN', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('TCN', 3, 2025) | True | metrics=0.9752991474483688, recomputed=0.9752991474483688 |
| rmse:('TCN', 3, 2025) | True | metrics=1.814527271239447, recomputed=1.814527271239447 |
| test_n:('ST-Transformer-lite', 3, 2025) | True | metrics=11878, parquet=11878 |
| mae:('ST-Transformer-lite', 3, 2025) | True | metrics=1.0004095508506712, recomputed=1.0004095508506712 |
| rmse:('ST-Transformer-lite', 3, 2025) | True | metrics=1.835210759805292, recomputed=1.8352107598052922 |
| test_n:('HA', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('HA', 3, 2026) | True | metrics=1.7670076734430764, recomputed=1.7670076734430764 |
| rmse:('HA', 3, 2026) | True | metrics=3.221253620625528, recomputed=3.2212536206255273 |
| test_n:('SeasonalHA', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('SeasonalHA', 3, 2026) | True | metrics=1.015958182557622, recomputed=1.015958182557622 |
| rmse:('SeasonalHA', 3, 2026) | True | metrics=1.943902548137346, recomputed=1.943902548137346 |
| test_n:('Persistence', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('Persistence', 3, 2026) | True | metrics=1.310700671402648, recomputed=1.3107006714026481 |
| rmse:('Persistence', 3, 2026) | True | metrics=3.2709789138092544, recomputed=3.2709789138092544 |
| test_n:('XGBoost', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('XGBoost', 3, 2026) | True | metrics=0.8774718724430801, recomputed=0.8774718724430801 |
| rmse:('XGBoost', 3, 2026) | True | metrics=1.66227703484509, recomputed=1.66227703484509 |
| test_n:('GRU', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('GRU', 3, 2026) | True | metrics=1.0681743873934049, recomputed=1.0681743873934049 |
| rmse:('GRU', 3, 2026) | True | metrics=1.9146789766254164, recomputed=1.9146789766254164 |
| test_n:('TCN', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('TCN', 3, 2026) | True | metrics=1.0721781453333192, recomputed=1.0721781453333192 |
| rmse:('TCN', 3, 2026) | True | metrics=1.8397670000835091, recomputed=1.8397670000835094 |
| test_n:('ST-Transformer-lite', 3, 2026) | True | metrics=11878, parquet=11878 |
| mae:('ST-Transformer-lite', 3, 2026) | True | metrics=0.9530041913509288, recomputed=0.9530041913509288 |
| rmse:('ST-Transformer-lite', 3, 2026) | True | metrics=1.825860432244613, recomputed=1.825860432244613 |
| test_n:('HA', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('HA', 3, 3407) | True | metrics=1.7670076734430764, recomputed=1.7670076734430764 |
| rmse:('HA', 3, 3407) | True | metrics=3.221253620625528, recomputed=3.2212536206255273 |
| test_n:('SeasonalHA', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('SeasonalHA', 3, 3407) | True | metrics=1.015958182557622, recomputed=1.015958182557622 |
| rmse:('SeasonalHA', 3, 3407) | True | metrics=1.943902548137346, recomputed=1.943902548137346 |
| test_n:('Persistence', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('Persistence', 3, 3407) | True | metrics=1.310700671402648, recomputed=1.3107006714026481 |
| rmse:('Persistence', 3, 3407) | True | metrics=3.2709789138092544, recomputed=3.2709789138092544 |
| test_n:('XGBoost', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('XGBoost', 3, 3407) | True | metrics=0.8638691671730834, recomputed=0.8638691671730834 |
| rmse:('XGBoost', 3, 3407) | True | metrics=1.6527685195222583, recomputed=1.6527685195222583 |
| test_n:('GRU', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('GRU', 3, 3407) | True | metrics=1.0338017365249603, recomputed=1.0338017365249605 |
| rmse:('GRU', 3, 3407) | True | metrics=1.803775393596504, recomputed=1.8037753935965037 |
| test_n:('TCN', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('TCN', 3, 3407) | True | metrics=1.0087301718664805, recomputed=1.0087301718664803 |
| rmse:('TCN', 3, 3407) | True | metrics=1.801372838019881, recomputed=1.801372838019881 |
| test_n:('ST-Transformer-lite', 3, 3407) | True | metrics=11878, parquet=11878 |
| mae:('ST-Transformer-lite', 3, 3407) | True | metrics=0.9400040219781134, recomputed=0.9400040219781134 |
| rmse:('ST-Transformer-lite', 3, 3407) | True | metrics=1.7767922236294489, recomputed=1.7767922236294487 |
| test_n:('HA', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('HA', 6, 42) | True | metrics=1.555868891613001, recomputed=1.555868891613001 |
| rmse:('HA', 6, 42) | True | metrics=2.78390590069934, recomputed=2.78390590069934 |
| test_n:('SeasonalHA', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('SeasonalHA', 6, 42) | True | metrics=0.9103676185940276, recomputed=0.9103676185940277 |
| rmse:('SeasonalHA', 6, 42) | True | metrics=1.5415282255127518, recomputed=1.5415282255127518 |
| test_n:('Persistence', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('Persistence', 6, 42) | True | metrics=1.6025600083736964, recomputed=1.6025600083736964 |
| rmse:('Persistence', 6, 42) | True | metrics=3.6998692720239874, recomputed=3.6998692720239874 |
| test_n:('XGBoost', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('XGBoost', 6, 42) | True | metrics=0.7833349846233648, recomputed=0.7833349846233648 |
| rmse:('XGBoost', 6, 42) | True | metrics=1.3482397623353466, recomputed=1.3482397623353466 |
| test_n:('GRU', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('GRU', 6, 42) | True | metrics=1.036771294240906, recomputed=1.036771294240906 |
| rmse:('GRU', 6, 42) | True | metrics=1.6349907896546962, recomputed=1.6349907896546962 |
| test_n:('TCN', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('TCN', 6, 42) | True | metrics=0.9193061027169404, recomputed=0.9193061027169404 |
| rmse:('TCN', 6, 42) | True | metrics=1.5223382176872675, recomputed=1.5223382176872675 |
| test_n:('ST-Transformer-lite', 6, 42) | True | metrics=12166, parquet=12166 |
| mae:('ST-Transformer-lite', 6, 42) | True | metrics=0.8868063855049702, recomputed=0.8868063855049702 |
| rmse:('ST-Transformer-lite', 6, 42) | True | metrics=1.5564880749260253, recomputed=1.5564880749260253 |
| test_n:('HA', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('HA', 6, 2024) | True | metrics=1.555868891613001, recomputed=1.555868891613001 |
| rmse:('HA', 6, 2024) | True | metrics=2.78390590069934, recomputed=2.78390590069934 |
| test_n:('SeasonalHA', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('SeasonalHA', 6, 2024) | True | metrics=0.9103676185940276, recomputed=0.9103676185940277 |
| rmse:('SeasonalHA', 6, 2024) | True | metrics=1.5415282255127518, recomputed=1.5415282255127518 |
| test_n:('Persistence', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('Persistence', 6, 2024) | True | metrics=1.6025600083736964, recomputed=1.6025600083736964 |
| rmse:('Persistence', 6, 2024) | True | metrics=3.6998692720239874, recomputed=3.6998692720239874 |
| test_n:('XGBoost', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('XGBoost', 6, 2024) | True | metrics=0.7843854444191171, recomputed=0.7843854444191171 |
| rmse:('XGBoost', 6, 2024) | True | metrics=1.3487850646684223, recomputed=1.3487850646684223 |
| test_n:('GRU', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('GRU', 6, 2024) | True | metrics=0.9505013424021896, recomputed=0.9505013424021896 |
| rmse:('GRU', 6, 2024) | True | metrics=1.537150595246842, recomputed=1.537150595246842 |
| test_n:('TCN', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('TCN', 6, 2024) | True | metrics=0.9421427672030442, recomputed=0.9421427672030442 |
| rmse:('TCN', 6, 2024) | True | metrics=1.519236551604223, recomputed=1.519236551604223 |
| test_n:('ST-Transformer-lite', 6, 2024) | True | metrics=12166, parquet=12166 |
| mae:('ST-Transformer-lite', 6, 2024) | True | metrics=0.8900082970888388, recomputed=0.8900082970888388 |
| rmse:('ST-Transformer-lite', 6, 2024) | True | metrics=1.5310866590641574, recomputed=1.5310866590641574 |
| test_n:('HA', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('HA', 6, 2025) | True | metrics=1.555868891613001, recomputed=1.555868891613001 |
| rmse:('HA', 6, 2025) | True | metrics=2.78390590069934, recomputed=2.78390590069934 |
| test_n:('SeasonalHA', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('SeasonalHA', 6, 2025) | True | metrics=0.9103676185940276, recomputed=0.9103676185940277 |
| rmse:('SeasonalHA', 6, 2025) | True | metrics=1.5415282255127518, recomputed=1.5415282255127518 |
| test_n:('Persistence', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('Persistence', 6, 2025) | True | metrics=1.6025600083736964, recomputed=1.6025600083736964 |
| rmse:('Persistence', 6, 2025) | True | metrics=3.6998692720239874, recomputed=3.6998692720239874 |
| test_n:('XGBoost', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('XGBoost', 6, 2025) | True | metrics=0.7888537169717829, recomputed=0.7888537169717829 |
| rmse:('XGBoost', 6, 2025) | True | metrics=1.3528689250057413, recomputed=1.3528689250057413 |
| test_n:('GRU', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('GRU', 6, 2025) | True | metrics=0.902780271019372, recomputed=0.902780271019372 |
| rmse:('GRU', 6, 2025) | True | metrics=1.4639736841659376, recomputed=1.4639736841659376 |
| test_n:('TCN', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('TCN', 6, 2025) | True | metrics=0.9584343797494644, recomputed=0.9584343797494643 |
| rmse:('TCN', 6, 2025) | True | metrics=1.5635670485159194, recomputed=1.5635670485159194 |
| test_n:('ST-Transformer-lite', 6, 2025) | True | metrics=12166, parquet=12166 |
| mae:('ST-Transformer-lite', 6, 2025) | True | metrics=0.8797634142941988, recomputed=0.8797634142941988 |
| rmse:('ST-Transformer-lite', 6, 2025) | True | metrics=1.4890291208327708, recomputed=1.4890291208327708 |
| test_n:('HA', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('HA', 6, 2026) | True | metrics=1.555868891613001, recomputed=1.555868891613001 |
| rmse:('HA', 6, 2026) | True | metrics=2.78390590069934, recomputed=2.78390590069934 |
| test_n:('SeasonalHA', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('SeasonalHA', 6, 2026) | True | metrics=0.9103676185940276, recomputed=0.9103676185940277 |
| rmse:('SeasonalHA', 6, 2026) | True | metrics=1.5415282255127518, recomputed=1.5415282255127518 |
| test_n:('Persistence', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('Persistence', 6, 2026) | True | metrics=1.6025600083736964, recomputed=1.6025600083736964 |
| rmse:('Persistence', 6, 2026) | True | metrics=3.6998692720239874, recomputed=3.6998692720239874 |
| test_n:('XGBoost', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('XGBoost', 6, 2026) | True | metrics=0.7870403119221577, recomputed=0.7870403119221577 |
| rmse:('XGBoost', 6, 2026) | True | metrics=1.3547759569338145, recomputed=1.3547759569338143 |
| test_n:('GRU', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('GRU', 6, 2026) | True | metrics=0.9282782982784372, recomputed=0.9282782982784373 |
| rmse:('GRU', 6, 2026) | True | metrics=1.558650568054961, recomputed=1.558650568054961 |
| test_n:('TCN', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('TCN', 6, 2026) | True | metrics=0.9204931759273812, recomputed=0.9204931759273812 |
| rmse:('TCN', 6, 2026) | True | metrics=1.4977414957878707, recomputed=1.4977414957878707 |
| test_n:('ST-Transformer-lite', 6, 2026) | True | metrics=12166, parquet=12166 |
| mae:('ST-Transformer-lite', 6, 2026) | True | metrics=0.918715313784919, recomputed=0.918715313784919 |
| rmse:('ST-Transformer-lite', 6, 2026) | True | metrics=1.6326448907126054, recomputed=1.6326448907126054 |
| test_n:('HA', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('HA', 6, 3407) | True | metrics=1.555868891613001, recomputed=1.555868891613001 |
| rmse:('HA', 6, 3407) | True | metrics=2.78390590069934, recomputed=2.78390590069934 |
| test_n:('SeasonalHA', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('SeasonalHA', 6, 3407) | True | metrics=0.9103676185940276, recomputed=0.9103676185940277 |
| rmse:('SeasonalHA', 6, 3407) | True | metrics=1.5415282255127518, recomputed=1.5415282255127518 |
| test_n:('Persistence', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('Persistence', 6, 3407) | True | metrics=1.6025600083736964, recomputed=1.6025600083736964 |
| rmse:('Persistence', 6, 3407) | True | metrics=3.6998692720239874, recomputed=3.6998692720239874 |
| test_n:('XGBoost', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('XGBoost', 6, 3407) | True | metrics=0.7897973072366183, recomputed=0.7897973072366183 |
| rmse:('XGBoost', 6, 3407) | True | metrics=1.348066913123569, recomputed=1.348066913123569 |
| test_n:('GRU', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('GRU', 6, 3407) | True | metrics=0.9442457480981674, recomputed=0.9442457480981674 |
| rmse:('GRU', 6, 3407) | True | metrics=1.4859898647246328, recomputed=1.4859898647246328 |
| test_n:('TCN', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('TCN', 6, 3407) | True | metrics=0.9484445172745244, recomputed=0.9484445172745245 |
| rmse:('TCN', 6, 3407) | True | metrics=1.5278579922060087, recomputed=1.5278579922060087 |
| test_n:('ST-Transformer-lite', 6, 3407) | True | metrics=12166, parquet=12166 |
| mae:('ST-Transformer-lite', 6, 3407) | True | metrics=0.9311357774409968, recomputed=0.9311357774409968 |
| rmse:('ST-Transformer-lite', 6, 3407) | True | metrics=1.770834587062946, recomputed=1.770834587062946 |
