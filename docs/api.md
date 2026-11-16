# 🔌 API Status and Interface Contract

## 1. Current status

No HTTP API, REST endpoint, GraphQL service, RPC interface, or network model-serving endpoint is implemented in this repository.

The supported ways to interact with the project are:

1. Execute the guided Jupyter notebook at `TimeSeriesForecasting.ipynb`.
2. Run the local command-line workflow at `scripts/forecast.py`.

The CLI is a local process interface. It is not an API server.

## 2. Current command-line interface

The script accepts the following arguments:

| Argument | Purpose | Default |
|---|---|---|
| `--data` | Input CSV path | Repository `AirPassengers.csv` |
| `--horizon` | Number of future monthly observations | 12 |
| `--test-months` | Number of final observations reserved for holdout evaluation | 24 |

Example:

```bash
python scripts/forecast.py --data AirPassengers.csv --horizon 12 --test-months 24
```

Use the script's help output to confirm the available options:

```bash
python scripts/forecast.py --help
```

The command validates the input, performs a chronological holdout evaluation, fits candidate models, and writes local artifacts. See [architecture.md](architecture.md) for the execution stages.

## 3. Why this page exists

A project documentation set sometimes includes an API guide even when the software has no API. This page makes the current boundary explicit so that readers do not assume endpoints, request schemas, authentication, or service guarantees exist.

## 4. Requirements for a future API

If a service interface is proposed, define the contract before writing endpoints.

### Request fields
A future request would need to define the target series or dataset identifier, observation frequency, historical range, forecast horizon, model identifier, and any optional model configuration. The current project does not define such a network request schema.

### Response fields
A useful response would likely include forecast timestamps, point predictions, model and data versions, units, generation time, and uncertainty intervals where supported. The current project does not return a network response.

### Validation
A future API would need to specify behaviour for missing dates, duplicate timestamps, malformed values, unsupported frequencies, invalid horizons, unavailable models, and oversized requests.

### Errors
A future contract should define stable error codes and HTTP status semantics. Do not invent status codes for an API that does not exist.

### Security
A deployed service would need authentication, authorization, rate limiting, transport security, input limits, audit logging, and secret management appropriate to its environment.

### Operations
A service would also need health checks, monitoring, request tracing, model versioning, deployment procedures, and a rollback strategy.

## 5. Why deployment should not come first

An API cannot make an unsuitable model useful. Before exposing forecasts over a network, the project would need current data, defensible validation, uncertainty communication, model acceptance criteria, and an identified operational use case. See [deployment.md](deployment.md).

## 6. Related documentation

- [CLI and architecture](architecture.md)
- [Installation](installation.md)
- [Testing](testing.md)
- [Deployment boundaries](deployment.md)
