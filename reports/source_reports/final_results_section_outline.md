# Final Results Section Outline

## 4.1 Data Audit and Forecasting-Window Feasibility
Report audit and leakage-free window construction.

## 4.2 Strong Baseline Performance
Present SeasonalHistoricalAverage as the strong comparator.

## 4.3 Controlled Deep Learning Performance
State that deep models improve 1h, 3h and 6h, but do not dominate all horizons.

## 4.4 Feature Ablation
State that TCN speed-only is strongest for direct forecasting. Reliability indicators are diagnostic.

## 4.5 History-Length Sensitivity
State that the best history length is horizon-dependent.

## 4.6 Robustness and Difficult-Sample Diagnosis
State that high volatility is the main difficult-sample source.

## 4.7 Repeated-Seed Stability
Use Phase 9B five-seed results if available; otherwise use Phase 9 three-seed results. Claim that all seeds outperform SeasonalHistoricalAverage only if the table flag is true.

## 4.8 Summary of Empirical Findings
Summarize the reproducible workflow, short/medium-horizon TCN speed-only advantage, diagnostic role of reliability indicators, horizon-dependent memory, and Phase 10 status.

## Appendix: Supplementary Public Benchmark Sanity Check
If Phase 10 outputs exist, report METR-LA-mini as a supplementary sanity check only. State that TCN speed-only completed five-seed runs and outperformed HistoricalAverage, but did not outperform Persistence. Do not claim SOTA or benchmark dominance.
