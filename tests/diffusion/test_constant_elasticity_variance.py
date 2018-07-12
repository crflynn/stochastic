"""Constant elasticity of variance tests."""
# flake8: noqa
import pytest

from stochastic.diffusion import ConstantElasticityVarianceProcess


def test_constant_elasticity_variance_str_repr(t, mu, sigma, gamma):
    instance = ConstantElasticityVarianceProcess(t, mu, sigma, gamma)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_constant_elasticity_variance_sample(t, mu, sigma, gamma, n, initial, zero, threshold):
    instance = ConstantElasticityVarianceProcess(t, mu, sigma, gamma)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)
