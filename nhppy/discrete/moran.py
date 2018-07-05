"""Moran process."""
import numpy as np


class MoranProcess(object):
    """Moran process.

    .. image:: _static/moran_process.png
        :scale: 50%

    A neutral drift Moran process, typically used to model populations. At
    each step this process will increase by one, decrease by one, or remain
    at the same value between values of zero and the number of
    states, :math:`n`. The process ends when its value reaches zero or the
    maximum valued state.

    :param int n_max: the maximum possible value for the process.
    """

    def __init__(self, n_max):
        self.n_max = n_max
        self.p = self._probabilities(n_max)

    def __str__(self):
        return 'Moran process with %s states' % self._n_max

    def __repr__(self):
        return "MoranProcess(n_max={n})".format(n=str(self.n_max))

    @property
    def n_max(self):
        """Maximum value."""
        return self._n_max

    @n_max.setter
    def n_max(self, value):
        if not isinstance(value, int):
            raise TypeError(
                'Number of states must be an integer.')
        if value <= 2:
            raise ValueError(
                'Number of states must be at least 3.')
        self._n_max = value

    def _probabilities(self, n):
        """Generate the transition probabilities for state :math:`n`.

        :param int n: the current state for which to generate transition
            probabilities.
        """
        probabilities = []
        for k in range(1, n):
            p_down = 1.0 * (n - k) / n * k / n
            p_up = 1.0 * k / n * (n - k) / n
            p_same = 1.0 - p_down - p_up
            probabilities.append([p_down, p_same, p_up])

        return probabilities

    def _sample_moran_process(self, n, start):
        """Generate a realization of the Moran process.

        Generate a Moran process until absorption occurs (state 0 or n) or
        length of process reaches length :math:`n_max`.
        """
        if not isinstance(start, int):
            raise TypeError('Initial state must be a positive integer.')
        if start < 0 or start > self.n_max:
            raise ValueError(
                'Initial state must be between 0 and ' + str(self.n_max))

        if not isinstance(n, int):
            raise TypeError('Sample length must be positive integer.')
        if n < 1:
            raise ValueError('Sample length must be at least 1.')

        s = [start]
        increments = [-1, 0, 1]
        for k in range(n - 1):
            if start in [0, self.n_max]:
                break
            start += np.random.choice(increments, p=self.p[start - 1])
            s.append(start)

        return np.array(s)

    def sample(self, n, start):
        """Generate a realization of the Moran process.

        Generate a Moran process until absorption occurs (state 0
        or :py:attr:`n_max`) or length of process reaches length :math:`n`.

        :param int n: the maximum number of steps to generate assuming
            absorption does not occur.
        :param int start: the initial state of the process.
        """
        return self._sample_moran_process(n, start)
