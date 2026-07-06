# Phase 9 Repeated-Seed Stability Report

Phase 9 repeats the core TCN speed-only configurations across three random seeds. It is descriptive stability testing only.

## Seed-Level Metrics
| model | input_feature_group | seed | history_hours | horizon_hours | split | best_epoch | best_val_MAE | n | MAE | RMSE | sMAPE | checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 42 | 72 | 1 | test | 5 | 0.8631505504759944 | 10327 | 0.921559664498251 | 2.464457546289207 | 0.0126432475322459 | outputs\checkpoints\phase9_tcn_speed_only_seed42_h72_y1.pt |
| TCN | speed_only | 2025 | 72 | 1 | test | 2 | 1.0160466127700278 | 10327 | 1.0802470377411098 | 2.5360867013366653 | 0.0148924630454127 | outputs\checkpoints\phase9_tcn_speed_only_seed2025_h72_y1.pt |
| TCN | speed_only | 20260623 | 72 | 1 | test | 1 | 0.9713008370373644 | 10327 | 1.0278608152777942 | 2.5178863983365125 | 0.0140077295928857 | outputs\checkpoints\phase9_tcn_speed_only_seed20260623_h72_y1.pt |
| TCN | speed_only | 42 | 168 | 3 | test | 5 | 1.1505704057388184 | 6312 | 1.0112939950631146 | 1.775941227951191 | 0.0132922870570154 | outputs\checkpoints\phase9_tcn_speed_only_seed42_h168_y3.pt |
| TCN | speed_only | 2025 | 168 | 3 | test | 3 | 1.079685228123803 | 6312 | 0.89997770819525 | 1.776589387439982 | 0.0123645373714377 | outputs\checkpoints\phase9_tcn_speed_only_seed2025_h168_y3.pt |
| TCN | speed_only | 20260623 | 168 | 3 | test | 3 | 1.119267727134706 | 6312 | 0.9861519472680618 | 1.7737138950899949 | 0.0131454297236588 | outputs\checkpoints\phase9_tcn_speed_only_seed20260623_h168_y3.pt |
| TCN | speed_only | 42 | 24 | 6 | test | 14 | 0.810630122779781 | 12166 | 0.899449512281642 | 1.512936940484077 | 0.0122290218353395 | outputs\checkpoints\phase9_tcn_speed_only_seed42_h24_y6.pt |
| TCN | speed_only | 2025 | 24 | 6 | test | 2 | 0.8156948555840386 | 12166 | 0.8621743500242495 | 1.569319419715213 | 0.0117267727491512 | outputs\checkpoints\phase9_tcn_speed_only_seed2025_h24_y6.pt |
| TCN | speed_only | 20260623 | 24 | 6 | test | 12 | 0.7407632941873664 | 12166 | 0.8173141542202976 | 1.468999128745931 | 0.0110275039223168 | outputs\checkpoints\phase9_tcn_speed_only_seed20260623_h24_y6.pt |

## Summary By Horizon
| horizon_hours | history_hours | seed_count | MAE_mean | MAE_std | MAE_min | MAE_max | MAE_cv | best_seed | worst_seed | SeasonalHistoricalAverage_MAE | all_seeds_outperform_seasonal | mean_improvement_percent_vs_seasonal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 72 | 3 | 1.0098891725057182 | 0.0808557701380978 | 0.921559664498251 | 1.0802470377411098 | 0.0800640033970064 | 42 | 2025 | 1.178897282310066 | True | 14.336118365899864 |
| 3 | 168 | 3 | 0.9658078835088088 | 0.0583801304228809 | 0.89997770819525 | 1.0112939950631146 | 0.0604469392098811 | 2025 | 42 | 1.0540818485088488 | True | 8.374488672290134 |
| 6 | 24 | 3 | 0.8596460055087297 | 0.0411260094764637 | 0.8173141542202976 | 0.899449512281642 | 0.0478406334850887 | 20260623 | 42 | 0.9519557742157024 | True | 9.69685474968886 |

