"""Test PoissonProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import MixedPoissonProcess

def test_mixed_poisson_process_str_repr(ratedist,ratedistparams):
    instance = MixedPoissonProcess(ratedist,ratedistparams)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_mixed_poisson_process_sample(ratedist,ratedistparams, n_fixture, length, zero):
    instance = MixedPoissonProcess(ratedist,ratedistparams)
    if n_fixture is None and length is None:
        with pytest.raises(ValueError):
            s = instance.sample(n_fixture, length, zero)
    elif length is not None and n_fixture is None:
        s = instance.sample(n_fixture, length, zero)
        assert s[-1] >= length
    else:  # n_fixture is not None:
        s = instance.sample(n_fixture, length, zero)
        assert len(s) == n_fixture + int(zero)

def test_poisson_process_times(ratedist,ratedistparams, n):
    instance = MixedPoissonProcess(ratedist,ratedistparams,)
    with pytest.raises(AttributeError):
        times = instance.times(n)