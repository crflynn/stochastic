import numpy as np


class RandomWalk(object):
    """
    A random walk is a sequence of random steps taken from a set of step sizes
    with a probability distribution. By default this object defines the steps
    to be [-1, 1] with probability 1/2 for each possibility.

    args:
        steps (list(int or float)): the possible steps to take at each
            increment of the random walk.
        p (list(int or float)): optional, the probabilities
            associated with each of the steps provided. By default the
            probabilities are 1/len(steps).
    """

    def __init__(self, steps=[-1, 1], p=None):
        self.steps = steps
        length = len(steps)
        if p is None:
            self.p = [1.0 / length for s in steps]
        else:
            if len(p) != length:
                raise ValueError(
                    'Length of probabilities must match length of possible steps')
            self.p = p

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 1:
            raise TypeError(
                'Steps must be a sequence of possible step values.')
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError('Step values must be numeric.')
        self._steps = values

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, values):
        values = np.array(values, copy=False)
        if values.ndim != 1:
            raise TypeError(
                'Probabilities must be a sequence of possible step values.')
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError('Probability values must be numeric.')
            if value < 0 or value > 1:
                raise ValueError('Probability values must be between 0 and 1.')
        if sum(values) != 1:
            raise ValueError('Probabilities must sum to 1.')
        self._p = values

    def __str__(self):
        return 'Random walk process with steps = %s and probabilities = %s' % \
            (str(self.steps), str(self.p))

    def __repr__(self):
        return self.__str__()

    def sample(self, n):
        """
        Generate a sample random walk including step at t=0.

        args:
            n (int) = the number of steps in the random walk
        """
        return np.array([0] + list(np.cumsum(self.sample_increments(n))))

    def sample_increments(self, n):
        """
        Generate the increments of a random walk.

        args:
            n (int) = the number of steps in the random walk
        """
        if not isinstance(n, int):
            raise TypeError('Sample length must be int.')
        if n < 1:
            raise ValueError('Sample length must be at least 1.')

        return np.random.choice(self.steps, p=self.p, size=n)
