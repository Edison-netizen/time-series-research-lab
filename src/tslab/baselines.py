from __future__ import annotations

from statistics import mean
from typing import Sequence


def seasonal_naive(history: Sequence[float], horizon: int, season_length: int) -> list[float]:
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if season_length <= 0:
        raise ValueError("season_length must be positive")
    if len(history) < season_length:
        raise ValueError("history is shorter than one season")

    season = list(history[-season_length:])
    return [season[i % season_length] for i in range(horizon)]


def moving_average(history: Sequence[float], horizon: int, window: int) -> list[float]:
    if horizon <= 0:
        raise ValueError("horizon must be positive")
    if window <= 0:
        raise ValueError("window must be positive")
    if len(history) < window:
        raise ValueError("history is shorter than moving-average window")

    value = mean(history[-window:])
    return [value] * horizon

