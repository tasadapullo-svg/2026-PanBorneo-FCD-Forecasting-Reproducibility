# Applied Intelligence 7-Figure / 4-Table Readiness Report

**Overall status: READY**
**Final decision: READY_FOR_PLOTTING_AND_WRITING**

This audit did not train models and did not modify Phase 13-22 experimental outputs. METR-LA-mini supplementary results are kept separate from Pan Borneo main figures/tables.

## Overall conclusion

- 7-figure / 4-table structure status: READY
- Critical errors: 0
- Warnings: 0

## Figure-by-figure diagnosis

### Figure1: READY
- Purpose: Study corridor, sparse FCD source, and leakage-controlled forecasting workflow.
- Detected source files: data\raw\package_extracted\03_nodes\nodes.csv, data\raw\package_extracted\06_audit\coverage_by_granularity.csv, outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv, outputs\plot_data\Fig01_workflow_data.csv, outputs\tables\data_inventory.csv, outputs\tables\train_val_test_split_summary.csv
- Missing files: None
- Missing columns: None
- Row count check: See checks
- Critical checks: 13 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Figure2: READY
- Purpose: Forecasting performance against statistical, ML, and deep baselines.
- Detected source files: outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv, outputs\tables\phase14_main_model_statistical_tests.csv
- Missing files: None
- Missing columns: None
- Row count check: metrics_rows=105 expected=105; parquet_checked=105
- Critical checks: 435 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Figure3: READY
- Purpose: Five-seed stability and paired improvement consistency.
- Detected source files: outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv, outputs\manuscript_package\phase19_applied_intelligence\figures\Figure2_strong_baseline_mean_std.csv
- Missing files: None
- Missing columns: None
- Row count check: seed_level_rows=105 expected=105
- Critical checks: 8 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Figure4: READY
- Purpose: Feature ablation of temporal, reliability, and volatility-aware groups.
- Detected source files: outputs\tables\phase14_feature_ablation_statistical_tests.csv, outputs\tables\phase15_feature_ablation_metrics.csv
- Missing files: None
- Missing columns: None
- Row count check: phase15_rows=75 expected=75; parquet_checked=75
- Critical checks: 311 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Figure5: READY
- Purpose: Stratified forecasting error under reliability, coverage, volatility, and traffic-state regimes.
- Detected source files: outputs\final_plot_table_data\main_figures\Fig05_stratified_error.csv, outputs\tables\phase14_stratified_statistical_tests.csv, outputs\tables\phase17_coverage_stratified_metrics.csv, outputs\tables\phase17_reliability_stratified_metrics.csv, outputs\tables\phase17_traffic_state_stratified_metrics.csv, outputs\tables\phase17_volatility_stratified_metrics.csv
- Missing files: None
- Missing columns: None
- Row count check: phase17_stratified_rows=180 expected=180
- Critical checks: 29 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Figure6: READY
- Purpose: Error heterogeneity explained by data-quality and traffic-dynamics regimes.
- Detected source files: outputs\final_result_diagnosis\final_stratified_interpretation.csv, outputs\tables\phase17_combined_stratified_summary.csv
- Missing files: None
- Missing columns: None
- Row count check: combined_stratified_summary_rows=36 raw strata rows; expected 36 raw or 12 derived best/worst rows
- Critical checks: 7 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Figure7: READY
- Purpose: Robustness under missingness, observation noise, and limited training data.
- Detected source files: outputs\tables\phase14_robustness_statistical_tests.csv, outputs\tables\phase16_degradation_summary.csv, outputs\tables\phase16_missingness_stress.csv, outputs\tables\phase16_noise_stress.csv, outputs\tables\phase16_small_sample_training.csv
- Missing files: None
- Missing columns: None
- Row count check: See checks
- Critical checks: 20 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

## Table-by-table diagnosis

### Table1: READY
- Purpose: Dataset audit and experimental design.
- Detected source files: data\raw\package_extracted\03_nodes\nodes.csv, data\raw\package_extracted\06_audit\coverage_by_granularity.csv, outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv, outputs\plot_data\Fig01_workflow_data.csv, outputs\tables\data_inventory.csv, outputs\tables\train_val_test_split_summary.csv
- Missing files: None
- Missing columns: None
- Row count check: See checks
- Critical checks: 13 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Table2: READY
- Purpose: Model settings and hyperparameters.
- Detected source files: outputs\final_plot_table_data\main_tables\Table02_model_settings.csv
- Missing files: None
- Missing columns: None
- Row count check: See checks
- Critical checks: 3 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Table3: READY
- Purpose: Main performance statistics.
- Detected source files: outputs\locked\phase13_full\tables\phase13_strong_baseline_metrics.csv, outputs\tables\phase14_final_mean_std_summary.csv, outputs\tables\phase14_main_model_statistical_tests.csv
- Missing files: None
- Missing columns: None
- Row count check: See checks
- Critical checks: 437 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

### Table4: READY
- Purpose: Ablation, robustness, and stratified summary.
- Detected source files: outputs\final_plot_table_data\main_figures\Fig05_stratified_error.csv, outputs\final_plot_table_data\main_tables\Table04_ablation_robustness_stratified_summary.csv, outputs\final_result_diagnosis\final_stratified_interpretation.csv, outputs\tables\phase14_feature_ablation_statistical_tests.csv, outputs\tables\phase14_robustness_statistical_tests.csv, outputs\tables\phase14_stratified_statistical_tests.csv, outputs\tables\phase15_feature_ablation_metrics.csv, outputs\tables\phase16_degradation_summary.csv, outputs\tables\phase16_missingness_stress.csv, outputs\tables\phase16_noise_stress.csv, outputs\tables\phase16_small_sample_training.csv, outputs\tables\phase17_combined_stratified_summary.csv, outputs\tables\phase17_coverage_stratified_metrics.csv, outputs\tables\phase17_reliability_stratified_metrics.csv, outputs\tables\phase17_traffic_state_stratified_metrics.csv, outputs\tables\phase17_volatility_stratified_metrics.csv
- Missing files: None
- Missing columns: None
- Row count check: See checks
- Critical checks: 369 passed/logged
- Critical errors: None
- Warnings: None
- Recommended action: No fix required.

## Applied Intelligence logic check

- Does Figure 1 establish a real-world sparse FCD problem? Yes
- Does Figure 2 provide strong baseline comparison? Yes
- Does Figure 3 support multi-seed stability? Yes
- Does Figure 4 support feature/mechanism interpretation? Yes
- Does Figure 5 support reliability-aware stratified diagnosis? Yes
- Does Figure 6 summarize error heterogeneity? Yes
- Does Figure 7 support robustness under missingness/noise/small-sample settings? Yes
- Does Table 3 support the main statistical claim? Yes

## Critical errors

- None.

## Warnings

- None.

## Recommended fix plan

- See outputs/applied_intelligence_readiness_audit/recommended_fix_plan.csv for exact file-level actions.

## Final decision

READY_FOR_PLOTTING_AND_WRITING
