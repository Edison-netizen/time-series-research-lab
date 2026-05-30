import unittest
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from tslab.windowing import WindowSpec, rolling_windows


class RollingWindowTests(unittest.TestCase):
    def test_rolling_windows_keeps_chronological_targets(self):
        values = list(range(10))
        windows = list(rolling_windows(values, WindowSpec(lookback=4, horizon=2, stride=2)))

        self.assertEqual(len(windows), 3)
        first_x, first_y = windows[0]
        self.assertEqual(first_x, [0, 1, 2, 3])
        self.assertEqual(first_y, [4, 5])


if __name__ == "__main__":
    unittest.main()
