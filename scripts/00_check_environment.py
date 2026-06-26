from __future__ import annotations
import importlib.util
import platform
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
print("Python:", sys.version.replace("\n", " "))
print("Platform:", platform.platform())
for name in ["pandas", "numpy", "matplotlib"]:
    print(f"{name}:", "available" if importlib.util.find_spec(name) else "missing")
for rel in ["data", "data/processed", "data/plot_data", "configs", "scripts", "reports", "docs", "figures"]:
    print(f"{rel}:", "exists" if (ROOT / rel).exists() else "missing")
print("Environment check complete.")
