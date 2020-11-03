"""Bernoulli tests."""
import pytest

from stochastic.processes.discrete import BernoulliProcess


def test_bernoulli_str_repr(p):
    instance = BernoulliProcess(p)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_bernoulli_sample(p, n):
    instance = BernoulliProcess(p)
    s = instance.sample(n)
    assert len(s) == n
    for trial in s:
        assert trial in [0, 1]


def test_bernoulli_probability(p_fixture):
    if not isinstance(p_fixture, (int, float)):
        with pytest.raises(TypeError):
            instance = BernoulliProcess(p_fixture)
    elif p_fixture > 1 or p_fixture < 0:
        with pytest.raises(ValueError):
            instance = BernoulliProcess(p_fixture)
    else:
        instance = BernoulliProcess(p_fixture)
        assert True
