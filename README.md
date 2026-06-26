# Pan Borneo Highway Floating-Car-Data Traffic Forecasting Reproducibility Package

## Project Overview

This repository provides the reproducibility package for a traffic forecasting study using floating-car data from the Pan Borneo Highway corridor in Sarawak, Malaysia.

The package is designed to support transparent review, figure reproduction, and result auditing for the associated manuscript. It contains processed analytical tables, figure-ready CSV files, experiment configuration files, validation scripts, and reproducibility documentation.

Raw provider-level floating-car records are not included because of data licensing and provider terms.

## Associated Study

The associated study develops and evaluates a leakage-controlled traffic forecasting workflow for a data-sparse highway corridor. The experiments include:

* Main forecasting performance comparison
* Multi-seed stability analysis
* Feature-group ablation
* History-length sensitivity analysis
* Volatility-error analysis
* Missingness robustness testing
* Noise robustness testing
* Small-sample training sensitivity analysis

The repository supports the manuscript figures, tables, and main experimental comparisons using processed and anonymized data products.

## Study Corridor

The case study corridor is located along the Pan Borneo Highway in Sarawak, Malaysia. The public release represents the corridor using anonymized monitoring points and processed hourly traffic features.

The released data are intended for reproducibility of the reported analysis rather than redistribution of the original provider-level observations.

## Data Source and Public Release Scope

The original data source consists of provider-level floating-car traffic observations. These raw records are excluded from this public package.

This repository includes:

* Processed analytical data
* Anonymized and aggregated traffic-feature tables
* Figure-ready CSV files
* Experiment configuration files
* Validation and manifest-generation scripts
* Reproducibility reports
* Documentation for data structure, variables, leakage control, and workflow interpretation

This repository excludes:

* Raw provider-level floating-car records
* Provider API response dumps
* API keys, tokens, credentials, and private logs
* Large intermediate window-index files
* Model checkpoints and temporary training artifacts
* Cache files and machine-specific local paths

## Repository Structure

```text
.
├── README.md
├── LICENSE_CODE.md
├── DATA_USE_NOTICE.md
├── CITATION.cff
├── .gitignore
│
├── data/
│   ├── README_DATA.md
│   ├── data_dictionary.csv
│   ├── file_manifest.csv
│   ├── processed/
│   └── plot_data/
│       └── deprecated/
│
├── configs/
├── scripts/
├── reports/
├── docs/
└── figures/
```

### Folder Description

| Folder / File                | Description                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `data/processed/`            | Processed analytical tables and compact anonymized data products used for model evaluation and result auditing.    |
| `data/plot_data/`            | Figure-ready CSV files used to reproduce the manuscript figures.                                                   |
| `data/plot_data/deprecated/` | Older plot-data files retained for traceability but not used in the current manuscript figure definition.          |
| `configs/`                   | YAML configuration files for forecasting, ablation, robustness, history-sensitivity, and small-sample experiments. |
| `scripts/`                   | Validation scripts, manifest-generation scripts, and selected public project scripts.                              |
| `reports/`                   | Preprocessing, experiment, validation, and reproducibility reports.                                                |
| `docs/`                      | Workflow documentation, variable definitions, leakage-control protocol, and GitHub upload checklist.               |
| `figures/`                   | Notes for figure reproduction and manuscript-specific plotting guidance.                                           |

## Data Availability Statement

Raw provider-level floating-car data are not redistributed because of data licensing and provider terms. This repository provides processed, anonymized, aggregated, and figure-ready data sufficient to reproduce the reported figures, tables, and main experimental comparisons.

Exact provider-level raw records may require independent access from the original data provider. The released package is intended for academic reproducibility and non-commercial research use.

## Reproducibility Workflow

The reproducibility workflow follows the sequence below:

```text
Raw floating-car data collection
→ Data cleaning and quality control
→ Hourly temporal alignment
→ Feature construction
→ Leakage-controlled train/validation/test splitting
→ Model training and evaluation
→ Robustness and sensitivity experiments
→ Figure-ready data generation
→ Public validation and release
```

