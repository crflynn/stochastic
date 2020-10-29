"""Pytest fixtures."""
import pytest


@pytest.fixture(params=[16])
def n(request):
    return request.param


@pytest.fixture(params=[1])
def end(request):
    return request.param
