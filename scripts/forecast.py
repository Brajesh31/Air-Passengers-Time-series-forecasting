"""
Air passenger forecasting reference implementation.

Run from the repository root:
    python -m pip install -r requirements.txt
    python scripts/forecast.py --horizon 12

The input is the historical monthly AirPassengers.csv teaching dataset.
Forecasts are illustrative and are not intended for operational airline planning.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "AirPassengers.csv"
OUTPUT_DIR = ROOT / "artifacts"


def load_series(path: Path) -> pd.Series:
    """Load a monthly passenger series with a validated monthly DatetimeIndex."""
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")
    frame = pd.read_csv(path)
    required = {"Month", "Passengers"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {sorted(missing)}")

    dates = pd.to_datetime(frame["Month"], dayfirst=True, errors="coerce")
    values = pd.to_numeric(frame["Passengers"], errors="coerce")
    if dates.isna().any() or values.isna().any():
        raise ValueError("Month and Passengers must contain valid, non-empty values.")
    if (values <= 0).any():
        raise ValueError("Passenger counts must be positive.")
    series = pd.Series(values.to_numpy(dtype=float), index=pd.DatetimeIndex(dates), name="Passengers")
    series = series.sort_index()
    if series.index.has_duplicates:
        raise ValueError("Monthly timestamps must be unique.")
    if len(series) < 36:
        raise ValueError("At least 36 monthly observations are required for seasonal modelling.")
    # Source data is dated on the 15th. Normalize to month starts before checking continuity.
    series.index = series.index.to_period("M").to_timestamp(how="start")
    expected = pd.date_range(series.index.min(), series.index.max(), freq="MS")
    if not series.index.equals(expected):
        raise ValueError("The dataset must contain a continuous monthly series without gaps.")
    return series


def metrics(actual: pd.Series, predicted: pd.Series) -> dict[str, float]:
    aligned = pd.concat([actual.rename("actual"), predicted.rename("predicted")], axis=1).dropna()
    if aligned.empty:
        raise ValueError("No overlapping actual and predicted observations.")
    mae = mean_absolute_error(aligned["actual"], aligned["predicted"])
    rmse = float(np.sqrt(mean_squared_error(aligned["actual"], aligned["predicted"])))
    mape = float((np.abs((aligned["actual"] - aligned["predicted"]) / aligned["actual"])).mean() * 100)
    return {"MAE": float(mae), "RMSE": rmse, "MAPE_percent": mape}


def fit_forecasts(train: pd.Series, horizon: int) -> dict[str, Any]:
    """Fit seasonal benchmark and SARIMA candidates, returning forecast series."""
    if horizon < 1:
        raise ValueError("Forecast horizon must be positive.")
    if len(train) < 36:
        raise ValueError("Training set needs at least 36 observations for annual seasonality.")

    seasonal = ExponentialSmoothing(
        train,
        trend="add",
        seasonal="add",
        seasonal_periods=12,
        initialization_method="estimated",
    ).fit(optimized=True)
    sarima = SARIMAX(
        train,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    ).fit(disp=False)

    index = pd.date_range(train.index[-1] + pd.offsets.MonthBegin(1), periods=horizon, freq="MS")
    return {
        "Seasonal Exponential Smoothing": pd.Series(seasonal.forecast(horizon).to_numpy(), index=index),
        "SARIMA(1,1,1)x(1,1,1,12)": pd.Series(sarima.forecast(horizon).to_numpy(), index=index),
        "models": {"seasonal_smoothing": seasonal, "sarima": sarima},
    }


def run(path: Path, horizon: int, test_months: int) -> dict[str, Any]:
    series = load_series(path)
    if test_months < 12 or test_months >= len(series) - 24:
        raise ValueError("test_months must be at least 12 and leave at least 24 training months.")

    train = series.iloc[:-test_months]
    test = series.iloc[-test_months:]
    candidates = fit_forecasts(train, len(test))
    forecast_series = {
        name: value for name, value in candidates.items() if isinstance(value, pd.Series)
    }
    forecast_metrics = {name: metrics(test, prediction) for name, prediction in forecast_series.items()}

    # ADF is a diagnostic, not a model-selection oracle. The null hypothesis is a unit root.
    adf = adfuller(train, autolag="AIC")
    future_candidates = fit_forecasts(series, horizon)
    future_forecasts = {
        name: value for name, value in future_candidates.items() if isinstance(value, pd.Series)
    }

    OUTPUT_DIR.mkdir(exist_ok=True)
    pd.DataFrame({"actual": test, **{name: pred for name, pred in forecast_series.items()}}).to_csv(
        OUTPUT_DIR / "backtest_predictions.csv", index_label="Month"
    )
    pd.DataFrame(future_forecasts).to_csv(OUTPUT_DIR / "future_forecasts.csv", index_label="Month")
    report = {
        "observations": int(len(series)),
        "start": str(series.index.min().date()),
        "end": str(series.index.max().date()),
        "train_observations": int(len(train)),
        "test_observations": int(len(test)),
        "test_start": str(test.index.min().date()),
        "test_end": str(test.index.max().date()),
        "adf_statistic": float(adf[0]),
        "adf_p_value": float(adf[1]),
        "backtest_metrics": forecast_metrics,
        "future_horizon_months": int(horizon),
        "future_forecasts": {
            model: {str(date.date()): float(value) for date, value in forecast.items()}
            for model, forecast in future_forecasts.items()
        },
        "note": "Historical teaching data only. Backtest performance is not a guarantee of future accuracy.",
    }
    (OUTPUT_DIR / "forecast_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    fig, ax = plt.subplots(figsize=(12, 6))
    series.plot(ax=ax, label="Observed")
    for name, prediction in forecast_series.items():
        prediction.plot(ax=ax, label=f"{name} backtest")
    ax.set_title("Air passengers: chronological holdout backtest")
    ax.set_xlabel("Month")
    ax.set_ylabel("Passengers (thousands in original source)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "backtest.png", dpi=150)
    plt.close(fig)

    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an AirPassengers seasonal forecasting backtest.")
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="Path to AirPassengers.csv")
    parser.add_argument("--horizon", type=int, default=12, help="Future forecast horizon in months")
    parser.add_argument("--test-months", type=int, default=24, help="Chronological holdout size")
    args = parser.parse_args()

    report = run(args.data, args.horizon, args.test_months)
    print(json.dumps({
        "observations": report["observations"],
        "test_start": report["test_start"],
        "test_end": report["test_end"],
        "backtest_metrics": report["backtest_metrics"],
        "future_horizon_months": report["future_horizon_months"],
    }, indent=2))


if __name__ == "__main__":
    main()
