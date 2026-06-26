from __future__ import annotations

import argparse
import logging
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import yaml


@dataclass
class MetricAccumulator:
    n: int = 0
    ae_sum: float = 0.0
    se_sum: float = 0.0
    ape_sum: float = 0.0
    ape_n: int = 0
    smape_sum: float = 0.0
    y_sum: float = 0.0
    y_sq_sum: float = 0.0
    sse_sum: float = 0.0

    def update(self, y_true: np.ndarray, y_pred: np.ndarray) -> None:
        mask = np.isfinite(y_true) & np.isfinite(y_pred)
        if not mask.any():
            return
        yt = y_true[mask].astype(float)
        yp = y_pred[mask].astype(float)
        err = yp - yt
        self.n += int(len(yt))
        self.ae_sum += float(np.abs(err).sum())
        self.se_sum += float(np.square(err).sum())
        safe = np.abs(yt) > 1e-8
        self.ape_sum += float((np.abs(err[safe]) / np.abs(yt[safe])).sum())
        self.ape_n += int(safe.sum())
        denom = np.abs(yt) + np.abs(yp)
        smape_mask = denom > 1e-8
        self.smape_sum += float((2.0 * np.abs(err[smape_mask]) / denom[smape_mask]).sum())
        self.y_sum += float(yt.sum())
        self.y_sq_sum += float(np.square(yt).sum())
        self.sse_sum += float(np.square(err).sum())

    def as_dict(self) -> dict:
        if self.n == 0:
            return {"n": 0, "MAE": np.nan, "RMSE": np.nan, "MAPE": np.nan, "sMAPE": np.nan, "R2": np.nan}
        mae = self.ae_sum / self.n
        rmse = math.sqrt(self.se_sum / self.n)
        mape = self.ape_sum / self.ape_n if self.ape_n else np.nan
        smape = self.smape_sum / self.n
        y_mean = self.y_sum / self.n
        sst = self.y_sq_sum - self.n * y_mean * y_mean
        r2 = 1.0 - self.sse_sum / sst if sst > 1e-12 else np.nan
        return {"n": self.n, "MAE": mae, "RMSE": rmse, "MAPE": mape, "sMAPE": smape, "R2": r2}


def read_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def setup_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("phase3_baseline")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


def standardize_panel_columns(panel: pd.DataFrame) -> pd.DataFrame:
    panel = panel.copy()
    if "point_id" not in panel.columns and "node_id" in panel.columns:
        panel["point_id"] = panel["node_id"]
    if "timestamp" not in panel.columns and "time_bin" in panel.columns:
        panel["timestamp"] = pd.to_datetime(panel["time_bin"])
    elif "timestamp" in panel.columns:
        panel["timestamp"] = pd.to_datetime(panel["timestamp"])
    if "hour_of_day" not in panel.columns and "hour" in panel.columns:
        panel["hour_of_day"] = panel["hour"]
    if "weekend_flag" not in panel.columns and "day_of_week" in panel.columns:
        panel["weekend_flag"] = (pd.to_numeric(panel["day_of_week"], errors="coerce").fillna(0) >= 5).astype(int)
    return panel


def validate_task_config(cfg: dict) -> None:
    task = cfg["task"]
    if task["target_variable"] != "speed":
        raise ValueError("Phase 3 baseline script is restricted to target_variable='speed'.")
    if task["target_column"] != "current_speed":
        raise ValueError("Phase 3 baseline script requires target_column='current_speed'.")
    if sorted(task["horizons_hours"]) != [1, 3, 6, 12, 24]:
        raise ValueError("Phase 3 main horizons must be exactly [1, 3, 6, 12, 24].")
    if 168 in task["horizons_hours"]:
        raise ValueError("168h horizon must not be included in Phase 3 main horizons.")
    if 168 not in task["excluded_horizons_hours"]:
        raise ValueError("168h horizon must remain excluded from the main baseline run.")


