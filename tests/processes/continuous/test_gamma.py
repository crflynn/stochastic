"""Test GammaProcess."""
import pytest

from stochastic.processes.continuous import GammaProcess


def test_gamma_process_init(
    mean_fixture, variance_fixture, rate_fixture, scale_fixture, t
):
    first_params = bool(mean_fixture) + bool(variance_fixture)
    second_params = bool(rate_fixture) + bool(scale_fixture)
    all_params = first_params + second_params
    if all_params != 2 or (first_params != 2 and second_params != 2):
        with pytest.raises((TypeError, ValueError)):
            _ = GammaProcess(
                mean_fixture, variance_fixture, rate_fixture, scale_fixture, t
            )
    else:
        instance = GammaProcess(
            mean_fixture, variance_fixture, rate_fixture, scale_fixture, t
        )
        assert isinstance(repr(instance), str)
        assert isinstance(str(instance), str)


def test_gamma_process_str_repr(mean, variance, t):
    instance = GammaProcess(mean, variance, t=t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_gamma_process_sample(mean, variance, t, n, threshold):
    instance = GammaProcess(mean, variance, t=t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_gamma_process_sample_at(mean, variance, t, times, threshold):
    instance = GammaProcess(mean, variance, t=t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
