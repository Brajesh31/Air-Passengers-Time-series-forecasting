# 🧪 Testing and Forecast Validation

Testing this project requires more than confirming that the notebook opens. The checks below distinguish file structure, Python syntax, command-line execution, and meaningful chronological forecasting evaluation.

## Automated repository checks

GitHub Actions runs:
1. Notebook format validation.
2. Python syntax parsing for code cells, excluding IPython magic and shell lines.
3. Repository unit tests.
4. Forecasting command smoke checks where configured.

These checks do not establish that a forecast is accurate or suitable for airline operations.

## Local validation

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_notebook.py
python -m pytest
```

Run the forecasting command:

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

The command writes metrics, predictions, and a plot under `artifacts/`, which is intentionally ignored by Git.

## Forecast validation protocol

- Preserve the order of monthly observations.
- Fit transformations only on the training period.
- Use a holdout period that occurs after the training period.
- Compare against a naive and seasonal-naive baseline.
- Prefer rolling-origin evaluation when comparing multiple forecasting methods.
- Report MAE and RMSE in the original passenger-count units.
- Report MAPE only when actual values are non-zero and explain its limitations.
- Examine residual autocorrelation and seasonal patterns.
- Do not tune repeatedly against the final test period.

## Known limitations

The built-in dataset has 144 monthly observations and covers 1949 through 1960. It is a classic demonstration series, not current airline data. No external operational variables are available in the checked-in CSV.