def load_panel(path: Path, target_col: str) -> pd.DataFrame:
    panel = pd.read_csv(path)
    panel = standardize_panel_columns(panel)
    required = {"point_id", "timestamp", target_col, "missing_mask", "hour_of_day", "day_of_week", "weekend_flag"}
    missing = required - set(panel.columns)
    if missing:
        raise ValueError(f"Panel file is missing required columns: {sorted(missing)}")
    panel = panel.sort_values(["point_id", "timestamp"]).reset_index(drop=True)
    return panel


def build_point_arrays(panel: pd.DataFrame, target_col: str) -> dict[str, dict[str, np.ndarray]]:
    arrays: dict[str, dict[str, np.ndarray]] = {}
    for point_id, g in panel.groupby("point_id", sort=True):
        g = g.sort_values("timestamp").reset_index(drop=True)
        arrays[str(point_id)] = {
            "time": g["timestamp"].to_numpy(),
            "speed": pd.to_numeric(g[target_col], errors="coerce").to_numpy(dtype=float),
            "missing_mask": pd.to_numeric(g["missing_mask"], errors="coerce").fillna(1).to_numpy(dtype=float),
            "hour_of_day": pd.to_numeric(g["hour_of_day"], errors="coerce").fillna(0).to_numpy(dtype=int),
            "day_of_week": pd.to_numeric(g["day_of_week"], errors="coerce").fillna(0).to_numpy(dtype=int),
            "weekend_flag": pd.to_numeric(g["weekend_flag"], errors="coerce").fillna(0).to_numpy(dtype=int),
        }
    return arrays


def load_split_ranges(path: Path) -> dict[str, tuple[pd.Timestamp, pd.Timestamp]]:
    split = pd.read_csv(path, parse_dates=["start_time", "end_time"])
    return {row["split"]: (row["start_time"], row["end_time"]) for _, row in split.iterrows()}


def fit_average_tables(panel: pd.DataFrame, split_ranges: dict[str, tuple[pd.Timestamp, pd.Timestamp]], target_col: str) -> dict:
    train_start, train_end = split_ranges["train"]
    train = panel[(panel["timestamp"] >= train_start) & (panel["timestamp"] <= train_end)].copy()
    global_mean = float(train[target_col].mean())
    point_mean = train.groupby("point_id")[target_col].mean().to_dict()
    seasonal = train.groupby(["point_id", "hour_of_day", "day_of_week"])[target_col].mean().to_dict()
    seasonal_hour = train.groupby(["point_id", "hour_of_day"])[target_col].mean().to_dict()
    return {
        "global_mean": global_mean,
        "point_mean": point_mean,
        "seasonal": seasonal,
        "seasonal_hour": seasonal_hour,
    }


def iter_filtered_windows(cfg: dict) -> Iterable[pd.DataFrame]:
    task = cfg["task"]
    usecols = [
        "window_id",
        "point_id",
        "input_start_time",
        "input_end_time",
        "target_start_time",
        "target_end_time",
        "history_hours",
        "horizon_hours",
        "split",
        "target_variable",
        "input_observed_ratio",
        "target_observed_ratio",
        "is_main_forecast",
        "is_extended_horizon",
    ]
    parse_dates = ["input_start_time", "input_end_time", "target_start_time", "target_end_time"]
    for chunk in pd.read_csv(
        cfg["paths"]["window_index"],
        usecols=usecols,
        parse_dates=parse_dates,
        chunksize=int(cfg["runtime"]["window_chunksize"]),
    ):
        mask = (
            chunk["target_variable"].eq(task["target_variable"])
            & chunk["history_hours"].isin(task["histories_hours"])
            & chunk["horizon_hours"].isin(task["horizons_hours"])
            & ~chunk["horizon_hours"].isin(task["excluded_horizons_hours"])
            & chunk["is_main_forecast"].eq(1)
            & chunk["is_extended_horizon"].eq(0)
            & (chunk["input_observed_ratio"] >= float(task["min_input_observed_ratio"]))
            & (chunk["target_observed_ratio"] >= float(task["min_target_observed_ratio"]))
        )
        filtered = chunk.loc[mask].copy()
        if not filtered.empty:
            yield filtered


