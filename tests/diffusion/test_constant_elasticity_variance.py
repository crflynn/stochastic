"""Constant elasticity of variance tests."""
import pytest

from stochastic.diffusion import ConstantElasticityVarianceProcess


def test_constant_elasticity_variance_str_repr(mu, sigma, gamma, t):
    instance = ConstantElasticityVarianceProcess(mu, sigma, gamma, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_constant_elasticity_variance_sample(mu, sigma, gamma, t, n, initial, zero, threshold):
    instance = ConstantElasticityVarianceProcess(mu, sigma, gamma, t)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)
