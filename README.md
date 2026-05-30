# Time Series Research Lab

Research-grade scaffold for deep learning experiments on time series.

This repository is a public lab notebook for forecasting baselines, ablation protocol, and reproducible experiment structure. The focus is not chasing leaderboard numbers first. The focus is making each experiment inspectable: data split, normalization, lookback/horizon, seed, metric, and failure mode.

## Scope

- Long-horizon forecasting baselines
- Multivariate time series preprocessing
- Rolling-window evaluation
- Seed variance and ablation tracking
- Clean experiment configs for repeatable runs

## Repository Shape

```text
configs/          experiment configs
src/tslab/        small reusable utilities
docs/             protocol notes and benchmark hygiene
```

## Baseline Queue

| Family | Models |
|---|---|
| Linear | DLinear, NLinear |
| Patch-based | PatchTST |
| Inception-style | TimesNet |
| Transformer variants | iTransformer, Informer-style baselines |

## Experiment Contract

Every run should answer:

1. What is the exact prediction horizon?
2. How was normalization fitted?
3. Is the validation window temporally after training?
4. Which seed changed the conclusion?
5. What failure mode did the model reveal?

## Current Status

The repo starts as a scaffold. Code will be added in small, auditable slices.

