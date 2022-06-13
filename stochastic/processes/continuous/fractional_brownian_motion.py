"""Fractional Brownian motion."""
import numpy as np

from stochastic.processes.noise import FractionalGaussianNoise


class FractionalBrownianMotion(FractionalGaussianNoise):
    r"""Fractional Brownian motion process.

    .. image:: _static/fractional_brownian_motion.png
        :scale: 50%

    A fractional Brownian motion (discretely sampled) has correlated Gaussian
    increments defined by Hurst parameter :math:`H`. When :math:`H = 1/2`,
    the process is a standard Brownian motion. When :math:`H > 1/2`, the
    increments are positively correlated. When :math:`H < 1/2`, the
    increments are negatively correlated.

    Hosking's method:

    * Hosking, Jonathan RM. "Modeling persistence in hydrological time series
      using fractional differencing." Water resources research 20, no. 12 (1984): 1898-1908.

    Davies Harte method:

    * Davies, Robert B., and D. S. Harte. "Tests for Hurst effect." Biometrika
      74, no. 1 (1987): 95-101.

    :param float hurst: the Hurst parameter on the interval (0, 1)
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, hurst=0.5, t=1, rng=None):
        super().__init__(hurst=hurst, t=t, rng=rng)

    def __str__(self):
        return "Fractional Brownian motion with Hurst {h} on [0, {t}].".format(
            h=str(self.hurst), t=str(self.t)
        )

    def __repr__(self):
        return "FractionalBrownianMotion(hurst={h}, t={t})".format(
            t=str(self.t), h=str(self.hurst)
        )

    def _sample_fractional_brownian_motion(self, n):
        """Generate a realization of fractional Brownian motion."""
        fgn = self._sample_fractional_gaussian_noise(n)
        fbm = fgn.cumsum()
        fbm = np.insert(fbm, [0], 0)
        return fbm

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_fractional_brownian_motion(n)
