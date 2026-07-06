# Phase 4 Deep Learning Smoke Test Report

This phase is a smoke test only. It verifies deep learning data loading, input/output shapes, short training, validation, logging, and checkpoint saving.

## Scope
- Target: `speed` / `current_speed`
- History: 24h only
- Horizons: 1h and 3h only
- Models: LSTM and TCN only
- Epochs: 2
- 168h horizon excluded
- No GRU, Transformer, ST-Transformer, benchmark datasets, uncertainty prediction, repeated seeds, or full training.

## Metrics
| model | history_hours | horizon_hours | epoch | split | train_loss | MAE | RMSE | elapsed_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LSTM | 24 | 1 | 1 | val | 6218.2873546875 | 69.16703506050109 | 70.12998776324659 | 0.9120968000024732 |
| LSTM | 24 | 1 | 2 | val | 3373.64525625 | 49.47891192016601 | 50.81211516374825 | 1.7314465000017663 |
| LSTM | 24 | 1 | 2 | test | nan | 49.40752267074585 | 50.715316612083484 | 1.796518000002834 |
| TCN | 24 | 1 | 1 | val | 255.97983263397217 | 1.8004510940551757 | 2.5019902790194446 | 13.533766900000046 |
| TCN | 24 | 1 | 2 | val | 8.341906860351562 | 1.278840397644043 | 2.2873933193615477 | 27.067534999998315 |
| TCN | 24 | 1 | 2 | test | nan | 1.3834121238708497 | 2.384964510167138 | 29.39217110000027 |
| LSTM | 24 | 3 | 1 | val | 5990.83424296875 | 66.95124430389404 | 67.90484242345626 | 1.1308563000020513 |
| LSTM | 24 | 3 | 2 | val | 3110.512283203125 | 47.104306130218504 | 48.292111188080916 | 2.053336200002377 |
| LSTM | 24 | 3 | 2 | test | nan | 47.02631616287231 | 48.17274526291684 | 2.132312500001717 |
| TCN | 24 | 3 | 1 | val | 580.3404461791993 | 2.592586399841309 | 2.8351649189206194 | 13.569518600001174 |
| TCN | 24 | 3 | 2 | val | 11.085920478820801 | 1.2063925811767577 | 1.7553665742624864 | 27.22831700000097 |
| TCN | 24 | 3 | 2 | test | nan | 1.2279879753112792 | 1.7191165714620658 | 29.55082820000098 |

## Runtime
| model | history_hours | horizon_hours | device | train_samples | val_samples | test_samples | seconds | checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LSTM | 24 | 1 | cuda | 20000 | 5000 | 5000 | 1.7984466000016255 | outputs\checkpoints\phase4_smoke_lstm_h24_y1.pt |
| TCN | 24 | 1 | cuda | 20000 | 5000 | 5000 | 29.394909099999495 | outputs\checkpoints\phase4_smoke_tcn_h24_y1.pt |
| LSTM | 24 | 3 | cuda | 20000 | 5000 | 5000 | 2.1339740000003076 | outputs\checkpoints\phase4_smoke_lstm_h24_y3.pt |
| TCN | 24 | 3 | cuda | 20000 | 5000 | 5000 | 29.553158099999564 | outputs\checkpoints\phase4_smoke_tcn_h24_y3.pt |

## Leakage Controls
- Windows are read from Phase 2 chronological splits only.
- Inputs are constructed only from the input window.
- Labels are the mean speed over the future target window and are used only for loss/metrics.
- Future target-window features are not used as inputs.
