"""Dirichlet process."""
import numpy as np

from stochastic.processes.base import BaseSequenceProcess
from stochastic.utils.validation import check_positive_number


class DirichletProcess(BaseSequenceProcess):
    r"""Dirichlet process.

    .. image:: _static/dirichlet_process.png
        :scale: 50%

    A Dirichlet process is a stochastic process in which the resulting samples
    can be interpreted as discrete probability distributions.

    For each step :math:`k \geq 1`, draw from the base distribution with
    probability

    .. math::
        \frac{\alpha}{\alpha + k - 1}

    Otherwise draw randomly from the previous steps.

    :param callable base: a zero argument callable used as the base
        distribution sampler. The default base distribution is Uniform(0, 1).
    :param float alpha: a non-negative value used to determine probability of
        drawing a new value from the base distribution
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, base=None, alpha=1, rng=None):
        super().__init__(rng=rng)
        if base is None:
            base = self.rng.uniform
        self.base = base
        self.alpha = alpha

    @property
    def base(self):
        """The base distribution callable for sampling new step values."""
        return self._base

    @base.setter
    def base(self, value):
        if not callable(value):
            raise ValueError("base must be callable")
        self._base = value

    @property
    def alpha(self):
        """Parameter for determining the probability of sampling new values."""
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        check_positive_number(value)
        self._alpha = value

    def _sample(self, n):
        """Generate a realization of the Dirichlet process.

        :param int n: the number of steps of the Dirichlet process to generate.
        """
        sequence = []
        for k in range(1, n + 1):
            draw_proba = self.alpha / (self.alpha + k - 1)
            if self.rng.uniform() < draw_proba:
                sequence.append(self.base())
            else:
                sequence.append(self.rng.choice(sequence))
        return np.array(sequence)

    def sample(self, n):
        """Generate a realization of the Dirichlet process.

        :param int n: the number of steps of the Dirichlet process to generate.
        """
        return self._sample(n)
