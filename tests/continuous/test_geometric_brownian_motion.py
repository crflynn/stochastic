"""Test GeometricBrownianMotion."""
import pytest

from stochastic.continuous import GeometricBrownianMotion


def test_geometric_brownian_motion_str_repr(drift, volatility, t):
    instance = GeometricBrownianMotion(drift, volatility, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_geometric_brownian_motion_sample(drift, volatility, t, n, zero, initial, threshold):
    instance = GeometricBrownianMotion(drift, volatility, t)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)


def test_geometric_brownian_motion_sample_at(drift, volatility, t, times, initial, threshold):
    instance = GeometricBrownianMotion(drift, volatility, t)
    s = instance.sample_at(times, initial)
    assert len(s) == len(times)
