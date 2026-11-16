# 🗄️ Database and Persistence

The repository does not use a database. It reads the checked-in `AirPassengers.csv` file into a Pandas Series.

The command-line workflow writes local generated outputs under `artifacts/`:
- Backtest predictions CSV.
- Future forecast CSV.
- Forecast report JSON.
- Backtest visualization PNG.

These are local generated files and are ignored by Git. No database server or persistent application storage is required for the current project.
