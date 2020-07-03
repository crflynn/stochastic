"""Pytest fixtures."""
import pytest


# Checks class fixtures
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


@pytest.fixture(params=[True, False, 0])
def zero_fixture(request):
    return request.param


has_negative = [-5, -4, 0, 4, 5]
bad_order = [0, 3, 2, 5]
good_example = list(range(10))


@pytest.fixture(params=[has_negative, bad_order, good_example])
def times_fixture(request):
    return request.param


# Continuous class fixtures
@pytest.fixture(params=[True, False])
def zero(request):
    return request.param


@pytest.fixture(params=[16])
def n(request):
    return request.param


@pytest.fixture(params=[1])
def end(request):
    return request.param
