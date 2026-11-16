# ❓ Frequently Asked Questions

## Project purpose

### Is this a live airline-demand forecasting system?

No. The repository is an educational project based on a historical monthly dataset that ends in December 1960. It is not connected to live airline data and does not provide current demand estimates.

### What should I learn from this project?

The project demonstrates data validation, time-series visualization, trend and seasonal analysis, stationarity diagnostics, chronological splitting, simple baselines, classical seasonal models, error metrics, residual inspection, and reproducible local execution.

### Is this a production-ready forecasting solution?

No. The dataset is small, old, aggregated, and lacks important explanatory variables. The project has no operational data pipeline, rolling-origin evaluation suite, calibrated prediction intervals, monitoring, model registry, API, or production deployment.

## Dataset questions

### How many observations are included?

The current CSV contains 144 monthly observations from January 1949 through December 1960.

### What do the values represent?

The classic series is conventionally interpreted as monthly passenger totals in thousands. Keep that unit in plots, metrics, and written interpretation.

### Why are source dates on the 15th but the analysis uses month starts?

The source uses the 15th as a date label for a monthly observation. Normalizing it to the first day of the month creates a consistent monthly index. It does not change the monthly measurement period.

### Can I replace the CSV with another dataset?

Yes, but it is not a drop-in change unless the new file follows the expected schema and validation rules. Verify source and licence, document units and frequency, inspect missing months and duplicates, update tests and documentation, and reconsider the evaluation design.

### Is the dataset licence the same as the repository MIT licence?

Not necessarily. A software licence does not automatically cover third-party data. Verify the original data source and terms before redistributing the CSV independently.

## Model questions

### Why not use random train/test splitting?

Forecasting is directional. A model should be trained on earlier observations and evaluated on later observations. Random splitting can place future information into training and invalidate the estimate of future performance.

### Why compare with naive baselines?

Simple methods can be surprisingly competitive on seasonal data. A complex model should demonstrate that it improves over a relevant baseline under the same split and horizon.

### Does the repository use LSTM?

No. The current notebook and CLI use classical methods. LSTM and other neural forecasting models are not implemented.

### Is TensorFlow required?

No. TensorFlow is not part of the current dependency set because no neural model is implemented.

### Does the repository use Prophet, XGBoost, or Transformers?

No. These methods are not part of the current executable project.

### What is the SARIMA order?

The current example uses non-seasonal order `(1, 1, 1)` and seasonal order `(1, 1, 1, 12)`. This is an illustrative configuration, not a proven optimum.

### Is Exponential Smoothing guaranteed to be the best model?

No. Model ranking depends on the training period, test window, model assumptions, and metric. Use the same chronological evaluation for every candidate and compare against baselines.

## Running the project

### Where should I run Jupyter?

Start Jupyter from the repository root so the notebook can find `AirPassengers.csv` using its relative path.

### Why does my notebook fail even though CI passes?

CI statically validates notebook structure and Python syntax. It does not execute every cell. Runtime imports, file paths, model fitting, and plots still require a clean-kernel notebook run.

### Where are CLI outputs saved?

The command-line script writes a report, CSV predictions, future forecasts, and a PNG plot under `artifacts/`. The directory is generated locally and ignored by Git.

### Why are my metrics different?

Check the dataset version, code commit, Python and package versions, exact train/test dates, horizon, model orders, and warnings. Ensure that the prediction and actual series are aligned by date.

## Architecture questions

### Does the project have a REST API?

No. The current entry points are the Jupyter notebook and local CLI script. See [api.md](api.md).

### Does the project use a database?

No. It reads a CSV and writes local output files. See [database.md](database.md).

### Can I deploy this as a web service?

The repository does not include a service layer or production deployment configuration. A production system would need current governed data, a service contract, validation, uncertainty communication, monitoring, access control, and operational ownership. See [deployment.md](deployment.md).

## Evaluation questions

### What is MAE?

Mean Absolute Error is the average absolute difference between actual and predicted values. It uses the target's units.

### What is RMSE?

Root Mean Squared Error is the square root of the average squared error. It penalizes larger misses more strongly than MAE.

### Should I use MAPE?

It can be a supplementary measure, but it becomes problematic when actual values approach zero and should not be used alone.

### Does a passing test prove the model is accurate?

No. Software tests verify specific code behaviour. Forecast quality requires an appropriate out-of-sample evaluation design and evidence across relevant time periods.

### What is rolling-origin evaluation?

It repeats the forecast process at several historical cutoffs, always fitting on data available before each cutoff and evaluating later observations. It provides more evidence than one holdout but is not yet implemented in the current CLI.

## Contributing and support

### How can I report a documentation problem?

Use the documentation request issue form or open an issue describing the file, section, and correction needed.

### What should a bug report include?

Include Python and operating system versions, the command or notebook cell, a sanitized traceback, expected behaviour, actual behaviour, and relevant dataset and model details.

### How do I report a security problem?

Use GitHub private vulnerability reporting where available. Do not publish secrets or exploit details in a public issue. Follow [SECURITY.md](../SECURITY.md).

## Further documentation

- [Documentation index](README.md)
- [Installation](installation.md)
- [Notebook walkthrough](notebook-guide.md)
- [Methodology](methodology.md)
- [Models](models.md)
- [Evaluation](evaluation.md)
- [Glossary](glossary.md)
