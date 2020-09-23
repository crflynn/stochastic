"""Constant elasticity of variance tests."""
from stochastic.diffusion import ConstantElasticityVarianceProcess


def test_constant_elasticity_variance_str_repr(mu, sigma, gamma, t):
    instance = ConstantElasticityVarianceProcess(mu, sigma, gamma, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_constant_elasticity_variance_sample(mu, sigma, gamma, t, n, initial, threshold):
    instance = ConstantElasticityVarianceProcess(mu, sigma, gamma, t)
    s = instance.sample(n, initial)
    assert len(s) == n + 1
