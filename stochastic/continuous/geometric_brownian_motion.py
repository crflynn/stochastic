"""Geometric Brownian motion."""
import numpy as np

from stochastic.base import Continuous
from stochastic.continuous.brownian_motion import BrownianMotion


class GeometricBrownianMotion(Continuous):
    r"""Geometric Brownian motion process.

    .. image:: _static/geometric_brownian_motion.png
        :scale: 50%

    A geometric Brownian motion :math:`S_t` is the analytic solution to the
    stochastic differential equation with Wiener process :math:`W_t`:

    .. math::

        dS_t = \mu S_t dt + \sigma S_t dW_t

    and can be represented with initial value :math:`S_0` in the form:

    .. math::

        S_t = S_0 \exp \left( \left( \mu - \frac{\sigma^2}{2} \right) t +
        \sigma W_t \right)

    :param float drift: the parameter :math:`\mu`
    :param float volatility: the parameter :math:`\sigma`
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, drift=0, volatility=1, t=1):
        super(GeometricBrownianMotion, self).__init__(t)
        self._brownian_motion = BrownianMotion(t=t)
        self.drift = drift
        self.volatility = volatility
        self._n = None

    def __str__(self):
        return "Geometric Brownian motion with drift {d} and volatility {v} on [0, {t}].".format(
            t=str(self.t), d=str(self.drift), v=str(self.volatility)
        )

    def __repr__(self):
        return "GeometricBrownianMotion(drift={d}, volatility={v}, t={t})".format(
            t=str(self.t), d=str(self.drift), v=str(self.volatility)
        )

    @property
    def drift(self):
        """Geometric Brownian motion drift parameter."""
        return self._drift

    @drift.setter
    def drift(self, value):
        self._check_number(value, "Drift")
        self._drift = value

    @property
    def volatility(self):
        """Geometric Brownian motion volatility parameter."""
        return self._volatility

    @volatility.setter
    def volatility(self, value):
        self._check_positive_number(value, "Volatility")
        self._volatility = value

    def _sample_geometric_brownian_motion(self, n, initial=1, zero=True):
        """Generate a realization of geometric Brownian motion."""
        self._check_increments(n)
        self._check_positive_number(initial, "Initial")
        self._check_zero(zero)

        # Opt for repeated use
        if self._n != n:
            self._n = n
            self._line = self._linspace(self.drift - self.volatility ** 2 / 2.0, n, zero)

        noise = self.volatility * self._brownian_motion.sample(n, zero)

        return initial * np.exp(self._line + noise)

    def _sample_geometric_brownian_motion_at(self, times, initial=1):
        """Generate a realization of geometric Brownian motion."""
        line = [(self.drift - self.volatility ** 2 / 2.0) * t for t in times]
        noise = self.volatility * self._brownian_motion.sample_at(times)

        return initial * np.exp(line + noise)

    def sample(self, n, initial=1, zero=True):
        """Generate a realization.

        :param int n: the number of increments to generate.
        :param float initial: the initial value of the process :math:`S_0`.
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample_geometric_brownian_motion(n, initial, zero)

    def sample_at(self, times, initial=1):
        """Generate a realization using specified times.

        :param times: a vector of increasing time values at which to generate
            the realization
        """
        return self._sample_geometric_brownian_motion_at(times, initial)
