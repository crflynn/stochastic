"""Test BrownianExcursion."""
import pytest

from stochastic.continuous import BrownianExcursion


def test_brownian_excursion_str_repr(t):
    instance = BrownianExcursion(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_brownian_excursion_sample(t, n, zero, threshold):
    instance = BrownianExcursion(t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)
    assert (s >= 0).all()
    if zero:
        assert s[0] == pytest.approx(0, threshold)
    assert s[-1] == pytest.approx(0, threshold)


def test_brownian_excursion_sample_at(t, times, threshold):
    instance = BrownianExcursion(t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
    assert (s >= 0).all()
    if times[0] == 0:
        assert s[0] == pytest.approx(0, threshold)
    assert s[-1] == pytest.approx(0, threshold)
