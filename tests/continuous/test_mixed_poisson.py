"""Test MixedPoissonProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import MixedPoissonProcess


def test_mixed_poisson_process_str_repr(rate_dist, rate_args, rate_kwargs):
    instance = MixedPoissonProcess(rate_dist, rate_args, rate_kwargs)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_mixed_poisson_process_sample(rate_dist, rate_args, rate_kwargs,
    n_fixture, length, zero):
    instance = MixedPoissonProcess(rate_dist, rate_args, rate_kwargs)
    instance.rate = rate_dist, rate_args, rate_kwargs
    assert instance.rate_dist == rate_dist
    assert instance.rate_args == rate_args
    assert instance.rate_kwargs == rate_kwargs
    if n_fixture is None and length is None:
        with pytest.raises(ValueError):
            s = instance.sample(n_fixture, length, zero)
    elif length is not None and n_fixture is None:
        s = instance.sample(n_fixture, length, zero)
        assert s[-1] >= length
    else:  # n_fixture is not None:
        s = instance.sample(n_fixture, length, zero)
        assert len(s) == n_fixture + int(zero)

def test_poisson_process_times(rate_dist, rate_args, rate_kwargs, n):
    instance = MixedPoissonProcess(rate_dist, rate_args, rate_kwargs)
    with pytest.raises(AttributeError):
        times = instance.times(n)
