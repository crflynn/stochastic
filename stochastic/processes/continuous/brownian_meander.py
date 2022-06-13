"""Brownian meander."""
import numpy as np

from stochastic.processes.continuous import BrownianBridge
from stochastic.utils.validation import check_nonnegative_number


class BrownianMeander(BrownianBridge):
    r"""Brownian meander process.

    .. image:: _static/brownian_meander.png
        :scale: 50%

    A Brownian motion conditioned such that the process is nonnegative.

    Generated using method by

    * Williams, David. "Decomposing the Brownian path." Bulletin of the
      American Mathematical Society 76, no. 4 (1970): 871-873.

    * Imhof, J-P. "Density factorizations for Brownian motion, meander and the
      three-dimensional Bessel process, and applications." Journal of Applied
      Probability 21, no. 3 (1984): 500-510.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, t=1, rng=None):
        super().__init__(t=t, rng=rng)

    def __str__(self):
        return "Brownian meander"

    def __repr__(self):
        return "BrownianMeander()"

    def _sample_brownian_meander(self, n, b=None):
        """Generate a Brownian meander realization.

        Williams, 1970, or Imhof, 1984.
        """
        if b is None:
            b = np.sqrt(2 * self.t * self.rng.exponential())
        else:
            check_nonnegative_number(b, "Right endpoint")

        bridge_1 = self._sample_brownian_bridge(n)
        bridge_2 = self._sample_brownian_bridge(n)
        bridge_3 = self._sample_brownian_bridge(n)
        return np.sqrt(
            (b * self.times(n) / self.t + bridge_1) ** 2 + bridge_2**2 + bridge_3**2
        )

    def _sample_brownian_meander_at(self, times, b=None):
        """Generate a Brownian meander realization.

        Williams, 1970, or Imhof, 1984.
        """
        if b is None:
            b = np.sqrt(2 * times[-1] * self.rng.exponential())
        else:
            check_nonnegative_number(b, "Right endpoint")

        bridge_1 = self._sample_brownian_bridge_at(times)
        bridge_2 = self._sample_brownian_bridge_at(times)
        bridge_3 = self._sample_brownian_bridge_at(times)

        return np.sqrt(
            (b * times / times[-1] + bridge_1) ** 2 + bridge_2**2 + bridge_3**2
        )

    def sample(self, n, b=None):
        r"""Generate a realization.

        :param int n: the number of increments to generate
        :param float b: the nonnegative right hand endpoint of the meander. If
            not provided, one is randomly selected from a :math:`\sqrt{2E}`
            random variable where :math:`E` is exponential.
        """
        return self._sample_brownian_meander(n, b)

    def sample_at(self, times, b=None):
        r"""Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        :param float b: the right endpoint value for :py:attr:`times` [-1]. If
            not provided, one is randomly selected from a :math:`\sqrt{2tE}`
            random variable where :math:`E` is exponential and :math:`t` is
            :py:attr:`times` [-1].
        """
        return self._sample_brownian_meander_at(times, b)
