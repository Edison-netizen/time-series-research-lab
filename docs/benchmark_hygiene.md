# Benchmark Hygiene

Time-series evaluation fails quietly. This checklist keeps experiments honest.

## Split

- Use chronological splits.
- Fit normalization on train only.
- Never shuffle before window construction.
- Keep validation and test windows strictly after train windows.

## Metrics

- Report MAE and MSE together.
- Add sMAPE only when values are non-degenerate.
- Inspect error by horizon, not only aggregate error.

## Reporting

- Record seed, lookback, horizon, batch size, and normalization.
- Save config with every result.
- Write down at least one failure case per experiment.

