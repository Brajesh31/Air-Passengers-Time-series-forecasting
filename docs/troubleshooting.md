# 🧯 Troubleshooting

## AirPassengers.csv not found

Run Jupyter or the command-line script from the repository root. Confirm that `AirPassengers.csv` is beside the notebook and script.

## Date parsing or frequency error

The source dates are written in day-month-year format. Use `dayfirst=True` when parsing. Normalize to month starts before setting a monthly frequency. Check for duplicate months and gaps.

## Missing dependencies

Activate the project's virtual environment and install `requirements.txt` or `requirements-dev.txt`. Do not install a TensorFlow stack for the current SARIMA/Exponential Smoothing workflow, which does not use TensorFlow.

## SARIMA convergence warnings

Review the model specification, training window, and residual diagnostics. Try simpler orders or compare against seasonal naive and exponential smoothing baselines. Do not suppress warnings before understanding them.

## Different forecast metrics

Check the exact chronological split, train end date, test horizon, package versions, and model specification. Confirm that no future observations were included in model fitting.

## Notebook state is inconsistent

Restart the kernel and run every cell in order. Old variable values can persist after out-of-order execution.

## Forecast artifact files are missing

Run `python scripts/forecast.py` from the repository root. The script creates the `artifacts/` directory when it runs successfully.
