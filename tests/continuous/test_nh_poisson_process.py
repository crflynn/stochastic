"""Test NHPP."""
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

<<<<<<< HEAD
def test_poisson_process_times(lambdaa,boundaries, n):
    instance = NHPP(lambdaa,boundaries)
    with pytest.raises(AttributeError):
        times = instance.times(n)
=======
# def test_poisson_process_times(rate, n):
    # instance = PoissonProcess(rate)
    # with pytest.raises(AttributeError):
        # times = instance.times(n)
>>>>>>> a444d7f5574c6e8df2bd3dc70ef09d557b6b1141
