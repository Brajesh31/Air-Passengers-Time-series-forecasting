# 🧪 Testing and Forecast Validation

Testing this project requires more than confirming that the notebook opens. These checks distinguish file structure, Python syntax, metric logic, and chronological forecasting evaluation.

## Automated checks

GitHub Actions performs:
1. Notebook format validation.
2. Python syntax parsing for notebook code cells, excluding IPython magic commands.
3. Repository and forecasting unit tests.
4. A command-line forecasting smoke test on the checked-in CSV.

These tests establish basic execution and data handling, not operational forecast validity.

## Local validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_notebook.py
python -m pytest
python scripts/forecast.py --horizon 12 --test-months 24
```

## Forecast validation protocol

- Preserve monthly order.
- Split chronologically.
- Fit preprocessing only on the training window.
- Compare against naive and seasonal-naive baselines.
- Prefer rolling-origin evaluation when comparing models.
- Report MAE and RMSE in the original target units.
- Explain MAPE limitations.
- Inspect residual autocorrelation and seasonal patterns.
- Do not tune against the final holdout set repeatedly.

## Known limits

The included dataset contains 144 monthly observations from 1949 through 1960. CI smoke tests use the exact checked-in data, but a passing test does not mean the model generalizes to current airline operations.
