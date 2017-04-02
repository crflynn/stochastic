import numpy as np


class MarkovChain(object):
    """
    A Markov Chain which changes between states according to the transition
    matrix.

    args:
        transition (square array-like) = an n-by-n array representing a
            right-stochastic matrix where each row sums to 1, n representing
            the number of states
        initial (list length n) = a list of probabilities corresponding to
            the n states of the Markov Chain. Default is 1/n for each state.
        states (list length n) = a map of aliases for the states of the
            Markov Chain, if desired
    """

    def __init__(self, transition=[[0.5, 0.5], [0.5, 0.5]],
                 initial=None,
                 states=None):
        self.transition = transition
        if initial is None:
            self.initial = [1.0 / len(self.transition)
                            for t in self.transition]
        else:
            self.initial = initial
        if states is None:
            self.states = range(len(self.transition))
        else:
            self.states = states
        self.num_states = len(self.states)

    @property
    def transition(self):
        return self._transition

    @transition.setter
    def transition(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 2 or values.shape[0] != values.shape[1]:
            raise ValueError('Transition matrix must be a square matrix.')
        for row in values:
            if sum(row) != 1:
                raise ValueError(
                    'Transition matrix is not a proper stochastic matrix.')
        self._transition = values

    @property
    def initial(self):
        return self._initial

    @initial.setter
    def initial(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 1 or len(values) != len(self.transition):
            raise ValueError(
                'Initial state probabilities must be one-to-one with states.')
        if sum(values) != 1:
            raise ValueError('Initial state probabilities must sum to 1.')
        self._initial = values

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 1 or len(values) != len(self.transition):
            raise ValueError(
                'Number of states aliases must match quantity of states ' +
                'given by transition matrix.')
        if  len(set(values)) != len(values):
            raise ValueError('State aliases must be distinct.')
        self._states = values

    def __str__(self):
        return 'Markov chain with states = {s}'.format(s=str(self.states)) + \
            'and transition matrix = \n{t}'.format(t=str(self.transition)) + \
            'and initial state probabilities = {p}'.format(p=str(self.initial))

    def __repr__(self):
        return self.__str__()

    def sample(self, n):
        """
        Generate a Markov chain sample of length n

        args:
            n (int) = the number of steps in the markov chain
        """
        if not isinstance(n, int):
            raise TypeError('Sample length must be positive integer.')
        if n < 1:
            raise ValueError('Sample length must be at least 1.')

        numbered_states = range(self.num_states)

        markovchain = [np.random.choice(numbered_states, p=self.initial)]
        count = 1
        while count < n:
            current_transition = self.transition[markovchain[-1]]
            markovchain.append(np.random.choice(numbered_states,
                                                p=current_transition))
            count += 1

        return np.array([self.states[num] for num in markovchain])
