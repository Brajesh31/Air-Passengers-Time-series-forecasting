# 📓 Notebook Walkthrough

## 1. Purpose

`TimeSeriesForecasting.ipynb` is the guided learning entry point. It demonstrates a sequence of exploratory and forecasting tasks using the monthly AirPassengers teaching series. The notebook is intended to be read and executed from top to bottom, not treated as a stateless collection of independent cells.

## 2. Before running

- Install runtime dependencies using [installation.md](installation.md).
- Open Jupyter from the repository root.
- Confirm that `AirPassengers.csv` is present beside the notebook.
- Restart the notebook kernel to remove variables from earlier runs.
- Run all cells in order.

The notebook uses a relative dataset path. Starting Jupyter from another directory can cause a file-not-found error even when the CSV exists elsewhere.

## 3. Notebook sections

### Environment and imports

The first code cell imports the data, plotting, metrics, and statsmodels functions used later. It sets warning behaviour and identifies the CSV path. Missing dependencies or a wrong working directory will fail early here.

### Data inspection

The notebook inspects descriptive statistics, observation count, date coverage, and missing values. This is the first check that the input resembles the expected monthly series. Do not proceed with modelling if the date index or target values are malformed.

### Historical visualization

The time plot shows the long-term movement of monthly passenger totals. Read the axis labels and units. A visible trend and changing seasonal amplitude suggest that a constant-level, non-seasonal model would be an incomplete description.

### Trend and seasonality

The notebook uses classical seasonal decomposition with a period of 12. The decomposition separates an estimated trend, seasonal component, and residual component under the selected model form. Decomposition is descriptive and depends on assumptions; it is not proof that the same pattern will persist.

### Stationarity diagnostics

The Augmented Dickey-Fuller test is applied to the original series and a log-transformed, seasonally differenced series. Its null hypothesis is a unit root. A small p-value is evidence against that null under the test assumptions, not a guarantee that a model is correct or that the data is fully stationary in every relevant sense.

### Chronological holdout

The final 24 observations are reserved as a test segment. Earlier observations form the training data. This preserves the direction of time and provides a simple demonstration of future-like evaluation. Do not shuffle the rows.

### Baselines

Naive and seasonal-naive predictions provide simple reference points. A model's error should be interpreted relative to these benchmarks, not in isolation.

### Seasonal models

The notebook fits seasonal Exponential Smoothing and SARIMA candidates using the training data. The selected seasonal period is 12 because the observations are monthly and the teaching series exhibits an annual pattern. Model parameters are examples, not universally optimal settings.

### Evaluation

The notebook calculates MAE, RMSE, and supplementary MAPE. MAE and RMSE retain the target units. MAPE is a relative percentage and has limitations, particularly near zero. The held-out period is small, so a metric should not be treated as a stable estimate of real-world performance.

### Residual diagnostics

The residual plot and distribution provide a basic check for unexplained structure. Residuals that retain obvious patterns may indicate model misspecification. Residual plots do not replace out-of-sample testing.

### Future forecast

The notebook refits an illustrative seasonal model on the full historical series and forecasts the next 12 months after the final observed month. These dates follow the end of the 1960 dataset. They are historical extrapolations for demonstration, not present-day forecasts.

### Conclusions and limitations

The final section summarizes the visible trend and seasonality and explains why the dataset cannot represent modern airline demand. Read these limitations before reusing the charts or forecast values.

## 4. Variable dependencies

Notebook cells create shared variables such as the loaded series, training and test segments, fitted model objects, forecasts, metrics, and future date index. Later cells depend on these names. Running a cell in isolation may fail or silently use an old value left in the kernel.

The safest execution method is **Restart Kernel, then Run All**.

## 5. Interpreting warnings

Do not hide convergence warnings or statistical warnings automatically. Check model fit, training length, parameter specification, and residual behaviour. A warning may not always invalidate a run, but it must be understood before a result is reported.

## 6. Notebook output hygiene

Before committing notebook changes:

- Ensure outputs correspond to the current code.
- Remove stale or misleading outputs.
- Avoid committing huge accidental arrays or debug output.
- Confirm plots have titles, axis labels, and units.
- Check that no private paths, credentials, or personal information appear.
- Review notebook metadata for machine-specific details.

## 7. Static validation versus execution

`scripts/validate_notebook.py` checks notebook format and Python syntax in code cells. It deliberately does not execute notebook cells. CI success therefore does not mean the complete notebook has been run. Manual clean-kernel execution is required after analytical notebook changes.

## 8. Related guides

- [Architecture](architecture.md)
- [Data documentation](data.md)
- [Methodology](methodology.md)
- [Evaluation](evaluation.md)
- [Testing](testing.md)
