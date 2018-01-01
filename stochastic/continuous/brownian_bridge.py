"""Brownian bridge."""
from stochastic.continuous.brownian_motion import BrownianMotion


class BrownianBridge(BrownianMotion):
    """Brownian bridge.

    A Brownian bridge is a Brownian motion with a conditional value on the
    right endpoint of the process.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param float b: the right endpoint value of the Brownian bridge at time t
    """

    def __init__(self, t=1, b=0):
        super().__init__(t, drift=0, scale=1)
        self.b = b

    @property
    def b(self):
        """The right endpoint value."""
        return self._b

    @b.setter
    def b(self, value):
        self._check_number(value, "Time end")
        self._b = value

    def __str__(self):
        return "Brownian bridge from 0 to {b} on [0, {t}]".format(
            t=str(self.t),
            b=str(self.b)
        )

    def __repr__(self):
        if self.t == 1:
            return "BrownianBridge(b={b})".format(
                t=str(self.t),
                b=str(self.b)
            )
        return "BrownianBridge(t={t}, b={b})".format(
            t=str(self.t),
            b=str(self.b),
        )

    def _sample_brownian_bridge(self, n, zero=True, b=None):
        """Generate a realization of a Brownian bridge."""
        self._check_zero(zero)
        if b is None:
            b = self.b

        bm = self._sample_brownian_motion(n, zero)
        times = self.times(n, zero)

        return bm + times * (b - bm[-1]) / self.t

    def sample(self, n, zero=True):
        """Generate a realization of a Brownian bridge.

        Generate realizations of a Brownian bridge in which the value at time
        :math:`t` is equal to :math:`b`.

        :param int n: the number of increments to generate
        :param bool zero: if True, include time :math:`t=0`
        """
        return self._sample_brownian_bridge(n, zero)

    def sample_at(self, times):
        """TODO"""
        raise NotImplementedError
