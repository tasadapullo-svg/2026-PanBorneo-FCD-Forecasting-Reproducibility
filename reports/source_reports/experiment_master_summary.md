# Experiment Master Summary

## Scope
This summary consolidates the locked Pan Borneo FCD forecasting experiment. Phase 10 is treated as a supplementary public benchmark sanity check only.

## Main Findings
- The 1h panel and leakage-free windows support short/medium-horizon forecasting.
- SeasonalHistoricalAverage is a strong periodic baseline.
- Deep models improve 1h, 3h and 6h horizons, but not 12h and 24h.
- TCN speed-only is the strongest direct forecasting configuration.
- Reliability indicators are useful for diagnosis and robustness interpretation, not direct accuracy improvement in this high-coverage dataset.
- Optimal history length is horizon-dependent.
- High volatility is the main difficult-sample source.

## Seed Stability
The seed-stability summary uses Phase 9B results with 5 seeds.
All seeds outperform SeasonalHistoricalAverage for every core horizon: True.
- 1h horizon, 72h history: MAE_mean=0.9776, MAE_std=0.0760, MAE_cv=0.0777, all seeds outperform seasonal=True.
- 3h horizon, 168h history: MAE_mean=0.9372, MAE_std=0.0580, MAE_cv=0.0619, all seeds outperform seasonal=True.
- 6h horizon, 24h history: MAE_mean=0.8677, MAE_std=0.0389, MAE_cv=0.0448, all seeds outperform seasonal=True.

## Phase 10 Status
Phase 10 completed as a supplementary public benchmark sanity check on METR-LA-mini with 5 seeds. TCN speed-only achieved MAE_mean=3.4183, MAE_std=0.5222, and MAE_cv=0.1528. It outperformed HistoricalAverage for all seeds (True) but did not outperform Persistence for all seeds (False). This supports pipeline portability, not public benchmark superiority.
