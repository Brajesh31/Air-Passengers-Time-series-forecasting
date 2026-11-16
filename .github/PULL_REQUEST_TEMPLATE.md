## Summary

Describe the change and the reason for it.

## Forecasting and data impact

- [ ] Monthly chronology is preserved.
- [ ] No future observations leak into training or preprocessing.
- [ ] Train/test boundaries and forecast horizon are documented.
- [ ] Baseline forecasts are included where model comparisons change.
- [ ] Metrics use the same validation window and units.

## Validation

- [ ] `python scripts/validate_notebook.py`
- [ ] `python -m pytest`
- [ ] `python scripts/forecast.py --horizon 12 --test-months 24` (when relevant)
- [ ] Notebook was run from a clean kernel (when relevant).

## Documentation and safety

- [ ] README/docs/changelog updated.
- [ ] No credentials, private data, or unrelated artifacts included.
- [ ] Limitations and warnings are stated honestly.
