"""Test BrownianBridge."""
# flake8: noqa
import pytest

from stochastic.continuous import BrownianBridge


def test_brownian_bridge_str_repr(t, b):
    if b is not None:
        instance = BrownianBridge(t, b)
    else:
        instance = BrownianBridge(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_brownian_bridge_sample(t, b, n, zero, threshold):
    if b is not None:
        instance = BrownianBridge(t, b)
    else:
        instance = BrownianBridge(t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)
    assert s[-1] == pytest.approx(instance.b, threshold)

def test_brownian_bridge_sample_at(t, b, times, threshold):
    if b is not None:
        instance = BrownianBridge(t, b)
    else:
        instance = BrownianBridge(t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
    assert s[-1] == pytest.approx(instance.b, threshold)
