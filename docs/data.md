# 📊 Dataset Documentation

## Included dataset

The repository includes `AirPassengers.csv`, a monthly time series with two columns:

| Column | Meaning | Type |
|---|---|---|
| `Month` | Observation month, stored as day-month-year text in the source CSV | Date |
| `Passengers` | Monthly passenger total in thousands in the classic source series | Numeric |

The series contains 144 observations from January 1949 through December 1960. The expected frequency is continuous monthly.

## Data preparation

The source dates are on the 15th of each month. The analysis normalizes them to month-start timestamps to establish a standard monthly index. That normalization does not change the fact that the measurements represent monthly totals.

## Provenance and licensing

This file matches the classic AirPassengers teaching series. Verify the original publisher and applicable licence for the specific copy before redistributing it elsewhere. Do not invent a source citation or imply that the data is current operational information.

## Limitations

- Only 12 years of historical observations.
- Aggregated passenger totals, not route-, carrier-, or cabin-level records.
- No fares, capacity, schedules, macroeconomic factors, weather, or disruption variables.
- Not representative of current airline markets.
- Not suitable as a standalone production planning input.

## Data validation

The command-line loader validates column names, date parsing, numeric positive passenger counts, unique monthly timestamps, and a continuous monthly index.

If updating the dataset, record source, licence, retrieval date, units, transformations, date range, and checksum. Keep all evaluation windows chronological.
