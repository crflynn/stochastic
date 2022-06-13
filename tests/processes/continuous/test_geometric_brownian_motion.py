"""Test GeometricBrownianMotion."""

from stochastic.processes.continuous import GeometricBrownianMotion


def test_geometric_brownian_motion_str_repr(drift, volatility, t):
    instance = GeometricBrownianMotion(drift, volatility, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_geometric_brownian_motion_sample(drift, volatility, t, n, initial, threshold):
    instance = GeometricBrownianMotion(drift, volatility, t)
    s = instance.sample(n, initial)
    assert len(s) == n + 1


def test_geometric_brownian_motion_sample_at(
    drift, volatility, t, times, initial, threshold
):
    instance = GeometricBrownianMotion(drift, volatility, t)
    s = instance.sample_at(times, initial)
    assert len(s) == len(times)
