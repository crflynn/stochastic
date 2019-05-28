"""Random walk tests."""
import pytest

from stochastic.discrete import RandomWalk


def test_random_walk_str_repr(steps, weights):
    instance = RandomWalk(steps, weights)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_random_walk_sample(steps, weights, n, zero):
    instance = RandomWalk(steps, weights)
    s = instance.sample(n, zero)
    assert len(s) == n + int(zero)


def test_random_walk_sample_increments(steps, weights, n):
    instance = RandomWalk(steps, weights)
    s = instance.sample_increments(n)
    assert len(s) == n


def test_random_walk_bad_steps(steps_fixture, weights):
    with pytest.raises((ValueError, TypeError)):
        instance = RandomWalk(steps_fixture, weights)


def test_random_walk_bad_weights(steps, weights_fixture):
    with pytest.raises((ValueError, TypeError)):
        instance = RandomWalk(steps, weights_fixture)
