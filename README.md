# ✈️ Air Passengers Time-Series Forecasting

A reproducible educational project exploring the classic monthly international airline passenger series from **January 1949 through December 1960**. The repository combines a historical CSV dataset, an explanatory Jupyter notebook, a command-line forecasting reference workflow, automated tests, and project documentation.

> [!IMPORTANT]
> This is a small historical teaching dataset. Forecasts are illustrative only. They are not current airline-demand estimates and must not be used for operational, commercial, staffing, scheduling, or investment decisions.

[![Forecasting Project Checks](https://github.com/Brajesh31/Air-Passengers-Time-series-forecasting/actions/workflows/ci.yml/badge.svg)](https://github.com/Brajesh31/Air-Passengers-Time-series-forecasting/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Notebook-Jupyter-orange.svg)](https://jupyter.org/)

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [What This Project Covers](#-what-this-project-covers)
- [Methods and Models](#-methods-and-models)
- [Repository Contents](#-repository-contents)
- [Dataset](#-dataset)
- [Getting Started](#-getting-started)
- [Run the Notebook](#-run-the-notebook)
- [Run the Command-Line Workflow](#-run-the-command-line-workflow)
- [Testing and Validation](#-testing-and-validation)
- [Generated Outputs](#-generated-outputs)
- [Documentation](#-documentation)
- [Known Limitations](#-known-limitations)
- [Contributing](#-contributing)
- [Security](#-security)
- [Maintainer](#-maintainer)
- [License](#-license)

## 🔎 Project Overview

The project studies how passenger volume changes over time and demonstrates a classical time-series workflow. It focuses on correct date handling, trend and seasonal exploration, stationarity diagnostics, chronological validation, baseline comparisons, and interpretable statistical forecasting methods.

There are two ways to explore the work:

1. **Jupyter notebook:** a step-by-step learning experience with visualizations and explanatory notes.
2. **Python command-line workflow:** a repeatable local backtest and future forecast reference that writes structured reports and plots.

The notebook and script are separate entry points. They have related analytical goals, but their exact implementation details and outputs should not be assumed to be identical.

## 🎯 What This Project Covers

- Loading and validating a monthly passenger series.
- Parsing the original date representation and normalizing observations to a monthly index.
- Exploring time-series level, trend, and annual seasonality.
- Applying the Augmented Dickey-Fuller test as a stationarity diagnostic.
- Preserving time order with chronological train/test splits.
- Establishing naive and seasonal-naive forecast benchmarks in the notebook.
- Comparing seasonal Exponential Smoothing and SARIMA models.
- Evaluating held-out forecasts with MAE, RMSE, and supplementary MAPE.
- Reviewing residual behaviour and common sources of forecasting error.
- Producing an illustrative future forecast and local output artifacts.
- Running static notebook checks, automated tests, and a CI smoke test.

## 📈 Methods and Models

The current notebook and command-line workflow use classical statistical methods.

| Method | Purpose |
|---|---|
| Naive baseline | Carries the last training observation forward |
| Seasonal-naive baseline | Repeats the previous annual seasonal pattern, included in the notebook |
| Exponential Smoothing | Models trend and annual seasonal structure |
| SARIMA | Models non-seasonal and seasonal autoregressive structure |
| Augmented Dickey-Fuller | Provides a unit-root stationarity diagnostic |
| MAE and RMSE | Measures forecast errors in the target's original units |
| MAPE | Supplementary percentage-based error measure |

**LSTM is not part of the current executable workflow.** Older descriptions may have referred to neural forecasting, but the maintained notebook and script do not currently implement an LSTM model. TensorFlow is therefore not required.

A model name alone does not establish that a forecast is good. Every comparison must use the same chronological validation window and should include simple baselines.

## 🗂️ Repository Contents

```text
Air-Passengers-Time-series-forecasting/
├── AirPassengers.csv
├── TimeSeriesForecasting.ipynb
├── scripts/
│   ├── forecast.py
│   └── validate_notebook.py
├── tests/
│   ├── test_forecast.py
│   └── test_repository.py
├── docs/
│   ├── README.md
│   ├── architecture.md
│   ├── notebook-guide.md
│   ├── methodology.md
│   ├── models.md
│   ├── data.md
│   ├── data-dictionary.md
│   ├── installation.md
│   ├── development.md
│   ├── evaluation.md
│   ├── experiment-protocol.md
│   ├── results-interpretation.md
│   ├── glossary.md
│   ├── maintenance.md
│   ├── reproducibility.md
│   ├── testing.md
│   ├── troubleshooting.md
│   ├── faq.md
│   ├── deployment.md
│   ├── api.md
│   └── database.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   ├── documentation_request.yml
│   │   └── config.yml
│   ├── workflows/
│   │   └── ci.yml
│   ├── dependabot.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── .editorconfig
├── .env.example
├── .gitattributes
├── .gitignore
├── CITATION.cff
├── CODEOWNERS
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
```

The tree above describes the maintained project files. Local virtual environments, Python caches, notebook checkpoints, editor state, logs, and generated forecasts should remain untracked.

## 📊 Dataset

The checked-in `AirPassengers.csv` file contains **144 monthly observations** from 1949 to 1960.

| Property | Description |
|---|---|
| File | `AirPassengers.csv` |
| Time coverage | January 1949 to December 1960 |
| Frequency | Monthly |
| Number of observations | 144 |
| Date field | `Month` |
| Target field | `Passengers` |
| Original target unit | Thousands of passengers in the classic teaching series |

The source file uses date strings representing the 15th day of each month. The analysis normalizes these observations to month-start timestamps for consistent monthly indexing. The measurements remain monthly totals.

Read [docs/data.md](docs/data.md) before changing or redistributing the dataset. Its exact source and licensing should be verified for the copy being used. The repository does not claim that historical observations represent present-day airline operations.

## ⚙️ Getting Started

### Prerequisites

- Python **3.10 or newer** is recommended.
- pip.
- Git, if cloning the repository.
- Jupyter, installed through the project requirements.

### 1. Clone the repository

```bash
git clone https://github.com/Brajesh31/Air-Passengers-Time-series-forecasting.git
cd Air-Passengers-Time-series-forecasting
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For development and test tools:

```bash
python -m pip install -r requirements-dev.txt
```

The dependency manifests currently specify compatible version ranges rather than a fully locked environment. Record installed package versions when reproducing or publishing a result.

## 📓 Run the Notebook

Start Jupyter from the repository root:

```bash
jupyter notebook
```

Open `TimeSeriesForecasting.ipynb`, restart the kernel, and run the cells in order. The notebook expects the dataset at the repository root.

The notebook includes data inspection, time-series plots, seasonal decomposition, stationarity diagnostics, a chronological holdout, baseline forecasts, seasonal model fitting, error metrics, residual inspection, and an illustrative future forecast.

For a clean analysis, do not execute cells out of order or reuse stale variables from a previous kernel session.

## 🖥️ Run the Command-Line Workflow

Run the maintained forecasting script from the repository root:

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

Options:

| Argument | Meaning | Default |
|---|---|---:|
| `--data` | Path to the input CSV | `AirPassengers.csv` |
| `--horizon` | Number of future months to forecast | 12 |
| `--test-months` | Number of most recent months reserved for the chronological holdout | 24 |

Example with a custom path and forecast horizon:

```bash
python scripts/forecast.py --data AirPassengers.csv --horizon 6 --test-months 24
```

The script validates the input series, fits seasonal model candidates on the training period, evaluates the held-out observations, and fits the candidates on the full history to create future forecasts. It writes local outputs under `artifacts/`.

## ✅ Testing and Validation

Run the same checks used by the repository's CI workflow:

```bash
python scripts/validate_notebook.py
python -m pytest
python scripts/forecast.py --horizon 6 --test-months 24
```

The checks cover:

- Notebook JSON structure and Python syntax in code cells.
- Repository dataset and manifest expectations.
- Monthly dataset loading and validation.
- Forecast metric calculations.
- A command-line smoke run against the checked-in dataset.

**Important distinction:** static notebook validation does not execute notebook cells. Unit tests and a CLI smoke test do not establish that a model will generalize to new airline data. Read [docs/testing.md](docs/testing.md) and [docs/evaluation.md](docs/evaluation.md) for the full validation guidance.

## 📁 Generated Outputs

The command-line workflow creates the following files inside `artifacts/`:

| Output | Description |
|---|---|
| `forecast_report.json` | Dataset coverage, holdout dates, diagnostic values, metrics, and future forecasts |
| `backtest_predictions.csv` | Actual holdout observations and candidate predictions |
| `future_forecasts.csv` | Future monthly point forecasts from the candidate models |
| `backtest.png` | Plot of the historical series and holdout predictions |

These files are generated locally and are excluded from version control by `.gitignore`. They are not checked-in model releases or guaranteed forecast products.

## 📚 Documentation

| Guide | Description |
|---|---|
| [Documentation index](docs/README.md) | Entry point to all guides |
| [Architecture](docs/architecture.md) | Notebook, script, data flow, and project boundaries |
| [Notebook walkthrough](docs/notebook-guide.md) | Cell sequence, dependencies, execution and output hygiene |
| [Methodology](docs/methodology.md) | Trend, seasonality, stationarity, differencing and forecasting workflow |
| [Model reference](docs/models.md) | Implemented models, parameters and non-implemented methods |
| [Data dictionary](docs/data-dictionary.md) | Field definitions, schema and validation contract |
| [Experiment protocol](docs/experiment-protocol.md) | Fair model comparison and experiment reporting |
| [Results interpretation](docs/results-interpretation.md) | Reading metrics, residuals and forecast limitations |
| [Glossary](docs/glossary.md) | Time-series and forecasting terminology |
| [Maintenance](docs/maintenance.md) | Repository, dependency and CI maintenance practices |
| [Dataset](docs/data.md) | Data schema, dates, units, provenance, and limitations |
| [Installation](docs/installation.md) | Environment setup and dependencies |
| [Development](docs/development.md) | Project structure and development standards |
| [Evaluation](docs/evaluation.md) | Metrics, baselines, and chronological validation |
| [Reproducibility](docs/reproducibility.md) | Experiment records and environment capture |
| [Testing](docs/testing.md) | Automated checks and validation protocol |
| [Troubleshooting](docs/troubleshooting.md) | Common setup and execution problems |
| [FAQ](docs/faq.md) | Common project questions |
| [Deployment](docs/deployment.md) | Current local-only status and production prerequisites |
| [API](docs/api.md) | Explicit statement of the absence of a network API |
| [Database](docs/database.md) | CSV input and local generated outputs |

## ⚠️ Known Limitations

- The series has only 144 monthly observations.
- The observations are historical and end in 1960.
- The data is aggregated and has no airline-, route-, fare-, or capacity-level features.
- Weather, economic conditions, schedule changes, disruptions, and other external drivers are not represented.
- A single chronological holdout is not enough for robust model selection.
- Prediction intervals and calibrated uncertainty are not currently provided by the documented workflow.
- The project is not a deployed service and has no online API or database.
- Statistical fit and a passing CI run do not prove future accuracy.

For meaningful operational use, an entirely different evidence base and validation process would be required. See [docs/deployment.md](docs/deployment.md).

## 🤝 Contributing

Contributions that improve analytical correctness, reproducibility, tests, or documentation are welcome.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Open an issue to discuss substantial changes.
3. Preserve chronological validation and prevent leakage.
4. Compare against appropriate baselines.
5. Run the local checks and document the evidence.
6. Update the relevant guides and [CHANGELOG.md](CHANGELOG.md).

GitHub issue forms are available for bug reports, feature requests, and documentation requests.

## 🔐 Security

Do not commit credentials, private datasets, or sensitive files. For vulnerability reports, follow [SECURITY.md](SECURITY.md) and use private reporting rather than a public issue.

## 👤 Maintainer

**Brajesh Kumar**  
GitHub: [@Brajesh31](https://github.com/Brajesh31)

## 📄 License

This repository is distributed under the MIT License. See [LICENSE](LICENSE) for the complete terms.
