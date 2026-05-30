from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from tslab.baselines import moving_average, seasonal_naive
from tslab.metrics import mae, mse, smape
from tslab.synthetic import seasonal_series
from tslab.windowing import WindowSpec, rolling_windows


def evaluate() -> None:
    values = seasonal_series(length=240, season_length=24, noise=0.03, seed=7)
    spec = WindowSpec(lookback=72, horizon=24, stride=24)

    rows: list[tuple[str, float, float, float]] = []
    for name in ("seasonal_naive", "moving_average"):
        actual_all: list[float] = []
        predicted_all: list[float] = []
        for history, target in rolling_windows(values, spec):
            if name == "seasonal_naive":
                pred = seasonal_naive(history, horizon=spec.horizon, season_length=24)
            else:
                pred = moving_average(history, horizon=spec.horizon, window=24)
            actual_all.extend(target)
            predicted_all.extend(pred)
        rows.append((name, mae(actual_all, predicted_all), mse(actual_all, predicted_all), smape(actual_all, predicted_all)))

    print("model           MAE       MSE       sMAPE")
    for name, mae_value, mse_value, smape_value in rows:
        print(f"{name:<15} {mae_value:.4f}    {mse_value:.4f}    {smape_value:.4f}")


if __name__ == "__main__":
    evaluate()

