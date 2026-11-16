# 📖 Time-Series Forecasting Glossary

This glossary defines terms used in the repository. Definitions are intentionally concise and refer to the project's monthly historical dataset.

| Term | Definition |
|---|---|
| Actual | The observed target value for a date |
| ADF test | Augmented Dickey-Fuller statistical test with a unit-root null hypothesis |
| Autocorrelation | Relationship between a series and lagged values of itself |
| Backtest | A historical simulation of forecasting where later actual observations are known |
| Baseline | A simple reference forecast used to judge more complex methods |
| Chronological split | A train/test division that keeps earlier observations in training and later observations in testing |
| CLI | Command-line interface, used here to run the Python forecasting script |
| Differencing | Subtracting an earlier observation from a later one to change time-series properties |
| Expanding window | Backtest design where the training set grows as the forecast origin moves forward |
| Forecast | A prediction of a future observation |
| Forecast horizon | Number of future time steps predicted |
| Holdout | Observations withheld from model fitting for evaluation |
| Irregular component | Variation not explained by the chosen trend and seasonal components |
| MAE | Mean Absolute Error, average absolute difference between actual and forecast |
| MAPE | Mean Absolute Percentage Error, average absolute percentage error |
| Monthly frequency | One observation for each calendar month |
| Naive forecast | Forecast that repeats the latest observed training value |
| Out-of-sample | Observations not used to fit the model |
| Overfitting | Fitting noise or peculiarities in training data rather than generalizable structure |
| Prediction interval | Range intended to contain a future observation at a stated probability level |
| Residual | Difference between an observation and a model's fitted value, under the relevant definition |
| RMSE | Root Mean Squared Error, square root of mean squared forecast error |
| SARIMA | Seasonal ARIMA model with non-seasonal and seasonal terms |
| Seasonal period | Number of observations in one seasonal cycle, 12 for annual seasonality in monthly data |
| Seasonal naive | Forecast that repeats values from the previous seasonal cycle |
| Seasonality | A pattern that repeats at a known time interval |
| Stationarity | Property of a time series whose relevant statistical characteristics are stable over time |
| Test set | Later observations reserved for measuring forecast performance |
| Training set | Earlier observations used to estimate a model |
| Trend | Long-term direction or movement in a series |
| Univariate series | Time series containing one target variable |
| Unit root | A stochastic property associated with non-stationary behaviour in some time-series processes |

## Important distinctions

### Fitted values versus forecasts

Fitted values describe model estimates associated with observations used during fitting. Forecasts predict observations beyond the information used for fitting. Their errors should not be reported as though they were the same evaluation.

### Residuals versus forecast errors

Residuals are often calculated on data used to fit a model. Forecast errors compare predictions with observations not used to produce those predictions. Out-of-sample forecast errors are more relevant for assessing future predictive performance.

### Monthly date label versus measurement interval

The source file's date label is on the 15th day of a month. The observation represents the monthly total, not a measurement taken only on that calendar day. Normalizing the date to month start is an indexing convention.

### Stationarity versus forecast accuracy

A stationarity test can inform model diagnostics and transformations. It does not directly measure forecast accuracy and cannot identify a best model by itself.

## Further reading within this repository

- [Methodology](methodology.md)
- [Model reference](models.md)
- [Evaluation](evaluation.md)
- [Interpreting results](results-interpretation.md)