## Versus Seasonal Historical Average
| model | input_feature_group | seed | history_hours | horizon_hours | split | best_epoch | best_val_MAE | n | MAE | RMSE | sMAPE | checkpoint | SeasonalHistoricalAverage_MAE | SeasonalHistoricalAverage_RMSE | SeasonalHistoricalAverage_sMAPE | delta_MAE_vs_seasonal | improvement_percent_vs_seasonal | outperforms_seasonal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 42 | 72 | 1 | test | 5 | 0.8631505504759944 | 10327 | 0.921559664498251 | 2.464457546289207 | 0.0126432475322459 | outputs\checkpoints\phase9_tcn_speed_only_seed42_h72_y1.pt | 1.178897282310066 | 2.733031629503305 | 0.0162567476422331 | 0.2573376178118151 | 21.82867173190512 | True |
| TCN | speed_only | 2025 | 72 | 1 | test | 2 | 1.0160466127700278 | 10327 | 1.0802470377411098 | 2.5360867013366653 | 0.0148924630454127 | outputs\checkpoints\phase9_tcn_speed_only_seed2025_h72_y1.pt | 1.178897282310066 | 2.733031629503305 | 0.0162567476422331 | 0.0986502445689563 | 8.368010177752701 | True |
| TCN | speed_only | 20260623 | 72 | 1 | test | 1 | 0.9713008370373644 | 10327 | 1.0278608152777942 | 2.5178863983365125 | 0.0140077295928857 | outputs\checkpoints\phase9_tcn_speed_only_seed20260623_h72_y1.pt | 1.178897282310066 | 2.733031629503305 | 0.0162567476422331 | 0.1510364670322719 | 12.811673188041777 | True |
| TCN | speed_only | 42 | 168 | 3 | test | 5 | 1.1505704057388184 | 6312 | 1.0112939950631146 | 1.775941227951191 | 0.0132922870570154 | outputs\checkpoints\phase9_tcn_speed_only_seed42_h168_y3.pt | 1.0540818485088488 | 2.0065083242358743 | 0.0142471720276558 | 0.0427878534457342 | 4.059253416256415 | True |
| TCN | speed_only | 2025 | 168 | 3 | test | 3 | 1.079685228123803 | 6312 | 0.89997770819525 | 1.776589387439982 | 0.0123645373714377 | outputs\checkpoints\phase9_tcn_speed_only_seed2025_h168_y3.pt | 1.0540818485088488 | 2.0065083242358743 | 0.0142471720276558 | 0.1541041403135987 | 14.619750879080344 | True |
| TCN | speed_only | 20260623 | 168 | 3 | test | 3 | 1.119267727134706 | 6312 | 0.9861519472680618 | 1.7737138950899949 | 0.0131454297236588 | outputs\checkpoints\phase9_tcn_speed_only_seed20260623_h168_y3.pt | 1.0540818485088488 | 2.0065083242358743 | 0.0142471720276558 | 0.067929901240787 | 6.444461721533644 | True |
| TCN | speed_only | 42 | 24 | 6 | test | 14 | 0.810630122779781 | 12166 | 0.899449512281642 | 1.512936940484077 | 0.0122290218353395 | outputs\checkpoints\phase9_tcn_speed_only_seed42_h24_y6.pt | 0.9519557742157024 | 1.6018649170103407 | 0.0127049756404673 | 0.0525062619340603 | 5.515619880274297 | True |
| TCN | speed_only | 2025 | 24 | 6 | test | 2 | 0.8156948555840386 | 12166 | 0.8621743500242495 | 1.569319419715213 | 0.0117267727491512 | outputs\checkpoints\phase9_tcn_speed_only_seed2025_h24_y6.pt | 0.9519557742157024 | 1.6018649170103407 | 0.0127049756404673 | 0.0897814241914529 | 9.43126000421838 | True |
| TCN | speed_only | 20260623 | 24 | 6 | test | 12 | 0.7407632941873664 | 12166 | 0.8173141542202976 | 1.468999128745931 | 0.0110275039223168 | outputs\checkpoints\phase9_tcn_speed_only_seed20260623_h24_y6.pt | 0.9519557742157024 | 1.6018649170103407 | 0.0127049756404673 | 0.1346416199954048 | 14.143684364573907 | True |

No statistical significance test is reported because per-sample baseline predictions are not available.
