# Synthetic Seasonal Baseline

Generated with:

```bash
python scripts/run_synthetic_baseline.py
```

Configuration:

- length: 240
- season length: 24
- lookback: 72
- horizon: 24
- stride: 24
- noise: 0.03
- seed: 7

Result:

```text
model           MAE       MSE       sMAPE
seasonal_naive  0.2397    0.0580    0.3270
moving_average  0.5982    0.4825    0.4872
```

Interpretation:

The seasonal naive baseline wins on this smoke dataset because the generator contains a strong 24-step periodic component. This is intentional: before testing neural models, the harness should make obvious seasonal structure easy to recover.

