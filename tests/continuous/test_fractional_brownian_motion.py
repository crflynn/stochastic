"""Test FractionalBrownianMotion."""
import pytest

from stochastic.continuous import FractionalBrownianMotion


def test_fractional_brownian_motion_str_repr(hurst, t):
    instance = FractionalBrownianMotion(hurst, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_fractional_brownian_motion_sample(hurst, t, n, zero, threshold):
    instance = FractionalBrownianMotion(hurst, t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)