def time_to_index(times: np.ndarray, timestamp: pd.Timestamp) -> int:
    idx = np.searchsorted(times, np.datetime64(timestamp), side="left")
    if idx >= len(times) or times[idx] != np.datetime64(timestamp):
        raise KeyError(f"Timestamp {timestamp} not found in point timeline")
    return int(idx)


def linear_trend(values: np.ndarray) -> float:
    mask = np.isfinite(values)
    if mask.sum() <= 1:
        return 0.0
    y = values[mask]
    x = np.arange(len(values), dtype=float)[mask]
    x = x - x.mean()
    denom = float(np.square(x).sum())
    if denom <= 1e-12:
        return 0.0
    return float((x * (y - y.mean())).sum() / denom)


def target_mean(values: np.ndarray) -> float:
    finite = values[np.isfinite(values)]
    if len(finite) == 0:
        return np.nan
    return float(finite.mean())


def seasonal_prediction(
    point_id: str,
    target_start_idx: int,
    horizon_steps: int,
    arrays: dict[str, np.ndarray],
    average_tables: dict,
) -> float:
    preds = []
    for idx in range(target_start_idx, target_start_idx + horizon_steps):
        hour = int(arrays["hour_of_day"][idx])
        dow = int(arrays["day_of_week"][idx])
        pred = average_tables["seasonal"].get((point_id, hour, dow))
        if pred is None or not np.isfinite(pred):
            pred = average_tables["seasonal_hour"].get((point_id, hour))
        if pred is None or not np.isfinite(pred):
            pred = average_tables["point_mean"].get(point_id, average_tables["global_mean"])
        preds.append(float(pred))
    return float(np.mean(preds))


def build_feature_rows(windows: pd.DataFrame, point_arrays: dict[str, dict[str, np.ndarray]], average_tables: dict) -> pd.DataFrame:
    rows = []
    for row in windows.itertuples(index=False):
        point_id = str(row.point_id)
        arrays = point_arrays[point_id]
        times = arrays["time"]
        input_start_idx = time_to_index(times, row.input_start_time)
        input_end_idx = time_to_index(times, row.input_end_time)
        target_start_idx = time_to_index(times, row.target_start_time)
        target_end_idx = time_to_index(times, row.target_end_time)

        input_speed = arrays["speed"][input_start_idx : input_end_idx + 1]
        target_speed = arrays["speed"][target_start_idx : target_end_idx + 1]
        input_missing = arrays["missing_mask"][input_start_idx : input_end_idx + 1]
        y = target_mean(target_speed)
        if not np.isfinite(y):
            continue

        finite_input = input_speed[np.isfinite(input_speed)]
        if len(finite_input) == 0:
            last_speed = average_tables["point_mean"].get(point_id, average_tables["global_mean"])
            mean_speed = last_speed
            std_speed = 0.0
            min_speed = last_speed
            max_speed = last_speed
            trend = 0.0
        else:
            last_finite_idx = np.where(np.isfinite(input_speed))[0][-1]
            last_speed = float(input_speed[last_finite_idx])
            mean_speed = float(finite_input.mean())
            std_speed = float(finite_input.std(ddof=1)) if len(finite_input) > 1 else 0.0
            min_speed = float(finite_input.min())
            max_speed = float(finite_input.max())
            trend = linear_trend(input_speed)

        input_end_hour = int(pd.Timestamp(row.input_end_time).hour)
        input_end_dow = int(pd.Timestamp(row.input_end_time).dayofweek)
        horizon_steps = int(row.horizon_hours)
        seasonal_pred = seasonal_prediction(point_id, target_start_idx, horizon_steps, arrays, average_tables)

        rows.append(
            {
                "window_id": int(row.window_id),
                "point_id": point_id,
                "split": row.split,
                "history_hours": int(row.history_hours),
                "horizon_hours": int(row.horizon_hours),
                "y_true": y,
                "persistence_pred": last_speed,
                "historical_average_pred": float(average_tables["point_mean"].get(point_id, average_tables["global_mean"])),
                "seasonal_historical_average_pred": seasonal_pred,
                "last_speed": last_speed,
                "mean_speed": mean_speed,
                "std_speed": std_speed,
                "min_speed": min_speed,
                "max_speed": max_speed,
                "speed_trend": trend,
                "missing_ratio": float(np.nanmean(input_missing)),
                "coverage_ratio": float(row.input_observed_ratio),
                "hour_of_day": input_end_hour,
                "day_of_week": input_end_dow,
                "weekend_flag": int(input_end_dow >= 5),
            }
        )
    return pd.DataFrame(rows)


