# Phase 20 METR-LA-mini Validation Report

**Status: PASS**

## Failures

- None.

## Checks

| Check | Passed | Detail |
| --- | --- | --- |
| TableS1_exists | True | D:\2026_PD\outputs\supplementary_metr_la_mini\TableS1_metr_la_mini_results.csv |
| FigS1_exists | True | D:\2026_PD\outputs\supplementary_metr_la_mini\FigS1_metr_la_mini_sanity.csv |
| prediction_dir_exists | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions |
| required_columns | True | missing=[] |
| row_count | True | rows=75 expected=75 |
| models | True | ['HA', 'Persistence', 'Proposed', 'ST-Transformer-lite', 'TCN'] |
| horizons | True | [1, 3, 6] |
| seeds | True | [42, 2024, 2025, 2026, 3407] |
| sensor_count | True | [np.int64(50)] |
| finite_metrics | True | numeric NaN/inf |
| unique_keys | True | duplicate model/horizon/seed |
| prediction_file_count | True | count=75 expected=75 |
| prediction_exists:HA:h1:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h1_seed42.parquet |
| prediction_columns:HA_h1_seed42.parquet | True | missing=[] |
| prediction_nonempty:HA_h1_seed42.parquet | True | rows=20200 |
| test_n:HA_h1_seed42.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:HA_h1_seed42.parquet | True | NaN/inf |
| mae_match:HA_h1_seed42.parquet | True | metrics=5.591034898474665 computed=5.591034898474665 |
| rmse_match:HA_h1_seed42.parquet | True | metrics=9.491157885122748 computed=9.491157885122748 |
| same_samples_h1:HA_h1_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h1:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h1_seed42.parquet |
| prediction_columns:Persistence_h1_seed42.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h1_seed42.parquet | True | rows=20200 |
| test_n:Persistence_h1_seed42.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Persistence_h1_seed42.parquet | True | NaN/inf |
| mae_match:Persistence_h1_seed42.parquet | True | metrics=3.213089498010012 computed=3.213089498010012 |
| rmse_match:Persistence_h1_seed42.parquet | True | metrics=6.806321891697 computed=6.806321891697 |
| same_samples_h1:Persistence_h1_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h1:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h1_seed42.parquet |
| prediction_columns:TCN_h1_seed42.parquet | True | missing=[] |
| prediction_nonempty:TCN_h1_seed42.parquet | True | rows=20200 |
| test_n:TCN_h1_seed42.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:TCN_h1_seed42.parquet | True | NaN/inf |
| mae_match:TCN_h1_seed42.parquet | True | metrics=2.8168352868297317 computed=2.8168352868297313 |
| rmse_match:TCN_h1_seed42.parquet | True | metrics=5.446140897004612 computed=5.446140897004612 |
| same_samples_h1:TCN_h1_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h1:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h1_seed42.parquet |
| prediction_columns:ST-Transformer-lite_h1_seed42.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h1_seed42.parquet | True | rows=20200 |
| test_n:ST-Transformer-lite_h1_seed42.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:ST-Transformer-lite_h1_seed42.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h1_seed42.parquet | True | metrics=3.298271263519136 computed=3.298271263519136 |
| rmse_match:ST-Transformer-lite_h1_seed42.parquet | True | metrics=6.380231568026823 computed=6.380231568026823 |
| same_samples_h1:ST-Transformer-lite_h1_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h1:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h1_seed42.parquet |
| prediction_columns:Proposed_h1_seed42.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h1_seed42.parquet | True | rows=20200 |
| test_n:Proposed_h1_seed42.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Proposed_h1_seed42.parquet | True | NaN/inf |
| mae_match:Proposed_h1_seed42.parquet | True | metrics=2.8168352868297317 computed=2.8168352868297313 |
| rmse_match:Proposed_h1_seed42.parquet | True | metrics=5.446140897004612 computed=5.446140897004612 |
| same_samples_h1:Proposed_h1_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h1:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h1_seed2024.parquet |
| prediction_columns:HA_h1_seed2024.parquet | True | missing=[] |
| prediction_nonempty:HA_h1_seed2024.parquet | True | rows=20200 |
| test_n:HA_h1_seed2024.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:HA_h1_seed2024.parquet | True | NaN/inf |
| mae_match:HA_h1_seed2024.parquet | True | metrics=5.591034898474665 computed=5.591034898474665 |
| rmse_match:HA_h1_seed2024.parquet | True | metrics=9.491157885122748 computed=9.491157885122748 |
| same_samples_h1:HA_h1_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h1:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h1_seed2024.parquet |
| prediction_columns:Persistence_h1_seed2024.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h1_seed2024.parquet | True | rows=20200 |
| test_n:Persistence_h1_seed2024.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Persistence_h1_seed2024.parquet | True | NaN/inf |
| mae_match:Persistence_h1_seed2024.parquet | True | metrics=3.213089498010012 computed=3.213089498010012 |
| rmse_match:Persistence_h1_seed2024.parquet | True | metrics=6.806321891697 computed=6.806321891697 |
| same_samples_h1:Persistence_h1_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h1:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h1_seed2024.parquet |
| prediction_columns:TCN_h1_seed2024.parquet | True | missing=[] |
| prediction_nonempty:TCN_h1_seed2024.parquet | True | rows=20200 |
| test_n:TCN_h1_seed2024.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:TCN_h1_seed2024.parquet | True | NaN/inf |
| mae_match:TCN_h1_seed2024.parquet | True | metrics=2.805095630400252 computed=2.8050956304002517 |
| rmse_match:TCN_h1_seed2024.parquet | True | metrics=5.460543079889218 computed=5.460543079889218 |
| same_samples_h1:TCN_h1_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h1:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h1_seed2024.parquet |
| prediction_columns:ST-Transformer-lite_h1_seed2024.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h1_seed2024.parquet | True | rows=20200 |
| test_n:ST-Transformer-lite_h1_seed2024.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:ST-Transformer-lite_h1_seed2024.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h1_seed2024.parquet | True | metrics=2.894165266339141 computed=2.8941652663391415 |
| rmse_match:ST-Transformer-lite_h1_seed2024.parquet | True | metrics=5.576408528954538 computed=5.576408528954538 |
| same_samples_h1:ST-Transformer-lite_h1_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h1:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h1_seed2024.parquet |
| prediction_columns:Proposed_h1_seed2024.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h1_seed2024.parquet | True | rows=20200 |
| test_n:Proposed_h1_seed2024.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Proposed_h1_seed2024.parquet | True | NaN/inf |
| mae_match:Proposed_h1_seed2024.parquet | True | metrics=2.805095630400252 computed=2.8050956304002517 |
| rmse_match:Proposed_h1_seed2024.parquet | True | metrics=5.460543079889218 computed=5.460543079889218 |
| same_samples_h1:Proposed_h1_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h1:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h1_seed2025.parquet |
| prediction_columns:HA_h1_seed2025.parquet | True | missing=[] |
| prediction_nonempty:HA_h1_seed2025.parquet | True | rows=20200 |
| test_n:HA_h1_seed2025.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:HA_h1_seed2025.parquet | True | NaN/inf |
| mae_match:HA_h1_seed2025.parquet | True | metrics=5.591034898474665 computed=5.591034898474665 |
| rmse_match:HA_h1_seed2025.parquet | True | metrics=9.491157885122748 computed=9.491157885122748 |
| same_samples_h1:HA_h1_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h1:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h1_seed2025.parquet |
| prediction_columns:Persistence_h1_seed2025.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h1_seed2025.parquet | True | rows=20200 |
| test_n:Persistence_h1_seed2025.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Persistence_h1_seed2025.parquet | True | NaN/inf |
| mae_match:Persistence_h1_seed2025.parquet | True | metrics=3.213089498010012 computed=3.213089498010012 |
| rmse_match:Persistence_h1_seed2025.parquet | True | metrics=6.806321891697 computed=6.806321891697 |
| same_samples_h1:Persistence_h1_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h1:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h1_seed2025.parquet |
| prediction_columns:TCN_h1_seed2025.parquet | True | missing=[] |
| prediction_nonempty:TCN_h1_seed2025.parquet | True | rows=20200 |
| test_n:TCN_h1_seed2025.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:TCN_h1_seed2025.parquet | True | NaN/inf |
| mae_match:TCN_h1_seed2025.parquet | True | metrics=2.7905283193304986 computed=2.7905283193304986 |
| rmse_match:TCN_h1_seed2025.parquet | True | metrics=5.457044678061667 computed=5.457044678061667 |
| same_samples_h1:TCN_h1_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h1:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h1_seed2025.parquet |
| prediction_columns:ST-Transformer-lite_h1_seed2025.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h1_seed2025.parquet | True | rows=20200 |
| test_n:ST-Transformer-lite_h1_seed2025.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:ST-Transformer-lite_h1_seed2025.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h1_seed2025.parquet | True | metrics=2.8849653457414988 computed=2.8849653457414988 |
| rmse_match:ST-Transformer-lite_h1_seed2025.parquet | True | metrics=5.564767327635426 computed=5.564767327635426 |
| same_samples_h1:ST-Transformer-lite_h1_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h1:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h1_seed2025.parquet |
| prediction_columns:Proposed_h1_seed2025.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h1_seed2025.parquet | True | rows=20200 |
| test_n:Proposed_h1_seed2025.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Proposed_h1_seed2025.parquet | True | NaN/inf |
| mae_match:Proposed_h1_seed2025.parquet | True | metrics=2.7905283193304986 computed=2.7905283193304986 |
| rmse_match:Proposed_h1_seed2025.parquet | True | metrics=5.457044678061667 computed=5.457044678061667 |
| same_samples_h1:Proposed_h1_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h1:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h1_seed2026.parquet |
| prediction_columns:HA_h1_seed2026.parquet | True | missing=[] |
| prediction_nonempty:HA_h1_seed2026.parquet | True | rows=20200 |
| test_n:HA_h1_seed2026.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:HA_h1_seed2026.parquet | True | NaN/inf |
| mae_match:HA_h1_seed2026.parquet | True | metrics=5.591034898474665 computed=5.591034898474665 |
| rmse_match:HA_h1_seed2026.parquet | True | metrics=9.491157885122748 computed=9.491157885122748 |
| same_samples_h1:HA_h1_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h1:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h1_seed2026.parquet |
| prediction_columns:Persistence_h1_seed2026.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h1_seed2026.parquet | True | rows=20200 |
| test_n:Persistence_h1_seed2026.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Persistence_h1_seed2026.parquet | True | NaN/inf |
| mae_match:Persistence_h1_seed2026.parquet | True | metrics=3.213089498010012 computed=3.213089498010012 |
| rmse_match:Persistence_h1_seed2026.parquet | True | metrics=6.806321891697 computed=6.806321891697 |
| same_samples_h1:Persistence_h1_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h1:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h1_seed2026.parquet |
| prediction_columns:TCN_h1_seed2026.parquet | True | missing=[] |
| prediction_nonempty:TCN_h1_seed2026.parquet | True | rows=20200 |
| test_n:TCN_h1_seed2026.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:TCN_h1_seed2026.parquet | True | NaN/inf |
| mae_match:TCN_h1_seed2026.parquet | True | metrics=2.8192962060116304 computed=2.8192962060116304 |
| rmse_match:TCN_h1_seed2026.parquet | True | metrics=5.454106189996587 computed=5.454106189996587 |
| same_samples_h1:TCN_h1_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h1:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h1_seed2026.parquet |
| prediction_columns:ST-Transformer-lite_h1_seed2026.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h1_seed2026.parquet | True | rows=20200 |
| test_n:ST-Transformer-lite_h1_seed2026.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:ST-Transformer-lite_h1_seed2026.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h1_seed2026.parquet | True | metrics=2.9282079025306325 computed=2.9282079025306325 |
| rmse_match:ST-Transformer-lite_h1_seed2026.parquet | True | metrics=5.534700342029477 computed=5.534700342029477 |
| same_samples_h1:ST-Transformer-lite_h1_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h1:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h1_seed2026.parquet |
| prediction_columns:Proposed_h1_seed2026.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h1_seed2026.parquet | True | rows=20200 |
| test_n:Proposed_h1_seed2026.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Proposed_h1_seed2026.parquet | True | NaN/inf |
| mae_match:Proposed_h1_seed2026.parquet | True | metrics=2.8192962060116304 computed=2.8192962060116304 |
| rmse_match:Proposed_h1_seed2026.parquet | True | metrics=5.454106189996587 computed=5.454106189996587 |
| same_samples_h1:Proposed_h1_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h1:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h1_seed3407.parquet |
| prediction_columns:HA_h1_seed3407.parquet | True | missing=[] |
| prediction_nonempty:HA_h1_seed3407.parquet | True | rows=20200 |
| test_n:HA_h1_seed3407.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:HA_h1_seed3407.parquet | True | NaN/inf |
| mae_match:HA_h1_seed3407.parquet | True | metrics=5.591034898474665 computed=5.591034898474665 |
| rmse_match:HA_h1_seed3407.parquet | True | metrics=9.491157885122748 computed=9.491157885122748 |
| same_samples_h1:HA_h1_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h1:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h1_seed3407.parquet |
| prediction_columns:Persistence_h1_seed3407.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h1_seed3407.parquet | True | rows=20200 |
| test_n:Persistence_h1_seed3407.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Persistence_h1_seed3407.parquet | True | NaN/inf |
| mae_match:Persistence_h1_seed3407.parquet | True | metrics=3.213089498010012 computed=3.213089498010012 |
| rmse_match:Persistence_h1_seed3407.parquet | True | metrics=6.806321891697 computed=6.806321891697 |
| same_samples_h1:Persistence_h1_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h1:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h1_seed3407.parquet |
| prediction_columns:TCN_h1_seed3407.parquet | True | missing=[] |
| prediction_nonempty:TCN_h1_seed3407.parquet | True | rows=20200 |
| test_n:TCN_h1_seed3407.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:TCN_h1_seed3407.parquet | True | NaN/inf |
| mae_match:TCN_h1_seed3407.parquet | True | metrics=2.8239175165761816 computed=2.8239175165761816 |
| rmse_match:TCN_h1_seed3407.parquet | True | metrics=5.419658530023569 computed=5.419658530023569 |
| same_samples_h1:TCN_h1_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h1:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h1_seed3407.parquet |
| prediction_columns:ST-Transformer-lite_h1_seed3407.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h1_seed3407.parquet | True | rows=20200 |
| test_n:ST-Transformer-lite_h1_seed3407.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:ST-Transformer-lite_h1_seed3407.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h1_seed3407.parquet | True | metrics=3.0637050030019024 computed=3.0637050030019024 |
| rmse_match:ST-Transformer-lite_h1_seed3407.parquet | True | metrics=5.759431838285415 computed=5.759431838285415 |
| same_samples_h1:ST-Transformer-lite_h1_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h1:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h1_seed3407.parquet |
| prediction_columns:Proposed_h1_seed3407.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h1_seed3407.parquet | True | rows=20200 |
| test_n:Proposed_h1_seed3407.parquet | True | metrics=20200 parquet=20200 |
| prediction_finite:Proposed_h1_seed3407.parquet | True | NaN/inf |
| mae_match:Proposed_h1_seed3407.parquet | True | metrics=2.8239175165761816 computed=2.8239175165761816 |
| rmse_match:Proposed_h1_seed3407.parquet | True | metrics=5.419658530023569 computed=5.419658530023569 |
| same_samples_h1:Proposed_h1_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h3:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h3_seed42.parquet |
| prediction_columns:HA_h3_seed42.parquet | True | missing=[] |
| prediction_nonempty:HA_h3_seed42.parquet | True | rows=20100 |
| test_n:HA_h3_seed42.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:HA_h3_seed42.parquet | True | NaN/inf |
| mae_match:HA_h3_seed42.parquet | True | metrics=5.595527209950917 computed=5.595527209950917 |
| rmse_match:HA_h3_seed42.parquet | True | metrics=9.503428974581972 computed=9.503428974581972 |
| same_samples_h3:HA_h3_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h3:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h3_seed42.parquet |
| prediction_columns:Persistence_h3_seed42.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h3_seed42.parquet | True | rows=20100 |
| test_n:Persistence_h3_seed42.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Persistence_h3_seed42.parquet | True | NaN/inf |
| mae_match:Persistence_h3_seed42.parquet | True | metrics=6.3192616467452165 computed=6.3192616467452165 |
| rmse_match:Persistence_h3_seed42.parquet | True | metrics=11.74912940588088 computed=11.74912940588088 |
| same_samples_h3:Persistence_h3_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h3:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h3_seed42.parquet |
| prediction_columns:TCN_h3_seed42.parquet | True | missing=[] |
| prediction_nonempty:TCN_h3_seed42.parquet | True | rows=20100 |
| test_n:TCN_h3_seed42.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:TCN_h3_seed42.parquet | True | NaN/inf |
| mae_match:TCN_h3_seed42.parquet | True | metrics=4.155731150404137 computed=4.155731150404137 |
| rmse_match:TCN_h3_seed42.parquet | True | metrics=7.496425351193922 computed=7.496425351193922 |
| same_samples_h3:TCN_h3_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h3:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h3_seed42.parquet |
| prediction_columns:ST-Transformer-lite_h3_seed42.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h3_seed42.parquet | True | rows=20100 |
| test_n:ST-Transformer-lite_h3_seed42.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:ST-Transformer-lite_h3_seed42.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h3_seed42.parquet | True | metrics=5.354900963342012 computed=5.354900963342012 |
| rmse_match:ST-Transformer-lite_h3_seed42.parquet | True | metrics=9.161225189156148 computed=9.161225189156148 |
| same_samples_h3:ST-Transformer-lite_h3_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h3:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h3_seed42.parquet |
| prediction_columns:Proposed_h3_seed42.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h3_seed42.parquet | True | rows=20100 |
| test_n:Proposed_h3_seed42.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Proposed_h3_seed42.parquet | True | NaN/inf |
| mae_match:Proposed_h3_seed42.parquet | True | metrics=4.155731150404137 computed=4.155731150404137 |
| rmse_match:Proposed_h3_seed42.parquet | True | metrics=7.496425351193922 computed=7.496425351193922 |
| same_samples_h3:Proposed_h3_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h3:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h3_seed2024.parquet |
| prediction_columns:HA_h3_seed2024.parquet | True | missing=[] |
| prediction_nonempty:HA_h3_seed2024.parquet | True | rows=20100 |
| test_n:HA_h3_seed2024.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:HA_h3_seed2024.parquet | True | NaN/inf |
| mae_match:HA_h3_seed2024.parquet | True | metrics=5.595527209950917 computed=5.595527209950917 |
| rmse_match:HA_h3_seed2024.parquet | True | metrics=9.503428974581972 computed=9.503428974581972 |
| same_samples_h3:HA_h3_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h3:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h3_seed2024.parquet |
| prediction_columns:Persistence_h3_seed2024.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h3_seed2024.parquet | True | rows=20100 |
| test_n:Persistence_h3_seed2024.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Persistence_h3_seed2024.parquet | True | NaN/inf |
| mae_match:Persistence_h3_seed2024.parquet | True | metrics=6.3192616467452165 computed=6.3192616467452165 |
| rmse_match:Persistence_h3_seed2024.parquet | True | metrics=11.74912940588088 computed=11.74912940588088 |
| same_samples_h3:Persistence_h3_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h3:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h3_seed2024.parquet |
| prediction_columns:TCN_h3_seed2024.parquet | True | missing=[] |
| prediction_nonempty:TCN_h3_seed2024.parquet | True | rows=20100 |
| test_n:TCN_h3_seed2024.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:TCN_h3_seed2024.parquet | True | NaN/inf |
| mae_match:TCN_h3_seed2024.parquet | True | metrics=4.030911698887004 computed=4.030911698887004 |
| rmse_match:TCN_h3_seed2024.parquet | True | metrics=7.269958364476932 computed=7.269958364476932 |
| same_samples_h3:TCN_h3_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h3:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h3_seed2024.parquet |
| prediction_columns:ST-Transformer-lite_h3_seed2024.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h3_seed2024.parquet | True | rows=20100 |
| test_n:ST-Transformer-lite_h3_seed2024.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:ST-Transformer-lite_h3_seed2024.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h3_seed2024.parquet | True | metrics=3.976348729774133 computed=3.9763487297741333 |
| rmse_match:ST-Transformer-lite_h3_seed2024.parquet | True | metrics=7.242463580068443 computed=7.242463580068443 |
| same_samples_h3:ST-Transformer-lite_h3_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h3:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h3_seed2024.parquet |
| prediction_columns:Proposed_h3_seed2024.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h3_seed2024.parquet | True | rows=20100 |
| test_n:Proposed_h3_seed2024.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Proposed_h3_seed2024.parquet | True | NaN/inf |
| mae_match:Proposed_h3_seed2024.parquet | True | metrics=4.030911698887004 computed=4.030911698887004 |
| rmse_match:Proposed_h3_seed2024.parquet | True | metrics=7.269958364476932 computed=7.269958364476932 |
| same_samples_h3:Proposed_h3_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h3:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h3_seed2025.parquet |
| prediction_columns:HA_h3_seed2025.parquet | True | missing=[] |
| prediction_nonempty:HA_h3_seed2025.parquet | True | rows=20100 |
| test_n:HA_h3_seed2025.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:HA_h3_seed2025.parquet | True | NaN/inf |
| mae_match:HA_h3_seed2025.parquet | True | metrics=5.595527209950917 computed=5.595527209950917 |
| rmse_match:HA_h3_seed2025.parquet | True | metrics=9.503428974581972 computed=9.503428974581972 |
| same_samples_h3:HA_h3_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h3:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h3_seed2025.parquet |
| prediction_columns:Persistence_h3_seed2025.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h3_seed2025.parquet | True | rows=20100 |
| test_n:Persistence_h3_seed2025.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Persistence_h3_seed2025.parquet | True | NaN/inf |
| mae_match:Persistence_h3_seed2025.parquet | True | metrics=6.3192616467452165 computed=6.3192616467452165 |
| rmse_match:Persistence_h3_seed2025.parquet | True | metrics=11.74912940588088 computed=11.74912940588088 |
| same_samples_h3:Persistence_h3_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h3:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h3_seed2025.parquet |
| prediction_columns:TCN_h3_seed2025.parquet | True | missing=[] |
| prediction_nonempty:TCN_h3_seed2025.parquet | True | rows=20100 |
| test_n:TCN_h3_seed2025.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:TCN_h3_seed2025.parquet | True | NaN/inf |
| mae_match:TCN_h3_seed2025.parquet | True | metrics=4.206038004652185 computed=4.206038004652185 |
| rmse_match:TCN_h3_seed2025.parquet | True | metrics=7.434342628978274 computed=7.434342628978274 |
| same_samples_h3:TCN_h3_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h3:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h3_seed2025.parquet |
| prediction_columns:ST-Transformer-lite_h3_seed2025.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h3_seed2025.parquet | True | rows=20100 |
| test_n:ST-Transformer-lite_h3_seed2025.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:ST-Transformer-lite_h3_seed2025.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h3_seed2025.parquet | True | metrics=4.122864090174585 computed=4.122864090174585 |
| rmse_match:ST-Transformer-lite_h3_seed2025.parquet | True | metrics=7.426607582567508 computed=7.426607582567508 |
| same_samples_h3:ST-Transformer-lite_h3_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h3:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h3_seed2025.parquet |
| prediction_columns:Proposed_h3_seed2025.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h3_seed2025.parquet | True | rows=20100 |
| test_n:Proposed_h3_seed2025.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Proposed_h3_seed2025.parquet | True | NaN/inf |
| mae_match:Proposed_h3_seed2025.parquet | True | metrics=4.206038004652185 computed=4.206038004652185 |
| rmse_match:Proposed_h3_seed2025.parquet | True | metrics=7.434342628978274 computed=7.434342628978274 |
| same_samples_h3:Proposed_h3_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h3:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h3_seed2026.parquet |
| prediction_columns:HA_h3_seed2026.parquet | True | missing=[] |
| prediction_nonempty:HA_h3_seed2026.parquet | True | rows=20100 |
| test_n:HA_h3_seed2026.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:HA_h3_seed2026.parquet | True | NaN/inf |
| mae_match:HA_h3_seed2026.parquet | True | metrics=5.595527209950917 computed=5.595527209950917 |
| rmse_match:HA_h3_seed2026.parquet | True | metrics=9.503428974581972 computed=9.503428974581972 |
| same_samples_h3:HA_h3_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h3:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h3_seed2026.parquet |
| prediction_columns:Persistence_h3_seed2026.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h3_seed2026.parquet | True | rows=20100 |
| test_n:Persistence_h3_seed2026.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Persistence_h3_seed2026.parquet | True | NaN/inf |
| mae_match:Persistence_h3_seed2026.parquet | True | metrics=6.3192616467452165 computed=6.3192616467452165 |
| rmse_match:Persistence_h3_seed2026.parquet | True | metrics=11.74912940588088 computed=11.74912940588088 |
| same_samples_h3:Persistence_h3_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h3:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h3_seed2026.parquet |
| prediction_columns:TCN_h3_seed2026.parquet | True | missing=[] |
| prediction_nonempty:TCN_h3_seed2026.parquet | True | rows=20100 |
| test_n:TCN_h3_seed2026.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:TCN_h3_seed2026.parquet | True | NaN/inf |
| mae_match:TCN_h3_seed2026.parquet | True | metrics=4.023886999822968 computed=4.023886999822968 |
| rmse_match:TCN_h3_seed2026.parquet | True | metrics=7.278841200636554 computed=7.278841200636554 |
| same_samples_h3:TCN_h3_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h3:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h3_seed2026.parquet |
| prediction_columns:ST-Transformer-lite_h3_seed2026.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h3_seed2026.parquet | True | rows=20100 |
| test_n:ST-Transformer-lite_h3_seed2026.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:ST-Transformer-lite_h3_seed2026.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h3_seed2026.parquet | True | metrics=4.060693457114756 computed=4.0606934571147555 |
| rmse_match:ST-Transformer-lite_h3_seed2026.parquet | True | metrics=7.351564358827948 computed=7.351564358827948 |
| same_samples_h3:ST-Transformer-lite_h3_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h3:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h3_seed2026.parquet |
| prediction_columns:Proposed_h3_seed2026.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h3_seed2026.parquet | True | rows=20100 |
| test_n:Proposed_h3_seed2026.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Proposed_h3_seed2026.parquet | True | NaN/inf |
| mae_match:Proposed_h3_seed2026.parquet | True | metrics=4.023886999822968 computed=4.023886999822968 |
| rmse_match:Proposed_h3_seed2026.parquet | True | metrics=7.278841200636554 computed=7.278841200636554 |
| same_samples_h3:Proposed_h3_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h3:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h3_seed3407.parquet |
| prediction_columns:HA_h3_seed3407.parquet | True | missing=[] |
| prediction_nonempty:HA_h3_seed3407.parquet | True | rows=20100 |
| test_n:HA_h3_seed3407.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:HA_h3_seed3407.parquet | True | NaN/inf |
| mae_match:HA_h3_seed3407.parquet | True | metrics=5.595527209950917 computed=5.595527209950917 |
| rmse_match:HA_h3_seed3407.parquet | True | metrics=9.503428974581972 computed=9.503428974581972 |
| same_samples_h3:HA_h3_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h3:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h3_seed3407.parquet |
| prediction_columns:Persistence_h3_seed3407.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h3_seed3407.parquet | True | rows=20100 |
| test_n:Persistence_h3_seed3407.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Persistence_h3_seed3407.parquet | True | NaN/inf |
| mae_match:Persistence_h3_seed3407.parquet | True | metrics=6.3192616467452165 computed=6.3192616467452165 |
| rmse_match:Persistence_h3_seed3407.parquet | True | metrics=11.74912940588088 computed=11.74912940588088 |
| same_samples_h3:Persistence_h3_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h3:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h3_seed3407.parquet |
| prediction_columns:TCN_h3_seed3407.parquet | True | missing=[] |
| prediction_nonempty:TCN_h3_seed3407.parquet | True | rows=20100 |
| test_n:TCN_h3_seed3407.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:TCN_h3_seed3407.parquet | True | NaN/inf |
| mae_match:TCN_h3_seed3407.parquet | True | metrics=3.975780799543087 computed=3.9757807995430867 |
| rmse_match:TCN_h3_seed3407.parquet | True | metrics=7.292131595519612 computed=7.292131595519612 |
| same_samples_h3:TCN_h3_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h3:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h3_seed3407.parquet |
| prediction_columns:ST-Transformer-lite_h3_seed3407.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h3_seed3407.parquet | True | rows=20100 |
| test_n:ST-Transformer-lite_h3_seed3407.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:ST-Transformer-lite_h3_seed3407.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h3_seed3407.parquet | True | metrics=4.038523926900987 computed=4.038523926900987 |
| rmse_match:ST-Transformer-lite_h3_seed3407.parquet | True | metrics=7.347613006707075 computed=7.347613006707075 |
| same_samples_h3:ST-Transformer-lite_h3_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h3:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h3_seed3407.parquet |
| prediction_columns:Proposed_h3_seed3407.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h3_seed3407.parquet | True | rows=20100 |
| test_n:Proposed_h3_seed3407.parquet | True | metrics=20100 parquet=20100 |
| prediction_finite:Proposed_h3_seed3407.parquet | True | NaN/inf |
| mae_match:Proposed_h3_seed3407.parquet | True | metrics=3.975780799543087 computed=3.9757807995430867 |
| rmse_match:Proposed_h3_seed3407.parquet | True | metrics=7.292131595519612 computed=7.292131595519612 |
| same_samples_h3:Proposed_h3_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h6:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h6_seed42.parquet |
| prediction_columns:HA_h6_seed42.parquet | True | missing=[] |
| prediction_nonempty:HA_h6_seed42.parquet | True | rows=19950 |
| test_n:HA_h6_seed42.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:HA_h6_seed42.parquet | True | NaN/inf |
| mae_match:HA_h6_seed42.parquet | True | metrics=5.5898292907676606 computed=5.5898292907676606 |
| rmse_match:HA_h6_seed42.parquet | True | metrics=9.495127010942282 computed=9.495127010942282 |
| same_samples_h6:HA_h6_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h6:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h6_seed42.parquet |
| prediction_columns:Persistence_h6_seed42.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h6_seed42.parquet | True | rows=19950 |
| test_n:Persistence_h6_seed42.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Persistence_h6_seed42.parquet | True | NaN/inf |
| mae_match:Persistence_h6_seed42.parquet | True | metrics=7.777251121501875 computed=7.777251121501875 |
| rmse_match:Persistence_h6_seed42.parquet | True | metrics=13.520325415030136 computed=13.520325415030136 |
| same_samples_h6:Persistence_h6_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h6:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h6_seed42.parquet |
| prediction_columns:TCN_h6_seed42.parquet | True | missing=[] |
| prediction_nonempty:TCN_h6_seed42.parquet | True | rows=19950 |
| test_n:TCN_h6_seed42.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:TCN_h6_seed42.parquet | True | NaN/inf |
| mae_match:TCN_h6_seed42.parquet | True | metrics=4.097716131473245 computed=4.097716131473245 |
| rmse_match:TCN_h6_seed42.parquet | True | metrics=7.328893414505664 computed=7.328893414505664 |
| same_samples_h6:TCN_h6_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h6:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h6_seed42.parquet |
| prediction_columns:ST-Transformer-lite_h6_seed42.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h6_seed42.parquet | True | rows=19950 |
| test_n:ST-Transformer-lite_h6_seed42.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:ST-Transformer-lite_h6_seed42.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h6_seed42.parquet | True | metrics=4.118159633053275 computed=4.118159633053275 |
| rmse_match:ST-Transformer-lite_h6_seed42.parquet | True | metrics=7.350218420124989 computed=7.350218420124989 |
| same_samples_h6:ST-Transformer-lite_h6_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h6:seed42 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h6_seed42.parquet |
| prediction_columns:Proposed_h6_seed42.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h6_seed42.parquet | True | rows=19950 |
| test_n:Proposed_h6_seed42.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Proposed_h6_seed42.parquet | True | NaN/inf |
| mae_match:Proposed_h6_seed42.parquet | True | metrics=4.097716131473245 computed=4.097716131473245 |
| rmse_match:Proposed_h6_seed42.parquet | True | metrics=7.328893414505664 computed=7.328893414505664 |
| same_samples_h6:Proposed_h6_seed42.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h6:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h6_seed2024.parquet |
| prediction_columns:HA_h6_seed2024.parquet | True | missing=[] |
| prediction_nonempty:HA_h6_seed2024.parquet | True | rows=19950 |
| test_n:HA_h6_seed2024.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:HA_h6_seed2024.parquet | True | NaN/inf |
| mae_match:HA_h6_seed2024.parquet | True | metrics=5.5898292907676606 computed=5.5898292907676606 |
| rmse_match:HA_h6_seed2024.parquet | True | metrics=9.495127010942282 computed=9.495127010942282 |
| same_samples_h6:HA_h6_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h6:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h6_seed2024.parquet |
| prediction_columns:Persistence_h6_seed2024.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h6_seed2024.parquet | True | rows=19950 |
| test_n:Persistence_h6_seed2024.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Persistence_h6_seed2024.parquet | True | NaN/inf |
| mae_match:Persistence_h6_seed2024.parquet | True | metrics=7.777251121501875 computed=7.777251121501875 |
| rmse_match:Persistence_h6_seed2024.parquet | True | metrics=13.520325415030136 computed=13.520325415030136 |
| same_samples_h6:Persistence_h6_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h6:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h6_seed2024.parquet |
| prediction_columns:TCN_h6_seed2024.parquet | True | missing=[] |
| prediction_nonempty:TCN_h6_seed2024.parquet | True | rows=19950 |
| test_n:TCN_h6_seed2024.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:TCN_h6_seed2024.parquet | True | NaN/inf |
| mae_match:TCN_h6_seed2024.parquet | True | metrics=4.078223038580185 computed=4.078223038580185 |
| rmse_match:TCN_h6_seed2024.parquet | True | metrics=7.468938615427874 computed=7.4689386154278745 |
| same_samples_h6:TCN_h6_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h6:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h6_seed2024.parquet |
| prediction_columns:ST-Transformer-lite_h6_seed2024.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h6_seed2024.parquet | True | rows=19950 |
| test_n:ST-Transformer-lite_h6_seed2024.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:ST-Transformer-lite_h6_seed2024.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h6_seed2024.parquet | True | metrics=4.010913042436567 computed=4.010913042436567 |
| rmse_match:ST-Transformer-lite_h6_seed2024.parquet | True | metrics=7.386279225420547 computed=7.386279225420547 |
| same_samples_h6:ST-Transformer-lite_h6_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h6:seed2024 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h6_seed2024.parquet |
| prediction_columns:Proposed_h6_seed2024.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h6_seed2024.parquet | True | rows=19950 |
| test_n:Proposed_h6_seed2024.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Proposed_h6_seed2024.parquet | True | NaN/inf |
| mae_match:Proposed_h6_seed2024.parquet | True | metrics=4.078223038580185 computed=4.078223038580185 |
| rmse_match:Proposed_h6_seed2024.parquet | True | metrics=7.468938615427874 computed=7.4689386154278745 |
| same_samples_h6:Proposed_h6_seed2024.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h6:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h6_seed2025.parquet |
| prediction_columns:HA_h6_seed2025.parquet | True | missing=[] |
| prediction_nonempty:HA_h6_seed2025.parquet | True | rows=19950 |
| test_n:HA_h6_seed2025.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:HA_h6_seed2025.parquet | True | NaN/inf |
| mae_match:HA_h6_seed2025.parquet | True | metrics=5.5898292907676606 computed=5.5898292907676606 |
| rmse_match:HA_h6_seed2025.parquet | True | metrics=9.495127010942282 computed=9.495127010942282 |
| same_samples_h6:HA_h6_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h6:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h6_seed2025.parquet |
| prediction_columns:Persistence_h6_seed2025.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h6_seed2025.parquet | True | rows=19950 |
| test_n:Persistence_h6_seed2025.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Persistence_h6_seed2025.parquet | True | NaN/inf |
| mae_match:Persistence_h6_seed2025.parquet | True | metrics=7.777251121501875 computed=7.777251121501875 |
| rmse_match:Persistence_h6_seed2025.parquet | True | metrics=13.520325415030136 computed=13.520325415030136 |
| same_samples_h6:Persistence_h6_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h6:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h6_seed2025.parquet |
| prediction_columns:TCN_h6_seed2025.parquet | True | missing=[] |
| prediction_nonempty:TCN_h6_seed2025.parquet | True | rows=19950 |
| test_n:TCN_h6_seed2025.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:TCN_h6_seed2025.parquet | True | NaN/inf |
| mae_match:TCN_h6_seed2025.parquet | True | metrics=4.099470177366023 computed=4.0994701773660225 |
| rmse_match:TCN_h6_seed2025.parquet | True | metrics=7.366669542337208 computed=7.366669542337208 |
| same_samples_h6:TCN_h6_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h6:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h6_seed2025.parquet |
| prediction_columns:ST-Transformer-lite_h6_seed2025.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h6_seed2025.parquet | True | rows=19950 |
| test_n:ST-Transformer-lite_h6_seed2025.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:ST-Transformer-lite_h6_seed2025.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h6_seed2025.parquet | True | metrics=4.042153483321494 computed=4.042153483321494 |
| rmse_match:ST-Transformer-lite_h6_seed2025.parquet | True | metrics=7.400762142930469 computed=7.400762142930469 |
| same_samples_h6:ST-Transformer-lite_h6_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h6:seed2025 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h6_seed2025.parquet |
| prediction_columns:Proposed_h6_seed2025.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h6_seed2025.parquet | True | rows=19950 |
| test_n:Proposed_h6_seed2025.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Proposed_h6_seed2025.parquet | True | NaN/inf |
| mae_match:Proposed_h6_seed2025.parquet | True | metrics=4.099470177366023 computed=4.0994701773660225 |
| rmse_match:Proposed_h6_seed2025.parquet | True | metrics=7.366669542337208 computed=7.366669542337208 |
| same_samples_h6:Proposed_h6_seed2025.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h6:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h6_seed2026.parquet |
| prediction_columns:HA_h6_seed2026.parquet | True | missing=[] |
| prediction_nonempty:HA_h6_seed2026.parquet | True | rows=19950 |
| test_n:HA_h6_seed2026.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:HA_h6_seed2026.parquet | True | NaN/inf |
| mae_match:HA_h6_seed2026.parquet | True | metrics=5.5898292907676606 computed=5.5898292907676606 |
| rmse_match:HA_h6_seed2026.parquet | True | metrics=9.495127010942282 computed=9.495127010942282 |
| same_samples_h6:HA_h6_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h6:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h6_seed2026.parquet |
| prediction_columns:Persistence_h6_seed2026.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h6_seed2026.parquet | True | rows=19950 |
| test_n:Persistence_h6_seed2026.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Persistence_h6_seed2026.parquet | True | NaN/inf |
| mae_match:Persistence_h6_seed2026.parquet | True | metrics=7.777251121501875 computed=7.777251121501875 |
| rmse_match:Persistence_h6_seed2026.parquet | True | metrics=13.520325415030136 computed=13.520325415030136 |
| same_samples_h6:Persistence_h6_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h6:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h6_seed2026.parquet |
| prediction_columns:TCN_h6_seed2026.parquet | True | missing=[] |
| prediction_nonempty:TCN_h6_seed2026.parquet | True | rows=19950 |
| test_n:TCN_h6_seed2026.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:TCN_h6_seed2026.parquet | True | NaN/inf |
| mae_match:TCN_h6_seed2026.parquet | True | metrics=4.14694519788699 computed=4.14694519788699 |
| rmse_match:TCN_h6_seed2026.parquet | True | metrics=7.401443293965154 computed=7.401443293965154 |
| same_samples_h6:TCN_h6_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h6:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h6_seed2026.parquet |
| prediction_columns:ST-Transformer-lite_h6_seed2026.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h6_seed2026.parquet | True | rows=19950 |
| test_n:ST-Transformer-lite_h6_seed2026.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:ST-Transformer-lite_h6_seed2026.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h6_seed2026.parquet | True | metrics=4.104635347543205 computed=4.104635347543205 |
| rmse_match:ST-Transformer-lite_h6_seed2026.parquet | True | metrics=7.487396397166414 computed=7.487396397166414 |
| same_samples_h6:ST-Transformer-lite_h6_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h6:seed2026 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h6_seed2026.parquet |
| prediction_columns:Proposed_h6_seed2026.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h6_seed2026.parquet | True | rows=19950 |
| test_n:Proposed_h6_seed2026.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Proposed_h6_seed2026.parquet | True | NaN/inf |
| mae_match:Proposed_h6_seed2026.parquet | True | metrics=4.14694519788699 computed=4.14694519788699 |
| rmse_match:Proposed_h6_seed2026.parquet | True | metrics=7.401443293965154 computed=7.401443293965154 |
| same_samples_h6:Proposed_h6_seed2026.parquet | True | sample_id set mismatch |
| prediction_exists:HA:h6:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\HA_h6_seed3407.parquet |
| prediction_columns:HA_h6_seed3407.parquet | True | missing=[] |
| prediction_nonempty:HA_h6_seed3407.parquet | True | rows=19950 |
| test_n:HA_h6_seed3407.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:HA_h6_seed3407.parquet | True | NaN/inf |
| mae_match:HA_h6_seed3407.parquet | True | metrics=5.5898292907676606 computed=5.5898292907676606 |
| rmse_match:HA_h6_seed3407.parquet | True | metrics=9.495127010942282 computed=9.495127010942282 |
| same_samples_h6:HA_h6_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:Persistence:h6:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Persistence_h6_seed3407.parquet |
| prediction_columns:Persistence_h6_seed3407.parquet | True | missing=[] |
| prediction_nonempty:Persistence_h6_seed3407.parquet | True | rows=19950 |
| test_n:Persistence_h6_seed3407.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Persistence_h6_seed3407.parquet | True | NaN/inf |
| mae_match:Persistence_h6_seed3407.parquet | True | metrics=7.777251121501875 computed=7.777251121501875 |
| rmse_match:Persistence_h6_seed3407.parquet | True | metrics=13.520325415030136 computed=13.520325415030136 |
| same_samples_h6:Persistence_h6_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:TCN:h6:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\TCN_h6_seed3407.parquet |
| prediction_columns:TCN_h6_seed3407.parquet | True | missing=[] |
| prediction_nonempty:TCN_h6_seed3407.parquet | True | rows=19950 |
| test_n:TCN_h6_seed3407.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:TCN_h6_seed3407.parquet | True | NaN/inf |
| mae_match:TCN_h6_seed3407.parquet | True | metrics=4.091964846063676 computed=4.091964846063676 |
| rmse_match:TCN_h6_seed3407.parquet | True | metrics=7.369772014154074 computed=7.369772014154074 |
| same_samples_h6:TCN_h6_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:ST-Transformer-lite:h6:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\ST-Transformer-lite_h6_seed3407.parquet |
| prediction_columns:ST-Transformer-lite_h6_seed3407.parquet | True | missing=[] |
| prediction_nonempty:ST-Transformer-lite_h6_seed3407.parquet | True | rows=19950 |
| test_n:ST-Transformer-lite_h6_seed3407.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:ST-Transformer-lite_h6_seed3407.parquet | True | NaN/inf |
| mae_match:ST-Transformer-lite_h6_seed3407.parquet | True | metrics=5.472836667971503 computed=5.472836667971503 |
| rmse_match:ST-Transformer-lite_h6_seed3407.parquet | True | metrics=9.431195355132346 computed=9.431195355132346 |
| same_samples_h6:ST-Transformer-lite_h6_seed3407.parquet | True | sample_id set mismatch |
| prediction_exists:Proposed:h6:seed3407 | True | D:\2026_PD\outputs\supplementary_metr_la_mini\predictions\Proposed_h6_seed3407.parquet |
| prediction_columns:Proposed_h6_seed3407.parquet | True | missing=[] |
| prediction_nonempty:Proposed_h6_seed3407.parquet | True | rows=19950 |
| test_n:Proposed_h6_seed3407.parquet | True | metrics=19950 parquet=19950 |
| prediction_finite:Proposed_h6_seed3407.parquet | True | NaN/inf |
| mae_match:Proposed_h6_seed3407.parquet | True | metrics=4.091964846063676 computed=4.091964846063676 |
| rmse_match:Proposed_h6_seed3407.parquet | True | metrics=7.369772014154074 computed=7.369772014154074 |
| same_samples_h6:Proposed_h6_seed3407.parquet | True | sample_id set mismatch |
| FigS1_nonempty | True | rows=15 |
| FigS1_finite | True | numeric NaN/inf |
