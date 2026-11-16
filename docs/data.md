# 📊 Dataset Documentation

## Included dataset

The repository includes `AirPassengers.csv`, a monthly time series with two columns:

| Column | Meaning | Type |
|---|---|---|
| `Month` | Observation month, stored as a day-month-year text value in the source CSV | Date |
| `Passengers` | Monthly passenger total in thousands in the classic source dataset | Numeric |

The series contains 144 monthly observations from January 1949 through December 1960. The expected monthly frequency is continuous, with no gaps.

## Data preparation

The forecasting notebook and CLI normalize the provided mid-month date values to month-start timestamps. Do not interpret those normalized dates as the exact day that passenger counts were collected. The underlying unit is monthly.

## Source and provenance

This file matches the classic AirPassengers teaching series. Before redistribution or reuse beyond educational analysis, verify the original publisher and applicable licence for the specific copy in this repository. Do not invent a source citation or imply the CSV is fresh operational data.

## Limitations

- The data covers only 12 years.
- It represents aggregated historical passenger totals rather than route-, airline-, or cabin-level activity.
- It does not include fares, capacity, schedules, economic factors, disruptions, or external regressors.
- It is not representative of contemporary airline markets.
- It is unsuitable as a standalone production planning input.

## Data quality checks

The project validates the required column names, parses month dates, validates numeric passenger counts, checks positive values, rejects duplicate timestamps, and checks for a continuous monthly sequence.

## Data updates

If replacing or extending the CSV, update this file and document publisher, licence, retrieval date, units, transformations, date range, and checksum. Keep validation periods chronological and ensure future records are never used to train models evaluated on earlier periods.
