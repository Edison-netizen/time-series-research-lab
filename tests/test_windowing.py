import numpy as np

from tslab.windowing import WindowSpec, rolling_windows


def test_rolling_windows_keeps_chronological_targets():
    values = np.arange(10)
    windows = list(rolling_windows(values, WindowSpec(lookback=4, horizon=2, stride=2)))

    assert len(windows) == 3
    first_x, first_y = windows[0]
    assert first_x.ravel().tolist() == [0, 1, 2, 3]
    assert first_y.ravel().tolist() == [4, 5]

