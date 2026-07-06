# Final Figure Plan

No image files are generated in Phase 11. This is a plotting plan only.

## Fig. 1 Overall experimental workflow
- Source CSV file: `outputs/tables/final_phase_status_summary.csv`
- Variables to plot: phase, experiment_name, status, main_scope
- Expected message: complete reproducible workflow from audit to stability testing.
- Placement: main text

## Fig. 2 Data coverage and window feasibility
- Source CSV file: `outputs/tables/coverage_by_point.csv`, `outputs/tables/window_feasibility_by_horizon.csv`
- Variables to plot: coverage ratio and feasible window counts
- Expected message: main horizons are feasible; 168h horizon is a stress test.
- Placement: main text or appendix

## Fig. 3 Baseline vs deep model performance
- Source CSV file: `outputs/tables/final_main_forecasting_results.csv`
- Variables to plot: model, horizon_hours, MAE, improvement_percent_vs_seasonal
- Expected message: deep models improve 1h/3h/6h but not 12h/24h.
- Placement: main text

## Fig. 4 Feature ablation results
- Source CSV file: `outputs/tables/final_ablation_summary.csv`
- Variables to plot: ablation_group, MAE
- Expected message: speed-only is strongest overall.
- Placement: main text

## Fig. 5 History-length sensitivity
- Source CSV file: `outputs/tables/final_history_sensitivity_summary.csv`
- Variables to plot: history_hours, horizon_hours, MAE
- Expected message: optimal memory length is horizon-dependent.
- Placement: main text

## Fig. 6 Volatility-stratified prediction error
- Source CSV file: `outputs/tables/phase8_error_by_volatility.csv`
- Variables to plot: horizon_hours, volatility_bin, MAE
- Expected message: high-volatility windows are the dominant difficult cases.
- Placement: main text

## Fig. 7 Robustness under missingness, noise, and limited training samples
- Panel 7(a) source CSV file: `outputs/plot_data/Fig07_missingness_stress_data.csv`
- Panel 7(b) source CSV file: `outputs/plot_data/Fig07_noise_stress_data.csv`
- Panel 7(c) source CSV file: `outputs/plot_data/Fig07_small_sample_training_data.csv`
- Panel 7(d) source CSV file: `outputs/plot_data/Fig07_degradation_summary_data.csv`
- Variables to plot: perturbation level, training data used percent, horizon_hours, MAE, MAE standard deviation, worst-case MAE increase percent
- Expected message: robustness is assessed across input missingness, input noise, and chronologically limited training samples.
- Placement: main text

## Fig. 8 Repeated-seed stability
- Source CSV file: `outputs/tables/final_seed_stability_summary.csv`
- Variables to plot: horizon_hours, MAE_mean, MAE_std
- Expected message: seed-stability conclusion uses Phase 9B five-seed results when available.
- Placement: main text

## Fig. 9 Supplementary public benchmark sanity check
- Source CSV file: `outputs/tables/final_public_benchmark_summary.csv`
- Variables to plot: dataset, MAE_mean, MAE_std, outperforms_historical_average_all_seeds, outperforms_persistence_all_seeds
- Expected message: the TCN speed-only pipeline runs on public traffic data, but this is portability evidence rather than public benchmark superiority.
- Placement: appendix or supplementary material
