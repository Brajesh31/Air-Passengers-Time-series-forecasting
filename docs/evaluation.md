# 📏 Forecast Evaluation

Forecast performance must be measured on observations that occur after the training period. Random train/test splitting is inappropriate for this chronological forecasting task.

## Metrics

### Mean Absolute Error (MAE)

`MAE = mean(|actual - forecast|)`

MAE is expressed in the same units as passenger counts.

### Root Mean Squared Error (RMSE)

`RMSE = sqrt(mean((actual - forecast)^2))`

RMSE also uses the target units and penalizes large errors more strongly.

### Mean Absolute Percentage Error (MAPE)

`MAPE = mean(|(actual - forecast) / actual|) * 100`

MAPE is percentage-based but can behave poorly near zero and can overemphasize low-volume months. Do not use it alone.

### R-squared caution

R-squared is primarily a regression goodness-of-fit statistic. It is not sufficient for comparing forecast models and can be negative on held-out observations. Prefer MAE and RMSE, plus baseline comparisons and residual diagnostics.

## Baselines

At minimum, compare a model with:
- Naive forecast: the most recent observed value.
- Seasonal naive forecast: the observation from the same month in the previous year.

A complex model that does not beat a simple seasonal baseline is not adding demonstrated forecasting value.

## Validation design

Use a chronological holdout and, where possible, rolling-origin backtesting. Record the train end date, test start/end dates, horizon, model order, seasonal period, and any transformations.

The command-line reference implementation reports MAE, RMSE, and MAPE for a 24-month chronological holdout and exports predictions. It does not constitute independent operational validation.
