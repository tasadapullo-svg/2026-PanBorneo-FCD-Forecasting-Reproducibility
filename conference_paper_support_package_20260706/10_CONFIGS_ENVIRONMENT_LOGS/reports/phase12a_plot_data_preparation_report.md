# Phase 12A Plot Data Preparation Report

No figures were generated. No training was run. Previous phase outputs and locked folders were not modified.

## Output CSV Summary

| csv_file | rows | columns | column_names |
| --- | --- | --- | --- |
| Fig01_workflow_data.csv | 10 | 11 | phase, experiment_name, status, main_scope, key_outputs, main_conclusion, usable_for_paper, phase_order, short_label, figure_group, include_in_main_workflow |
| Fig02_main_forecasting_performance.csv | 21 | 18 | source_phase, model, feature_group, history_hours, horizon_hours, split, MAE, RMSE, sMAPE, comparison_baseline, improvement_percent_vs_seasonal, interpretation, MAE_std, plot_model_label, plot_group, is_final_five_seed, has_errorbar, horizon_label |
| Fig03_five_seed_stability_mean_std.csv | 3 | 16 | horizon_hours, history_hours, seed_count, MAE_mean, MAE_std, MAE_cv, all_seeds_outperform_seasonal, mean_improvement_percent_vs_seasonal, source_phase, interpretation, SeasonalHistoricalAverage_MAE, horizon_label, model_label, baseline_label, yerr_low, yerr_high |
| Fig03_seed_scatter.csv | 15 | 22 | model, input_feature_group, seed, history_hours, horizon_hours, split, best_epoch, best_val_MAE, n, MAE, RMSE, sMAPE, checkpoint, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, outperforms_seasonal, horizon_label, seed_label, jitter_group |
| Fig03_improvement_boxplot.csv | 15 | 7 | seed, horizon_hours, history_hours, improvement_percent_vs_seasonal, outperforms_seasonal, horizon_label, zero_reference |
| Fig04_ablation_data.csv | 15 | 22 | model, ablation_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds, speed_only_MAE, delta_MAE_vs_speed_only, improvement_percent_vs_speed_only, improvement_percent_vs_seasonal, horizon_label, ablation_label, is_speed_only, recommended_color_group, interpretation_short |
| Fig05_history_sensitivity_data.csv | 9 | 20 | model, input_feature_group, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, is_best_history_for_horizon, history_label, horizon_label, best_marker, plot_order |
| Fig06_volatility_error_data.csv | 12 | 10 | horizon_hours, volatility_bin, n, MAE, RMSE, sMAPE, horizon_label, volatility_label, volatility_order, high_vs_low_flag |
| Fig07_missingness_stress_data.csv | 12 | 13 | history_hours, horizon_hours, missing_level, n, MAE, RMSE, sMAPE, horizon_label, perturbation_type, perturbation_level, baseline_MAE_at_zero, MAE_increase_vs_zero, MAE_increase_percent_vs_zero |
| Fig07_noise_stress_data.csv | 12 | 13 | history_hours, horizon_hours, noise_level, n, MAE, RMSE, sMAPE, horizon_label, perturbation_type, perturbation_level, baseline_MAE_at_zero, MAE_increase_vs_zero, MAE_increase_percent_vs_zero |
| Fig07_small_sample_training_data.csv | 15 | 15 | train_ratio, train_ratio_percent, horizon_hours, model, feature_group, mae_mean, mae_std, rmse_mean, rmse_std, smape_mean, smape_std, mae_full_train_mean, mae_degradation_vs_full_pct, n_train_windows_mean, n_test_windows_mean |
| Fig07_degradation_summary_data.csv | 3 | 5 | stress_type, worst_case_mae_increase_pct, horizon_hours, level, source_csv |
| Fig07_noise_missingness_combined_data.csv | 24 | 9 | perturbation_type, perturbation_level, horizon_hours, horizon_label, MAE, RMSE, sMAPE, MAE_increase_vs_zero, MAE_increase_percent_vs_zero |
| FigA1_public_benchmark_sanity_data.csv | 11 | 24 | dataset, model, feature_group, seed_count, history_steps, horizon_steps, MAE_mean, MAE_std, MAE_cv, RMSE_mean, sMAPE_mean, outperforms_historical_average_all_seeds, outperforms_persistence_all_seeds, interpretation, baseline_name, baseline_MAE, seed, MAE, outperforms_HA, outperforms_Persistence, dataset_label, benchmark_role, claim_boundary, recommended_location |
| Table_main_results_for_paper.csv | 18 | 11 | result_group, model, feature_group, history_hours, horizon_hours, MAE, MAE_std, RMSE, sMAPE, improvement_percent_vs_seasonal, interpretation |
| Table_key_findings_for_paper.csv | 9 | 6 | finding_id, finding, supporting_phase, supporting_metric, paper_interpretation, caution_or_limitation |
| plot_data_manifest.csv | 16 | 9 | figure_id, figure_title, source_files, required_columns, plot_type, recommended_location, main_message, csv_file, status |

## Interpretation Constraints
- Reliability features are not claimed to directly improve forecasting accuracy.
- Deep learning is not claimed to dominate all horizons.
- Longer history is not claimed to always be better.
- Phase 10 is labelled as supplementary sanity check only.
- Pan Borneo Phase 9B five-seed results remain the main evidence.