"""Cox-Ingersoll-Ross tests."""
from stochastic.processes.diffusion import CoxIngersollRossProcess


def test_cox_ingersoll_ross_str_repr(speed, mean, vol, t):
    instance = CoxIngersollRossProcess(speed, mean, vol, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_cox_ingersoll_ross_sample(speed, mean, vol, t, n, initial, threshold):
    instance = CoxIngersollRossProcess(speed, mean, vol, t)
    s = instance.sample(n, initial)
    assert len(s) == n + 1
