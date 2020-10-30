"""Test BrownianMotion."""

from stochastic.processes.continuous import BrownianMotion


def test_brownian_motion_str_repr(drift, scale, t):
    instance = BrownianMotion(drift, scale, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_brownian_motion_sample(drift, scale, t, n, threshold):
    instance = BrownianMotion(drift, scale, t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_brownian_motion_sample_at(drift, scale, t, times, threshold):
    instance = BrownianMotion(drift, scale, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
