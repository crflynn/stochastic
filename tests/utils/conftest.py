"""Pytest fixtures."""
import pytest


@pytest.fixture(params=[4, 4.2, "4", -4])
def increments_fixture(request):
    return request.param


@pytest.fixture(params=[4, 4.2, "4"])
def number_fixture(request):
    return request.param


@pytest.fixture(params=[4, 0, -4])
def positive_number_fixture(request):
    return request.param


@pytest.fixture(params=["PARAMETER_NAME"])
def parameter_name_fixture(request):
    return request.param


@pytest.fixture(params=[4, 0, -4])
def nonnegative_number_fixture(request):
    return request.param


@pytest.fixture(params=[16])
def n(request):
    return request.param


@pytest.fixture(params=[1])
def end(request):
    return request.param
