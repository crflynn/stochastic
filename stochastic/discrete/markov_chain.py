"""Markov chain."""
import numpy as np

from stochastic.base import Checks


class MarkovChain(Checks):
    """Finite state Markov chain.

    .. image:: _static/markov_chain.png
        :scale: 50%

    A Markov Chain which changes between states according to the transition
    matrix.

    :param transition: a square matrix representing the transition
        probabilities between states.
    :param initial: a vector representing the initial state probabilities. If
        not provided, each state has equal initial probability.
    """

    def __init__(self, transition=[[0.5, 0.5], [0.5, 0.5]], initial=None):
        self.transition = transition
        if initial is None:
            self.initial = [1.0 / len(self.transition) for t in self.transition]
        else:
            self.initial = initial
        self.num_states = len(self.initial)

    def __str__(self):
        return "Markov chain with transition matrix = \n{t} ".format(
            t=str(self.transition)
        ) + "and initial state probabilities = {p}".format(p=str(self.initial))

    def __repr__(self):
        return "MarkovChain(transition={t}, initial={i})".format(t=str(self.transition), i=str(self.initial))

    @property
    def transition(self):
        """Transition probability matrix."""
        return self._transition

    @transition.setter
    def transition(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 2 or values.shape[0] != values.shape[1]:
            raise ValueError("Transition matrix must be a square matrix.")
        for row in values:
            if sum(row) != 1:
                raise ValueError("Transition matrix is not a proper stochastic matrix.")
        self._transition = values

    @property
    def initial(self):
        """Vector of initial state probabilities."""
        return self._initial

    @initial.setter
    def initial(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 1 or len(values) != len(self.transition):
            raise ValueError("Initial state probabilities must be one-to-one with states.")
        if sum(values) != 1:
            raise ValueError("Initial state probabilities must sum to 1.")
        self._initial = values

    def sample(self, n):
        """Generate a realization of the Markov chain.

        :param int n: the number of steps of the Markov chain to generate.
        """
        self._check_increments(n)

        states = range(self.num_states)

        markov_chain = [np.random.choice(states, p=self.initial)]
        for _ in range(n - 1):
            markov_chain.append(np.random.choice(states, p=self.transition[markov_chain[-1]]))

        return np.array(markov_chain)
