# Pan Borneo Highway Floating-Car-Data Traffic Forecasting Reproducibility Package

## Purpose of This Repository

This repository provides the public reproducibility and manuscript-support package for a Pan Borneo Highway sparse floating-car-data (FCD) traffic forecasting study.

The repository is intended to support:

- conference paper review;
- transparent checking of reported experimental results;
- reproduction of figure and table source data;
- inspection of model-comparison, ablation, robustness, statistical-test, and supplementary sanity-check outputs;
- archival of the validated data products used for manuscript writing.

Raw provider-level floating-car records are not included because of data licensing and provider terms. The released files are processed, anonymized, aggregated, and audit-ready data products.

## Most Important Folder for the Current Paper

The current complete conference-paper support package is:

```text
conference_paper_support_package_20260706/
```

This folder contains the latest validated results and manuscript-support data generated from the local project state on 2026-07-06.

Use this folder first when checking the current paper results.

Direct GitHub folder:

```text
https://github.com/tasadapullo-svg/2026-PanBorneo-FCD-Forecasting-Reproducibility/tree/main/conference_paper_support_package_20260706
```

## Status Summary

The uploaded support package is marked:

```text
READY_FOR_PLOTTING_AND_WRITING
```

This means the local readiness audit found the result data sufficient for preparing the manuscript figures and tables. It does not mean the repository contains private raw provider records or final rendered manuscript figures.

Key validated components include:

- Phase 13 main baseline comparison;
- Phase 13A full-output validation;
- Phase 15 feature ablation;
- Phase 16 robustness experiments;
- Phase 17 stratified evaluation outputs where available in the package;
- Phase 14 final statistical tests;
- Phase 18 figure/table consistency audit;
- Phase 19 manuscript data package;
- Phase 20 METR-LA-mini supplementary sanity check;
- figure-candidate CSV files;
- table-candidate CSV files;
- prediction parquet files used for paired checks;
- configuration files, scripts, logs, reports, and checksums.

## Repository Structure

```text
.
|-- README.md
|-- LICENSE_CODE.md
|-- DATA_USE_NOTICE.md
|-- CITATION.cff
|-- data/
|   |-- README_DATA.md
|   |-- data_dictionary.csv
|   |-- file_manifest.csv
|   |-- processed/
|   `-- plot_data/
|       `-- deprecated/
|-- configs/
|-- scripts/
|-- reports/
|-- docs/
|-- figures/
`-- conference_paper_support_package_20260706/
    |-- 00_READ_FIRST/
    |-- 01_FIGURE_CANDIDATE_DATA/
    |-- 02_TABLE_CANDIDATE_DATA/
    |-- 03_PHASE13_MAIN_RESULTS/
    |-- 04_PHASE15_ABLATION_RESULTS/
    |-- 05_PHASE16_ROBUSTNESS_RESULTS/
    |-- 06_PHASE20_FULL_RESULTS/
    |-- 07_PREDICTION_PARQUETS/
    |-- 08_STATISTICAL_TESTS/
    |-- 09_SUPPLEMENTARY_DATA/
    |-- 10_CONFIGS_ENVIRONMENT_LOGS/
    |-- 11_GITHUB_ZENODO_METADATA/
    |-- 12_AUDIT_REPORTS/
    |-- release_archive/
    |-- PUBLIC_UPLOAD_NOTICE.md
    `-- PUBLIC_UPLOAD_CHECKSUMS_SHA256.csv
```

## Current Support Package Contents

The folder `conference_paper_support_package_20260706/` contains 536 files. It is a curated public upload package prepared from the local project after the major validation steps were completed.

### `00_READ_FIRST/`

Start here. This folder contains the top-level package explanation and review-facing notes. It is intended to help reviewers or collaborators understand what is included, what is excluded, and how the package should be interpreted.

### `01_FIGURE_CANDIDATE_DATA/`

Contains CSV files prepared as candidate source data for the manuscript figures.

These files are not the final rendered figures. They are figure-input data tables intended for plotting and review.

Expected manuscript figure coverage includes:

- Figure 1: study corridor, data source, and leakage-controlled workflow;
- Figure 2: main model and baseline forecasting performance;
- Figure 3: seed stability and performance consistency;
- Figure 4: feature ablation;
- Figure 5: sensitivity or diagnostic figure data where available;
- Figure 6: volatility or error-heterogeneity figure data where available;
- Figure 7: robustness under missingness, noise, and small-sample training.

### `02_TABLE_CANDIDATE_DATA/`

Contains CSV files prepared as candidate source data for manuscript tables.

These files are table-input data, not final formatted manuscript tables. They should be used to prepare the paper tables while preserving traceability to the experiment outputs.

Expected table coverage includes:

- dataset audit and experimental design summary;
- main model comparison summary;
- statistical test summary with corrected p-values and effect sizes;
- robustness, ablation, stratified, and supplementary summaries where applicable.

### `03_PHASE13_MAIN_RESULTS/`

Contains the main strong-baseline comparison outputs.

Phase 13 evaluates the forecasting target using the same chronological split and shared test samples across model comparisons. The expected full design is:

