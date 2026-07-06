# Final package audit report

## Executive Summary

- Figure candidate data status: PASS
- Table candidate data status: PASS
- Phase 13 status: PASS
- Phase 15 status: PASS
- Phase 16 status: PASS
- Phase 20 status: PASS
- Statistical test data status: PASS
- GitHub/Zenodo metadata status: PASS
- Ready for GPT review: YES

## Confirmed validation results

- Phase 13 metrics row count: 105
- Phase 13 prediction parquet count: 105
- Phase 13 parquet readable/non-empty: YES
- Phase 13 metric recomputation from parquet: YES
- Phase 13 same-horizon sample_id consistency: YES
- Phase 15 metrics row count: 75
- Phase 15 prediction parquet count: 75
- Phase 15 speed_only reference check: YES
- Phase 15 same horizon + seed sample_id consistency: YES
- Phase 16 missingness row count: 60
- Phase 16 noise row count: 60
- Phase 16 small-sample row count: 75
- Phase 16 reference checks: YES
- Table3 corrected p-value: YES
- Table3 effect size: YES
- METR-LA-mini exclusion from main figures/tables: YES

## Figure-by-figure summary

Fig01-Fig07 candidate data folders are populated under 01_FIGURE_CANDIDATE_DATA. GPT can inspect them for plotting later. Risk level is LOW for main validated data; Fig05/Fig06 derived ranking/interpretation should be reviewed for wording.

## Table-by-table summary

Table01-Table04 candidate folders are populated under 02_TABLE_CANDIDATE_DATA. Values are traceable to Phase outputs and final readiness CSVs. GPT can inspect for table construction later.

## Supplementary data summary

METR-LA-mini Phase20 full validation passed and is packaged only under supplementary/Phase20 sections. Prediction parquets and validation logs are included for reproducibility.

## Main warnings

- Restricted/provider-derived raw data are excluded and recorded.
- METR-LA-mini is supplementary only; Proposed equals TCN alias in Phase20 sanity check.

## Final recommendation

This ZIP is ready for GPT review. GPT can now inspect which data can be used for figures and tables. No additional reruns are needed. Plotting should still be delayed until GPT reviews candidate data and manuscript layout decisions.
