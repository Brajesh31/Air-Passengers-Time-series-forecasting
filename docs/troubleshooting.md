# 🧯 Troubleshooting Guide

## 1. How to use this guide

Start with the exact command that failed and read the complete error message. Confirm which Python executable is running, whether the virtual environment is active, and whether the terminal is positioned at the repository root. Avoid applying unrelated fixes before identifying the failure stage.

## 2. Dataset file not found

**Symptom:** The notebook or CLI raises a file-not-found error for `AirPassengers.csv`.

**Checks:**

```bash
python -c "from pathlib import Path; print(Path.cwd()); print(Path('AirPassengers.csv').resolve()); print(Path('AirPassengers.csv').is_file())"
```

The notebook expects the CSV in the repository root. Start Jupyter from that directory. The CLI accepts a custom path:

```bash
python scripts/forecast.py --data path/to/AirPassengers.csv --horizon 12 --test-months 24
```

A valid path does not guarantee a valid dataset. The file must still satisfy the schema and monthly continuity checks.

## 3. Wrong Python environment or missing dependency

**Symptom:** An import fails even after packages were installed.

Check the executable and pip target:

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
python -m pip list
```

Activate the intended environment and install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Use `python -m pip` rather than an unrelated global `pip` command so installation targets the same interpreter that runs the project.

## 4. Jupyter uses the wrong interpreter

Jupyter may be installed in one environment while the notebook kernel points to another. Confirm the Python executable from inside a notebook cell:

```python
import sys
print(sys.executable)
```

If it is not the project environment, install and select the appropriate Jupyter kernel for that environment. Do not install packages repeatedly into several Python installations without checking which kernel is active.

## 5. Date parsing or monthly frequency errors

**Possible causes:**
- Source dates use a different date format.
- A date string is malformed.
- Two rows refer to the same month.
- One or more months are missing.
- Dates are not normalized to a monthly index.

The CLI expects day-first source dates, normalizes timestamps to month starts, and checks for unique, continuous monthly observations. Do not disable these checks simply to make a malformed CSV load. Correct the source or document a deliberate transformation.

## 6. Required CSV columns are missing

The CLI expects `Month` and `Passengers`. Inspect the header:

```python
import pandas as pd
frame = pd.read_csv("AirPassengers.csv")
print(frame.columns.tolist())
print(frame.head())
```

If a new dataset uses different column names, update the loader, data dictionary, tests, and documentation together. Do not silently guess column meanings.

## 7. Invalid passenger values

The CLI rejects values that cannot be parsed as numeric, missing values, zero or negative passenger counts. Inspect the rows before deciding whether they are data errors or a legitimate change in the dataset definition.

Do not fill missing months or replace invalid values without recording the method. Imputation can affect trends, seasonal estimates, and evaluation.

## 8. Too few observations

The CLI requires at least 36 monthly observations for seasonal modelling and requires the test window to leave at least 24 months for training. A custom dataset with fewer observations may fail these checks.

These are safeguards for the current implementation, not universal statistical laws. Changing them requires a model-specific justification and tests.

## 9. Notebook state is inconsistent

**Symptom:** A cell behaves differently depending on what was run earlier.

Jupyter retains variables in memory. Restart the kernel and run all cells in order. Avoid executing model cells with stale training or test variables.

## 10. Notebook validator fails

Run:

```bash
python scripts/validate_notebook.py
```

Inspect the notebook file and reported cell. The validator checks notebook format and parses Python syntax while omitting IPython magic and shell lines. It does not run the cells. A notebook can pass static validation and still fail during execution because of missing files, imports, runtime errors, or model-fitting issues.

## 11. Pytest fails

Run the test suite with verbose output:

```bash
python -m pytest -vv
```

Reproduce the failing test before changing code. Check the assertion, fixture data, Python version, package versions, and current repository state. Do not delete a test because it exposes a regression.

## 12. SARIMA or Exponential Smoothing warnings

Model fitting can produce convergence or numerical warnings. Check:
- Training series length.
- Date frequency and seasonal period.
- Model order and differencing assumptions.
- Whether the series contains missing or extreme values.
- Whether the optimizer converged.
- Residual plots and autocorrelation.
- Whether simpler baselines perform comparably.

Do not suppress all warnings without understanding them. A completed fit is not proof of model adequacy.

## 13. Metrics differ between machines

Check the dataset file, Git commit, Python and package versions, train/test boundary, model order, seasonal period, and numerical warnings. Floating-point and solver behaviour can vary between library versions. Compare the actual prediction series, not only the rounded metric printed to the terminal.

## 14. Generated artifacts are missing

Run the CLI from the repository root:

```bash
python scripts/forecast.py --horizon 6 --test-months 24
```

A successful run creates `artifacts/` and writes the report, predictions, future forecasts, and plot. If the directory is absent, inspect the complete traceback and file-system permissions. Generated outputs are ignored by Git by design.

## 15. CLI argument validation errors

Check the help output:

```bash
python scripts/forecast.py --help
```

The horizon must be positive. The test window must satisfy the script's minimum and training-length requirements. A test size that consumes too much of the dataset will be rejected.

## 16. GitHub Actions failure

Open the failing workflow run and identify the first failed step. Common stages are dependency installation, notebook validation, pytest, and the CLI smoke test. Reproduce the same command locally using a clean environment. Do not assume a later successful run proves that every earlier commit was tested.

## 17. Different forecast metrics

Metrics can differ if the split dates, forecast horizon, model configuration, data, or dependency versions differ. Ensure that both predictions are aligned to the same actual dates and target units. A comparison across different holdout periods is not a fair model comparison.

## 18. Security and data handling

Do not paste credentials, private data, or unredacted environment files into a public issue. Follow [SECURITY.md](../SECURITY.md) for vulnerability reporting. For support requests, provide sanitized error output and environment details.

## 19. When reporting a new problem

Include:
- Operating system and Python version.
- Git commit or branch.
- Environment installation commands.
- Exact command or notebook cell.
- Complete sanitized traceback.
- Expected and actual behaviour.
- Dataset schema and date range, without sensitive data.
- Model parameters and train/test dates where relevant.
- Steps already attempted.

See [SUPPORT.md](../SUPPORT.md) for the reporting checklist.
