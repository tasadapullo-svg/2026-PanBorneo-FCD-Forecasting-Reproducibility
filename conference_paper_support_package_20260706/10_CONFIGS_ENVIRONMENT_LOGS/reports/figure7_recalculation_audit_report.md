# Figure 7 Recalculation Audit Report

Generated: 2026-06-26 11:50:30

## 1. Source Files Used
- `D:\2026_PD\outputs\tables\phase8_small_sample_metrics.csv`
- `D:\2026_PD\outputs\plot_data\Fig07_missingness_stress_data.csv`
- `D:\2026_PD\outputs\plot_data\Fig07_noise_stress_data.csv`

## 2. Detected Columns In phase8_small_sample_metrics.csv
- MAE column: `mae`
- Horizon column: `horizon_hours`
- Seed column: `seed`
- Training-ratio column: `train_ratio`
- All columns: experiment, model, feature_group, target, target_column, history_hours, horizon_hours, train_ratio, seed, mae, rmse, smape, n_train_windows, n_val_windows, n_test_windows, best_epoch, best_val_mae, train_start, train_end_selected, val_start, val_end, test_start, test_end

## 3. Formula Used For Panel (c)
For each horizon and seed: `relative_change_pct = (MAE_ratio_seed - MAE_100_seed) / MAE_100_seed * 100`.
The 100% training condition is the reference condition.

## 4. 100% Training Mean Check
100% training mean equals exactly 0.0 for every horizon: `True`.

## 5. 100% Training Std Check
100% training std equals exactly 0.0 for every horizon: `True`.

## 6. Recalculated Panel (c) Values
| horizon | training_ratio | mean_relative_change_pct | std_relative_change_pct | n_seeds |
| --- | --- | --- | --- | --- |
| 1.0 | 20.0 | 7.185349842427202 | 12.754818001514419 | 5.0 |
| 1.0 | 40.0 | 6.356617463178708 | 6.857886512560691 | 5.0 |
| 1.0 | 60.0 | -1.4689389546498557 | 5.212689644910735 | 5.0 |
| 1.0 | 80.0 | 2.1252696411205436 | 4.496213658957373 | 5.0 |
| 1.0 | 100.0 | 0.0 | 0.0 | 5.0 |
| 3.0 | 20.0 | 6.284419313190696 | 8.437395354070548 | 5.0 |
| 3.0 | 40.0 | 13.362053340829544 | 3.862636747403028 | 5.0 |
| 3.0 | 60.0 | 7.166992601985363 | 8.402509943702835 | 5.0 |
| 3.0 | 80.0 | -0.4712125538136157 | 4.934601858805354 | 5.0 |
| 3.0 | 100.0 | 0.0 | 0.0 | 5.0 |
| 6.0 | 20.0 | 10.707956070278938 | 6.40480645267385 | 5.0 |
| 6.0 | 40.0 | 11.816867118961886 | 8.843940571793846 | 5.0 |
| 6.0 | 60.0 | 8.693473652622554 | 9.71089109447973 | 5.0 |
| 6.0 | 80.0 | 14.09205118367457 | 5.688522611956883 | 5.0 |
| 6.0 | 100.0 | 0.0 | 0.0 | 5.0 |

## 7. Formula Used For Panel (d) Limited Training
For limited training, the maximum observed degradation was defined as the maximum positive MAE change among 20%, 40%, 60%, and 80% training ratios relative to the 100% full-training setting.

## 8. Recalculated Panel (d) Degradation Values
| stress_type | horizon | maximum_observed_mae_degradation_pct | source_condition |
| --- | --- | --- | --- |
| limited_training | 1 | 7.185349842427202 | training_ratio=20 |
| limited_training | 3 | 13.362053340829544 | training_ratio=40 |
| limited_training | 6 | 14.09205118367457 | training_ratio=80 |
| missingness | 1 | 8.008742474003418 | missing_level=0.2 |
| missingness | 3 | 6.124617716560418 | missing_level=0.2 |
| missingness | 6 | 8.739153804782598 | missing_level=0.2 |
| noise | 1 | 27.95677080271166 | noise_level=0.05 |
| noise | 3 | 12.33218841379392 | noise_level=0.05 |
| noise | 6 | 30.481520788031258 | noise_level=0.05 |

## 9. Y-Axis Label Changes
- Panel (c): MAE change relative to full training (%)
- Panel (d): Maximum observed MAE degradation (%)
- Panel (d) terminology: Maximum observed degradation summary

## 10. Files Modified
- `D:\2026_PD\outputs\plot_data\Fig07_small_sample_training_data.csv`
- `D:\2026_PD\outputs\plot_data\Fig07_degradation_summary_data.csv`
- `D:\2026_PD\scripts\phase12a_prepare_plot_data.py`
- `D:\2026_PD\outputs\gpt_plot_package\phase8_small_sample\Fig07_small_sample_training_data.csv`
- `D:\2026_PD\outputs\gpt_plot_package\phase8_small_sample\Fig07_degradation_summary_data.csv`
- `D:\2026_PD\GitHub\outputs\github_release\PanBorneo_FCD_Forecasting_Reproducibility_Package\data\plot_data\Fig07_small_sample_training_data.csv`
- `D:\2026_PD\GitHub\outputs\github_release\PanBorneo_FCD_Forecasting_Reproducibility_Package\data\plot_data\Fig07_degradation_summary_data.csv`
- `D:\2026_PD\GitHub\outputs\github_release\PanBorneo_FCD_Forecasting_Reproducibility_Package\scripts\original_project_scripts\phase12a_prepare_plot_data.py`
- `D:\2026_PD\GitHub\outputs\github_release\PanBorneo_FCD_Forecasting_Reproducibility_Package\figures\README_FIGURES.md`
- `D:\2026_PD\GitHub\outputs\github_release\PanBorneo_FCD_Forecasting_Reproducibility_Package\reports\figure7_recalculation_audit_report.md`

## 11. Files Not Modified
- `D:\2026_PD\outputs\tables\phase8_small_sample_metrics.csv`
- `D:\2026_PD\outputs\plot_data\Fig07_missingness_stress_data.csv`
- `D:\2026_PD\outputs\plot_data\Fig07_noise_stress_data.csv`

## 12. Warnings
- none

## Caption Clarification
For limited training, the maximum observed degradation was defined as the maximum positive MAE change among 20%, 40%, 60%, and 80% training ratios relative to the 100% full-training setting.
