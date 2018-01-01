"""Brownian meander."""
import numpy as np

from stochastic.continuous.brownian_bridge import BrownianBridge


class BrownianMeander(BrownianBridge):
    """Brownian meander process.

    A Brownian motion conditioned such that the process is nonnegative.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, t=1):
        super().__init__(t)

    def __str__(self):
        return "Brownian meander"""

    def __repr__(self):
        return "BrownianMeander()"

    def _sample_brownian_meander(self, n, b=None, zero=True):
        """Generate a Brownian meander realization.

        Williams, 1970, or Imhof, 1984.
        """
        if b is None:
            b = np.sqrt(2 * np.random.exponential())
        else:
            self._check_number(b, "Right endpoint")
            if b < 0:
                raise ValueError("Right endpoint must be nonnegative.")
        bridge_1 = self._sample_brownian_bridge(n, zero)
        bridge_2 = self._sample_brownian_bridge(n, zero)
        bridge_3 = self._sample_brownian_bridge(n, zero)
        times = self.times(n, zero)

        return np.sqrt(
            (b * times / self.t + bridge_1) ** 2 +
            bridge_2 ** 2 + bridge_3 ** 2
        )

    def sample(self, n, b=None, zero=True):
        """Generate a Brownian meander realization.

        Generage a Brownian meander using the Williams, 1970 / Imhof, 1984
        algorithm.

        :param int n: the number of increments to generate
        :param float b: the nonnegative right hand endpoint of the meander
        :param bool zero: if True, include time :math:`t=0`
        """
        return self._sample_brownian_meander(n, b, zero)

    def sample_at(self, times):
        """TODO"""
        raise NotImplementedError
