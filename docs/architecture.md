# 🏗️ Project Architecture

## 1. Purpose and scope

The repository is organized around a small, reproducible time-series learning exercise. It contains one historical CSV dataset, a notebook for guided analysis, a Python command-line reference workflow, automated checks, and documentation. Its architecture is intentionally local and simple.

There is no web application, HTTP service, database, background worker, cloud deployment, data warehouse, model registry, or scheduled ingestion pipeline. Those systems should not be inferred from the presence of documentation describing why they are currently absent.

## 2. Main components

| Component | Path | Responsibility |
|---|---|---|
| Historical input | `AirPassengers.csv` | Monthly observations used by the project |
| Learning workflow | `TimeSeriesForecasting.ipynb` | Explanatory analysis, plots, diagnostics, baselines, models and forecast |
| CLI workflow | `scripts/forecast.py` | Input validation, chronological holdout, model fitting, metrics and local outputs |
| Notebook validator | `scripts/validate_notebook.py` | Notebook format validation and static Python syntax parsing |
| Automated tests | `tests/` | Tests for data loading, metrics, notebook format and repository expectations |
| Runtime dependencies | `requirements.txt` | Packages needed for the notebook and forecast script |
| Development dependencies | `requirements-dev.txt` | Runtime dependencies plus testing and notebook validation tools |
| CI | `.github/workflows/ci.yml` | Installs dependencies, validates notebooks, runs tests and executes a CLI smoke test |
| Documentation | `docs/` | Methodology, data, setup, testing, reproducibility and maintenance guidance |

## 3. Data flow

```text
                 AirPassengers.csv
                         |
                         v
             Read CSV and validate schema
                         |
                         v
             Parse and normalize monthly dates
                         |
                         v
              Ordered monthly passenger series
                         |
             +-----------+-----------+
             |                       |
             v                       v
      Jupyter notebook         CLI forecasting script
             |                       |
      Explore and plot          Validate input series
      Decompose series          Chronological split
      Stationarity tests        Fit seasonal candidates
      Baselines                 Calculate metrics
      Seasonal models           Refit on full history
      Residual review           Write local artifacts
             |                       |
             v                       v
      Interactive analysis       JSON / CSV / PNG files
```

The notebook and script are separate implementations. They share the same dataset and broad analytical purpose, but they are not a single shared library and should not be assumed to produce identical metrics or plots.

## 4. CLI execution stages

The command-line workflow in `scripts/forecast.py` follows these stages:

1. Parse command-line arguments.
2. Resolve the dataset path.
3. Read the CSV and check the required `Month` and `Passengers` columns.
4. Parse dates, coerce passenger values to numeric values, and reject invalid or non-positive observations.
5. Sort the series and reject duplicate or discontinuous monthly timestamps.
6. Reserve the most recent requested months as the holdout period.
7. Fit seasonal Exponential Smoothing and SARIMA candidates using training observations only.
8. Align predictions with the held-out dates and calculate MAE, RMSE, and MAPE.
9. Fit the candidates again using the complete historical series.
10. Create future monthly dates and point forecasts.
11. Write reports and a backtest plot to `artifacts/`.

The script rejects invalid horizons and unsuitable split sizes rather than silently producing a misleading result.

## 5. Notebook execution stages

The notebook is designed to be run from top to bottom in a clean Jupyter kernel. It imports its analytical libraries, reads the root-level CSV, explores the observations, visualizes trend and seasonality, runs stationarity diagnostics, creates a chronological holdout, compares baselines and seasonal models, evaluates errors, inspects residuals, and produces an illustrative future forecast.

Notebook cells depend on variables created earlier. Running cells out of order can reuse stale variables or fail because required state has not been created.

## 6. Generated artifacts

The CLI writes the following local files:

| Path | Content |
|---|---|
| `artifacts/forecast_report.json` | Dataset summary, holdout information, diagnostics, metrics and future predictions |
| `artifacts/backtest_predictions.csv` | Actual held-out observations and candidate predictions |
| `artifacts/future_forecasts.csv` | Candidate forecasts for future months |
| `artifacts/backtest.png` | Historical series and holdout forecast visualization |

The generated directory is ignored by Git. These outputs are disposable run artifacts, not versioned model releases.

## 7. Dependency boundaries

NumPy and Pandas support data processing; Matplotlib and Seaborn support visual analysis; scikit-learn supplies error metrics; statsmodels supplies classical time-series models and diagnostics; Jupyter and nbformat support notebook use and validation; pytest and nbconvert support development checks.

The current workflow does not implement neural networks, so TensorFlow is not a runtime requirement. It does not require credentials or environment variables. The example environment file documents this explicitly.

## 8. Security and trust boundaries

The checked-in CSV is treated as project input. External CSV files should be treated as untrusted and validated before analysis. Notebook cells execute local Python code, so contributors and users should inspect notebooks before running them. Never commit credentials, private data, or machine-specific environment files.

## 9. Architectural constraints

The single series is intentionally small. The project does not provide scalable ingestion, concurrent prediction requests, model persistence, access control, service availability, or monitoring. Adding these systems would materially change the project scope and should require a separate design proposal, operational requirements, and tests.

## 10. Related documentation

- [Notebook walkthrough](notebook-guide.md)
- [Dataset documentation](data.md)
- [Forecasting methodology](methodology.md)
- [Model reference](models.md)
- [Evaluation protocol](evaluation.md)
- [Deployment boundaries](deployment.md)
