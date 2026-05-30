import unittest
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from tslab.baselines import moving_average, seasonal_naive
from tslab.metrics import mae, mse, smape


class BaselineTests(unittest.TestCase):
    def test_seasonal_naive_repeats_last_season(self):
        pred = seasonal_naive([1, 2, 3, 10, 20, 30], horizon=5, season_length=3)
        self.assertEqual(pred, [10, 20, 30, 10, 20])

    def test_moving_average_repeats_recent_mean(self):
        pred = moving_average([1, 2, 3, 4], horizon=3, window=2)
        self.assertEqual(pred, [3.5, 3.5, 3.5])

    def test_metrics_are_basic_and_explicit(self):
        actual = [1, 2, 3]
        predicted = [1, 1, 5]
        self.assertAlmostEqual(mae(actual, predicted), 1.0)
        self.assertAlmostEqual(mse(actual, predicted), 5 / 3)
        self.assertGreater(smape(actual, predicted), 0)


if __name__ == "__main__":
    unittest.main()
