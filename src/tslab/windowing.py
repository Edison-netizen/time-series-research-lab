from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Sequence, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class WindowSpec:
    lookback: int
    horizon: int
    stride: int = 1


def rolling_windows(values: Sequence[T], spec: WindowSpec) -> Iterator[tuple[list[T], list[T]]]:
    """Yield chronological input/target windows for time-series forecasting."""
    if spec.lookback <= 0:
        raise ValueError("lookback must be positive")
    if spec.horizon <= 0:
        raise ValueError("horizon must be positive")
    if spec.stride <= 0:
        raise ValueError("stride must be positive")

    total = spec.lookback + spec.horizon
    if total > len(values):
        return

    for start in range(0, len(values) - total + 1, spec.stride):
        pivot = start + spec.lookback
        yield list(values[start:pivot]), list(values[pivot:pivot + spec.horizon])