- 7 models;
- 3 horizons: 1h, 3h, 6h;
- 5 seeds: 42, 2024, 2025, 2026, 3407;
- 105 metric rows;
- 105 prediction parquet files.

The model set is:

- HA;
- SeasonalHA;
- Persistence;
- XGBoost;
- GRU;
- TCN;
- ST-Transformer-lite.

The metrics include MAE, RMSE, MAPE, sMAPE, R2, timing fields, configuration hash, and data hash where available.

### `04_PHASE15_ABLATION_RESULTS/`

Contains feature-ablation outputs.

Phase 15 evaluates whether different feature groups improve or change forecasting performance relative to a speed-only reference.

Feature groups:

- `speed_only`;
- `speed_time`;
- `speed_reliability`;
- `speed_volatility`;
- `full_features`.

Expected full design:

- 5 feature groups;
- 3 horizons;
- 5 seeds;
- 75 metric rows;
- 75 prediction parquet files.

The `speed_only` reference is expected to have `relative_MAE_change_from_speed_only_percent = 0`.

### `05_PHASE16_ROBUSTNESS_RESULTS/`

Contains robustness experiment outputs.

Phase 16 evaluates model behavior under sparse, noisy, and small-sample conditions.

Included robustness families:

- missingness stress;
- noise stress;
- small-sample training.

Expected full checks:

- missingness stress: 4 levels x 3 horizons x 5 seeds = 60 rows;
- noise stress: 4 levels x 3 horizons x 5 seeds = 60 rows;
- small-sample training: 5 ratios x 3 horizons x 5 seeds = 75 rows.

Reference conditions:

- 0% missingness relative change should be 0;
- clean noise relative change should be 0;
- 100% small-sample training relative change should be 0.

### `06_PHASE20_FULL_RESULTS/`

Contains the supplementary METR-LA-mini sanity-check outputs.

Important interpretation rule:

METR-LA-mini is supplementary only. It must not be mixed with the Pan Borneo main manuscript figures or main tables.

The supplementary check is intended to answer whether the workflow behavior is plausible outside the Pan Borneo corridor. It is not a full benchmark comparison and should not be presented as a state-of-the-art METR-LA benchmark.

Known note:

- In the Phase 20 package, `Proposed` is documented as an alias/implementation equivalent to the TCN-style proposed model used in that supplementary setting. Do not overclaim method differences based on this supplementary result.

### `07_PREDICTION_PARQUETS/`

Contains prediction parquet files used for reproducibility checks and paired statistical testing.

Typical parquet columns include:

- `sample_id`;
- `timestamp`;
- `node_id`;
- `horizon`;
- model or feature-group identifier;
- `seed`;
- `y_true`;
- `y_pred`;
- `abs_error`;
- `squared_error`.

These files allow MAE and RMSE to be recomputed from sample-level predictions.

### `08_STATISTICAL_TESTS/`

Contains statistical-test output tables.

These files are used to support manuscript claims about:

- proposed/main model vs baselines;
- feature groups vs speed-only reference;
- robustness perturbations vs clean/reference conditions;
- stratified or grouped error differences where available.

The expected statistical fields include:

- test name;
- statistic;
- raw p-value;
- corrected p-value;
- effect size;
- effect-size type;
- significance label;
- sample count or pair count.

Paired tests should use paired sample-level predictions where applicable. Independent strata should not be treated as paired comparisons.

### `09_SUPPLEMENTARY_DATA/`

Contains supplementary outputs that should remain separate from the main Pan Borneo manuscript results.

The main example is METR-LA-mini. These files may be useful for supplementary material or reviewer response, but they are not part of the primary Pan Borneo experimental claims.

### `10_CONFIGS_ENVIRONMENT_LOGS/`

Contains reproducibility support files:

- YAML configuration files;
- selected scripts;
- logs;
- environment or command records where available.

These files document the experimental procedure and help explain how the outputs were generated.

This folder is not a full Python environment export. Conda environments, package caches, and machine-specific runtime folders are intentionally excluded.

### `11_GITHUB_ZENODO_METADATA/`

Contains release-support metadata, manifests, checksums, and documentation intended for GitHub or Zenodo-style archiving.

Use this folder when preparing a formal archival release or when checking whether the package files are complete.

### `12_AUDIT_REPORTS/`

Contains validation and readiness reports.

Important report types include:

- phase validation reports;
- figure/table consistency audit reports;
- applied-intelligence readiness audit reports;
- package-generation summaries;
- warning lists and critical-error checks where available.

### `release_archive/`

Contains a ZIP archive copy of the paper data package:

```text
paper_data_package_for_gpt_review.zip
```

GitHub accepted this file, but it is larger than GitHub's recommended 50 MB file-size guideline. It is below GitHub's 100 MB hard file-size limit.

For long-term archival, a Zenodo release is preferable for large packaged archives.

### `PUBLIC_UPLOAD_NOTICE.md`

Explains what was included and excluded from the public upload.

Read this file before reusing or redistributing the data.

