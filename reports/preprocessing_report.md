# Preprocessing Report

The original source was provider-level floating-car traffic data for the Pan Borneo Highway corridor in Sarawak, Malaysia. Raw provider records are not included.

The workflow aligns observations to an hourly modelling panel, standardizes monitoring point identifiers, derives traffic features, and constructs future-window speed targets. The main target is future-window mean speed based on `current_speed`.

Train, validation, and test splits are chronological. Scaling is fitted on training data only and then applied to validation and test data. This prevents temporal leakage. Public-release limitations are that raw records and some large intermediate indices are excluded.
