"""Test VarianceGammaProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import VarianceGammaProcess


def test_variance_gamma_init(t, drift, variance, scale):
    instance = VarianceGammaProcess(t, drift, variance, scale)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_variance_gamma_str_repr(t, drift, variance, scale):
    instance = VarianceGammaProcess(t, drift, variance, scale)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_variance_gamma_sample(t, drift, variance, scale, n, zero, threshold):
    instance = VarianceGammaProcess(t, drift, variance, scale)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)

def test_variance_gamma_sample_at(t, drift, variance, scale, times, threshold):
    instance = VarianceGammaProcess(t, drift, variance, scale)
    s = instance.sample_at(times)
    assert len(s) == len(times)
