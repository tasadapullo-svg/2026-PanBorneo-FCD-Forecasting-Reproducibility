# Phase 3 Baseline Report

Phase 3 ran baseline models for the main forecasting task only. No deep learning or benchmark experiments are included.

## Scope
- Target variable: `speed`
- Histories: [24, 72, 168]
- Horizons: [1, 3, 6, 12, 24]
- Excluded horizons: [168]
- Target aggregation: `mean` over the target window

## Target Definition Clarification
The Phase 3 prediction target is the mean speed over the future target window. It is not the terminal speed at the last horizon step. For example, the 24h horizon evaluates the average speed over the next 24 hourly steps, not the speed exactly 24 hours later.

Because the target is temporally averaged, longer horizons such as 24h can appear to have lower errors: averaging smooths short-term fluctuations and reduces high-frequency noise. This should not be interpreted as long-horizon point forecasting being easier. The main baseline experiment remains limited to 1h, 3h, 6h, 12h, and 24h horizons; the 168h horizon remains excluded from the main baseline experiment.

## Test Metrics
| model | split | n | MAE | RMSE | MAPE | sMAPE | R2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Persistence | test | 139795 | 1.572627496358871 | 3.6651199463714135 | 0.0229764821368752 | 0.0230128737932241 | 0.9462864742712348 |
| HistoricalAverage | test | 139795 | 1.4072502734039187 | 2.742222318861239 | 0.0205131451349468 | 0.0204119047661666 | 0.9699314421887776 |
| SeasonalHistoricalAverage | test | 139795 | 0.9346006145900384 | 1.84139726079369 | 0.0125457389224895 | 0.0125603592912129 | 0.9864417929607946 |
| RidgeRegression | test | 139795 | 1.2860652424501615 | 2.399725874416052 | 0.0182740978024508 | 0.0181551843930258 | 0.9769733614263154 |

## Runtime Summary
| stage | seconds | rows |
| --- | --- | --- |
| load_panel_and_fit_average_tables | 0.225 | nan |
| build_feature_matrix | 180.023 | 1235042.0 |
| ridge_regression | 3.503 | 1235042.0 |
| write_metrics | 3.981 | 1235042.0 |

## Leakage Controls
- Phase 3 consumes Phase 2 windows where `is_main_forecast=1` and `is_extended_horizon=0`.
- Features are computed only from `input_start_time` through `input_end_time`.
- Historical and seasonal averages are fitted from the chronological train panel only.
- Labels are computed from the target window only for metric evaluation.
