from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

import numpy as np


@dataclass(frozen=True)
class WindowSpec:
    lookback: int
    horizon: int
    stride: int = 1


def rolling_windows(values: np.ndarray, spec: WindowSpec) -> Iterator[tuple[np.ndarray, np.ndarray]]:
    """Yield chronological input/target windows for time-series forecasting."""
    if values.ndim == 1:
        values = values[:, None]
    total = spec.lookback + spec.horizon
    if total > len(values):
        return

    for start in range(0, len(values) - total + 1, spec.stride):
        pivot = start + spec.lookback
        yield values[start:pivot], values[pivot:pivot + spec.horizon]

