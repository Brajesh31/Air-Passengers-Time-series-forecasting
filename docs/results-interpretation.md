# 📊 Interpreting Forecast Results

## 1. Start with the context

A forecast metric is not meaningful on its own. Before interpreting a result, identify:

- The dataset and its date coverage.
- The target field and units.
- The training and test dates.
- The forecast horizon.
- The model configuration.
- The baseline used for comparison.
- The software environment.
- Any warnings or convergence problems.

The current data is a historical series from 1949 to 1960. All conclusions must be framed within that narrow context.

## 2. MAE interpretation

Mean Absolute Error is the average magnitude of the forecast error, ignoring direction. It is expressed in the same units as the target. For this dataset, interpret the unit using the conventional thousands-of-passengers scale.

MAE is easy to explain, but it hides whether errors are consistently positive or negative and can conceal a small number of very large misses. Review the individual prediction errors as well.

## 3. RMSE interpretation

Root Mean Squared Error penalizes large errors more strongly than MAE. If RMSE is substantially larger than MAE, a few large misses may be contributing disproportionately. Inspect the dates and context of those misses rather than assuming the model is generally poor or generally strong.

## 4. MAPE interpretation

Mean Absolute Percentage Error expresses error relative to actual values. It can help communicate proportional error, but it is unstable when actual values approach zero and can overweight errors during low-volume periods. The current dataset has positive passenger counts, but that does not make MAPE universally sufficient.

Never select a model based on MAPE alone.

## 5. Compare with a baseline

The key question is not "Is the error small?" but "Is the error meaningfully better than a simple forecast under the same conditions?"

For monthly annual seasonality, the seasonal-naive benchmark is particularly important. If a complex model barely improves on seasonal naive, the additional complexity may not be justified.

## 6. Understand the forecast horizon

Forecast errors generally depend on how far ahead the model predicts. A one-month forecast and a 24-month forecast are not interchangeable. Report horizon-specific results where possible. Avoid combining different horizons into a single score without explaining the aggregation.

## 7. Backtest versus future forecast

A backtest forecasts dates for which actual values are known. It can therefore be scored. A future forecast extends beyond the last observed date and cannot be evaluated until new actual observations become available.

The CLI writes both holdout predictions and future forecasts. Do not use future forecast values as evidence of accuracy.

## 8. Model warnings

Convergence warnings, numerical warnings, or suspicious parameter estimates require investigation. A successful script exit does not guarantee that every model fit is statistically appropriate. Record warnings and inspect residuals before relying on the output.

## 9. Residual patterns

Residuals with trends, seasonal patterns, changing variance, or autocorrelation may indicate that the model has not captured important structure. Random-looking residuals are a useful diagnostic, but they do not guarantee good future performance.

## 10. Avoid overclaiming

The dataset is short, old, aggregated, and lacks external explanatory variables. A model that performs well on this series is not proven to work on current airline data, different routes, or different carriers. Do not write claims such as "accurately predicts airline demand" or "production-ready forecasting" based only on this project.

## 11. Responsible result summary

A responsible summary states what was tested, on which dates, with what model and baseline, and what limitations remain. For example:

"The configured seasonal models were compared on a chronological historical holdout from the supplied AirPassengers series. The reported errors describe that split only. The data ends in 1960 and does not establish performance on modern airline demand."

Replace this example with actual dates and measured results when reporting a real run. Do not fabricate scores.

## 12. Related guides

- [Evaluation protocol](evaluation.md)
- [Experiment protocol](experiment-protocol.md)
- [Methodology](methodology.md)
- [Data limitations](data.md)
