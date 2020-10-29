"""Markov chain tests."""
import pytest

from stochastic.processes.discrete import MarkovChain


def test_markov_chain_str_repr(transition, initial):
    instance = MarkovChain(transition, initial)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_markov_chain_sample(transition, initial, n):
    instance = MarkovChain(transition, initial)
    s = instance.sample(n)
    assert len(s) == n
    states = list(range(len(instance.initial)))
    for state in s:
        assert state in states


@pytest.mark.parametrize(
    "transition,initial",
    [
        ([[0.5, 0.5], [0.5]], None),  # non-square transition
        ([[0.5, 0.25], [0.5, 0.5]], None),  # non-stochastic transition
        ([[0.5, 0.5], [0.5, 0.5]], [0.5]),  # invalid initial
        ([[0.5, 0.5], [0.5, 0.5]], [0.5, 0.25]),  # non-stochastic initial
    ],
)
def test_markov_chain_probability(transition, initial):
    with pytest.raises(ValueError):
        instance = MarkovChain(transition, initial)
