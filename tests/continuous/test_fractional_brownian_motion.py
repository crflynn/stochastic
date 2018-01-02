"""Test FractionalBrownianMotion."""
# flake8: noqa
import pytest

from stochastic.continuous import FractionalBrownianMotion


def test_fractional_brownian_motion_str_repr(t, hurst):
    instance = FractionalBrownianMotion(t, hurst)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_fractional_brownian_motion_sample(t, hurst, n, zero, threshold):
    instance = FractionalBrownianMotion(t, hurst)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)
