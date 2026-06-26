# Data Package Validation Report

## CSV Files

| file | rows | columns | column_names |
| --- | ---: | ---: | --- |
| data/data_dictionary.csv | 844 | 8 | file_name, column_name, data_type, description, unit, allowed_values_or_range, missing_value_rule, notes |
| data/file_manifest.csv | 143 | 10 | relative_path, file_name, file_type, file_size_kb, rows, columns, sha256, purpose, public_release_status, notes |
| data/plot_data/deprecated/Fig07_noise_missingness_combined_data.csv | 24 | 9 | perturbation_type, perturbation_level, horizon_hours, horizon_label, MAE, RMSE, sMAPE, MAE_increase_vs_zero, MAE_increase_percent_vs_zero |
| data/plot_data/Fig01_workflow_data.csv | 10 | 11 | phase, experiment_name, status, main_scope, key_outputs, main_conclusion, usable_for_paper, phase_order, short_label, figure_group, include_in_main_workflow |
| data/plot_data/Fig02_main_forecasting_performance.csv | 21 | 18 | source_phase, model, feature_group, history_hours, horizon_hours, split, MAE, RMSE, sMAPE, comparison_baseline, improvement_percent_vs_seasonal, interpretation, MAE_std, plot_model_label, plot_group, is_final_five_seed, has_errorbar, horizon_label |
| data/plot_data/Fig03_five_seed_stability_mean_std.csv | 3 | 16 | horizon_hours, history_hours, seed_count, MAE_mean, MAE_std, MAE_cv, all_seeds_outperform_seasonal, mean_improvement_percent_vs_seasonal, source_phase, interpretation, SeasonalHistoricalAverage_MAE, horizon_label, model_label, baseline_label, yerr_low, yerr_high |
| data/plot_data/Fig03_improvement_boxplot.csv | 15 | 7 | seed, horizon_hours, history_hours, improvement_percent_vs_seasonal, outperforms_seasonal, horizon_label, zero_reference |
| data/plot_data/Fig03_seed_scatter.csv | 15 | 22 | model, input_feature_group, seed, history_hours, horizon_hours, split, best_epoch, best_val_MAE, n, MAE, RMSE, sMAPE, checkpoint, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, outperforms_seasonal, horizon_label, seed_label, jitter_group |
| data/plot_data/Fig04_ablation_data.csv | 15 | 22 | model, ablation_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds, speed_only_MAE, delta_MAE_vs_speed_only, improvement_percent_vs_speed_only, improvement_percent_vs_seasonal, horizon_label, ablation_label, is_speed_only, recommended_color_group, interpretation_short |
| data/plot_data/Fig05_history_sensitivity_data.csv | 9 | 20 | model, input_feature_group, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, is_best_history_for_horizon, history_label, horizon_label, best_marker, plot_order |
| data/plot_data/Fig06_volatility_error_data.csv | 12 | 10 | horizon_hours, volatility_bin, n, MAE, RMSE, sMAPE, horizon_label, volatility_label, volatility_order, high_vs_low_flag |
| data/plot_data/Fig07_degradation_summary_data.csv | 3 | 5 | stress_type, worst_case_mae_increase_pct, horizon_hours, level, source_csv |
| data/plot_data/Fig07_missingness_stress_data.csv | 12 | 13 | history_hours, horizon_hours, missing_level, n, MAE, RMSE, sMAPE, horizon_label, perturbation_type, perturbation_level, baseline_MAE_at_zero, MAE_increase_vs_zero, MAE_increase_percent_vs_zero |
| data/plot_data/Fig07_noise_stress_data.csv | 12 | 13 | history_hours, horizon_hours, noise_level, n, MAE, RMSE, sMAPE, horizon_label, perturbation_type, perturbation_level, baseline_MAE_at_zero, MAE_increase_vs_zero, MAE_increase_percent_vs_zero |
| data/plot_data/Fig07_small_sample_training_data.csv | 15 | 15 | train_ratio, train_ratio_percent, horizon_hours, model, feature_group, mae_mean, mae_std, rmse_mean, rmse_std, smape_mean, smape_std, mae_full_train_mean, mae_degradation_vs_full_pct, n_train_windows_mean, n_test_windows_mean |
| data/plot_data/FigA1_public_benchmark_sanity_data.csv | 11 | 24 | dataset, model, feature_group, seed_count, history_steps, horizon_steps, MAE_mean, MAE_std, MAE_cv, RMSE_mean, sMAPE_mean, outperforms_historical_average_all_seeds, outperforms_persistence_all_seeds, interpretation, baseline_name, baseline_MAE, seed, MAE, outperforms_HA, outperforms_Persistence, dataset_label, benchmark_role, claim_boundary, recommended_location |
| data/plot_data/phase8_small_sample_metrics.csv | 75 | 23 | experiment, model, feature_group, target, target_column, history_hours, horizon_hours, train_ratio, seed, mae, rmse, smape, n_train_windows, n_val_windows, n_test_windows, best_epoch, best_val_mae, train_start, train_end_selected, val_start, val_end, test_start, test_end |
| data/plot_data/plot_data_manifest.csv | 16 | 9 | figure_id, figure_title, source_files, required_columns, plot_type, recommended_location, main_message, csv_file, status |
| data/plot_data/Table_key_findings_for_paper.csv | 9 | 6 | finding_id, finding, supporting_phase, supporting_metric, paper_interpretation, caution_or_limitation |
| data/plot_data/Table_main_results_for_paper.csv | 18 | 11 | result_group, model, feature_group, history_hours, horizon_hours, MAE, MAE_std, RMSE, sMAPE, improvement_percent_vs_seasonal, interpretation |
| data/processed/coverage_by_point.csv | 51 | 14 | point_id, record_rows, first_time, last_time, global_expected_steps, point_expected_steps, observed_steps, coverage_ratio, duplicate_timestamp_rows, speed_anomaly_count, travel_time_anomaly_count, congestion_anomaly_count, coverage_group, max_consecutive_missing_steps |
| data/processed/coverage_by_time.csv | 1980 | 6 | time_bin, total_panel_rows, observed_points, total_points, coverage_ratio, date |
| data/processed/final_ablation_summary.csv | 5 | 12 | ablation_group, model, history_hours, horizons, test_MAE_mean_across_horizons, test_RMSE_mean_across_horizons, test_sMAPE_mean_across_horizons, best_horizon_hours, best_horizon_MAE, mean_improvement_percent_vs_speed_only, mean_improvement_percent_vs_seasonal, interpretation |
| data/processed/final_empirical_findings_summary.csv | 9 | 6 | finding_id, finding, supporting_phase, supporting_metric, paper_interpretation, caution_or_limitation |
| data/processed/final_history_sensitivity_summary.csv | 6 | 9 | summary_type, history_hours, horizon_hours, MAE, RMSE, sMAPE, improvement_percent_vs_seasonal, is_best_history_for_horizon, interpretation |
| data/processed/final_main_forecasting_results.csv | 21 | 12 | source_phase, model, feature_group, history_hours, horizon_hours, split, MAE, RMSE, sMAPE, comparison_baseline, improvement_percent_vs_seasonal, interpretation |
| data/processed/final_phase_status_summary.csv | 10 | 7 | phase, experiment_name, status, main_scope, key_outputs, main_conclusion, usable_for_paper |
| data/processed/final_public_benchmark_summary.csv | 1 | 14 | dataset, model, feature_group, seed_count, history_steps, horizon_steps, MAE_mean, MAE_std, MAE_cv, RMSE_mean, sMAPE_mean, outperforms_historical_average_all_seeds, outperforms_persistence_all_seeds, interpretation |
| data/processed/final_robustness_summary.csv | 12 | 10 | summary_type, history_hours, horizon_hours, condition, level, n, MAE, RMSE, sMAPE, interpretation |
| data/processed/final_seed_stability_summary.csv | 3 | 10 | horizon_hours, history_hours, seed_count, MAE_mean, MAE_std, MAE_cv, all_seeds_outperform_seasonal, mean_improvement_percent_vs_seasonal, source_phase, interpretation |
| data/processed/missing_summary.csv | 52 | 5 | column, dtype, missing_count, missing_rate, unique_count |
| data/processed/phase3_baseline_metrics.csv | 12 | 8 | model, split, n, MAE, RMSE, MAPE, sMAPE, R2 |
| data/processed/phase3_baseline_metrics_by_history.csv | 36 | 9 | model, split, history_hours, n, MAE, RMSE, MAPE, sMAPE, R2 |
| data/processed/phase3_baseline_metrics_by_horizon.csv | 60 | 9 | model, split, horizon_hours, n, MAE, RMSE, MAPE, sMAPE, R2 |
| data/processed/phase3_baseline_runtime_summary.csv | 4 | 3 | stage, seconds, rows |
| data/processed/phase5_deep_metrics.csv | 144 | 12 | model, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds |
| data/processed/phase5_deep_metrics_by_horizon.csv | 20 | 9 | model, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE |
| data/processed/phase5_deep_metrics_by_model.csv | 4 | 6 | model, split, n, MAE, RMSE, sMAPE |
| data/processed/phase5_deep_runtime_summary.csv | 10 | 12 | model, history_hours, horizon_hours, device, train_samples, val_samples, test_samples, best_epoch, best_val_MAE, seconds, checkpoint, scaler_metadata |
| data/processed/phase5_deep_vs_baseline_comparison.csv | 10 | 9 | model, history_hours, horizon_hours, MAE, RMSE, sMAPE, SeasonalHistoricalAverage_MAE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal |
| data/processed/phase6_ablation_metrics.csv | 188 | 13 | model, ablation_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds |
| data/processed/phase6_ablation_metrics_by_group.csv | 10 | 7 | model, ablation_group, split, n, MAE, RMSE, sMAPE |
| data/processed/phase6_ablation_metrics_by_horizon.csv | 30 | 10 | model, ablation_group, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE |
| data/processed/phase6_ablation_runtime_summary.csv | 15 | 13 | model, ablation_group, history_hours, horizon_hours, device, train_samples, val_samples, test_samples, best_epoch, best_val_MAE, seconds, checkpoint, scaler_metadata |
| data/processed/phase6_ablation_vs_full.csv | 15 | 16 | model, ablation_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds, full_features_MAE, delta_MAE_vs_full, improvement_percent_vs_full |
| data/processed/phase6_ablation_vs_seasonal.csv | 15 | 18 | model, ablation_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal |
| data/processed/phase6_ablation_vs_speed_only.csv | 15 | 16 | model, ablation_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds, speed_only_MAE, delta_MAE_vs_speed_only, improvement_percent_vs_speed_only |
| data/processed/phase7_history_best_by_horizon.csv | 3 | 11 | model, input_feature_group, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE, is_best_history_for_horizon |
| data/processed/phase7_history_metrics.csv | 81 | 13 | model, input_feature_group, history_hours, horizon_hours, epoch, split, train_loss, MAE, RMSE, sMAPE, best_val_MAE, best_epoch, elapsed_seconds |
| data/processed/phase7_history_metrics_by_history.csv | 6 | 8 | model, input_feature_group, history_hours, split, n, MAE, RMSE, sMAPE |
| data/processed/phase7_history_metrics_by_horizon.csv | 18 | 10 | model, input_feature_group, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE |
| data/processed/phase7_history_runtime_summary.csv | 9 | 13 | model, input_feature_group, history_hours, horizon_hours, device, train_samples, val_samples, test_samples, best_epoch, best_val_MAE, seconds, checkpoint, scaler_metadata |
| data/processed/phase7_history_vs_seasonal.csv | 9 | 16 | model, input_feature_group, history_hours, horizon_hours, split, n, best_epoch, MAE, RMSE, sMAPE, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, is_best_history_for_horizon |
| data/processed/phase8_error_by_hour_group.csv | 9 | 6 | horizon_hours, hour_group, n, MAE, RMSE, sMAPE |
| data/processed/phase8_error_by_input_observed_ratio.csv | 9 | 6 | horizon_hours, input_observed_ratio_bin, n, MAE, RMSE, sMAPE |
| data/processed/phase8_error_by_point.csv | 153 | 6 | horizon_hours, point_id, n, MAE, RMSE, sMAPE |
| data/processed/phase8_error_by_target_observed_ratio.csv | 7 | 6 | horizon_hours, target_observed_ratio_bin, n, MAE, RMSE, sMAPE |
| data/processed/phase8_error_by_volatility.csv | 12 | 6 | horizon_hours, volatility_bin, n, MAE, RMSE, sMAPE |
| data/processed/phase8_missingness_stress_metrics.csv | 12 | 7 | history_hours, horizon_hours, missing_level, n, MAE, RMSE, sMAPE |
| data/processed/phase8_noise_stress_metrics.csv | 12 | 7 | history_hours, horizon_hours, noise_level, n, MAE, RMSE, sMAPE |
| data/processed/phase8_robustness_metrics.csv | 3 | 7 | history_hours, horizon_hours, checkpoint, n, MAE, RMSE, sMAPE |
| data/processed/phase8_runtime_summary.csv | 3 | 7 | history_hours, horizon_hours, checkpoint, scaler_metadata, samples, seconds, device |
| data/processed/phase8_small_sample_metrics.csv | 75 | 23 | experiment, model, feature_group, target, target_column, history_hours, horizon_hours, train_ratio, seed, mae, rmse, smape, n_train_windows, n_val_windows, n_test_windows, best_epoch, best_val_mae, train_start, train_end_selected, val_start, val_end, test_start, test_end |
| data/processed/phase9_seed_metrics.csv | 9 | 13 | model, input_feature_group, seed, history_hours, horizon_hours, split, best_epoch, best_val_MAE, n, MAE, RMSE, sMAPE, checkpoint |
| data/processed/phase9_seed_summary_by_horizon.csv | 3 | 13 | horizon_hours, history_hours, seed_count, MAE_mean, MAE_std, MAE_min, MAE_max, MAE_cv, best_seed, worst_seed, SeasonalHistoricalAverage_MAE, all_seeds_outperform_seasonal, mean_improvement_percent_vs_seasonal |
| data/processed/phase9_seed_vs_seasonal.csv | 9 | 19 | model, input_feature_group, seed, history_hours, horizon_hours, split, best_epoch, best_val_MAE, n, MAE, RMSE, sMAPE, checkpoint, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, outperforms_seasonal |
| data/processed/phase9b_five_seed_metrics.csv | 15 | 13 | model, input_feature_group, seed, history_hours, horizon_hours, split, best_epoch, best_val_MAE, n, MAE, RMSE, sMAPE, checkpoint |
| data/processed/phase9b_five_seed_summary_by_horizon.csv | 3 | 13 | horizon_hours, history_hours, seed_count, MAE_mean, MAE_std, MAE_min, MAE_max, MAE_cv, best_seed, worst_seed, SeasonalHistoricalAverage_MAE, all_seeds_outperform_seasonal, mean_improvement_percent_vs_seasonal |
| data/processed/phase9b_five_seed_vs_seasonal.csv | 15 | 19 | model, input_feature_group, seed, history_hours, horizon_hours, split, best_epoch, best_val_MAE, n, MAE, RMSE, sMAPE, checkpoint, SeasonalHistoricalAverage_MAE, SeasonalHistoricalAverage_RMSE, SeasonalHistoricalAverage_sMAPE, delta_MAE_vs_seasonal, improvement_percent_vs_seasonal, outperforms_seasonal |
| data/processed/point_metadata.csv | 51 | 3 | point_id, point_code, point_quality_group |
| data/processed/point_quality_summary.csv | 51 | 15 | point_id, record_rows, first_time, last_time, global_expected_steps, point_expected_steps, observed_steps, coverage_ratio, duplicate_timestamp_rows, speed_anomaly_count, travel_time_anomaly_count, congestion_anomaly_count, coverage_group, max_consecutive_missing_steps, meets_coverage_threshold_for_direct_1week |
| data/processed/target_variable_summary.csv | 4 | 10 | target_variable, source_column, available, non_missing_count, missing_rate, mean, std, min, max, recommended_main_target |
| data/processed/time_continuity_check.csv | 51 | 6 | point_id, inferred_frequency, unique_timestamps, gap_count_larger_than_frequency, max_gap_hours, duplicate_timestamp_rows |
| data/processed/time_coverage_summary.csv | 1980 | 6 | time_bin, total_panel_rows, observed_points, total_points, coverage_ratio, date |
| data/processed/train_val_test_split_summary.csv | 3 | 6 | split, start_time, end_time, time_steps, rows, points |
| data/processed/window_count_by_split.csv | 184 | 5 | split, history_hours, horizon_hours, target_variable, window_count |
| data/processed/window_feasibility_by_horizon.csv | 64 | 9 | history_hours, horizon_hours, target_variable, is_main_forecast, is_extended_horizon, candidate_windows, valid_windows_min_80pct_observed, valid_window_ratio, feasible_as_main_experiment |
| data/processed/window_feasibility_summary.csv | 18 | 6 | history_hours, horizon_hours, frequency, candidate_windows, fully_observed_target_windows, fully_observed_target_window_ratio |
| data/processed/window_missingness_summary.csv | 64 | 7 | history_hours, horizon_hours, target_variable, window_count, mean_input_observed_ratio, mean_target_observed_ratio, mean_input_missing_mask_ratio |

## Figure Data Status

| figure | file | status |
| --- | --- | --- |
| Figure 1 | Fig01_workflow_data.csv | ok |
| Figure 2 | Fig02_main_forecasting_performance.csv | ok |
| Figure 3 | Fig03_five_seed_stability_mean_std.csv | ok |
| Figure 3 | Fig03_seed_scatter.csv | ok |
| Figure 3 | Fig03_improvement_boxplot.csv | ok |
| Figure 4 | Fig04_ablation_data.csv | ok |
| Figure 5 | Fig05_history_sensitivity_data.csv | ok |
| Figure 6 | Fig06_volatility_error_data.csv | ok |
| Figure 7 | Fig07_missingness_stress_data.csv | ok |
| Figure 7 | Fig07_noise_stress_data.csv | ok |
| Figure 7 | Fig07_small_sample_training_data.csv | ok |
| Figure 7 | Fig07_degradation_summary_data.csv | ok |
| Figure 7 | phase8_small_sample_metrics.csv | ok |

## Warnings

- none
