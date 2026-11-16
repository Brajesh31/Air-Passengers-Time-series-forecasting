from pathlib import Path

import nbformat
import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_notebook_is_valid_nbformat():
    path = ROOT / "TimeSeriesForecasting.ipynb"
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    assert len(notebook.cells) >= 20


def test_dataset_manifest_has_monthly_dataset():
    csv = ROOT / "AirPassengers.csv"
    assert csv.is_file()
    assert csv.stat().st_size > 0


def test_project_dependencies_exist():
    assert (ROOT / "requirements.txt").is_file()
    assert (ROOT / "requirements-dev.txt").is_file()
