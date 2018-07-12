"""Cox-Ingersoll-Ross tests."""
# flake8: noqa
import pytest

from stochastic.diffusion import CoxIngersollRossProcess


def test_cox_ingersoll_ross_str_repr(t, speed, mean, vol):
    instance = CoxIngersollRossProcess(t, speed, mean, vol)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_cox_ingersoll_ross_sample(t, speed, mean, vol, n, initial, zero, threshold):
    instance = CoxIngersollRossProcess(t, speed, mean, vol)
    s = instance.sample(n, initial, zero)
    assert len(s) == n + int(zero)
