# Phase 15 Feature Ablation Report

## Design

- Main model: **TCN**, matching the Phase 13 proposed main-model architecture.
- Samples: identical leakage-controlled Phase 2 chronological windows for every feature group within each horizon.
- Scaling: fitted separately on each feature group's training samples only.
- All inputs are historical window columns only; no future target, coverage, reliability, or volatility values are used.

## Best Feature Group by Horizon

| feature_group | horizon | MAE_mean | MAE_std | relative_change_mean |
| --- | --- | --- | --- | --- |
| speed_only | 1 | 0.9656069591411803 | 0.08417013353565879 | 0.0 |
| speed_volatility | 3 | 1.012684306048207 | 0.04931236662272278 | -2.7126749705574444 |
| speed_only | 6 | 0.9297849753920859 | 0.025191466400926017 | 0.0 |

## Mean Metrics Across Seeds

| feature_group | horizon | MAE_mean | MAE_std | relative_change_mean |
| --- | --- | --- | --- | --- |
| full_features | 1 | 1.2215965808754885 | 0.10855826383624176 | 26.686258513265535 |
| full_features | 3 | 1.148554125906422 | 0.037066107595814544 | 10.230770587815773 |
| full_features | 6 | 1.080662756296986 | 0.053457463533523056 | 16.22657419234759 |
| speed_only | 1 | 0.9656069591411803 | 0.08417013353565879 | 0.0 |
| speed_only | 3 | 1.0421897657272048 | 0.028340268801321254 | 0.0 |
| speed_only | 6 | 0.9297849753920859 | 0.025191466400926017 | 0.0 |
| speed_reliability | 1 | 1.1682658752304556 | 0.07664755756734497 | 21.975004280123777 |
| speed_reliability | 3 | 1.1139459306813586 | 0.06690947026494606 | 6.971390254914479 |
| speed_reliability | 6 | 1.0552833752159458 | 0.1047568869917704 | 13.69503805641873 |
| speed_time | 1 | 1.1549255906986402 | 0.016266871628211818 | 20.33025450937983 |
| speed_time | 3 | 1.0676678055523823 | 0.0186490227635986 | 2.5414673637536516 |
| speed_time | 6 | 0.9853306508350389 | 0.029412375455762616 | 6.049940114217403 |
| speed_volatility | 1 | 1.0759072207588105 | 0.07411905973507447 | 12.117821983477967 |
| speed_volatility | 3 | 1.012684306048207 | 0.04931236662272278 | -2.7126749705574444 |
| speed_volatility | 6 | 0.9502898019178906 | 0.04375380599458462 | 2.354031643433626 |

## Interpretation

### Does full_features improve over speed_only?

| horizon | relative_change_mean |
| --- | --- |
| 1.0 | 26.686258513265535 |
| 3.0 | 10.230770587815773 |
| 6.0 | 16.22657419234759 |

### Are reliability features helpful for point forecasting?

| horizon | relative_change_mean |
| --- | --- |
| 1.0 | 21.975004280123777 |
| 3.0 | 6.971390254914479 |
| 6.0 | 13.69503805641873 |

### Are volatility features helpful for difficult horizons?

| horizon | relative_change_mean |
| --- | --- |
| 1.0 | 12.117821983477967 |
| 3.0 | -2.7126749705574444 |
| 6.0 | 2.354031643433626 |

### Is the conclusion stable across seeds?

| feature_group | mean_relative_MAE_change_percent | std_across_horizon_seed_percent |
| --- | --- | --- |
| speed_time | 9.640553995783629 | 10.366894549206318 |
| speed_reliability | 14.213810863818996 | 13.296167996617521 |
| speed_volatility | 3.9197262187847164 | 10.677866969303375 |
| full_features | 17.714534431142965 | 8.806326601069296 |

A negative relative MAE change indicates improvement over speed_only. Results are reported as observed; full_features is not assumed to be best.
