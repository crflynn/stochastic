"""Test BrownianMeander."""
import pytest

from stochastic.processes.continuous import BrownianMeander


def test_brownian_meander_str_repr(t):
    instance = BrownianMeander(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_brownian_meander_sample(t, n, b, threshold):
    instance = BrownianMeander(t)
    s = instance.sample(n, b)
    assert len(s) == n + 1
    assert (s >= 0).all()
    assert s[0] == pytest.approx(0, threshold)


def test_brownian_meander_sample_at(t, times, b, threshold):
    instance = BrownianMeander(t)
    s = instance.sample_at(times, b)
    assert len(s) == len(times)
    assert (s >= 0).all()
    if times[0] == 0:
        assert s[0] == pytest.approx(0, threshold)
