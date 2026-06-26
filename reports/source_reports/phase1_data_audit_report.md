# Phase 1 Data Audit Report

## Data Source
- Primary panel: `04_panels/panel_1h.csv.gz`
- Rows in primary panel: 100,980
- Monitoring points: 51
- Time range: 2025-12-08 13:00:00 to 2026-03-01 00:00:00
- Inferred fields: `{"point_id": "node_id", "timestamp": "time_bin", "speed": "current_speed", "free_flow_speed": "free_flow_speed", "travel_time": "current_travel_time", "free_flow_travel_time": "free_flow_travel_time", "congestion": "tti", "has_observation": "has_observation", "missing_mask": "missing_mask", "observed_count": "observed_count"}`

## Inventory
- Files scanned: 31
- CSV/GZ files scanned with row counts: 23

## Missingness and Coverage
- Median point coverage ratio: 0.962
- Mean point coverage ratio: 0.962
- High/medium/low coverage points: {'high': 51}
- Worst max consecutive missing steps: 25
- Mean timestamp coverage ratio: 0.962

## Continuity and Validity
- Duplicate point-timestamp rows in primary panel: 0
- Points with timeline gaps larger than inferred frequency: 0
- Speed anomaly rows: 0
- Travel-time anomaly rows: 0
- Congestion anomaly rows: 0

## Train/Val/Test Split
| split | start_time | end_time | time_steps | rows | points |
| --- | --- | --- | --- | --- | --- |
| train | 2025-12-08 13:00:00 | 2026-02-04 06:00:00 | 1386 | 70686 | 51 |
| val | 2026-02-04 07:00:00 | 2026-02-16 15:00:00 | 297 | 15147 | 51 |
| test | 2026-02-16 16:00:00 | 2026-03-01 00:00:00 | 297 | 15147 | 51 |

## One-Week Forecasting Feasibility
- Fully observed target windows for 168h history -> 168h horizon: 16,337
- Ratio among candidate windows: 0.1947
- Fully observed target windows for 72h history -> 24h horizon: 69,006
- Direct 1-week recommendation: direct 7-day forecasting can be retained as a stress-test target, but it should not be the only task.

## Required Output Files
- `outputs/tables/data_inventory.csv`
- `outputs/tables/missing_summary.csv`
- `outputs/tables/coverage_by_point.csv`
- `outputs/tables/time_coverage_summary.csv`
- `outputs/tables/coverage_by_time.csv`
- `outputs/tables/time_continuity_check.csv`
- `outputs/tables/point_quality_summary.csv`
- `outputs/tables/train_val_test_split_summary.csv`
- `outputs/tables/window_feasibility_summary.csv`
- `outputs/logs/phase1_data_audit.log`

## Next Phase
Build leakage-free rolling-window indices from the time-ordered split, retain missing masks and coverage/reliability variables, and begin with Persistence and Historical Average baselines before adding tree and neural models.
