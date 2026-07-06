# Phase 10 Benchmark Data Preparation Report

## Status

Phase 10 public benchmark data preparation is complete. No Phase 10 training was run.

## Dataset

- Dataset name: METR-LA
- Role in this project: supplementary public benchmark sanity check only
- Source used: Zenodo record "PEMS-BAY and METR-LA in csv"
- Source URL: https://zenodo.org/records/5146275
- Downloaded file: `METR-LA.csv`

## Local Files

- Primary local file: `D:\2026_PD\data\benchmark\METR-LA-mini\METR-LA.csv`
- Compressed copy: `D:\2026_PD\data\benchmark\METR-LA-mini\METR-LA.csv.gz`
- File format: CSV and CSV.GZ
- Original CSV size: 72,802,450 bytes
- Compressed CSV.GZ size: 13,096,857 bytes

## Read Verification

- Read method: `pandas.read_csv`
- DataFrame shape: `(34272, 208)`
- Number of time steps: `34272`
- Total columns: `208`
- First column: `Unnamed: 0`
- First column appears timestamp/index-like: `True`
- Numeric sensor-speed columns after the first column: `207`
- Missing value count: `0`

First 10 columns:

```text
['Unnamed: 0', '773869', '767541', '767542', '717447', '717446', '717445', '773062', '767620', '737529']
```

First 10 dtypes:

```text
Unnamed: 0     object
773869        float64
767541        float64
767542        float64
717447        float64
717446        float64
717445        float64
773062        float64
767620        float64
737529        float64
```

## Phase 10 Readiness

- Phase 10 can be run: `Yes`
- Recommended Phase 10 input: `D:\2026_PD\data\benchmark\METR-LA-mini\METR-LA.csv`
- Alternative compressed input: `D:\2026_PD\data\benchmark\METR-LA-mini\METR-LA.csv.gz`
- The remaining columns after `Unnamed: 0` appear to be numeric sensor-speed columns.
- The first column can be treated as the timestamp/index column.

## Script Format Support

- `scripts/phase10_public_benchmark_sanity.py` already supports `.csv` and `.csv.gz`.
- `.h5` support is not required for this prepared METR-LA CSV dataset.
- No Phase 10 script update was needed for data preparation.

## Methodological Note

Phase 10 must remain a supplementary public benchmark sanity check. It should verify that the implemented speed-only TCN forecasting pipeline can run on a public traffic speed matrix. It should not be described as a state-of-the-art comparison or a comprehensive benchmark study.
