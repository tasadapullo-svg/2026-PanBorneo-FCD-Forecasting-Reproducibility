# Phase 13 Strong Baseline Experiment Gap Audit

## Scope

This is a scaffolding and audit deliverable only. No Phase 13 training has been run while creating these files. Raw data and the existing `reports/locked_phase*` outputs were not modified.

## Existing files reused

- `data/processed/phase2_panel_1h_model_ready.csv.gz`: the model-ready, one-hour panel.
- `outputs/tables/window_index_all.csv`: Phase 2 leakage-controlled window index and chronological split labels.
- `configs/phase2_window_construction.yaml`: source of the Phase 2 chronological, same-split windowing design.
- `scripts/phase3_run_baselines.py`: reference implementation for train-only HA/Seasonal HA tables and window filtering.
- `scripts/phase5_controlled_deep_training.py`: reference implementation for sequence construction and train-only feature/target scaling.

## New files

- `configs/phase13_strong_baselines.yaml`
- `scripts/phase13_strong_baselines.py`
- `run_phase13_strong_baselines_smoke.bat`
- `run_phase13_strong_baselines_full.bat`
- This audit report.

When executed, Phase 13 creates only `outputs/tables/phase13_strong_baseline_metrics.csv`, `outputs/predictions/phase13/*.parquet`, and `logs/phase13_strong_baselines_*.log`.

## Leakage and comparability controls

- Samples are selected exclusively from the Phase 2 window index, retaining its chronological `train`, `val`, and `test` labels.
- Every model for a given horizon is supplied the same filtered sample object, so test samples are identical across models and seeds.
- HA and Seasonal HA lookup tables are fitted only from observations no later than the Phase 2 training windows.
- Neural feature and target scalers are fitted only on training samples. XGBoost is not scaled because tree models do not require scaling.
- Inputs end at `input_end_time`; target-window values are only used to compute labels and metrics.
- The cleaned panel was checked during scaffold validation and contains 51 stable nodes. The runner enforces that network-wide count before training and records 51 in every metric row. Smoke caps may contain fewer observed nodes, but are only a mechanical preflight; the full run uses all feasible Phase 2 windows.

## Planned models

HA, Seasonal HA, Persistence, XGBoost, GRU, TCN, and ST-Transformer-lite. The ST-Transformer-lite combines learned stable-node embeddings with temporal positional embeddings and a compact Transformer encoder. Each model/horizon/seed writes a prediction parquet containing the required reproducibility columns.

## Commands

Smoke test (small caps and two epochs):

```bat
run_phase13_strong_baselines_smoke.bat
```

Full experiment (full cleaned dataset and 30-epoch maximum with validation early stopping):

```bat
run_phase13_strong_baselines_full.bat
```
