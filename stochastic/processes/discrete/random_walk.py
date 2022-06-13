"""Random walk process."""
import numpy as np

from stochastic.processes.base import BaseSequenceProcess
from stochastic.utils.validation import check_positive_integer


class RandomWalk(BaseSequenceProcess):
    """Random walk.

    .. image:: _static/random_walk.png
        :scale: 50%

    A random walk is a sequence of random steps taken from a set of step sizes
    with a probability distribution. By default this object defines the steps
    to be [-1, 1] with probability 1/2 for each possibility.

    :param steps: a vector of possible deltas to apply at each step.
    :param weights: a corresponding vector of weights associated with each
        step value. If not provided each step has equal weight/probability.
    """

    def __init__(self, steps=None, weights=None, rng=None):
        super().__init__(rng=rng)
        self.steps = steps or [-1, 1]
        length = len(steps)
        if length < 1:
            raise ValueError("Steps must have at least one element.")
        if weights is None:
            self.weights = [1 for _ in steps]
            self.p = [1.0 / length for _ in steps]
        else:
            if len(weights) != length:
                raise ValueError("Steps and probabilities must have same length.")
            self.weights = weights
            total = sum(weights)
            self.p = [1.0 * w / total for w in weights]

    @property
    def p(self):
        """Step probabilities, normalized from :py:attr:`weights`."""
        return self._p

    @p.setter
    def p(self, values):
        values = np.array(values, copy=True)
        self._p = values

    @property
    def steps(self):
        """Possible steps."""
        return self._steps

    @steps.setter
    def steps(self, values):
        for value in values:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("Step values must be numeric.")
        values = np.array(values, copy=True)
        self._steps = values

    @property
    def weights(self):
        """Step weights provided."""
        return self._weights

    @weights.setter
    def weights(self, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("Weight values must be numeric.")
            if value < 0:
                raise ValueError("Weight values must be nonnegative.")
        values = np.array(values, copy=True)
        self._weights = values

    def __str__(self):
        return "Random walk steps = {s} and weights = {w}".format(
            s=str(self.steps), w=str(self.weights)
        )

    def __repr__(self):
        return "RandomWalk(steps={s}, weights={w})".format(
            s=str(self.steps), w=str(self.weights)
        )

    def _sample_random_walk(self, n):
        """Generate a random walk."""
        return np.array([0] + list(np.cumsum(self._sample_random_walk_increments(n))))

    def sample(self, n):
        """Generate a sample random walk.

        :param int n: the number of steps to generate
        """
        return self._sample_random_walk(n)

    def _sample_random_walk_increments(self, n):
        """Generate a sample of random walk increments."""
        check_positive_integer(n)
        return self.rng.choice(self.steps, p=self.p, size=n)

    def sample_increments(self, n):
        """Generate a sample of random walk increments.

        :param int n: the number of increments to generate.
        """
        return self._sample_random_walk_increments(n)
