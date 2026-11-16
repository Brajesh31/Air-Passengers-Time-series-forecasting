# 🧾 Data Dictionary and Validation Contract

## 1. Purpose

This document defines the expected structure of the repository's historical CSV input. It is a practical contract for contributors who inspect or replace the dataset. It does not claim that the current dataset has a complete externally verified provenance record.

## 2. Dataset file

**Path:** `AirPassengers.csv`

The file is a two-column monthly time series. The current script expects the exact header names `Month` and `Passengers`.

## 3. Field definitions

| Field | Type in source | Meaning | Validation expectation |
|---|---|---|---|
| `Month` | Date-like text | Label for the observation month | Must parse into a valid date |
| `Passengers` | Numeric text or number | Monthly passenger total | Must parse to a positive numeric value |

### Month

The source uses dates represented on the 15th of each month. The CLI parses using day-first interpretation, converts dates to monthly periods, and normalizes them to the first day of each month.

The normalized month-start index is used to express monthly frequency consistently. It is not a change to the measurement period.

### Passengers

The target is the monthly total in the conventional thousands-of-passengers unit for the classic AirPassengers series. Keep this unit consistent across data, charts, error metrics, and documentation. If the data is converted to individual passengers, document the scaling and update all labels and tests.

## 4. Current data contract

The CLI loader requires:

- The CSV path must exist and point to a file.
- Both required columns must be present.
- Every date must parse successfully.
- Every target value must convert to a number.
- No target value may be missing or non-positive.
- Monthly timestamps must be unique.
- The normalized index must contain every month between the first and last observations.
- At least 36 observations must be present for seasonal modelling.

The loader sorts the observations chronologically before checking the monthly sequence. This means an unsorted source file can be accepted after sorting, but duplicate or missing months are not accepted.

## 5. Expected current coverage

The repository's test suite expects 144 observations, beginning in January 1949 and ending in December 1960. These expectations are specific to the currently checked-in historical file. If the data is intentionally updated, revise the tests and documentation with evidence rather than weakening the assertions without explanation.

## 6. Invalid input examples

The following conditions should be rejected or investigated:

- Header renamed from `Month` to `Date` without updating the loader.
- A date such as `not-a-date`.
- Passenger count containing non-numeric text.
- Empty date or passenger cells.
- Zero or negative passenger counts.
- Two rows belonging to the same month.
- A missing month between two otherwise valid dates.
- A very short series that cannot support the seasonal modelling assumptions.

## 7. Transformation record

Any preprocessing beyond the current date normalization should be documented. Record the original field, transformation, reason, order of operations, effect on units, and whether the transformation is fitted using training data only.

Do not calculate statistics over the full series and then use them to transform the training segment for an honest holdout evaluation if those statistics depend on future observations.

## 8. Dataset replacement checklist

- [ ] Source and version verified.
- [ ] Licence and redistribution terms reviewed.
- [ ] Retrieval date recorded.
- [ ] File checksum recorded.
- [ ] Column names and data types documented.
- [ ] Units and aggregation level documented.
- [ ] Frequency and time zone documented where relevant.
- [ ] Duplicate and missing periods checked.
- [ ] Invalid and non-positive values checked.
- [ ] Start and end dates updated.
- [ ] Tests updated with explicit justification.
- [ ] README and dataset guide updated.
- [ ] Evaluation split reconsidered.
- [ ] No personal or restricted information included.

## 9. Data governance

Do not commit passenger-level, customer-level, booking-level, or commercially restricted data. The repository's educational purpose does not justify publishing private or proprietary datasets. Any new dataset with personal or confidential information requires a separate governance review.

## 10. Related guides

- [Dataset documentation](data.md)
- [Reproducibility](reproducibility.md)
- [Testing](testing.md)
- [Evaluation](evaluation.md)
