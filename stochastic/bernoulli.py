import numpy as np


class Bernoulli(object):
    """
    A Bernoulli process consists of a sequence of Bernoulli random
    variables. A Bernoulli random variable is
        1 with probability p
        0 with probaiility 1-p

    args:
        p (float) = probability of success (probability of a Bernoulli random
            variable realization of 1)
        states (list length 2) = a map of aliases for states 0 and 1 if
            desired (eg ['OFF', 'ON'])

    methods:

    sample
        args:
            n (int) = discrete length of sample
        returns:
            (list length n) of iid Bernoulli(p) with states values
    """

    def __init__(self, p=0.5, states=[0, 1]):
        self.p = p
        self.states = states

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                'Probability of success must be a number between 0 and 1.')
        if value < 0 or value > 1:
            raise ValueError(
                'Probability of success p must be between 0 and 1.')
        self._p = value

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 1 or len(values) != 2:
            raise ValueError(
                'Possible states must be a sequence of length 2.')
        self._states = values

    def __str__(self):
        return 'Bernoulli process with p = %s and states = %s' % \
            (self.p, str(self.states))

    def __repr__(self):
        return self.__str__()

    def sample(self, n):
        """
        Generate a Bernoulli process sample of length n
        """
        if not isinstance(n, int):
            raise TypeError('Sample length must be positive integer.')
        if n < 1:
            raise ValueError('Sample length must be at least 1.')

        return np.array([self.states[1] if s > self.p else self.states[0]
                         for s in np.random.uniform(size=n)])
