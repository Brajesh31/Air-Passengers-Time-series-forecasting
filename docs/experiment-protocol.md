# 🧪 Experiment Protocol

## 1. Purpose

This protocol describes how to conduct and report a forecasting experiment so that comparisons are understandable and reproducible. It is a recommended procedure for future experiments. It does not imply that the current repository already runs a multi-origin experiment tracker or automated model search.

## 2. Define the question first

Before fitting a model, write down:

- What target is being forecast?
- What is the observation frequency?
- How far ahead is the forecast?
- What information would be available at forecast time?
- What baseline should the model beat?
- What error metric matters and why?
- What limitations affect interpretation?

A model experiment without a defined question often becomes repeated parameter tweaking against a convenient metric.

## 3. Freeze the data and code

Record the Git commit SHA, dataset file, checksum, source, observation count, date coverage, field names, and target units. If the data changes, it is a different experiment and should be labelled accordingly.

Do not overwrite an old result without preserving enough metadata to understand what changed.

## 4. Define the time split

Use a chronological split. Record the training period and test period explicitly. For the current 144-observation dataset, the default CLI holdout is 24 months, but the appropriate horizon depends on the experiment question.

The final test window must not be used repeatedly for parameter selection. If parameters need tuning, use a separate validation process, preferably rolling-origin evaluation.

## 5. Establish baselines

Include at least a naive forecast and seasonal-naive forecast where relevant. For a monthly series with annual seasonality, the seasonal-naive period is 12.

Baselines should be calculated using only the information available at each forecast origin. Do not accidentally use actual values from the test period to construct a seasonal baseline.

## 6. Specify candidate models

For every candidate, record the full configuration:

- Model family.
- Non-seasonal and seasonal orders.
- Trend and seasonal component forms.
- Seasonal period.
- Transformations.
- Optimizer or estimation settings.
- Training range.
- Forecast horizon.
- Package version.
- Warnings and convergence status.

Avoid reporting only a model family name such as "SARIMA" without its parameterization.

## 7. Fit and forecast

Fit each candidate using the training observations only. Generate forecasts for the same test dates and horizon. Keep the output date index explicit and align predictions and actuals before computing metrics.

If a transformation is learned from data, estimate it from training data only and apply it consistently to the forecast path.

## 8. Evaluate

Report MAE and RMSE in the target units. MAPE may be included as a supplementary measure with its limitations. Compare each model with the same baselines under the same split. Include plots and residual checks where they add insight.

A single lower metric is not enough to claim that one model is universally better. Consider error distribution, horizon-specific performance, stability across origins, and model complexity.

## 9. Rolling-origin extension

For stronger evidence, repeat the evaluation at several forecast origins. Each origin should use only observations available before that origin. Save the origin date, training range, forecast horizon, actual values, predictions, and metrics.

Summarize both the distribution of errors and per-origin behaviour. A model that performs well on average but fails badly at some origins may be unsuitable for the intended use.

## 10. Record uncertainty

If prediction intervals are available, report their nominal level and evaluate empirical coverage and width. Do not invent uncertainty bounds around point forecasts. The current workflow does not implement a complete interval calibration and evaluation process.

## 11. Experiment report template

```text
Experiment ID:
Question:
Git commit:
Dataset file and checksum:
Observation range:
Target and units:
Training range:
Test range:
Forecast horizon:
Baseline definitions:
Model configuration:
Transformations:
Python and package versions:
Warnings and convergence:
MAE:
RMSE:
MAPE (if reported):
Residual observations:
Artifacts:
Limitations:
Conclusion:
```

## 12. Decision rules

A candidate should not be promoted merely because it has more parameters or a lower in-sample loss. Prefer a simpler model when performance is comparable. Reject results affected by leakage, invalid date alignment, unrecorded data changes, or non-comparable test windows.

## 13. Current implementation boundary

The CLI currently performs one chronological holdout and fits two seasonal model candidates. The notebook includes naive and seasonal-naive baselines. Multi-origin backtesting, systematic experiment tracking, automated selection, and interval coverage evaluation remain future improvements.
