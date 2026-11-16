# 🔌 API

No HTTP or network API is implemented in this repository. The user interfaces are the Jupyter notebook and the local command-line script `scripts/forecast.py`.

A future forecasting API would need an explicit contract for:
- Historical observation dates and units.
- Forecast horizon and frequency.
- Model identifier and version.
- Point forecasts and uncertainty intervals.
- Input validation and missing-date behaviour.
- Error responses and request limits.

Do not describe the current command-line script as a REST API.
