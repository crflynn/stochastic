"""Test BrownianMeander."""
import pytest

from stochastic.continuous import BrownianMeander


def test_brownian_meander_str_repr(t):
    instance = BrownianMeander(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_brownian_meander_sample(t, n, b, zero, threshold):
    instance = BrownianMeander(t)
    s = instance.sample(n, b, zero)
    assert len(s) == n + int(zero)
    assert (s >= 0).all()
    if zero:
        assert s[0] == pytest.approx(0, threshold)


def test_brownian_meander_sample_at(t, times, b, threshold):
    instance = BrownianMeander(t)
    s = instance.sample_at(times, b)
    assert len(s) == len(times)
    assert (s >= 0).all()
    if times[0] == 0:
        assert s[0] == pytest.approx(0, threshold)
