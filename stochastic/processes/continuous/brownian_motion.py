"""Brownian motion and derivative processes."""
import numpy as np

from stochastic.processes.noise.gaussian_noise import GaussianNoise
from stochastic.utils import generate_times
from stochastic.utils.validation import check_numeric
from stochastic.utils.validation import check_positive_number


class BrownianMotion(GaussianNoise):
    """Brownian motion.

    .. image:: _static/brownian_motion.png
        :scale: 50%

    A standard Brownian motion (discretely sampled) has independent and
    identically distributed Gaussian increments with variance equal to
    increment length. Non-standard Brownian motion includes a linear drift
    parameter and scale factor.

    :param float drift: rate of change of the expected value
    :param float scale: scale factor of the Gaussian process
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, drift=0, scale=1, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        self.drift = drift
        self.scale = scale
        self._line = None
        self._n = None

    def __str__(self):
        if self.drift == 0 and self.scale == 1:
            s = "Standard Brownian motion on interval [0, {t}]".format(t=self.t)
            return s
        s = "Brownian motion with drift {d} and scale {s} on interval [0, {t}]."
        return s.format(t=str(self.t), d=str(self.drift), s=str(self.scale))

    def __repr__(self):
        return "BrownianMotion(drift={d}, scale={s}, t={t})".format(
            t=str(self.t), d=str(self.drift), s=str(self.scale)
        )

    @property
    def drift(self):
        """Drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        check_numeric(value, "Drift")
        self._drift = value

    @property
    def scale(self):
        """Scale parameter."""
        return self._scale

    @scale.setter
    def scale(self, value):
        check_positive_number(value, "Scale")
        self._scale = value

    def _sample_brownian_motion(self, n):
        """Generate a realization of Brownian Motion.

        Generate a Brownian motion realization with n increments. If zero is
        True then include W_0 = 0.
        """
        # Some opt for repeats
        if self.drift != 0 and (self._line is None or len(self._line) != n):
            self._n = n
            self._line = generate_times(self.drift, n)

        bm = np.cumsum(self.scale * self._sample_gaussian_noise(n))
        bm = np.insert(bm, [0], 0)

        if self.drift != 0:
            return self._line + bm
        else:
            return bm

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_brownian_motion(n)

    def _sample_brownian_motion_at(self, times):
        """Generate a Brownian motion at specified times."""
        bm = np.cumsum(self.scale * self._sample_gaussian_noise_at(times))

        if times[0] == 0:
            bm = np.insert(bm, 0, [0])

        if self.drift != 0:
            bm += [self.drift * t for t in times]

        return bm

    def sample_at(self, times):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_brownian_motion_at(times)
