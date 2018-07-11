"""Test MultifractionalBrownianMotion."""
# flake8: noqa
import pytest

from stochastic.continuous import MultifractionalBrownianMotion


def test_multifractional_brownian_motion_str_repr(t, hurst_func):
    instance = MultifractionalBrownianMotion(t, hurst_func)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_multifractional_brownian_motion_sample(t, hurst_func, n, zero):
    instance = MultifractionalBrownianMotion(t, hurst_func)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)

def test_multifractional_brownian_motion_invalid_hurst(t, hurst_invalid):
    with pytest.raises(ValueError):
        instance = MultifractionalBrownianMotion(t, hurst_invalid)
        s = instance.sample(16)
