# Leakage-Control Protocol

The workflow uses a temporal train/validation/test split. Feature and target scalers are fitted on training data only. Features avoid future target-window information. Targets are constructed by forecast horizon. Seed repetition supports stability assessment. Fair comparisons use consistent validation and test periods.
