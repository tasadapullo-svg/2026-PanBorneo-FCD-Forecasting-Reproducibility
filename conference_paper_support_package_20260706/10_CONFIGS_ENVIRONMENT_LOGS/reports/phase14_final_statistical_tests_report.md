# Phase 14 Final Statistical Tests

- Phase 13 proposed-vs-baseline comparisons: paired sample-level Wilcoxon tests using locked prediction parquet files.
- Phase 15/16 comparisons: paired seed-level Wilcoxon tests on matched seed MAE values.
- Phase 17 strata: independent Kruskal-Wallis tests across stratum seed-level MAEs.
- Holm correction is applied within each output test family; effect sizes are rank-biserial correlation or epsilon-squared.

See the Phase 14 CSV tables for n_pairs/total_n, raw and corrected p-values, effects, and mean +/- std.
