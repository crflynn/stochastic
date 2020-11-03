"""Gaussian Noise."""
import numpy as np

from stochastic.processes.base import BaseTimeProcess
from stochastic.utils.validation import check_positive_integer
from stochastic.utils.validation import times_to_increments


class GaussianNoise(BaseTimeProcess):
    """Gaussian noise process.

    .. image:: _static/gaussian_noise.png
        :scale: 50%

    Generate a sequence of Gaussian random variables.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(t=t, rng=rng)

    def __str__(self):
        return "Gaussian noise generator on interval [0, {t}]".format(t=str(self.t))

    def __repr__(self):
        return "GaussianNoise(t={t})".format(t=str(self.t))

    def _sample_gaussian_noise(self, n):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.
        """
        check_positive_integer(n)
        delta_t = 1.0 * self.t / n

        noise = self.rng.normal(scale=np.sqrt(delta_t), size=n)

        return noise

    def _sample_gaussian_noise_at(self, times):
        """Generate Gaussian noise increments at specified times from zero."""
        if times[0] != 0:
            times = np.concatenate(([0], times))
        increments = times_to_increments(times)

        noise = np.array([self.rng.normal(scale=np.sqrt(inc)) for inc in increments])

        return noise

    def sample(self, n):
        """Generate a realization of Gaussian noise.

        Generate a Gaussian noise realization with n increments.

        :param int n: the number of increments to generate.
        """
        return self._sample_gaussian_noise(n)

    def sample_at(self, times):
        """Generate Gaussian noise increments at specified times from zero.

        :param times: a vector of increasing time values for which to generate
            noise increments.
        """
        return self._sample_gaussian_noise_at(times)
