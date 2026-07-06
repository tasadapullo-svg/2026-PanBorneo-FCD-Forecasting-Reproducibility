# Phase 10 Public Benchmark Sanity Check Report

Phase 10 is a supplementary public benchmark sanity check only. It verifies that the speed-only TCN pipeline can run on a public traffic speed matrix.

It is not a comprehensive public benchmark study and should not be described as a competitive benchmark claim.

## Dataset
- Dataset folder: `METR-LA-mini`
- Source file: `data\benchmark\METR-LA-mini\METR-LA.csv`
- File format: `.csv`
- Raw shape: `(34272, 208)`
- Sensor columns: `207`
- Timestamp column: `Unnamed: 0`

## Five-Seed TCN Metrics
| dataset | model | feature_group | seed | history_steps | horizon_steps | split | best_step | best_val_MAE | n | MAE | RMSE | sMAPE | checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| METR-LA-mini | TCN | speed_only | 42 | 12 | 12 | test | 3 | 8.148970650291442 | 10000 | 3.1925295333862307 | 4.619663797594772 | 0.0717418670596761 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed42_h12_y12.pt |
| METR-LA-mini | TCN | speed_only | 2025 | 12 | 12 | test | 1 | 8.42064466571808 | 10000 | 3.875455109024048 | 5.013587077641721 | 0.0819171642448815 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed2025_h12_y12.pt |
| METR-LA-mini | TCN | speed_only | 20260623 | 12 | 12 | test | 1 | 8.25971893119812 | 10000 | 3.2719146606445317 | 4.677137235002751 | 0.0729940607457361 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed20260623_h12_y12.pt |
| METR-LA-mini | TCN | speed_only | 1234 | 12 | 12 | test | 3 | 7.931615483283997 | 10000 | 2.741011911392212 | 4.246848328442164 | 0.0644782394910112 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed1234_h12_y12.pt |
| METR-LA-mini | TCN | speed_only | 3407 | 12 | 12 | test | 2 | 8.488771273612976 | 10000 | 4.010458123207092 | 5.168413862745486 | 0.0848995950638955 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed3407_h12_y12.pt |

## Summary By Horizon
| dataset | model | feature_group | history_steps | horizon_steps | seed_count | MAE_mean | MAE_std | MAE_min | MAE_max | MAE_cv | RMSE_mean | sMAPE_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| METR-LA-mini | TCN | speed_only | 12 | 12 | 5 | 3.418273867530823 | 0.5221977976101612 | 2.741011911392212 | 4.010458123207092 | 0.1527665183794558 | 4.745130060285378 | 0.0752061853210401 |

## Versus Simple Baselines
| dataset | baseline | seed | history_steps | horizon_steps | baseline_MAE | TCN_MAE | delta_MAE_vs_baseline | improvement_percent_vs_baseline | outperforms_baseline |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| METR-LA-mini | Persistence | 42 | 12 | 12 | 2.2743840793609618 | 3.1925295333862307 | -0.9181454540252688 | -40.368971202227286 | False |
| METR-LA-mini | Persistence | 2025 | 12 | 12 | 2.2743840793609618 | 3.875455109024048 | -1.601071029663086 | -70.39580711947922 | False |
| METR-LA-mini | Persistence | 20260623 | 12 | 12 | 2.2743840793609618 | 3.2719146606445317 | -0.9975305812835696 | -43.859372316915255 | False |
| METR-LA-mini | Persistence | 1234 | 12 | 12 | 2.2743840793609618 | 2.741011911392212 | -0.46662783203125 | -20.51666806260618 | False |
| METR-LA-mini | Persistence | 3407 | 12 | 12 | 2.2743840793609618 | 4.010458123207092 | -1.7360740438461306 | -76.33161257151953 | False |
| METR-LA-mini | HistoricalAverage | 42 | 12 | 12 | 12.50999147090912 | 3.1925295333862307 | 9.31746193752289 | 74.48016219027667 | True |
| METR-LA-mini | HistoricalAverage | 2025 | 12 | 12 | 12.50999147090912 | 3.875455109024048 | 8.634536361885072 | 69.02112109319917 | True |
| METR-LA-mini | HistoricalAverage | 20260623 | 12 | 12 | 12.50999147090912 | 3.2719146606445317 | 9.238076810264587 | 73.84558839825687 | True |
| METR-LA-mini | HistoricalAverage | 1234 | 12 | 12 | 12.50999147090912 | 2.741011911392212 | 9.768979559516907 | 78.08941822409557 | True |
| METR-LA-mini | HistoricalAverage | 3407 | 12 | 12 | 12.50999147090912 | 4.010458123207092 | 8.499533347702027 | 67.94195957260995 | True |

## Runtime
| dataset | seed | device | history_steps | horizon_steps | train_samples | val_samples | test_samples | best_step | best_val_MAE | seconds | checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| METR-LA-mini | 42 | cuda | 12 | 12 | 50000 | 10000 | 10000 | 3 | 8.148970650291442 | 154.59275749999506 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed42_h12_y12.pt |
| METR-LA-mini | 2025 | cuda | 12 | 12 | 50000 | 10000 | 10000 | 1 | 8.42064466571808 | 93.92324459999509 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed2025_h12_y12.pt |
| METR-LA-mini | 20260623 | cuda | 12 | 12 | 50000 | 10000 | 10000 | 1 | 8.25971893119812 | 94.3049589000002 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed20260623_h12_y12.pt |
| METR-LA-mini | 1234 | cuda | 12 | 12 | 50000 | 10000 | 10000 | 3 | 7.931615483283997 | 153.60848439999972 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed1234_h12_y12.pt |
| METR-LA-mini | 3407 | cuda | 12 | 12 | 50000 | 10000 | 10000 | 2 | 8.488771273612976 | 123.90304949998972 | outputs\checkpoints\phase10_tcn_speed_only_metr-la-mini_seed3407_h12_y12.pt |
