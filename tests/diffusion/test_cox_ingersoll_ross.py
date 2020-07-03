"""Cox-Ingersoll-Ross tests."""
import pytest

from stochastic.diffusion import CoxIngersollRossProcess


def test_cox_ingersoll_ross_str_repr(speed, mean, vol, t):
    instance = CoxIngersollRossProcess(speed, mean, vol, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_cox_ingersoll_ross_sample(speed, mean, vol, t, n, initial, zero, threshold):
    instance = CoxIngersollRossProcess(speed, mean, vol, t)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)
