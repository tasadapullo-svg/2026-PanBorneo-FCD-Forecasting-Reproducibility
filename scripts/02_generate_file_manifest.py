from __future__ import annotations
import hashlib
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "file_manifest.csv"
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()
def purpose(rel: str) -> str:
    if rel.startswith("data/plot_data/deprecated/"):
        return "deprecated figure-data traceability"
    if rel.startswith("data/plot_data/"):
        return "figure-ready plotting data"
    if rel.startswith("data/processed/"):
        return "processed analytical data"
    if rel.startswith("configs/"):
        return "experiment configuration"
    if rel.startswith("scripts/original_project_scripts/"):
        return "source project reproducibility script"
    if rel.startswith("scripts/"):
        return "release validation helper"
    if rel.startswith("reports/"):
        return "reproducibility report"
    if rel.startswith("docs/"):
        return "documentation"
    return "package metadata"
def status(rel: str) -> str:
    if rel.startswith("data/plot_data/deprecated/"):
        return "deprecated"
    if rel.startswith("data/plot_data/") or rel.startswith("data/processed/"):
        return "include_aggregated"
    return "include"
rows = []
for path in sorted(ROOT.rglob("*")):
    if path.is_dir():
        continue
    if ".git" in path.relative_to(ROOT).parts:
        continue
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    nrows = ncols = ""
    if path.suffix.lower() == ".csv":
        try:
            df = pd.read_csv(path)
            nrows, ncols = len(df), len(df.columns)
        except Exception:
            nrows = ncols = "unreadable"
    rows.append({
        "relative_path": rel,
        "file_name": path.name,
        "file_type": path.suffix.lower().lstrip(".") or "no_extension",
        "file_size_kb": round(path.stat().st_size / 1024, 3),
        "rows": nrows,
        "columns": ncols,
        "sha256": sha256(path),
        "purpose": purpose(rel),
        "public_release_status": status(rel),
        "notes": "generated release manifest",
    })
pd.DataFrame(rows).to_csv(OUT, index=False, encoding="utf-8-sig")
print(f"Manifest written. files={len(rows)}")
