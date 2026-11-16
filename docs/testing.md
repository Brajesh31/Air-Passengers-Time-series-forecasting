# 🧪 Testing, Static Validation, and Forecast Verification

## 1. Testing objectives

Testing in this repository covers several different concerns. A valid notebook file does not prove that every cell runs. Passing unit tests does not prove that a forecasting model generalizes. A successful smoke test does not establish that the model is suitable for airline operations.

Keep these evidence categories separate:

1. File and notebook structure.
2. Static Python syntax.
3. Unit-level function behaviour.
4. Repository input and configuration expectations.
5. End-to-end command-line smoke execution.
6. Analytical validation of forecast quality.
7. Clean-kernel notebook execution.

## 2. Continuous integration workflow

The GitHub Actions workflow at `.github/workflows/ci.yml` currently:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs `requirements-dev.txt`.
4. Runs `scripts/validate_notebook.py`.
5. Runs pytest.
6. Executes `scripts/forecast.py --horizon 6 --test-months 24`.

The workflow runs for pushes to `main`, pull requests, and manual dispatch. It uses read-only repository contents permission.

## 3. Notebook validation

Run:

```bash
python scripts/validate_notebook.py
```

The validator reads root-level notebooks using nbformat, validates their structure, and parses Python syntax from code cells. It omits IPython magic and shell-command lines from the static syntax parse.

This validator does not execute code cells, load the CSV, fit models, render plots, or check the numerical correctness of outputs. A clean-kernel notebook run is required when notebook logic changes.

## 4. Unit and repository tests

Run:

```bash
python -m pytest
```

The current tests cover monthly dataset loading and schema rejection, metric calculations for a perfect prediction, notebook nbformat validity, dataset presence, and dependency manifest presence.

Tests are intentionally scoped to the current repository implementation. They are not a comprehensive test suite for all statistical edge cases, every malformed dataset, or every operating system.

## 5. CLI smoke test

Run:

```bash
python scripts/forecast.py --horizon 6 --test-months 24
```

This command exercises the integrated data loading, split validation, model fitting, metric calculation, future forecasting, and artifact-writing path using the checked-in CSV. It is a smoke test, not a benchmark or accuracy certification.

## 6. Manual notebook test

When notebook code changes:

1. Create or activate a clean environment.
2. Start Jupyter from the repository root.
3. Restart the kernel.
4. Run every cell in order.
5. Confirm that all cells finish without unhandled exceptions.
6. Review statistical warnings.
7. Confirm charts and labels are readable.
8. Confirm that train/test dates are correct.
9. Confirm that no future observations enter training.
10. Review outputs before committing the notebook.

## 7. Data validation cases

The data loader should be tested against valid input and invalid cases, including:

- Missing input file.
- Missing `Month` or `Passengers` columns.
- Unparseable dates.
- Non-numeric passenger values.
- Missing values.
- Zero or negative counts.
- Duplicate months.
- Missing months in the monthly index.
- Fewer than the required minimum observations.
- Unsorted source rows that should be sorted chronologically.

The current tests cover only a subset of these cases. Expanding edge-case coverage is a suitable testing improvement, provided it does not alter expected valid behaviour without a reason.

## 8. Forecast validation is not the same as software testing

Forecast quality must be evaluated using future-like observations. Use chronological holdouts and preferably rolling-origin backtesting. Compare models against naive and seasonal-naive benchmarks. Report MAE and RMSE, explain MAPE limitations, and inspect residual behaviour.

See [evaluation.md](evaluation.md) and [experiment-protocol.md](experiment-protocol.md).

## 9. Interpreting failures

- **Dependency installation failure:** inspect Python version, pip output, and package compatibility.
- **Notebook validator failure:** inspect notebook JSON and the reported cell syntax.
- **Pytest failure:** reproduce the failing test locally and inspect the assertion and traceback.
- **CLI smoke failure:** verify dataset path, schema, monthly continuity, split size, model warnings, and artifact permissions.
- **Notebook runtime failure:** restart the kernel and execute from the first cell.
- **Different numerical output:** compare package versions, model parameters, and train/test boundaries before assuming a regression.

Do not disable a failing test merely to obtain a green badge. Fix the underlying issue or explain why the test is invalid and replace it with a better check.

## 10. Current test coverage limitations

CI does not currently execute the full notebook. It does not run multiple Python versions or operating systems, perform rolling-origin evaluation, validate prediction-interval coverage, or compare forecast accuracy against a benchmark threshold. These are potential future improvements, not existing guarantees.
