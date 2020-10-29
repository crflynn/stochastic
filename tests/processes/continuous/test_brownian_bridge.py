"""Test BrownianBridge."""
import pytest

from stochastic.processes.continuous import BrownianBridge


def test_brownian_bridge_str_repr(b, t):
    if b is not None:
        instance = BrownianBridge(b, t)
    else:
        instance = BrownianBridge(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_brownian_bridge_sample(b, t, n, threshold):
    if b is not None:
        instance = BrownianBridge(b, t)
    else:
        instance = BrownianBridge(t)
    s = instance.sample(n)
    assert len(s) == n + 1
    assert s[-1] == pytest.approx(instance.b, threshold)


def test_brownian_bridge_sample_at(b, t, times, threshold):
    if b is not None:
        instance = BrownianBridge(b, t)
    else:
        instance = BrownianBridge(t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
    assert s[-1] == pytest.approx(instance.b, threshold)
