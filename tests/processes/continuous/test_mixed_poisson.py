"""Test MixedPoissonProcess."""
import pytest

from stochastic.processes.continuous import MixedPoissonProcess


def test_mixed_poisson_process_str_repr(rate_func, rate_args, rate_kwargs):
    instance = MixedPoissonProcess(rate_func, rate_args, rate_kwargs)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_mixed_poisson_process_sample(
    rate_func, rate_args, rate_kwargs, n_fixture, length
):
    instance = MixedPoissonProcess(rate_func, rate_args, rate_kwargs)
    if n_fixture is None and length is None:
        with pytest.raises(ValueError):
            s = instance.sample(n_fixture, length)
    elif length is not None and n_fixture is None:
        s = instance.sample(n_fixture, length)
        assert s[-1] >= length
    else:  # n_fixture is not None:
        s = instance.sample(n_fixture, length)
        assert len(s) == n_fixture + 1


def test_mixed_poisson_process_times(rate_func, rate_args, rate_kwargs, n):
    instance = MixedPoissonProcess(rate_func, rate_args, rate_kwargs)
    with pytest.raises(AttributeError):
        _ = instance.times(n)


def test_mixed_poisson_process_invalid_func(
    rate_func_invalid, rate_args, rate_kwargs, n
):
    with pytest.raises(ValueError):
        _ = MixedPoissonProcess(rate_func_invalid, rate_args, rate_kwargs)


def test_mixed_poisson_process_invalid_args(
    rate_func, rate_args_invalid, rate_kwargs, n
):
    with pytest.raises(ValueError):
        _ = MixedPoissonProcess(rate_func, rate_args_invalid, rate_kwargs)


def test_mixed_poisson_process_invalid_kwargs(
    rate_func, rate_args, rate_kwargs_invalid, n
):
    with pytest.raises(ValueError):
        _ = MixedPoissonProcess(rate_func, rate_args, rate_kwargs_invalid)
