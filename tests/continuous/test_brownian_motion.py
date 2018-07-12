"""Test BrownianMotion."""
# flake8: noqa
import pytest

from stochastic.continuous import BrownianMotion


def test_brownian_motion_str_repr(t, drift, scale):
    instance = BrownianMotion(t, drift, scale)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_brownian_motion_sample(t, drift, scale, n, zero, threshold):
    instance = BrownianMotion(t, drift, scale)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)

def test_brownian_motion_sample_at(t, drift, scale, times, threshold):
    instance = BrownianMotion(t, drift, scale)
    s = instance.sample_at(times)
    assert len(s) == len(times)
