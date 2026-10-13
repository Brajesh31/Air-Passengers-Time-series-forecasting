# Air Passengers Time-Series Forecasting

This repository explores monthly international airline passenger data from 1949-1960 using exploratory analysis, time-series decomposition, classical forecasting, and neural-network experiments.

## Contents

- `AirPassengers.csv` - monthly passenger observations.
- `TimeSeriesForecasting.ipynb` - analysis, preprocessing, models, visualizations, and evaluation.

The notebook discusses ARIMA and LSTM approaches and uses metrics such as MAE, MSE, and RMSE. Exact outputs depend on the notebook cells, library versions, random seeds, and hardware.

## Setup

Create a Python environment with Jupyter and the libraries imported by the notebook:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install jupyter pandas numpy matplotlib seaborn statsmodels scikit-learn tensorflow
jupyter notebook
```

Open `TimeSeriesForecasting.ipynb` and run cells in order. Keep `AirPassengers.csv` beside the notebook unless the notebook is deliberately updated to use a different path.

## Dataset and limitations

The dataset is a small historical demonstration set, not a current airline planning source. It does not represent every route, market, season, disruption, or operational constraint. Forecasts are educational and must not be treated as production demand plans without current data, validation, uncertainty intervals, and domain review.

See [docs/data.md](docs/data.md), [docs/development.md](docs/development.md), and [docs/reproducibility.md](docs/reproducibility.md).

## Ownership

Maintained by Brajesh Kumar (`brajesh31`).

Last updated: 2026-10-13 21:12 UTC
