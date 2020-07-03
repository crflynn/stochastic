"""Test VarianceGammaProcess."""
import pytest

from stochastic.continuous import VarianceGammaProcess


def test_variance_gamma_init(drift, variance, scale, t):
    instance = VarianceGammaProcess(drift, variance, scale, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_variance_gamma_str_repr(drift, variance, scale, t):
    instance = VarianceGammaProcess(drift, variance, scale, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_variance_gamma_sample(drift, variance, scale, t, n, zero, threshold):
    instance = VarianceGammaProcess(drift, variance, scale, t)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)


def test_variance_gamma_sample_at(drift, variance, scale, t, times, threshold):
    instance = VarianceGammaProcess(drift, variance, scale, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
