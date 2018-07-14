"""Test PoissonProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import NHPP

def test_poisson_process_str_repr(lambdaa,boundaries):
    instance = NHPP(lambdaa,boundaries)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_poisson_process_sample(lambdaa,boundaries, n_fixture):
    instance = NHPP(lambdaa,boundaries)
    if n_fixture is None:
        with pytest.raises(ValueError):
            s = instance.sample(n_fixture)
    else:  # n_fixture is not None:
        s = instance.sample(n_fixture)
        assert len(s) == n_fixture 

# def test_poisson_process_times(rate, n):
    # instance = PoissonProcess(rate)
    # with pytest.raises(AttributeError):
        # times = instance.times(n)