def collect_feature_matrix(cfg: dict, point_arrays: dict[str, dict[str, np.ndarray]], average_tables: dict, logger: logging.Logger) -> pd.DataFrame:
    frames = []
    max_rows_per_split = cfg["runtime"].get("max_rows_per_split")
    split_seen: dict[str, int] = {}
    for chunk_idx, windows in enumerate(iter_filtered_windows(cfg), start=1):
        features = build_feature_rows(windows, point_arrays, average_tables)
        if max_rows_per_split is not None:
            kept_parts = []
            for split, g in features.groupby("split", sort=False):
                already = split_seen.get(split, 0)
                remaining = int(max_rows_per_split) - already
                if remaining <= 0:
                    continue
                keep = g.head(remaining)
                split_seen[split] = already + len(keep)
                kept_parts.append(keep)
            features = pd.concat(kept_parts, ignore_index=True) if kept_parts else pd.DataFrame()
        if not features.empty:
            frames.append(features)
        logger.info("Processed window chunk %s; accumulated feature frames=%s", chunk_idx, len(frames))
    if not frames:
        raise ValueError("No Phase 3 feature rows were created. Check filters and Phase 2 outputs.")
    out = pd.concat(frames, ignore_index=True)
    if cfg["runtime"].get("save_feature_matrix", False):
        path = Path(cfg["runtime"]["feature_matrix_path"])
        path.parent.mkdir(parents=True, exist_ok=True)
        out.to_csv(path, index=False, compression="gzip")
        logger.info("Saved feature matrix to %s", path)
    return out


def metric_rows(df: pd.DataFrame, pred_col: str, model_name: str, group_cols: list[str]) -> list[dict]:
    rows = []
    if group_cols:
        iterator = df.groupby(group_cols, dropna=False)
    else:
        iterator = [((), df)]
    for key, g in iterator:
        key_tuple = key if isinstance(key, tuple) else (key,)
        acc = MetricAccumulator()
        acc.update(g["y_true"].to_numpy(dtype=float), g[pred_col].to_numpy(dtype=float))
        row = {"model": model_name}
        for col, value in zip(group_cols, key_tuple):
            row[col] = value
        row.update(acc.as_dict())
        rows.append(row)
    return rows


def fit_predict_ridge(features: pd.DataFrame, cfg: dict, logger: logging.Logger) -> pd.Series:
    try:
        from sklearn.compose import ColumnTransformer
        from sklearn.linear_model import Ridge
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import OneHotEncoder, StandardScaler
    except ImportError as exc:
        raise ImportError("Ridge baseline requires scikit-learn in the local conda environment.") from exc

    numeric = [
        "last_speed",
        "mean_speed",
        "std_speed",
        "min_speed",
        "max_speed",
        "speed_trend",
        "missing_ratio",
        "coverage_ratio",
        "hour_of_day",
        "day_of_week",
        "weekend_flag",
        "history_hours",
        "horizon_hours",
    ]
    categorical = ["point_id"]
    train = features["split"].eq("train")
    pre = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ]
    )
    model = Pipeline([("preprocess", pre), ("ridge", Ridge(alpha=float(cfg["baselines"]["ridge_regression"]["alpha"])))])
    logger.info("Fitting Ridge baseline on %s training rows", int(train.sum()))
    model.fit(features.loc[train, numeric + categorical], features.loc[train, "y_true"])
    return pd.Series(model.predict(features[numeric + categorical]), index=features.index)


