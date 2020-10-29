"""Test BesselProcess."""
import pytest

from stochastic.processes.continuous import BesselProcess


def test_bessel_str_repr(dim, t):
    instance = BesselProcess(dim, t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_bessel_init(dim_fixture, t):
    if not isinstance(dim_fixture, int):
        with pytest.raises(TypeError):
            _ = BesselProcess(dim_fixture, t)
    elif dim_fixture < 1:
        with pytest.raises(ValueError):
            _ = BesselProcess(dim_fixture, t)
    else:
        _ = BesselProcess(dim_fixture, t)


def test_bessel_sample(dim, t, n):
    instance = BesselProcess(dim, t)
    s = instance.sample(n)
    assert len(s) == n + 1


def test_bessel_sample_at(dim, t, times):
    instance = BesselProcess(dim, t)
    s = instance.sample_at(times)
    assert len(s) == len(times)
