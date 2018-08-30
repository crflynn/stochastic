"""Test NonHomogeneousPoissonProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import NonHomogeneousPoissonProcess

def test_non_homogeneous_poisson_process_str_repr(rate_func, rate_args, rate_kwargs):
    if not isinstance(rate_args, (list, tuple)):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    elif not isinstance(rate_kwargs, dict):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    elif not callable(rate_func):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    else: 
        instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
        assert isinstance(repr(instance), str)
        assert isinstance(str(instance), str)

def test_non_homogeneous_poisson_process_sample(rate_func, rate_args, rate_kwargs, n_fixture, length, zero, algo):
    if not isinstance(rate_args, (list, tuple)):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    elif not isinstance(rate_kwargs, dict):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    elif not callable(rate_func):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    else: 
        instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
        if n_fixture is None and length is None and (algo is not 'thinning' or algo is not 'inversion'):
            with pytest.raises(ValueError):
                s = instance.sample(n_fixture, length, zero, algo)
        elif length is not None and n_fixture is None and (algo is 'thinning' or algo is 'inversion'):
            s = instance.sample(n_fixture, length, zero, algo)
            assert s[-1] >= length
        elif length is None and n_fixture is not None and (algo is 'thinning' or algo is 'inversion'):
            s = instance.sample(n_fixture, length, zero, algo)
            assert len(s) == n_fixture + int(zero)

def test_non_homogeneous_poisson_process_times(rate_func, rate_args, rate_kwargs, n):
    if not isinstance(rate_args, (list, tuple)):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    elif not isinstance(rate_kwargs, dict):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    elif not callable(rate_func):
        with pytest.raises(ValueError):
            instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
    else: 
        instance = NonHomogeneousPoissonProcess(rate_func, rate_args, rate_kwargs)
        with pytest.raises(AttributeError):
            times = instance.times(n)

