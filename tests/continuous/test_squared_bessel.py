"""Test SquaredBesselProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import SquaredBesselProcess


def test_squared_bessel_str_repr(t, dim):
    instance = SquaredBesselProcess(t, dim)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_squared_bessel_init(t, dim_fixture):
    if not isinstance(dim_fixture, int):
        with pytest.raises(TypeError):
            instance = SquaredBesselProcess(t, dim_fixture)
    elif dim_fixture < 1:
        with pytest.raises(ValueError):
            instance = SquaredBesselProcess(t, dim_fixture)
    else:
        instance = SquaredBesselProcess(t, dim_fixture)

def test_squared_bessel_sample(t, dim, n, zero):
    instance = SquaredBesselProcess(t, dim)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)

def test_squared_bessel_sample_at(t, dim, times):
    instance = SquaredBesselProcess(t, dim)
    s = instance.sample_at(times)
    assert len(s) == len(times)