Only the public, processed, and figure-ready stages are included in this repository. Steps requiring private raw provider data are documented but not directly reproducible from this public release.

## Validation

To validate the package locally, run the following commands from the repository root:

```bash
python scripts/00_check_environment.py
python scripts/01_validate_data_package.py
python scripts/02_generate_file_manifest.py
python scripts/01_validate_data_package.py
```

The validation scripts check:

* CSV readability
* File manifest completeness
* Figure 1–7 data availability
* Missing or empty files
* Duplicate CSV columns
* Suspicious private fields or credentials
* Absolute local paths
* Raw, log, cache, checkpoint, and temporary files

The generated validation output is stored in:

```text
reports/data_package_validation_report.md
```

## Figure-Data Mapping

| Manuscript Figure | Purpose                                                           | Required CSV Files                                                                                                                                                                  | Status    |
| ----------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Figure 1          | Study corridor, data source, and workflow overview                | `Fig01_workflow_data.csv`                                                                                                                                                           | Available |
| Figure 2          | Main forecasting performance against baseline models              | `Fig02_main_forecasting_performance.csv`                                                                                                                                            | Available |
| Figure 3          | Five-seed stability and improvement consistency                   | `Fig03_five_seed_stability_mean_std.csv`; `Fig03_seed_scatter.csv`; `Fig03_improvement_boxplot.csv`                                                                                 | Available |
| Figure 4          | Feature-group ablation analysis                                   | `Fig04_ablation_data.csv`                                                                                                                                                           | Available |
| Figure 5          | History-length sensitivity of forecasting performance             | `Fig05_history_sensitivity_data.csv`                                                                                                                                                | Available |
| Figure 6          | Volatility-error relationship and error heterogeneity             | `Fig06_volatility_error_data.csv`                                                                                                                                                   | Available |
| Figure 7          | Robustness under missingness, noise, and limited training samples | `Fig07_missingness_stress_data.csv`; `Fig07_noise_stress_data.csv`; `Fig07_small_sample_training_data.csv`; `Fig07_degradation_summary_data.csv`; `phase8_small_sample_metrics.csv` | Available |

## Figure 7 Definition

The current manuscript definition of Figure 7 is:

**Robustness under missingness, noise, and limited training samples**

It contains four panels:

* **Panel (a):** Missingness stress test
* **Panel (b):** Noise stress test
* **Panel (c):** Small-sample training sensitivity
* **Panel (d):** Maximum observed degradation summary

Older combined robustness data files, if retained, are placed under:

```text
data/plot_data/deprecated/
```

These files are retained for traceability but are not part of the current Figure 7 definition.

## Included Files

This release includes:

* Processed analytical CSV files
* Figure-ready CSV files
* Data dictionary
* File manifest with SHA256 hashes
* YAML experiment configurations
* Public validation scripts
* Reproducibility reports
* Workflow documentation
* Variable definitions
* Leakage-control protocol
* Figure reproduction notes

## Excluded Files

The following files are intentionally excluded:

* Raw floating-car provider records
* Raw API response JSON files
* API keys, tokens, passwords, and credentials
* Private logs and provider-access records
* Local machine paths
* Large intermediate window-index files
* Model checkpoints
* Temporary cache files
* ZIP, RAR, and other archive files

## Notes on Reproducibility

The repository supports reproduction of the reported tables, figure data, and main experimental comparisons from the released processed files.

Full end-to-end reconstruction from raw provider data is not included because the raw provider-level records are not publicly redistributed. The preprocessing and leakage-control logic are documented in the `reports/` and `docs/` folders.

## Citation

Please cite the associated manuscript and this repository when using the data, scripts, or documentation.

Citation metadata are provided in:

```text
CITATION.cff
```

## Contact

For academic correspondence, please refer to the corresponding author information in the associated manuscript.
