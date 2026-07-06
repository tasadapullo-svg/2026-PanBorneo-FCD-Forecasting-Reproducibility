# README for GPT

Purpose: this ZIP packages candidate data for GPT review of manuscript figures/tables. It does not contain rendered final figures or final manuscript tables, and no experiments were rerun.

Validated results:
- Phase 13: 105 metrics rows; 105 prediction parquets; parquet recomputation and sample consistency passed.
- Phase 15: 75 metrics rows; 75 prediction parquets; speed_only reference is zero; sample consistency passed.
- Phase 16: missingness 60 rows; noise 60 rows; small-sample 75 rows; all reference conditions are zero.
- Phase 20: 75 METR-LA-mini rows; 75 prediction parquets; supplementary sanity check only.

GPT should first review:
1. 12_AUDIT_REPORTS/final_package_audit_report.md
2. 00_READ_FIRST/PACKAGE_MASTER_INDEX.csv
3. 01_FIGURE_CANDIDATE_DATA/
4. 02_TABLE_CANDIDATE_DATA/
5. 08_STATISTICAL_TESTS/

Figure mapping:
- Fig01: workflow/data audit/split/coverage
- Fig02: Phase13 baselines
- Fig03: seed stability/statistics
- Fig04: Phase15 feature ablation
- Fig05: stratified error with error_rank
- Fig06: error heterogeneity interpretation
- Fig07: Phase16 robustness

Table mapping:
- Table01: dataset audit/design
- Table02: model settings/hyperparameters
- Table03: main performance/statistics
- Table04: ablation/robustness/stratified summary

Supplementary:
- METR-LA-mini Phase20 external sanity check only.

GitHub/Zenodo:
- See 11_GITHUB_ZENODO_METADATA.

Main risks:
- Restricted raw provider data are excluded.
- METR-LA-mini is not mixed into main figures/tables.
- Proposed equals TCN alias in METR-LA-mini sanity check; do not overclaim.
