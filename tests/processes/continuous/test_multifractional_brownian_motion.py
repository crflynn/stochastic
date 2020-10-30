"""Test MultifractionalBrownianMotion."""
import pytest

from stochastic.processes.continuous import MultifractionalBrownianMotion


def test_multifractional_brownian_motion_str_repr(hurst_func, t):
    instance = MultifractionalBrownianMotion(hurst_func, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_multifractional_brownian_motion_sample(hurst_func, t, n):
    instance = MultifractionalBrownianMotion(hurst_func, t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_multifractional_brownian_motion_invalid_hurst(hurst_invalid, t):
    with pytest.raises(ValueError):
        instance = MultifractionalBrownianMotion(hurst_invalid, t)
        s = instance.sample(16)
