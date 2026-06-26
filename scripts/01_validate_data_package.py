from __future__ import annotations
import re
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "data_package_validation_report.md"
words = ["api" + "_" + "key", "to" + "ken", "pass" + "word", "se" + "cret", "creden" + "tial", "em" + "ail", "ph" + "one"]
SUSPICIOUS = re.compile("|".join(words), re.IGNORECASE)
ABS_PATH = re.compile(r"(?:" + "|".join(re.escape(d + ":") for d in ["D", "C", "E"]) + r")(?:\\|/)")
private_words = ["raw" + "_" + "private", "api" + "_" + "response", "creden" + "tial", "to" + "ken", "ca" + "che"]
PRIVATE = re.compile("|".join(private_words), re.IGNORECASE)
REQUIRED = {
    "Figure 1": ["Fig01_workflow_data.csv"],
    "Figure 2": ["Fig02_main_forecasting_performance.csv"],
    "Figure 3": ["Fig03_five_seed_stability_mean_std.csv", "Fig03_seed_scatter.csv", "Fig03_improvement_boxplot.csv"],
    "Figure 4": ["Fig04_ablation_data.csv"],
    "Figure 5": ["Fig05_history_sensitivity_data.csv"],
    "Figure 6": ["Fig06_volatility_error_data.csv"],
    "Figure 7": ["Fig07_missingness_stress_data.csv", "Fig07_noise_stress_data.csv", "Fig07_small_sample_training_data.csv", "Fig07_degradation_summary_data.csv", "phase8_small_sample_metrics.csv"],
}
def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")
rows, warnings = [], []
for path in sorted(ROOT.rglob("*")):
    if path.is_dir():
        name = rel(path)
        if PRIVATE.search(name) or "/raw/" in f"/{name.lower()}/":
            warnings.append(f"private-like folder: {name}")
        continue
    name = rel(path)
    if PRIVATE.search(name) or "/raw/" in f"/{name.lower()}":
        warnings.append(f"private-like file path: {name}")
    if path.suffix.lower() in {".csv", ".md", ".py", ".yaml", ".yml", ".cff", ".gitignore"}:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if SUSPICIOUS.search(text) and not name.endswith("01_validate_data_package.py"):
            warnings.append(f"suspicious text keyword: {name}")
        if ABS_PATH.search(text):
            warnings.append(f"absolute local path: {name}")
    if path.suffix.lower() == ".csv":
        try:
            df = pd.read_csv(path)
            rows.append((name, len(df), len(df.columns), ", ".join(df.columns)))
            if len(df) == 0:
                warnings.append(f"empty CSV: {name}")
            if len(df.columns) != len(set(df.columns)):
                warnings.append(f"duplicate columns: {name}")
        except Exception as exc:
            warnings.append(f"unreadable CSV: {name}: {exc}")
lines = ["# Data Package Validation Report", "", "## CSV Files", "", "| file | rows | columns | column_names |", "| --- | ---: | ---: | --- |"]
for name, nrows, ncols, cols in rows:
    lines.append(f"| {name} | {nrows} | {ncols} | {cols.replace('|', '/')} |")
lines += ["", "## Figure Data Status", "", "| figure | file | status |", "| --- | --- | --- |"]
for fig, files in REQUIRED.items():
    for file in files:
        status = "ok" if (ROOT / "data" / "plot_data" / file).exists() else "missing"
        lines.append(f"| {fig} | {file} | {status} |")
lines += ["", "## Warnings", ""]
lines += [f"- {w}" for w in warnings] if warnings else ["- none"]
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Validation complete. CSV files={len(rows)} warnings={len(warnings)}")
