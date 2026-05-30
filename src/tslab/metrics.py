from __future__ import annotations

from math import isclose
from typing import Sequence


def _same_length(actual: Sequence[float], predicted: Sequence[float]) -> None:
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have the same length")
    if not actual:
        raise ValueError("metric input must not be empty")


def mae(actual: Sequence[float], predicted: Sequence[float]) -> float:
    _same_length(actual, predicted)
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


def mse(actual: Sequence[float], predicted: Sequence[float]) -> float:
    _same_length(actual, predicted)
    return sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)


def smape(actual: Sequence[float], predicted: Sequence[float]) -> float:
    _same_length(actual, predicted)
    terms: list[float] = []
    for a, p in zip(actual, predicted):
        denom = (abs(a) + abs(p)) / 2
        if isclose(denom, 0.0):
            terms.append(0.0)
        else:
            terms.append(abs(a - p) / denom)
    return sum(terms) / len(terms)

