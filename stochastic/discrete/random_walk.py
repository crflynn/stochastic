"""Random walk process."""
import numpy as np

from stochastic.base import Sequence


class RandomWalk(Sequence):
    """Random walk.

    A random walk is a sequence of random steps taken from a set of step sizes
    with a probability distribution. By default this object defines the steps
    to be [-1, 1] with probability 1/2 for each possibility.
    """

    def __init__(self, steps=[-1, 1], weights=None):
        self.steps = steps
        length = len(steps)
        if weights is None:
            self.weights = [1 for s in steps]
            self.p = [1.0 / length for s in steps]
        else:
            if len(weights) != length:
                raise ValueError(
                    "Steps and probabilities must have same length.")
            self.weights = weights
            total = sum(weights)
            self.p = [w / total for w in weights]

    @property
    def p(self):
        """Step probabilities."""
        return self._p

    @p.setter
    def p(self, values):
        values = np.array(values, copy=True)
        if values.ndim != 1:
            raise TypeError(
                "Probabilities must be a sequence of possible step values.")
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("Probability values must be numeric.")
            if value < 0 or value > 1:
                raise ValueError("Probability values must be between 0 and 1.")
        if sum(values) != 1:
            raise ValueError("Probabilities must sum to 1.")
        self._p = values

    @property
    def steps(self):
        """Possible steps."""
        return self._steps

    @steps.setter
    def steps(self, values):
        values = np.array(values, copy=True)
        if values.ndim != 1:
            raise TypeError(
                "Steps must be a sequence of possible step values.")
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("Step values must be numeric.")
        self._steps = values

    @property
    def weights(self):
        """Step weights."""
        return self._weights

    @weights.setter
    def weights(self, values):
        values = np.array(values, copy=True)
        if values.ndim != 1:
            raise TypeError(
                "Weights must be a sequence of weight values.")
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("Weight values must be numeric.")
            if value < 0:
                raise ValueError("Weight values must be nonnegative.")

    def __str__(self):
        return "Random walk steps = {s} and weights = {w}".format(
            s=str(self.steps),
            w=str(self.weights)
        )

    def __repr__(self):
        return "RandomWalk(steps={s}, weights={w})".format(
            s=str(self.steps),
            w=str(self.weights)
        )

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
            raise TypeError("Sample length must be int.")
        if n < 1:
            raise ValueError("Sample length must be at least 1.")

        return np.random.choice(self.steps, p=self.p, size=n)
