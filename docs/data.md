# 📊 Dataset Documentation and Provenance

## 1. Dataset summary

The repository includes `AirPassengers.csv`, a classic historical monthly airline passenger series commonly used to teach trend, seasonality, decomposition, and time-series forecasting. The file contains 144 observations spanning January 1949 through December 1960.

The dataset is deliberately small and historical. It is suitable for learning analytical workflows, not for estimating current passenger demand or making airline operating decisions.

| Attribute | Current repository value |
|---|---|
| File | `AirPassengers.csv` |
| Observation count | 144 |
| Start month | January 1949 |
| End month | December 1960 |
| Frequency | Monthly |
| Date column | `Month` |
| Target column | `Passengers` |
| Target interpretation | Monthly passenger total in thousands in the classic series |
| Expected index | Continuous monthly timestamps |
| Missing values | The loader rejects invalid or missing dates and values |

## 2. File format

The CSV has two required columns:

- `Month`: a textual date representing the observation month. The checked-in file uses day-month-year-style dates with the day set to the 15th.
- `Passengers`: a numeric monthly total.

The script expects these exact column names. A CSV with renamed headers is not automatically interpreted as equivalent. This strictness is intentional because silent schema guessing can cause incorrect analyses.

See [data-dictionary.md](data-dictionary.md) for field-level definitions and validation rules.

## 3. Date interpretation

The source dates use the 15th day of each month as a date label. The command-line loader parses the dates using day-first interpretation, then converts the timestamps to monthly periods and finally to month-start timestamps.

For example, a source date on the 15th of January is represented in the normalized time index as the first day of January. This is a monthly indexing convention. It does not mean the passenger count was measured only on the first day.

The loader checks that the normalized timestamps are unique and that every month between the first and last observation exists. A gap, duplicate month, or malformed date is rejected.

## 4. Data units and interpretation

The classic teaching series is conventionally expressed in thousands of passengers. Interpret plotted values and forecast errors using that unit convention. Do not silently relabel the series as individual passenger counts. If a future data version changes units, update the dataset documentation, data dictionary, plot labels, tests, and metric descriptions together.

## 5. Data preparation in the current code

The command-line loader performs these checks:

1. Confirms that the file exists.
2. Reads the CSV.
3. Checks for `Month` and `Passengers`.
4. Parses dates and converts passenger values to numeric.
5. Rejects unparseable or missing values.
6. Rejects zero or negative passenger counts.
7. Sorts observations chronologically.
8. Rejects duplicate timestamps.
9. Requires at least 36 observations for seasonal modelling.
10. Normalizes dates to month starts.
11. Checks that the monthly index is continuous.

The notebook performs its own data loading and analysis. Refer to the actual notebook cells when assessing its exact validation behaviour; do not assume that every script-level validation check is duplicated in the notebook.

## 6. Provenance and redistribution

The file matches the classic AirPassengers teaching series. However, the repository should not invent a publisher, download URL, retrieval date, checksum, or licence that has not been verified for the exact copy stored here.

Before redistributing the CSV separately or using it in a publication, identify the original source and verify the applicable terms. If provenance is established, add a stable citation, source version or retrieval date, licence statement, and checksum to the repository. A software licence in the root directory does not automatically grant rights to third-party data included in a repository.

## 7. Known limitations

- Only 12 years of observations are available.
- All observations are historical and end in 1960.
- The data is aggregated and does not identify airlines, routes, airports, cabins, or passenger segments.
- There are no fares, capacity, schedules, aircraft availability, macroeconomic factors, weather, or disruption indicators.
- The series cannot represent modern market structure, travel behaviour, or current shocks.
- A single series cannot support route-specific or carrier-specific forecasts.
- The dataset does not contain explicit explanatory variables for causal analysis.

## 8. Updating or replacing the dataset

A dataset change is not a routine file replacement. Before accepting one:

- Record the exact source and source version.
- Verify permission and licence terms.
- Document units, date format, time zone if relevant, frequency, and aggregation level.
- Record retrieval date and a cryptographic checksum.
- Check for duplicates, missing periods, invalid values, and structural breaks.
- Explain all transformations and excluded observations.
- Update the data dictionary and README.
- Update tests for the expected schema and coverage.
- Revisit train/test boundaries and evaluation assumptions.
- Do not combine different sources or units without documenting the reconciliation.

## 9. Privacy and sensitive data

The current dataset is aggregated historical data. Do not replace it with passenger-level records, personal information, booking records, or restricted commercial data. Any future dataset containing personal or confidential information requires a separate privacy, access-control, retention, and legal review.

## 10. Related documentation

- [Data dictionary](data-dictionary.md)
- [Architecture](architecture.md)
- [Reproducibility](reproducibility.md)
- [Evaluation protocol](evaluation.md)
