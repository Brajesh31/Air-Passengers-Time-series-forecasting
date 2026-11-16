# 📐 Forecasting Methodology

## 1. Analytical objective

The project demonstrates how a univariate monthly time series can be inspected, validated, divided chronologically, modelled, and evaluated. The target is the monthly passenger total in the classic historical AirPassengers series.

This is a teaching workflow. The goal is to explain the reasoning behind time-series steps, not to claim that a fitted model can predict current airline demand.

## 2. Univariate time-series framing

A univariate series contains observations of one target over time. Here, the passenger count is observed monthly. The models use historical values of this target and its temporal structure. They do not use explanatory variables such as ticket prices, route capacity, weather, macroeconomic conditions, airline schedules, or disruptions.

A univariate model can capture patterns present in the series, but it cannot directly explain external causes that are not represented in the data.

## 3. Trend and seasonality

- **Trend** describes a longer-term increase or decrease in the series level.
- **Seasonality** describes a pattern that repeats at a known interval, such as a yearly cycle in monthly data.
- **Irregular variation** is the remaining movement not explained by the chosen trend and seasonal structure.

The notebook visualizes the series and uses a period of 12 for annual seasonality. The seasonal period is based on the monthly observation frequency and the teaching series structure.

## 4. Additive and multiplicative structure

An additive decomposition represents the observed series as trend plus seasonal component plus residual. A multiplicative decomposition represents it as trend multiplied by seasonal and irregular factors. Multiplicative structure is often considered when seasonal variation grows with the level of the series.

The notebook uses multiplicative seasonal decomposition as a diagnostic. This choice should be reviewed if data values include zero or negative values, because multiplicative models and log transforms require positive observations.

## 5. Stationarity

Many classical time-series methods rely on assumptions about stable statistical properties. A series with changing level or seasonal structure may require transformations or differencing.

The Augmented Dickey-Fuller test has a unit-root null hypothesis. A low p-value can provide evidence against the unit-root null under the test's assumptions. The test result should be interpreted alongside the plot, differencing choice, sample length, and model residuals.

A p-value does not tell whether the model will forecast well. It does not automatically identify the correct model order.

## 6. Log transformation

A logarithm can help stabilize variance when the scale of seasonal fluctuations increases with the level. It is only defined for positive values. A log transformation changes the scale of analysis, so interpretation and back-transformation require care.

The notebook uses a log series for diagnostic exploration. Do not assume that every model in the repository is fitted on the log scale; inspect the relevant cell or function.

## 7. Differencing

First differencing compares each observation with the previous observation. Seasonal differencing compares an observation with the observation one seasonal cycle earlier. For monthly annual seasonality, a seasonal lag of 12 is common.

Differencing can help remove changing level or seasonal structure. Excessive differencing can remove useful signal and induce unnecessary complexity. The differencing order should be justified rather than chosen mechanically.

## 8. Chronological train/test design

The final 24 months are held out in the notebook and CLI default. The model is fitted on earlier observations and evaluated on later observations. This imitates the direction of a real forecast.

All fitted preprocessing, parameter estimation, and model selection must avoid information from the holdout. Repeatedly changing parameters after inspecting the final holdout turns that holdout into part of the model-selection process.

## 9. Baseline-first reasoning

Naive and seasonal-naive models are essential reference points. The naive model carries forward the most recent value. The seasonal-naive model repeats the corresponding month from the previous annual cycle.

A sophisticated model is useful only if it demonstrates a meaningful improvement over a relevant baseline under the same evaluation protocol. Complexity without measurable value increases maintenance cost without evidence of benefit.

## 10. Seasonal Exponential Smoothing

Exponential Smoothing assigns greater weight to recent observations through a structured set of level, trend, and seasonal components. The project uses an additive trend and additive seasonal specification with a seasonal period of 12 in the relevant implementations.

The choice of additive components is a modelling assumption. Alternative trend or seasonal forms may behave differently. Parameter estimation and model diagnostics should be reviewed before interpreting forecasts.

## 11. SARIMA

Seasonal Autoregressive Integrated Moving Average models extend ARIMA with seasonal autoregressive, differencing, and moving-average terms. A SARIMA specification contains non-seasonal order ((p,d,q)) and seasonal order ((P,D,Q,s)).

The current reference script uses a fixed illustrative order. It is not a universal optimum and is not the result of an exhaustive automated search. The order should be reported explicitly with every comparison.

## 12. Error measurement

MAE summarizes average absolute error. RMSE gives greater influence to large errors. MAPE expresses error as a percentage but has important limitations. Report metric definitions, target units, and the dates included in the evaluation.

## 13. Residual analysis

Residual diagnostics can identify remaining autocorrelation, changing variance, outliers, or systematic structure. A model with strongly structured residuals may be missing relevant information. A visually unstructured residual series still does not prove future generalization.

## 14. Future forecasting

After the holdout evaluation, the CLI and notebook refit selected example models using all available historical observations and generate future point forecasts. The forecast horizon is a user-selected number of months. The future dates begin after the final observed month.

The future forecast is not the same thing as a backtest. Backtesting has actual observations available for comparison; future forecasts do not.

## 15. Methodology limitations

The series has only 144 monthly observations, and the data ends in 1960. The workflow does not include exogenous regressors, rolling-origin evaluation, formal model selection across a broad search space, calibrated prediction intervals, or production monitoring. The methods are examples for learning, not a validated airline forecasting solution.

## 16. Related guides

- [Model reference](models.md)
- [Evaluation protocol](evaluation.md)
- [Experiment protocol](experiment-protocol.md)
- [Interpreting results](results-interpretation.md)
- [Glossary](glossary.md)
