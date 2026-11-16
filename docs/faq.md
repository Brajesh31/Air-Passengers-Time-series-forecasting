# ❓ Frequently Asked Questions

## Is this a live airline-demand forecasting system?

No. It uses a small historical monthly training dataset from 1949-1960.

## Why should I not use random train/test splitting?

Random splitting leaks temporal context and does not reflect forecasting into the future. Use earlier months for training and later months for testing.

## Why include simple baselines?

A seasonal time series can be forecast surprisingly well by repeating the previous year's pattern. Complex models must demonstrate value beyond those baselines.

## Does the repository use LSTM?

The current rebuilt notebook and command-line workflow focus on classical seasonal methods: seasonal naive, Exponential Smoothing, and SARIMA. A neural network is not part of the current executable workflow.

## Is TensorFlow required?

No. The current project dependencies do not include TensorFlow because the implemented pipeline does not use it.

## Does the project have an API or database?

No. It is a local notebook and command-line analysis project.

## Where are generated outputs saved?

The command-line script writes metrics, forecasts, prediction CSV files, and a plot under `artifacts/`. This generated directory is excluded from Git.

## Are model results production-ready?

No. Current data, rolling-origin validation, prediction intervals, monitoring, operational variables, and domain review would be required.
