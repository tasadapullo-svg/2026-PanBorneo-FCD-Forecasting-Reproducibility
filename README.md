# Pan Borneo Highway Floating-Car-Data Traffic Forecasting Reproducibility Package

        ## Project Overview
        This release package supports a traffic forecasting manuscript project for the Pan Borneo Highway corridor in Sarawak, Malaysia.

        ## Paper Description
        This repository supports a traffic forecasting study using floating car data collected along the Pan Borneo Highway corridor in Sarawak, Malaysia. The repository provides processed analytical data, figure-ready CSV files, configuration files, scripts, and reproducibility documentation for forecasting, ablation, robustness, history-sensitivity, volatility-error, and small-sample experiments.

        ## Study Corridor
        The study corridor is the Pan Borneo Highway in Sarawak, Malaysia, represented by anonymized monitoring points and hourly processed traffic features.

        ## Data Source
        The source data are provider-level floating-car traffic observations. Raw provider records are excluded from this public package.

        ## Repository Structure
        - `data/processed/`: processed analytical tables and compact anonymized processed data.
        - `data/plot_data/`: figure-ready CSV files.
        - `data/plot_data/deprecated/`: older plot-data files retained for traceability.
        - `configs/`: YAML experiment configuration files.
        - `scripts/`: validation helpers and original project scripts.
        - `reports/`: public reproducibility reports and selected source reports.
        - `docs/`: workflow, variable, leakage-control, and upload documentation.
        - `figures/`: figure reproduction notes.

        ## Data Availability Statement
        Raw provider-level floating-car data are not redistributed because of data licensing and provider terms. This package provides processed, anonymized, aggregated, and figure-ready data sufficient to reproduce the reported figures, tables, and main experimental comparisons. Exact provider raw data may require independent access from the original data provider.

        ## Reproducibility Workflow
        Run `python scripts/00_check_environment.py`, then `python scripts/01_validate_data_package.py`, then `python scripts/02_generate_file_manifest.py`, and then validate once more. Use `data/plot_data/` with manuscript-specific plotting scripts.

        ## Figure-Data Mapping Table
        | Figure | Required CSV files | Status |
| --- | --- | --- |
| Figure 1 | Fig01_workflow_data.csv | ok |
| Figure 2 | Fig02_main_forecasting_performance.csv | ok |
| Figure 3 | Fig03_five_seed_stability_mean_std.csv, Fig03_seed_scatter.csv, Fig03_improvement_boxplot.csv | ok, ok, ok |
| Figure 4 | Fig04_ablation_data.csv | ok |
| Figure 5 | Fig05_history_sensitivity_data.csv | ok |
| Figure 6 | Fig06_volatility_error_data.csv | ok |
| Figure 7 | Fig07_missingness_stress_data.csv, Fig07_noise_stress_data.csv, Fig07_small_sample_training_data.csv, Fig07_degradation_summary_data.csv, phase8_small_sample_metrics.csv | ok, ok, ok, ok, ok |

        ## How To Validate The Package
        ```bash
        python scripts/00_check_environment.py
        python scripts/01_validate_data_package.py
        python scripts/02_generate_file_manifest.py
        python scripts/01_validate_data_package.py
        ```

        ## What Is Included
        Processed analytical data, figure-ready CSV files, YAML configs, public scripts, source experiment reports, data dictionary, file manifest, and reproducibility documentation.

        ## What Is Excluded
        Raw provider data, private raw files, provider response dumps, cache files, temporary logs, model checkpoints, and very large intermediate window-index files.

        ## Citation Placeholder
        Please cite the associated paper and this repository. See `CITATION.cff`.

        ## Contact Placeholder
        Please use the associated manuscript or institutional profile for correspondence.
