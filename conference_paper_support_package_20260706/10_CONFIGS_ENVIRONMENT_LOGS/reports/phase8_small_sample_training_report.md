# Phase 8 Small-Sample Training Report

## Purpose
This experiment measures TCN speed-only robustness when the chronological training period is reduced while validation and test periods remain unchanged.

## Data Split Design
- Chronological train/validation/test split is read from the existing Phase 2 window index.
- For each training ratio, only the earliest share of original train-period target timestamps is retained.
- Validation and test windows are unchanged across all ratios and seeds.

## Leakage Control
- Raw data are not modified.
- Selected training windows are defined before sample tensors are built.
- Feature and target scalers are fitted only on the selected training samples.
- Validation and test tensors are transformed using the selected-training scaler.

## Design
- Training ratios: [0.2, 0.4, 0.6, 0.8, 1.0]
- Horizons: [1, 3, 6]
- Seeds: [1, 2, 3, 4, 5]
- History length: 168h

## Output Files
| file | exists_now | rows |
| --- | --- | --- |
| outputs/tables/phase8_small_sample_metrics.csv | True | 75 |
| outputs/plot_data/Fig07_small_sample_training_data.csv | False | 0 |

## Metric Summary
| horizon_hours | train_ratio | seed_count | n_train_windows_mean | mae_mean | mae_std |
| --- | --- | --- | --- | --- | --- |
| 1.0 | 0.2 | 5.0 | 12431.0 | 1.0431741849708793 | 0.05614962598637944 |
| 1.0 | 0.4 | 5.0 | 24756.0 | 1.0383416347527181 | 0.02020534664317277 |
| 1.0 | 0.6 | 5.0 | 37036.0 | 0.9625596974251744 | 0.024266844809814975 |
| 1.0 | 0.8 | 5.0 | 49141.0 | 1.0000236083194154 | 0.07524241492861639 |
| 1.0 | 1.0 | 5.0 | 61291.0 | 0.9800523406333312 | 0.07601392441315646 |
| 3.0 | 0.2 | 5.0 | 12405.0 | 1.0125757589690736 | 0.03691719947513745 |
| 3.0 | 0.4 | 5.0 | 24450.0 | 1.0849979554141278 | 0.0968833822554246 |
| 3.0 | 0.6 | 5.0 | 36509.0 | 1.0208494347160155 | 0.03079260400108929 |
| 3.0 | 0.8 | 5.0 | 47924.0 | 0.9509362960496329 | 0.06476049830293867 |
| 3.0 | 1.0 | 5.0 | 59597.0 | 0.9570834672345256 | 0.07888375086312586 |
| 6.0 | 0.2 | 5.0 | 12393.0 | 0.9546915445084853 | 0.04793188099490413 |
| 6.0 | 0.4 | 5.0 | 24742.0 | 0.9635869672377263 | 0.05804977580836814 |
| 6.0 | 0.6 | 5.0 | 37069.0 | 0.9372605353815423 | 0.07869077057621744 |
| 6.0 | 0.8 | 5.0 | 49304.0 | 0.9846644949071903 | 0.05901884335877596 |
| 6.0 | 1.0 | 5.0 | 61570.0 | 0.8628667427380426 | 0.022016536854425867 |

## Warnings
| warning |
| --- |
| none |

## Manuscript Interpretation Template
Small-sample sensitivity can be reported as the percentage MAE degradation of the 20% chronological-training model relative to the full-training model for the same forecast horizon. Stable degradation across seeds supports robustness under limited labelled history; sharp degradation identifies horizons that require longer training coverage.
