# Phase 7 History-Length Sensitivity Report

Phase 7 tests whether longer speed-only input histories improve TCN forecasting performance.

## Scope
- Target: future-window mean speed
- Feature group: speed_only
- Model: TCN only
- Histories: 24h, 72h, 168h
- Horizons: 1h, 3h, 6h only
- Feature and target scaling are fitted on the train split only.

## Metrics By History
| model | input_feature_group | history_hours | split | n | MAE | RMSE | sMAPE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 24 | test | 3 | 0.9429989654534396 | 2.0204296781030893 | 0.0130904576327093 |
| TCN | speed_only | 24 | val | 23 | 1.010582385255487 | 1.9761107493165284 | 0.0137473041787224 |
| TCN | speed_only | 72 | test | 3 | 0.9276232851274558 | 1.976045811367818 | 0.0126025105555313 |
| TCN | speed_only | 72 | val | 22 | 1.051098099576068 | 2.179967271572788 | 0.0145664322448085 |
| TCN | speed_only | 168 | test | 3 | 0.9240849008713956 | 1.8738464331596705 | 0.0127013913024887 |
| TCN | speed_only | 168 | val | 27 | 1.3253284438478634 | 2.5811911499218847 | 0.0178727719041913 |

## Metrics By Horizon
| model | input_feature_group | history_hours | horizon_hours | split | n | best_epoch | MAE | RMSE | sMAPE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 24 | 1 | test | 1 | 3 | 0.9832630992567496 | 2.522738497384306 | 0.0134893221437661 |
| TCN | speed_only | 24 | 1 | val | 7 | 3 | 1.1090467406261086 | 2.5655883303620093 | 0.0150651732307146 |
| TCN | speed_only | 24 | 3 | test | 1 | 1 | 1.032555193627276 | 2.002799346189581 | 0.0143279136057772 |
| TCN | speed_only | 24 | 3 | val | 5 | 1 | 1.0660695596436325 | 1.9117987522370337 | 0.0145124312268658 |
| TCN | speed_only | 24 | 6 | test | 1 | 7 | 0.8131786034762928 | 1.5357511907353814 | 0.0114541371485847 |
| TCN | speed_only | 24 | 6 | val | 11 | 7 | 0.7601028572799813 | 1.474502440167092 | 0.010557781708615 |
| TCN | speed_only | 72 | 1 | test | 1 | 4 | 0.917775044866484 | 2.4874600530074025 | 0.0127312215165924 |
| TCN | speed_only | 72 | 1 | val | 8 | 4 | 1.1460046905369352 | 2.6531675018413616 | 0.0154682317200105 |
| TCN | speed_only | 72 | 3 | test | 1 | 3 | 0.9295604460620738 | 1.8950580157266264 | 0.0126923632422575 |
| TCN | speed_only | 72 | 3 | val | 7 | 3 | 1.073898028236666 | 1.9064554443314647 | 0.0143337951499993 |
| TCN | speed_only | 72 | 6 | test | 1 | 3 | 0.9355343644538096 | 1.5456193653694252 | 0.0123839469077441 |
| TCN | speed_only | 72 | 6 | val | 7 | 3 | 1.0843369443555504 | 1.6242559757078054 | 0.0142683669519425 |
| TCN | speed_only | 168 | 1 | test | 1 | 5 | 0.9926097419494178 | 2.343961904731657 | 0.0136274177989545 |
| TCN | speed_only | 168 | 1 | val | 9 | 5 | 1.4115326314823131 | 3.314847685807386 | 0.0191294991591899 |
| TCN | speed_only | 168 | 3 | test | 1 | 4 | 0.9244928154504194 | 1.775107011405854 | 0.0126309471657841 |
| TCN | speed_only | 168 | 3 | val | 8 | 4 | 1.3457771615716063 | 2.302573893036277 | 0.0174159481411565 |
| TCN | speed_only | 168 | 6 | test | 1 | 6 | 0.8551521452143493 | 1.5024703833414996 | 0.0118458089427276 |
| TCN | speed_only | 168 | 6 | val | 10 | 6 | 1.1626353569235486 | 1.9355667331356945 | 0.0152410473421516 |

## Best History By Horizon
| model | input_feature_group | history_hours | horizon_hours | split | n | best_epoch | MAE | RMSE | sMAPE | is_best_history_for_horizon |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 72 | 1 | test | 1 | 4 | 0.917775044866484 | 2.4874600530074025 | 0.0127312215165924 | True |
| TCN | speed_only | 168 | 3 | test | 1 | 4 | 0.9244928154504194 | 1.775107011405854 | 0.0126309471657841 | True |
| TCN | speed_only | 24 | 6 | test | 1 | 7 | 0.8131786034762928 | 1.5357511907353814 | 0.0114541371485847 | True |

