from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MAPPING = {
    "Figure 1": ["Fig01_workflow_data.csv"],
    "Figure 2": ["Fig02_main_forecasting_performance.csv"],
    "Figure 3": ["Fig03_five_seed_stability_mean_std.csv", "Fig03_seed_scatter.csv", "Fig03_improvement_boxplot.csv"],
    "Figure 4": ["Fig04_ablation_data.csv"],
    "Figure 5": ["Fig05_history_sensitivity_data.csv"],
    "Figure 6": ["Fig06_volatility_error_data.csv"],
    "Figure 7": ["Fig07_missingness_stress_data.csv", "Fig07_noise_stress_data.csv", "Fig07_small_sample_training_data.csv", "Fig07_degradation_summary_data.csv"],
}
print("This placeholder does not generate final manuscript figures.")
print("Final figure styling is manuscript-specific.")
for fig, files in MAPPING.items():
    print(fig)
    for file in files:
        print(f"  {file}: {'ok' if (ROOT / 'data' / 'plot_data' / file).exists() else 'missing'}")
