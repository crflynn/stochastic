"""Multifractional Brownian motion."""
import inspect

import numpy as np
from scipy.special import gamma

from stochastic.processes.base import BaseTimeProcess


class MultifractionalBrownianMotion(BaseTimeProcess):
    r"""Multifractional Brownian motion process.

    .. image:: _static/multifractional_brownian_motion.png
        :scale: 50%

    A multifractional Brownian motion generalizes a fractional Brownian
    motion with a Hurst parameter which is a function of time,
    :math:`h(t)`. If the Hurst is constant, the process is a fractional
    Brownian motion. If Hurst is constant equal to 0.5, the process is a
    Brownian motion.

    Approximate method originally proposed for fBm in

    * Rambaldi, Sandro, and Ombretta Pinazza. "An accurate fractional Brownian
      motion generator." Physica A: Statistical Mechanics and its Applications
      208, no. 1 (1994): 21-30.

    Adapted to approximate mBm in

    * Muniandy, S. V., and S. C. Lim. "Modeling of locally self-similar
      processes using multifractional Brownian motion of Riemann-Liouville
      type." Physical Review E 63, no. 4 (2001): 046104.

    :param float hurst: a callable with one argument :math:`h(t)` such that
        :math:`h(t') \in (0, 1) \forall t' \in [0, t]`. Default is
        :math:`h(t) = 0.5`.
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, hurst=None, t=1, rng=None):
        super().__init__(t=t, rng=rng)
        self.hurst = hurst if hurst is not None else lambda x: 0.5
        self._n = None

    def __str__(self):
        return (
            "Multifractional Brownian motion with Hurst function "
            + "{h} on [0, {t}].".format(t=str(self.t), h=self.hurst.__name__)
        )

    def __repr__(self):
        return "FractionalBrownianMotion(hurst={h}, t={t})".format(
            t=str(self.t), h=self.hurst.__name__
        )

    @property
    def hurst(self):
        """Hurst function."""
        return self._hurst

    @hurst.setter
    def hurst(self, value):
        try:
            num_args = len(inspect.signature(value).parameters)
        except Exception:
            raise ValueError("Hurst parameter must be a function of one argument.")
        if not callable(value) or num_args != 1:
            raise ValueError("Hurst parameter must be a function of one argument.")
        self._hurst = value
        self._changed = True

    def _check_hurst(self, value):
        self._hs = [value(t) for t in self.times(self._n)]
        for h in self._hs:
            if h <= 0 or h >= 1:
                raise ValueError("Hurst range must be on interval (0, 1).")

    def _sample_multifractional_brownian_motion(self, n):
        """Generate Riemann-Liouville mBm."""
        gn = self.rng.normal(0.0, 1.0, n)
        self._set_times(n)
        self._dt = 1.0 * self.t / self._n
        self._check_hurst(self.hurst)
        mbm = [0]
        coefs = [(g / np.sqrt(self._dt)) * self._dt for g in gn]
        for k in range(1, self._n + 1):
            weights = [self._w(t, self._hs[k]) for t in self._times[1 : k + 1]]
            seq = [coefs[i - 1] * weights[k - i] for i in range(1, k + 1)]
            mbm.append(sum(seq))
        return np.array(mbm)

    def sample(self, n):
        """Generate a realization.

        :param int n: the number of increments to generate
        """
        return self._sample_multifractional_brownian_motion(n)

    def _w(self, t, hurst):
        """Get the Riemann-Liouville method weight for time t."""
        w = (
            1.0
            / gamma(hurst + 0.5)
            * np.sqrt(
                (t ** (2 * hurst) - (t - self._dt) ** (2 * hurst))
                / (2 * hurst * self._dt)
            )
        )
        return w
