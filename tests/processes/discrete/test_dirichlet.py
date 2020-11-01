"""Dirichlet process tests."""
import pytest

from stochastic import random
from stochastic.processes.discrete import DirichletProcess


def test_dirichlet_process_str_repr(base, alpha):
    if (not callable(base) and base is not None) or alpha <= 0:
        with pytest.raises(ValueError):
            _ = DirichletProcess(base, alpha)
        return
    instance = DirichletProcess(base, alpha)
    if base is None:
        assert instance.base == random.generator.uniform
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_dirichlet_process_sample(base, alpha, n):
    if (not callable(base) and base is not None) or alpha <= 0:
        with pytest.raises(ValueError):
            _ = DirichletProcess(base, alpha)
        return
    instance = DirichletProcess(base, alpha)
    s = instance.sample(n)
    assert len(s) == n
