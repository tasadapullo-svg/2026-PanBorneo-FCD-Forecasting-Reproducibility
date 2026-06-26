# Phase 2 Window Construction Report

## Scope
Phase 2 constructed leakage-free sliding-window indices only. No model training was run.

## Target Variables
| target_variable | source_column | available | non_missing_count | missing_rate | mean | std | min | max | recommended_main_target |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| speed | current_speed | True | 97094 | 0.0384828678946326 | 88.84711173364643 | 16.27039158901787 | 15.0 | 100.0 | True |
| travel_time | current_travel_time | True | 97094 | 0.0384828678946326 | 909.8166482995861 | 263.51647754551647 | 343.0 | 2155.0 | False |
| congestion_index | tti | True | 97094 | 0.0384828678946326 | 1.044511207278892 | 0.13686220917384131 | 1.0 | 3.742424242424242 | False |
| travel_time_delay | travel_time_delay | True | 97094 | 0.0384828678946326 | 34.82199964295768 | 89.37460933003545 | 0.0 | 940.0 | False |

Recommended main prediction target: `speed`. It is preferred because speed is directly available, interpretable, and has the same missing rate as the primary traffic fields.

## Chronological Split
- train: 2025-12-08 13:00:00 to 2026-02-04 06:00:00
- val: 2026-02-04 07:00:00 to 2026-02-16 15:00:00
- test: 2026-02-16 16:00:00 to 2026-03-01 00:00:00

The strict Phase 2 rule requires input and target timestamps to be fully contained inside the assigned split.

## Window Counts by History-Horizon
| history_hours | horizon_hours | is_main_forecast | is_extended_horizon | candidate_windows | valid_windows_min_80pct_observed |
| --- | --- | --- | --- | --- | --- |
| 24 | 1 | 1 | 0 | 389232 | 364204 |
| 24 | 3 | 1 | 0 | 388008 | 353048 |
| 24 | 6 | 1 | 0 | 386172 | 362320 |
| 24 | 12 | 1 | 0 | 382500 | 358856 |
| 24 | 24 | 1 | 0 | 375156 | 353692 |
| 72 | 1 | 1 | 0 | 359856 | 345984 |
| 72 | 3 | 1 | 0 | 358632 | 335412 |
| 72 | 6 | 1 | 0 | 356796 | 344004 |
| 72 | 12 | 1 | 0 | 353124 | 338608 |
| 72 | 24 | 1 | 0 | 345780 | 334248 |
| 168 | 1 | 1 | 0 | 301104 | 295556 |
| 168 | 3 | 1 | 0 | 299880 | 286152 |
| 168 | 6 | 1 | 0 | 298044 | 293924 |
| 168 | 12 | 1 | 0 | 294372 | 289316 |
| 168 | 24 | 1 | 0 | 287028 | 284844 |
| 168 | 168 | 0 | 1 | 214404 | 214404 |

## Window Counts by Split
| split | window_count |
| --- | --- |
| test | 614448 |
| train | 4161192 |
| val | 614448 |

## Horizon Feasibility
- Main horizons 1h, 3h, 6h, 12h, and 24h are feasible when judged by the 80% input/target observed-ratio rule: True.
- 168h is retained as extended stress-test only: True.
- Horizon/target combinations below 50% valid ratio: 0.
- Points excluded: none.
- Leakage failures detected: 0.
- Total rows in `window_index_all.csv`: 5,390,088.

## Leakage Controls
- `input_end_time < target_start_time` for every emitted window.
- Train, validation, and test samples are assigned only when both input and target stay within the same chronological split.
- Reliability fields such as coverage ratios and recent volatility are computed from the input window only.

## Phase 3 Recommendation
Run baseline models only: Persistence, Historical Average, and optionally ARIMA/Random Forest after verifying the baseline feature matrix. Use `speed` as the first target, then repeat for `travel_time` and `tti` if baseline logs are clean.
