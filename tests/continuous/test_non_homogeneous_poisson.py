"""Test NonHomogeneousPoissonProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import NonHomogeneousPoissonProcess

def test_non_homogeneous_poisson_process_str_repr(rate_func):
    instance = NonHomogeneousPoissonProcess(rate_func)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_non_homogeneous_poisson_process_sample(rate_func, n_fixture, length, zero, algo):
    instance = NonHomogeneousPoissonProcess(rate_func)
    if n_fixture is None and length is None:
        with pytest.raises(ValueError):
            s = instance.sample(n_fixture, length, zero, algo)
    elif length is not None and n_fixture is None:
        s = instance.sample(n_fixture, length, zero, algo)
        assert s[-1] >= length
    else:  # n_fixture is not None:
        s = instance.sample(n_fixture, length, zero, algo)
        assert len(s) == n_fixture + int(zero)

def test_non_homogeneous_poisson_process_times(rate_func, n):
    instance = NonHomogeneousPoissonProcess(rate_func)
    with pytest.raises(AttributeError):
        times = instance.times(n)

