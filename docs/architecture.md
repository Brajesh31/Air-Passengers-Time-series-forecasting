# Analysis architecture

The notebook follows a linear analytical workflow:

1. Load and inspect `AirPassengers.csv`.
2. Parse monthly observations and visualize trend and seasonality.
3. Transform or decompose the series as needed.
4. Train forecasting models using time-aware splits.
5. Compare predictions with held-out observations using documented metrics.

Future work should preserve temporal ordering and avoid leakage from future observations.
