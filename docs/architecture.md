# 🏗️ Architecture

This project has two complementary analysis entry points.

## 1. Notebook workflow

`TimeSeriesForecasting.ipynb` provides a learner-oriented sequence:
1. Read and validate the monthly CSV.
2. Inspect the historical series.
3. Visualize trend and annual seasonality.
4. Run stationarity diagnostics.
5. Split observations chronologically.
6. Establish naive and seasonal-naive benchmarks.
7. Fit seasonal Exponential Smoothing and SARIMA models.
8. Evaluate the held-out period using MAE, RMSE, and MAPE.
9. Inspect residuals.
10. Refit and illustrate a future forecast.

## 2. Command-line workflow

`scripts/forecast.py` provides an executable reference implementation with:
- Dataset and schema validation.
- Continuous monthly-index validation.
- Chronological holdout evaluation.
- Seasonal Exponential Smoothing and SARIMA candidates.
- Forecast metrics and output files under `artifacts/`.

## Data flow

```text
AirPassengers.csv
       |
       v
Date parsing + validation
       |
       v
Monthly passenger series
       |
       +--> Chronological train/test split
       |            |
       |            v
       |      Baselines + fitted models
       |            |
       |            v
       |      Holdout metrics and plots
       |
       +--> Full history refit
                    |
                    v
             Future forecast
```

## Boundaries

There is no online API, database, model-serving service, or automated ingestion process. The checked-in CSV is the only input dataset. The forecasts are educational outputs, not an airline planning product.