def fit_predict_random_forest(features: pd.DataFrame, cfg: dict, logger: logging.Logger) -> pd.Series:
    try:
        from sklearn.compose import ColumnTransformer
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.pipeline import Pipeline
        from sklearn.preprocessing import OneHotEncoder
    except ImportError as exc:
        raise ImportError("Random Forest baseline requires scikit-learn in the local conda environment.") from exc

    rf_cfg = cfg["baselines"]["random_forest"]
    numeric = [
        "last_speed",
        "mean_speed",
        "std_speed",
        "min_speed",
        "max_speed",
        "speed_trend",
        "missing_ratio",
        "coverage_ratio",
        "hour_of_day",
        "day_of_week",
        "weekend_flag",
        "history_hours",
        "horizon_hours",
    ]
    categorical = ["point_id"]
    train_idx = features.index[features["split"].eq("train")]
    max_train_rows = rf_cfg.get("max_train_rows")
    if max_train_rows is not None and len(train_idx) > int(max_train_rows):
        train_idx = train_idx[: int(max_train_rows)]
        logger.info("Random Forest train rows capped at %s by config", len(train_idx))
    pre = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numeric),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ]
    )
    model = Pipeline(
        [
            ("preprocess", pre),
            (
                "rf",
                RandomForestRegressor(
                    n_estimators=int(rf_cfg["n_estimators"]),
                    max_depth=rf_cfg["max_depth"],
                    min_samples_leaf=int(rf_cfg["min_samples_leaf"]),
                    n_jobs=int(rf_cfg["n_jobs"]),
                    random_state=int(cfg["project"]["random_seed"]),
                ),
            ),
        ]
    )
    logger.info("Fitting Random Forest baseline on %s training rows", len(train_idx))
    model.fit(features.loc[train_idx, numeric + categorical], features.loc[train_idx, "y_true"])
    return pd.Series(model.predict(features[numeric + categorical]), index=features.index)


