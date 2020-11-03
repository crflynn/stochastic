"""Test FractionalBrownianMotion."""

from stochastic.processes.continuous import FractionalBrownianMotion


def test_fractional_brownian_motion_str_repr(hurst, t):
    instance = FractionalBrownianMotion(hurst, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_fractional_brownian_motion_sample(hurst, t, n, threshold):
    instance = FractionalBrownianMotion(hurst, t)
    s = instance.sample(n)
    assert len(s) == n + 1
