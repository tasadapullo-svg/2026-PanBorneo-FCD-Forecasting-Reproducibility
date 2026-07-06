# Phase 18 Figure/Table Consistency Audit

**Status: PASS**

- Critical errors: 0
- Warnings: 0

## Critical Errors

- None.

## Warnings

- None.

## Recommended Fixes

- Sources are consistent. Proceed to Phase 19 manuscript package preparation.

## Source Inventory

| Check | Passed | Severity | Source | Rows | Detail |
| --- | --- | --- | --- | --- | --- |
| phase13_exists | True | info | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv | 105 | loaded |
| phase15_exists | True | info | outputs\tables\phase15_feature_ablation_metrics.csv | 75 | loaded |
| phase16_missingness_exists | True | info | outputs\tables\phase16_missingness_stress.csv | 60 | loaded |
| phase16_noise_exists | True | info | outputs\tables\phase16_noise_stress.csv | 60 | loaded |
| phase16_small_sample_exists | True | info | outputs\tables\phase16_small_sample_training.csv | 75 | loaded |
| phase16_degradation_exists | True | info | outputs\tables\phase16_degradation_summary.csv | 9 | loaded |
| phase17_summary_exists | True | info | outputs\tables\phase17_combined_stratified_summary.csv | 36 | loaded |
| phase14_main_model_statistical_tests.csv_exists | True | info | outputs\tables\phase14_main_model_statistical_tests.csv | 18 | loaded |
| phase14_feature_ablation_statistical_tests.csv_exists | True | info | outputs\tables\phase14_feature_ablation_statistical_tests.csv | 12 | loaded |
| phase14_robustness_statistical_tests.csv_exists | True | info | outputs\tables\phase14_robustness_statistical_tests.csv | 30 | loaded |
| phase14_stratified_statistical_tests.csv_exists | True | info | outputs\tables\phase14_stratified_statistical_tests.csv | 12 | loaded |
| phase14_final_mean_std_summary.csv_exists | True | info | outputs\tables\phase14_final_mean_std_summary.csv | 36 | loaded |
| phase14_final_effect_size_summary.csv_exists | True | info | outputs\tables\phase14_final_effect_size_summary.csv | 72 | loaded |
| phase13_finite | True | critical | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv | 105 | all numeric values finite |
| phase13_duplicates | True | critical | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv | 105 | no duplicate full rows |
| phase15_finite | True | critical | outputs\tables\phase15_feature_ablation_metrics.csv | 75 | all numeric values finite |
| phase15_duplicates | True | critical | outputs\tables\phase15_feature_ablation_metrics.csv | 75 | no duplicate full rows |
| phase16_missingness_finite | True | critical | outputs\tables\phase16_missingness_stress.csv | 60 | all numeric values finite |
| phase16_missingness_duplicates | True | critical | outputs\tables\phase16_missingness_stress.csv | 60 | no duplicate full rows |
| phase16_noise_finite | True | critical | outputs\tables\phase16_noise_stress.csv | 60 | all numeric values finite |
| phase16_noise_duplicates | True | critical | outputs\tables\phase16_noise_stress.csv | 60 | no duplicate full rows |
| phase16_small_sample_finite | True | critical | outputs\tables\phase16_small_sample_training.csv | 75 | all numeric values finite |
| phase16_small_sample_duplicates | True | critical | outputs\tables\phase16_small_sample_training.csv | 75 | no duplicate full rows |
| phase16_degradation_finite | True | critical | outputs\tables\phase16_degradation_summary.csv | 9 | all numeric values finite |
| phase16_degradation_duplicates | True | critical | outputs\tables\phase16_degradation_summary.csv | 9 | no duplicate full rows |
| phase17_summary_finite | True | critical | outputs\tables\phase17_combined_stratified_summary.csv | 36 | all numeric values finite |
| phase17_summary_duplicates | True | critical | outputs\tables\phase17_combined_stratified_summary.csv | 36 | no duplicate full rows |
| phase14_main_model_statistical_tests.csv_finite | True | critical | outputs\tables\phase14_main_model_statistical_tests.csv | 18 | all numeric values finite |
| phase14_main_model_statistical_tests.csv_duplicates | True | critical | outputs\tables\phase14_main_model_statistical_tests.csv | 18 | no duplicate full rows |
| phase14_feature_ablation_statistical_tests.csv_finite | True | critical | outputs\tables\phase14_feature_ablation_statistical_tests.csv | 12 | all numeric values finite |
| phase14_feature_ablation_statistical_tests.csv_duplicates | True | critical | outputs\tables\phase14_feature_ablation_statistical_tests.csv | 12 | no duplicate full rows |
| phase14_robustness_statistical_tests.csv_finite | True | critical | outputs\tables\phase14_robustness_statistical_tests.csv | 30 | all numeric values finite |
| phase14_robustness_statistical_tests.csv_duplicates | True | critical | outputs\tables\phase14_robustness_statistical_tests.csv | 30 | no duplicate full rows |
| phase14_stratified_statistical_tests.csv_finite | True | critical | outputs\tables\phase14_stratified_statistical_tests.csv | 12 | all numeric values finite |
| phase14_stratified_statistical_tests.csv_duplicates | True | critical | outputs\tables\phase14_stratified_statistical_tests.csv | 12 | no duplicate full rows |
| phase14_final_mean_std_summary.csv_finite | True | critical | outputs\tables\phase14_final_mean_std_summary.csv | 36 | all numeric values finite |
| phase14_final_mean_std_summary.csv_duplicates | True | critical | outputs\tables\phase14_final_mean_std_summary.csv | 36 | no duplicate full rows |
| phase14_final_effect_size_summary.csv_finite | True | critical | outputs\tables\phase14_final_effect_size_summary.csv | 72 | all numeric values finite |
| phase14_final_effect_size_summary.csv_duplicates | True | critical | outputs\tables\phase14_final_effect_size_summary.csv | 72 | no duplicate full rows |
| figure2_models | True | critical | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv | 105 | found=['GRU', 'HA', 'Persistence', 'ST-Transformer-lite', 'SeasonalHA', 'TCN', 'XGBoost'] |
| figure2_horizons | True | critical | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv |  | [1, 3, 6] |
| figure3_seeds | True | critical | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv |  | [42, 2024, 2025, 2026, 3407] |
| phase13_node_count | True | critical | outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv |  | [np.int64(51)] |
| figure4_feature_groups | True | critical | outputs\tables\phase15_feature_ablation_metrics.csv |  | found=['full_features', 'speed_only', 'speed_reliability', 'speed_time', 'speed_volatility'] |
| phase15_horizons | True | critical |  |  | [1, 3, 6] |
| phase15_seeds | True | critical |  |  | [42, 2024, 2025, 2026, 3407] |
| phase15_node_count | True | critical |  |  | [np.int64(51)] |
| figure7_missingness_reference | True | critical |  |  | 0% missingness reference must equal zero |
| figure7_noise_reference | True | critical |  |  | clean noise reference must equal zero |
| figure7_small_sample_reference | True | critical |  |  | 100% training reference must equal zero |
| degradation_maximum_observed | True | critical |  |  | verified |
| table3_statistics_columns | True | critical |  |  | missing p/effect columns |
| table3_mean_std_columns | True | critical |  |  | missing mean/std columns |
| table4_sources | True | critical |  |  | Table 4 needs ablation, robustness, and stratified summary sources |
| standardized_terms_registry | True | info |  |  | ST-Transformer-lite; SeasonalHA; Persistence; speed_only; speed_time; speed_reliability; speed_volatility; full_features; missingness stress; noise stress; small-sample training; reliability stratification; coverage stratification; volatility stratification; traffic-state stratification |
