"""Variance gamma process."""
import numpy as np

from stochastic.processes.base import BaseTimeProcess
from stochastic.processes.noise import GaussianNoise
from stochastic.utils.validation import check_numeric
from stochastic.utils.validation import check_positive_integer
from stochastic.utils.validation import check_positive_number


class VarianceGammaProcess(BaseTimeProcess):
    r"""Variance Gamma process.

    .. image:: _static/variance_gamma_process.png
        :scale: 50%

    A variance gamma process has independent increments which follow the
    variance-gamma distribution. It can be represented as a Brownian motion
    with drift subordinated by a Gamma process:

    .. math::

        \theta \Gamma(t; 1, \nu) + \sigma W(\Gamma(t; 1, \nu))

    :param float drift: the drift parameter of the Brownian motion,
        or :math:`\theta` above
    :param float variance: the variance parameter of the Gamma subordinator,
        or :math:`\nu` above
    :param float scale: the scale parameter of the Brownian motion,
        or :math:`\sigma` above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, drift=0, variance=1, scale=1, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        self.drift = drift
        self.variance = variance
        self.scale = scale
        self.gn = GaussianNoise(t)

    @property
    def drift(self):
        """Drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        check_numeric(value, "Drift")
        self._drift = value

    @property
    def variance(self):
        """Variance parameter."""
        return self._variance

    @variance.setter
    def variance(self, value):
        check_positive_number(value, "Variance")
        self._variance = value

    @property
    def scale(self):
        """Scale parameter."""
        return self._scale

    @scale.setter
    def scale(self, value):
        check_positive_number(value, "Scale")
        self._scale = value

    def _sample_variance_gamma_process(self, n):
        """Generate a realization of a variance gamma process."""
        check_positive_integer(n)

        delta_t = 1.0 * self.t / n
        shape = delta_t / self.variance
        scale = self.variance

        gammas = self.rng.gamma(shape=shape, scale=scale, size=n)
        gn = self.gn.sample(n)

        increments = self.drift * gammas + self.scale * np.sqrt(gammas) * gn

        samples = np.cumsum(increments)

        return np.concatenate(([0], samples))

    def _sample_variance_gamma_process_at(self, times):
        """Generate a realization of a variance gamma process."""
        if times[0] != 0:
            zero = False
            times = np.array([0] + list(times))
        else:
            zero = True

        shapes = np.diff(times) / self.variance
        scale = self.variance

        gammas = np.array(
            [self.rng.gamma(shape=shape, scale=scale, size=1)[0] for shape in shapes]
        )
        gn = self.gn.sample_at(times)

        increments = self.drift * gammas + self.scale * np.sqrt(gammas) * gn

        samples = np.cumsum(increments)
        if zero:
            samples = np.insert(samples, 0, [0])
        return samples

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_variance_gamma_process(n)

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_variance_gamma_process_at(times)
