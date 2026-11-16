# ✈️ Air Passengers Time-Series Forecasting

A reproducible educational project exploring monthly international airline passenger data from 1949 to 1960. The repository includes the historical CSV dataset, a Jupyter notebook, a command-line forecasting workflow, tests, documentation, and GitHub Actions validation.

> **Important:** This is a small historical teaching dataset. The forecasts are not current airline-demand estimates and are not suitable for operational planning.

## 📚 Contents

- `AirPassengers.csv`: 144 monthly observations from January 1949 through December 1960.
- `TimeSeriesForecasting.ipynb`: data inspection, stationarity diagnostics, seasonal decomposition, chronological validation, baselines, SARIMA, and Exponential Smoothing.
- `scripts/forecast.py`: command-line backtest and forecasting reference workflow.
- `scripts/validate_notebook.py`: static notebook validation.
- `tests/`: dataset, metric, and repository tests.
- `docs/`: project architecture, data, methodology, testing, and responsible-use guides.

## 🔬 Methods

The current workflow compares:
- Naive and seasonal-naive forecasts.
- Additive seasonal Exponential Smoothing.
- SARIMA with annual seasonality.

The notebook includes monthly date normalization, trend and seasonality plots, Augmented Dickey-Fuller diagnostics, chronological train/test separation, MAE, RMSE, MAPE, residual inspection, and a future forecast illustration.

**LSTM is not part of the current executable workflow.** Older repository text mentioned it, but the original notebook did not contain an LSTM implementation.

## 🗂️ Repository structure

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
│   ├── data.md
│   ├── evaluation.md
│   ├── installation.md
│   ├── development.md
│   ├── testing.md
│   ├── reproducibility.md
│   ├── troubleshooting.md
│   ├── faq.md
│   ├── deployment.md
│   ├── api.md
│   └── database.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/ci.yml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── .gitignore
├── LICENSE
└── project policy files
```

## ⚙️ Installation

**Windows PowerShell**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For development checks, install `requirements-dev.txt`.

## ▶️ Run the notebook

Start Jupyter from the repository root:

```bash
jupyter notebook
```

Open `TimeSeriesForecasting.ipynb`, restart the kernel, and run all cells in order.

## 🖥️ Run the command-line workflow

```bash
python scripts/forecast.py --horizon 12 --test-months 24
```

The script validates the monthly series, compares seasonal models on a chronological holdout, and writes outputs under `artifacts/`:
- `forecast_report.json`
- `backtest_predictions.csv`
- `future_forecasts.csv`
- `backtest.png`

Generated outputs are intentionally ignored by Git.

## ✅ Validate the project

```bash
python scripts/validate_notebook.py
python -m pytest
```

GitHub Actions runs static notebook checks, repository tests, and a CLI smoke test. Static notebook validation does not execute the notebook cells or prove forecast accuracy.

## 📊 Dataset limitations

The dataset contains aggregated monthly passenger totals. It does not contain route, airline, capacity, fare, schedule, economic, weather, or disruption variables. It is historical and cannot demonstrate forecasting performance on modern airline operations.

Use chronological holdout or rolling-origin evaluation. Do not shuffle observations or tune repeatedly against the final test window.

## 📖 Documentation

See [docs/README.md](docs/README.md) for the complete documentation index.

## 📄 License

See [LICENSE](LICENSE).

Maintained by Brajesh Kumar, GitHub: [@Brajesh31](https://github.com/Brajesh31).
