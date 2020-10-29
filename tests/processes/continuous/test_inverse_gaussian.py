"""Test GeometricBrownianMotion."""
import pytest

from stochastic.processes.continuous import InverseGaussianProcess


def test_inverse_gaussian_process_str_repr(mean_func, scale, t):
    instance = InverseGaussianProcess(mean_func, scale, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_inverse_gaussian_process_sample(mean_func, scale, t, n):
    instance = InverseGaussianProcess(mean_func, scale, t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_inverse_gaussian_process_sample_invalid(mean_func_invalid, scale, t, n):
    with pytest.raises(ValueError):
        instance = InverseGaussianProcess(mean_func_invalid, scale, t)
        _ = instance.sample(n)


def test_inverse_gaussian_process_sample_at(mean_func, scale, t, times):
    instance = InverseGaussianProcess(mean_func, scale, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