### `PUBLIC_UPLOAD_CHECKSUMS_SHA256.csv`

Contains SHA256 checksums for uploaded package files. This file can be used to verify file integrity after download.

## Main Experimental Phases Represented

| Phase | Purpose | Main Output Type |
|---|---|---|
| Phase 13 | Strong baseline comparison | Metrics CSV and prediction parquet files |
| Phase 13A | Full-output validation | Validation report and summary |
| Phase 15 | Feature ablation | Metrics CSV, prediction parquet files, report |
| Phase 16 | Robustness under missingness, noise, and small-sample training | Robustness CSV tables and report |
| Phase 17 | Stratified evaluation | Reliability, coverage, volatility, and traffic-state stratified tables where available |
| Phase 14 | Final statistical tests | p-values, corrected p-values, effect sizes, mean/std summaries |
| Phase 18 | Figure/table consistency audit | Readiness and consistency reports |
| Phase 19 | Manuscript data package | Figure/table candidate data and package manifest |
| Phase 20 | Supplementary METR-LA-mini sanity check | Supplementary-only metrics and prediction files |

## Data Availability and Restrictions

The original source data were provider-level floating-car observations. Those raw records are excluded from this public repository.

This repository includes:

- processed analytical data;
- anonymized and aggregated traffic-feature tables;
- figure-ready candidate CSV files;
- table-ready candidate CSV files;
- experiment metrics;
- prediction parquet files needed for reproducibility checks;
- configuration files;
- scripts;
- logs and reports;
- manifests and checksums.

This repository excludes:

- raw provider-level floating-car records;
- provider API response dumps;
- API keys, tokens, credentials, and private access logs;
- local conda environments;
- package caches;
- temporary runtime files;
- machine-specific hidden caches;
- unrestricted raw records that cannot be redistributed under provider terms.

## Leakage-Control and Split Assumptions

The reported forecasting experiments are designed around a leakage-controlled workflow:

- chronological train/validation/test split;
- scalers fitted only on training data;
- shared test samples across comparable model runs;
- horizons fixed at 1h, 3h, and 6h;
- main node count documented as 51 where applicable;
- repeated evaluation across seeds 42, 2024, 2025, 2026, and 3407 where required.

Validation reports in the support package should be used to confirm which checks passed for each phase.

## How to Use This Repository for Paper Review

Recommended review sequence:

1. Open `conference_paper_support_package_20260706/00_READ_FIRST/`.
2. Check `conference_paper_support_package_20260706/12_AUDIT_REPORTS/`.
3. Use `01_FIGURE_CANDIDATE_DATA/` for figure source data.
4. Use `02_TABLE_CANDIDATE_DATA/` for table source data.
5. Use `03_PHASE13_MAIN_RESULTS/` for main model comparison.
6. Use `04_PHASE15_ABLATION_RESULTS/` for feature-group analysis.
7. Use `05_PHASE16_ROBUSTNESS_RESULTS/` for missingness, noise, and small-sample robustness.
8. Use `08_STATISTICAL_TESTS/` for p-values, corrected p-values, effect sizes, and mean/std summaries.
9. Use `09_SUPPLEMENTARY_DATA/` and `06_PHASE20_FULL_RESULTS/` only for supplementary METR-LA-mini discussion.
10. Use `PUBLIC_UPLOAD_CHECKSUMS_SHA256.csv` to verify file integrity if needed.

## Important Interpretation Notes

1. The package supports manuscript plotting and writing, but it does not contain final rendered journal figures.
2. METR-LA-mini is supplementary only and must not be merged into Pan Borneo main results.
3. Raw provider-level FCD records are not public. Reproducing the entire pipeline from raw observations requires independent provider access.
4. Processed prediction files are included so that key metrics can be recomputed.
5. Statistical interpretation should distinguish paired model comparisons from independent stratum comparisons.
6. If future manuscript versions change figure or table definitions, regenerate a new dated package rather than overwriting this one.

## Validation and Audit

The package was prepared after local validation/audit steps reported readiness for plotting and writing.

Relevant audit outputs are stored under:

```text
conference_paper_support_package_20260706/12_AUDIT_REPORTS/
```

The top-level readiness result was:

```text
READY_FOR_PLOTTING_AND_WRITING
```

If users want to rerun validation scripts, they should inspect the scripts and configuration files under:

```text
conference_paper_support_package_20260706/10_CONFIGS_ENVIRONMENT_LOGS/
```

Some scripts may require the original local project layout or private raw-data access and therefore may not be fully executable from this public repository alone.

## Legacy Top-Level Data Folders

The repository also contains earlier public reproducibility folders:

- `data/`;
- `configs/`;
- `scripts/`;
- `reports/`;
- `docs/`;
- `figures/`.

These remain available for traceability. For the current conference paper support package, prefer the dated folder:

```text
conference_paper_support_package_20260706/
```

## Citation

Please cite the associated manuscript and this repository when using the data, scripts, reports, or documentation.

Citation metadata are provided in:

```text
CITATION.cff
```

## Contact

For academic correspondence, refer to the corresponding author information in the associated manuscript.
