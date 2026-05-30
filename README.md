# Time Series Research Lab

Runnable notes and baselines for time-series forecasting.

This repository starts from the boring parts of forecasting research: chronological windows, baseline models, metrics, and experiment notes. If those are sloppy, neural models do not mean much.

## Scope

- Naive and moving-average baselines
- Univariate and multivariate window construction
- Rolling-window evaluation
- MAE / MSE / sMAPE metrics
- Synthetic smoke tests before real datasets

## Repository Shape

```text
configs/          experiment configs
scripts/          runnable smoke experiments
src/tslab/        reusable forecasting utilities
tests/            stdlib unittest coverage
docs/             protocol notes and benchmark hygiene
```

## Quick Smoke Run

```bash
python scripts/run_synthetic_baseline.py
python -m unittest discover -s tests
```

Expected shape:

```text
model           MAE       MSE       sMAPE
seasonal_naive  0.2397    0.0580    0.3270
moving_average  0.5982    0.4825    0.4872
```

## Baseline Queue

- seasonal naive
- moving average
- linear regression baseline
- DLinear-style decomposition baseline
- patch-based neural model notes

## Experiment Contract

Every run should answer:

1. What is the exact prediction horizon?
2. How was normalization fitted?
3. Is the validation window temporally after training?
4. Which seed changed the conclusion?
5. What failure mode did the model reveal?

## Current Status

Small, auditable code first. Neural models come after the baseline harness is hard to fool.
