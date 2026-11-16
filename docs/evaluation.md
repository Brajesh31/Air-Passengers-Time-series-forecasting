# 📏 Forecast Evaluation and Backtesting Protocol

## 1. Why evaluation design matters

A forecasting model must be evaluated on observations that occur after the data used to fit it. The purpose of evaluation is to estimate how the model would behave when asked to predict an unseen future period.

Random train/test splitting is inappropriate for this task because it can place later observations in the training set while earlier observations are in the test set. This breaks the forecasting chronology and can leak information about future levels or seasonal patterns.

A low error score is meaningful only when the validation design, target units, forecast horizon, and comparison baseline are clear.

## 2. Current CLI evaluation design

The command-line workflow reserves the most recent `test_months` observations as the holdout. The default is 24 months. All earlier observations form the training series.

The script fits seasonal Exponential Smoothing and SARIMA candidates on the training data, predicts the held-out horizon, aligns forecasts with the actual test dates, and calculates metrics. It then refits the candidate models on the full history for the separate future-forecast output.

The CLI implementation does not currently provide a rolling-origin backtest or a full baseline report equivalent to every baseline shown in the notebook. Do not describe it as doing so.

## 3. Chronological split

Let the ordered observations be (y_1, y_2, \ldots, y_T). For a holdout of (h) months:

- Training observations are (y_1, \ldots, y_{T-h}).
- Test observations are (y_{T-h+1}, \ldots, y_T).
- The model is fitted only to the training segment.
- Predictions are evaluated against the test segment in date order.

The training and test ranges should be recorded with every reported result. The test period must not influence parameter selection or preprocessing.

## 4. Error metrics

### Mean Absolute Error

`MAE = (1/n) × Σ |yᵢ - ŷᵢ|`

MAE is the average absolute error. It is expressed in the same units as the target and is relatively easy to explain.

### Root Mean Squared Error

`RMSE = sqrt((1/n) × Σ (yᵢ - ŷᵢ)²)`

RMSE penalizes larger errors more strongly than MAE. A few large misses can therefore have a noticeable effect.

### Mean Absolute Percentage Error

`MAPE = (100/n) × Σ |(yᵢ - ŷᵢ) / yᵢ|`

MAPE expresses error as a percentage. It is undefined when actual values are zero and can overemphasize errors at low-volume observations. It should be supplementary, not the sole selection metric.

### R-squared

R-squared is not the primary metric for forecasting comparisons. It can be negative on a holdout and does not replace comparison with a forecast baseline.

## 5. Baseline models

At minimum, a seasonal dataset should be compared against simple methods:

- **Naive:** repeats the latest training observation.
- **Seasonal naive:** repeats the observation from the same seasonal position in the previous cycle.

The notebook includes these baseline forecasts. The CLI does not currently export a full baseline comparison table. A future CLI enhancement should add that without changing the meaning of existing outputs.

If a complex method does not outperform a relevant simple baseline under the same test design, its added complexity is not justified by the available evidence.

## 6. Rolling-origin evaluation

A single holdout gives one view of performance. Rolling-origin evaluation repeats the forecast process at multiple historical cutoffs.

At each origin:

1. Select observations available at that date.
2. Fit the model using only those observations.
3. Forecast the next fixed horizon.
4. Compare with the subsequently observed values.
5. Move the origin forward and repeat.
6. Aggregate errors across origins while preserving per-origin results.

An expanding-window design keeps all earlier observations and grows the training set. A sliding-window design uses a fixed-length recent history. The choice should match the intended forecasting use case and be documented.

Rolling-origin evaluation is a roadmap improvement, not a claim about the current CLI implementation.

## 7. Fair model comparisons

For a fair comparison, candidate models must use:

- The same dataset version.
- The same training and test boundaries.
- The same forecast horizon.
- The same target units.
- Comparable treatment of missing dates.
- The same metric definitions.
- Clearly reported model parameters.

Do not compare one model's 12-month error with another model's 24-month error and call the lower number a win.

## 8. Residual diagnostics

Residuals are the differences between observed and fitted values under the relevant model definition. Useful checks include residual time plots, autocorrelation, seasonal patterns, changing variance, extreme errors, and systematic bias.

Residual diagnostics can reveal that a model has failed to capture structure. They do not prove future accuracy. Residuals used for in-sample diagnosis must not be confused with genuine out-of-sample forecast errors.

## 9. Forecast uncertainty

A point forecast is not a guarantee. Real forecasting work should communicate uncertainty, for example through prediction intervals, and evaluate whether interval coverage is calibrated. The current workflow does not provide a complete prediction-interval evaluation framework.

## 10. Reporting template

A defensible model comparison should report:

| Field | Required information |
|---|---|
| Dataset | File/version and checksum where available |
| Target | Field name and units |
| Frequency | Monthly |
| Training period | Start and end dates |
| Test period | Start and end dates |
| Horizon | Number of months |
| Model | Family, order, seasonal order, configuration |
| Baselines | Naive and seasonal naive where appropriate |
| Metrics | MAE, RMSE, supplementary MAPE |
| Diagnostics | Warnings, residual patterns, convergence |
| Environment | Python and package versions |
| Limitations | Small sample, data age, omitted drivers |

## 11. Interpretation boundary

The dataset contains 144 monthly observations ending in 1960. It is useful for demonstrating evaluation mechanics, not for validating current airline demand forecasting. See [results-interpretation.md](results-interpretation.md) and [data.md](data.md).
