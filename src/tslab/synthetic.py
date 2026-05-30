from __future__ import annotations

import math
import random


def seasonal_series(length: int, season_length: int, noise: float = 0.0, seed: int = 42) -> list[float]:
    if length <= 0:
        raise ValueError("length must be positive")
    if season_length <= 1:
        raise ValueError("season_length must be greater than 1")

    rng = random.Random(seed)
    values: list[float] = []
    for t in range(length):
        seasonal = math.sin(2 * math.pi * t / season_length)
        trend = 0.01 * t
        values.append(trend + seasonal + rng.uniform(-noise, noise))
    return values

