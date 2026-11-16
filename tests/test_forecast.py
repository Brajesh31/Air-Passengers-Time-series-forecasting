from pathlib import Path

import pandas as pd
import pytest

from scripts.forecast import load_series, metrics

ROOT = Path(__file__).resolve().parents[1]


def test_dataset_loads_as_complete_monthly_series():
    series = load_series(ROOT / "AirPassengers.csv")
    assert len(series) == 144
    assert series.index.is_monotonic_increasing
    assert series.index.freqstr == "MS"
    assert series.index[0] == pd.Timestamp("1949-01-01")
    assert series.index[-1] == pd.Timestamp("1960-12-01")


def test_dataset_has_expected_schema_validation(tmp_path):
    path = tmp_path / "bad.csv"
    path.write_text("date,value\n1949-01-01,10\n", encoding="utf-8")
    with pytest.raises(ValueError, match="required columns"):
        load_series(path)


def test_metrics_are_zero_for_perfect_forecast():
    actual = pd.Series([10.0, 20.0, 30.0])
    predicted = pd.Series([10.0, 20.0, 30.0])
    scores = metrics(actual, predicted)
    assert scores["MAE"] == pytest.approx(0.0)
    assert scores["RMSE"] == pytest.approx(0.0)
    assert scores["MAPE_percent"] == pytest.approx(0.0)