def write_metrics(features: pd.DataFrame, prediction_cols: dict[str, str], out_tables: Path) -> None:
    all_rows = []
    by_horizon = []
    by_history = []
    by_point = []
    for model, pred_col in prediction_cols.items():
        all_rows.extend(metric_rows(features, pred_col, model, ["split"]))
        by_horizon.extend(metric_rows(features, pred_col, model, ["split", "horizon_hours"]))
        by_history.extend(metric_rows(features, pred_col, model, ["split", "history_hours"]))
        by_point.extend(metric_rows(features, pred_col, model, ["split", "point_id"]))

    pd.DataFrame(all_rows).to_csv(out_tables / "phase3_baseline_metrics.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(by_horizon).to_csv(out_tables / "phase3_baseline_metrics_by_horizon.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(by_history).to_csv(out_tables / "phase3_baseline_metrics_by_history.csv", index=False, encoding="utf-8-sig")
    pd.DataFrame(by_point).to_csv(out_tables / "phase3_baseline_metrics_by_point.csv", index=False, encoding="utf-8-sig")


def write_report(path: Path, cfg: dict, runtimes: list[dict], metrics: pd.DataFrame) -> None:
    test_metrics = metrics[metrics["split"].eq("test")].copy()
    lines = [
        "# Phase 3 Baseline Report",
        "",
        "Phase 3 ran baseline models for the main forecasting task only. No deep learning or benchmark experiments are included.",
        "",
        "## Scope",
        f"- Target variable: `{cfg['task']['target_variable']}`",
        f"- Histories: {cfg['task']['histories_hours']}",
        f"- Horizons: {cfg['task']['horizons_hours']}",
        f"- Excluded horizons: {cfg['task']['excluded_horizons_hours']}",
        f"- Target aggregation: `{cfg['task']['target_aggregation']}` over the target window",
        "",
        "## Test Metrics",
        dataframe_to_markdown(test_metrics),
        "",
        "## Runtime Summary",
        dataframe_to_markdown(pd.DataFrame(runtimes)),
        "",
        "## Leakage Controls",
        "- Phase 3 consumes Phase 2 windows where `is_main_forecast=1` and `is_extended_horizon=0`.",
        "- Features are computed only from `input_start_time` through `input_end_time`.",
        "- Historical and seasonal averages are fitted from the chronological train panel only.",
        "- Labels are computed from the target window only for metric evaluation.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def dataframe_to_markdown(df: pd.DataFrame, max_rows: int = 40) -> str:
    if df.empty:
        return "_No rows._"
    view = df.head(max_rows).copy()
    cols = list(view.columns)
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    if len(df) > max_rows:
        lines.append(f"\n_Showing first {max_rows} of {len(df)} rows._")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/phase3_baselines.yaml")
    args = parser.parse_args()
    cfg = read_config(Path(args.config))
    validate_task_config(cfg)

    out_tables = Path(cfg["paths"]["output_tables"])
    out_logs = Path(cfg["paths"]["output_logs"])
    reports = Path(cfg["paths"]["reports"])
    out_tables.mkdir(parents=True, exist_ok=True)
    out_logs.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)
    logger = setup_logger(out_logs / "phase3_baseline.log")
    logger.info("Starting Phase 3 baseline run")

    runtimes = []
    t0 = time.perf_counter()
    panel = load_panel(Path(cfg["paths"]["panel_1h"]), cfg["task"]["target_column"])
    point_arrays = build_point_arrays(panel, cfg["task"]["target_column"])
    split_ranges = load_split_ranges(Path(cfg["paths"]["split_summary"]))
    average_tables = fit_average_tables(panel, split_ranges, cfg["task"]["target_column"])
    runtimes.append({"stage": "load_panel_and_fit_average_tables", "seconds": round(time.perf_counter() - t0, 3)})

    t0 = time.perf_counter()
    features = collect_feature_matrix(cfg, point_arrays, average_tables, logger)
    runtimes.append({"stage": "build_feature_matrix", "seconds": round(time.perf_counter() - t0, 3), "rows": len(features)})
    logger.info("Feature matrix rows: %s", len(features))

    prediction_cols = {}
    if cfg["baselines"]["persistence"]["enabled"]:
        prediction_cols["Persistence"] = "persistence_pred"
    if cfg["baselines"]["historical_average"]["enabled"]:
        prediction_cols["HistoricalAverage"] = "historical_average_pred"
    if cfg["baselines"]["seasonal_historical_average"]["enabled"]:
        prediction_cols["SeasonalHistoricalAverage"] = "seasonal_historical_average_pred"

    if cfg["baselines"]["ridge_regression"]["enabled"]:
        t0 = time.perf_counter()
        features["ridge_regression_pred"] = fit_predict_ridge(features, cfg, logger)
        runtimes.append({"stage": "ridge_regression", "seconds": round(time.perf_counter() - t0, 3), "rows": len(features)})
        prediction_cols["RidgeRegression"] = "ridge_regression_pred"

    if cfg["baselines"]["random_forest"]["enabled"]:
        t0 = time.perf_counter()
        features["random_forest_pred"] = fit_predict_random_forest(features, cfg, logger)
        runtimes.append({"stage": "random_forest", "seconds": round(time.perf_counter() - t0, 3), "rows": len(features)})
        prediction_cols["RandomForest"] = "random_forest_pred"

    t0 = time.perf_counter()
    write_metrics(features, prediction_cols, out_tables)
    runtimes.append({"stage": "write_metrics", "seconds": round(time.perf_counter() - t0, 3), "rows": len(features)})
    runtime_df = pd.DataFrame(runtimes)
    runtime_df.to_csv(out_tables / "phase3_baseline_runtime_summary.csv", index=False, encoding="utf-8-sig")

    metrics = pd.read_csv(out_tables / "phase3_baseline_metrics.csv")
    write_report(reports / "phase3_baseline_report.md", cfg, runtimes, metrics)
    logger.info("Phase 3 baseline run completed")


if __name__ == "__main__":
    main()
