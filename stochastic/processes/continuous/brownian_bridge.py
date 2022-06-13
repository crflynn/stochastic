"""Brownian bridge."""
import numpy as np

from stochastic.processes.continuous.brownian_motion import BrownianMotion
from stochastic.utils.validation import check_numeric


class BrownianBridge(BrownianMotion):
    """Brownian bridge.

    .. image:: _static/brownian_bridge.png
        :scale: 50%

    A Brownian bridge is a Brownian motion with a conditional value on the
    right endpoint of the process.

    :param float b: the right endpoint value of the Brownian bridge at time t
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, b=0, t=1, rng=None):
        super().__init__(drift=0, scale=1, t=t, rng=rng)
        self.b = b

    def __str__(self):
        return "Brownian bridge from 0 to {b} on [0, {t}]".format(
            t=str(self.t), b=str(self.b)
        )

    def __repr__(self):
        return "BrownianBridge(b={b}, t={t})".format(t=str(self.t), b=str(self.b))

    @property
    def b(self):
        """Right endpoint value."""
        return self._b

    @b.setter
    def b(self, value):
        check_numeric(value, "Time end")
        self._b = value

    def _sample_brownian_bridge(self, n, b=None):
        """Generate a realization of a Brownian bridge."""
        if b is None:
            b = self.b
        bm = self._sample_brownian_motion(n)
        return bm + self.times(n) * (b - bm[-1]) / self.t

    def _sample_brownian_bridge_at(self, times, b=None):
        """Generate a realization of a Brownian bridge at times."""
        if b is None:
            b = self.b
        bm = self._sample_brownian_motion_at(times)
        return bm + np.array(times) * (b - bm[-1]) / times[-1]

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_brownian_bridge(n)

    def sample_at(self, times, b=None):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        :param float b: the right endpoint value for :py:attr:`times` [-1]
        """
        return self._sample_brownian_bridge_at(times, b)
