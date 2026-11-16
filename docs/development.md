# 🛠️ Development Guide

## 1. Development philosophy

This repository is a learning-oriented time-series project. Good contributions improve correctness, explainability, reproducibility, accessibility, testing, or maintainability. A larger code change is not automatically a better contribution. Avoid adding infrastructure, dependencies, or modelling complexity without a specific problem and evidence that the change is useful.

The most important technical rule is to preserve time order. Forecasting estimates future observations from past observations. Random splitting, fitting transformations on the complete series before evaluation, or selecting a model using future test observations can invalidate the reported performance.

## 2. Project layout

| Path | Purpose |
|---|---|
| `AirPassengers.csv` | Historical monthly input data |
| `TimeSeriesForecasting.ipynb` | Guided exploratory and forecasting notebook |
| `scripts/forecast.py` | CLI reference workflow |
| `scripts/validate_notebook.py` | Static notebook validation |
| `tests/` | Automated tests |
| `docs/` | User, methodology, and maintenance documentation |
| `.github/workflows/ci.yml` | GitHub Actions validation |
| `requirements.txt` | Runtime dependencies |
| `requirements-dev.txt` | Development dependencies |

## 3. Local environment

Create and activate a virtual environment, then install the development requirements:

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

See [installation.md](installation.md) for platform-specific setup and environment verification.

## 4. Coding standards

- Use clear names that describe the data or operation.
- Prefer small functions with a single responsibility.
- Add type hints where they improve clarity.
- Raise actionable errors for invalid user input.
- Avoid silent coercion that could hide malformed data.
- Keep file paths explicit and robust.
- Do not introduce hidden global state.
- Keep generated outputs outside tracked source directories.
- Add tests for new validation rules and meaningful edge cases.
- Keep dependency additions minimal and justified.
- Do not suppress warnings without understanding their cause.

## 5. Time-series standards

1. Preserve chronological ordering at every stage.
2. Do not randomly shuffle observations for forecasting evaluation.
3. Fit transformations and model parameters using training data only.
4. Use a chronological holdout or rolling-origin evaluation.
5. Include naive and seasonal-naive benchmarks where appropriate.
6. State the forecast horizon, training end, test dates, and seasonal period.
7. Report MAE and RMSE in the original target units.
8. Explain the limitations of MAPE.
9. Inspect residual patterns and model convergence.
10. Avoid tuning repeatedly against the final holdout.

## 6. Notebook development

Before editing notebook analysis:

- Restart the kernel.
- Run the notebook from the first cell to the last.
- Confirm all referenced files are available.
- Review warnings and model convergence messages.
- Ensure plots have readable titles, axes, and units.
- Remove stale outputs when they no longer correspond to the code.
- Check that narrative claims match the actual implementation.
- Confirm that no secrets or private data appear in cell outputs.

The static validator checks notebook structure and Python syntax. It does not execute cells, so it cannot replace a clean-kernel notebook run.

## 7. Script development

The CLI script is responsible for validating the input dataset, enforcing a continuous monthly index, creating a chronological holdout, fitting candidate models, calculating metrics, and writing generated artifacts. Keep these stages explicit.

When changing input validation, test both valid and invalid cases. Examples include missing columns, malformed dates, non-numeric values, non-positive counts, duplicate months, gaps in monthly coverage, too few observations, invalid horizons, and invalid test-window sizes.

When changing model logic, compare results against the same baseline and validation window. Do not report an improvement based on a different test split.

## 8. Testing commands

```bash
python scripts/validate_notebook.py
python -m pytest
python scripts/forecast.py --horizon 6 --test-months 24
```

Run all relevant commands before submitting. If a change affects model logic, also execute the notebook and document the test period and metrics.

## 9. Pull request evidence

A useful pull request description states:

- The problem being solved.
- The scope and files changed.
- The assumptions made.
- Whether the dataset, units, or date handling changed.
- Whether the evaluation protocol changed.
- Commands run and their outcomes.
- Model parameters and test-window boundaries where relevant.
- Any warnings, limitations, or unresolved issues.

Do not use statements such as "more accurate" or "best model" without a comparable evaluation protocol and evidence.

## 10. Documentation updates

Update the affected guide whenever behaviour, setup, assumptions, dependencies, or outputs change. Update the root README if user-facing commands or repository structure change. Add a changelog entry for material user-visible changes. Keep documentation specific to implemented behaviour.

## 11. Scope boundaries

The current project is local and file-based. It does not implement a REST API, database, production deployment, online model serving, or automatic ingestion. Do not add those components as decorative scaffolding. A proposal for such a change must describe the user need, data governance, operational requirements, security, testing, and maintenance cost.

## 12. Further reading

- [Forecasting methodology](methodology.md)
- [Model reference](models.md)
- [Evaluation protocol](evaluation.md)
- [Testing](testing.md)
- [Experiment protocol](experiment-protocol.md)
