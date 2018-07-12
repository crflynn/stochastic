"""Test GeometricBrownianMotion."""
# flake8: noqa
import pytest

from stochastic.continuous import GeometricBrownianMotion


def test_geometric_brownian_motion_str_repr(t, drift, volatility):
    instance = GeometricBrownianMotion(t, drift, volatility)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_geometric_brownian_motion_sample(t, drift, volatility, n, zero, initial, threshold):
    instance = GeometricBrownianMotion(t, drift, volatility)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)

def test_geometric_brownian_motion_sample_at(t, drift, volatility, times, initial, threshold):
    instance = GeometricBrownianMotion(t, drift, volatility)
    s = instance.sample_at(times, initial)
    assert len(s) == len(times)