## Versus Seasonal Historical Average
| model | input_feature_group | history_hours | horizon_hours | split | n | best_epoch | MAE | RMSE | sMAPE | SeasonalHistoricalAverage_MAE | SeasonalHistoricalAverage_RMSE | SeasonalHistoricalAverage_sMAPE | delta_MAE_vs_seasonal | improvement_percent_vs_seasonal | is_best_history_for_horizon |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 24 | 1 | test | 1 | 3 | 0.9832630992567496 | 2.522738497384306 | 0.0134893221437661 | 1.178897282310066 | 2.733031629503305 | 0.0162567476422331 | 0.1956341830533164 | 16.59467588812899 | False |
| TCN | speed_only | 24 | 3 | test | 1 | 1 | 1.032555193627276 | 2.002799346189581 | 0.0143279136057772 | 1.0540818485088488 | 2.0065083242358743 | 0.0142471720276558 | 0.0215266548815726 | 2.042218534739522 | False |
| TCN | speed_only | 24 | 6 | test | 1 | 7 | 0.8131786034762928 | 1.5357511907353814 | 0.0114541371485847 | 0.9519557742157024 | 1.6018649170103407 | 0.0127049756404673 | 0.1387771707394096 | 14.578111136911314 | True |
| TCN | speed_only | 72 | 1 | test | 1 | 4 | 0.917775044866484 | 2.4874600530074025 | 0.0127312215165924 | 1.178897282310066 | 2.733031629503305 | 0.0162567476422331 | 0.261122237443582 | 22.149702214251374 | True |
| TCN | speed_only | 72 | 3 | test | 1 | 3 | 0.9295604460620738 | 1.8950580157266264 | 0.0126923632422575 | 1.0540818485088488 | 2.0065083242358743 | 0.0142471720276558 | 0.124521402446775 | 11.813257445133749 | False |
| TCN | speed_only | 72 | 6 | test | 1 | 3 | 0.9355343644538096 | 1.5456193653694252 | 0.0123839469077441 | 0.9519557742157024 | 1.6018649170103407 | 0.0127049756404673 | 0.0164214097618927 | 1.7250181370476 | False |
| TCN | speed_only | 168 | 1 | test | 1 | 5 | 0.9926097419494178 | 2.343961904731657 | 0.0136274177989545 | 1.178897282310066 | 2.733031629503305 | 0.0162567476422331 | 0.1862875403606483 | 15.801846620225914 | False |
| TCN | speed_only | 168 | 3 | test | 1 | 4 | 0.9244928154504194 | 1.775107011405854 | 0.0126309471657841 | 1.0540818485088488 | 2.0065083242358743 | 0.0142471720276558 | 0.1295890330584294 | 12.294019979734196 | True |
| TCN | speed_only | 168 | 6 | test | 1 | 6 | 0.8551521452143493 | 1.5024703833414996 | 0.0118458089427276 | 0.9519557742157024 | 1.6018649170103407 | 0.0127049756404673 | 0.096803629001353 | 10.168920828397484 | False |

## Runtime
| model | input_feature_group | history_hours | horizon_hours | device | train_samples | val_samples | test_samples | best_epoch | best_val_MAE | seconds | checkpoint | scaler_metadata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCN | speed_only | 24 | 1 | cuda | 66585 | 12201 | 12265 | 3 | 0.8757360152128963 | 695.750334700002 | outputs\checkpoints\phase7_tcn_speed_only_h24_y1.pt | outputs\checkpoints\phase7_tcn_speed_only_h24_y1_scaler.json |
| TCN | speed_only | 24 | 3 | cuda | 64783 | 11601 | 11878 | 1 | 0.9585152977797996 | 493.9539744000067 | outputs\checkpoints\phase7_tcn_speed_only_h24_y3.pt | outputs\checkpoints\phase7_tcn_speed_only_h24_y3_scaler.json |
| TCN | speed_only | 24 | 6 | cuda | 66714 | 11700 | 12166 | 7 | 0.7514632709209735 | 1118.0725511000055 | outputs\checkpoints\phase7_tcn_speed_only_h24_y6.pt | outputs\checkpoints\phase7_tcn_speed_only_h24_y6_scaler.json |
| TCN | speed_only | 72 | 1 | cuda | 65463 | 10706 | 10327 | 4 | 0.8407551223666517 | 769.4418925999926 | outputs\checkpoints\phase7_tcn_speed_only_h72_y1.pt | outputs\checkpoints\phase7_tcn_speed_only_h72_y1_scaler.json |
| TCN | speed_only | 72 | 3 | cuda | 63763 | 10055 | 10035 | 3 | 0.855083202284287 | 649.7195842000074 | outputs\checkpoints\phase7_tcn_speed_only_h72_y3.pt | outputs\checkpoints\phase7_tcn_speed_only_h72_y3_scaler.json |
| TCN | speed_only | 72 | 6 | cuda | 65745 | 10058 | 10198 | 3 | 0.9155553672488628 | 672.0356767000048 | outputs\checkpoints\phase7_tcn_speed_only_h72_y6.pt | outputs\checkpoints\phase7_tcn_speed_only_h72_y6_scaler.json |
| TCN | speed_only | 168 | 1 | cuda | 61291 | 6110 | 6488 | 5 | 1.168564152444443 | 812.4458821000007 | outputs\checkpoints\phase7_tcn_speed_only_h168_y1.pt | outputs\checkpoints\phase7_tcn_speed_only_h168_y1_scaler.json |
| TCN | speed_only | 168 | 3 | cuda | 59597 | 5629 | 6312 | 4 | 1.0868923704330653 | 699.95714459999 | outputs\checkpoints\phase7_tcn_speed_only_h168_y3.pt | outputs\checkpoints\phase7_tcn_speed_only_h168_y3_scaler.json |
| TCN | speed_only | 168 | 6 | cuda | 61570 | 5590 | 6321 | 6 | 1.0300886908242868 | 900.383839999995 | outputs\checkpoints\phase7_tcn_speed_only_h168_y6.pt | outputs\checkpoints\phase7_tcn_speed_only_h168_y6_scaler.json |
