"""Test WienerProcess."""
import pytest

from stochastic.continuous import WienerProcess


def test_wiener_str_repr(t):
    instance = WienerProcess(t)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)
