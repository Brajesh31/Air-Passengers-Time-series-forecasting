# 📚 Model Reference

## 1. Purpose

This guide describes the model families currently used in the repository and clarifies where each appears. It distinguishes implemented methods from possible future work. The presence of a model in a general forecasting textbook or an earlier project description does not mean that it is implemented here.

## 2. Implementation map

| Method | Notebook | CLI script | Status |
|---|---:|---:|---|
| Naive forecast | Yes | No full baseline output | Implemented in notebook |
| Seasonal-naive forecast | Yes | No full baseline output | Implemented in notebook |
| Seasonal Exponential Smoothing | Yes | Yes | Implemented |
| SARIMA | Yes | Yes | Implemented |
| LSTM / neural network | No | No | Not implemented |
| Prophet | No | No | Not implemented |
| XGBoost | No | No | Not implemented |

## 3. Naive forecast

The naive forecast repeats the final training observation for every date in the forecast horizon. It is a minimal benchmark and can be useful when the series changes slowly. It does not explicitly model annual seasonality.

## 4. Seasonal-naive forecast

The seasonal-naive forecast repeats the last available seasonal cycle. For monthly data with an annual period, it uses the latest 12 training observations and repeats them across the forecast horizon.

This is a strong baseline for a series with stable annual seasonality. It is not a fitted statistical model, but it provides an important reference point.

## 5. Exponential Smoothing

The project uses statsmodels' `ExponentialSmoothing` with an additive trend, additive seasonal component, and seasonal period of 12. The model estimates level, trend, and seasonal behaviour from the training series.

### Assumptions and interpretation

- The seasonal cycle is represented by a fixed period.
- Additive seasonal effects are used in the current configuration.
- Forecasts extrapolate the estimated structure.
- The model does not use external explanatory variables.
- Forecast quality depends on the training window and stability of the pattern.

Do not claim the additive specification is optimal without comparing it with alternatives under the same validation design.

## 6. SARIMA

SARIMA combines non-seasonal and seasonal autoregressive, differencing, and moving-average terms. The CLI reference uses:

- Non-seasonal order: `(1, 1, 1)`
- Seasonal order: `(1, 1, 1, 12)`

The notebook uses the same illustrative seasonal order in its model-fitting cell. The configuration includes settings that relax stationarity and invertibility enforcement in the statsmodels estimator. These are implementation details, not evidence that all convergence or model adequacy concerns have been resolved.

### Parameter meaning

- (p): non-seasonal autoregressive order.
- (d): non-seasonal differencing order.
- (q): non-seasonal moving-average order.
- (P): seasonal autoregressive order.
- (D): seasonal differencing order.
- (Q): seasonal moving-average order.
- (s): seasonal period, 12 for monthly annual seasonality.

## 7. Model fitting and data boundaries

For holdout evaluation, the candidate models are fitted using the training segment only. The forecast is then compared against the later test observations. For future forecasting, the reference workflow fits the candidates again on the full observed series.

These are different tasks:

- Backtest: historical forecast where actual outcomes are known.
- Future forecast: extrapolation beyond the latest observation where outcomes are not yet available.

Do not mix their metrics or describe future predictions as evaluated results.

## 8. Model comparison

Use identical train/test dates and horizons. Compare candidate methods with naive and seasonal-naive baselines. Report MAE and RMSE, use MAPE cautiously, inspect residuals, and record warnings. If model selection is performed across many configurations, use a validation design separate from the final test period.

## 9. Not currently implemented

The repository does not currently implement LSTM, recurrent neural networks, transformer forecasting, Prophet, XGBoost, automated hyperparameter search, prediction intervals, or model serving. These methods should not appear as implemented features in the README, screenshots, or project summaries.

A neural model would be especially easy to overfit on only 144 observations. Any future experiment would need a defensible validation design and a clear comparison against simple baselines.

## 10. Related guides

- [Methodology](methodology.md)
- [Evaluation](evaluation.md)
- [Experiment protocol](experiment-protocol.md)
- [Results interpretation](results-interpretation.md)
