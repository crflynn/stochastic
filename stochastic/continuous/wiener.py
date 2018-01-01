"""Wiener process."""
from stochastic.continuous.brownian_motion import BrownianMotion


class WienerProcess(BrownianMotion):
    """Wiener process, or standard Brownian motion.

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, t=1):
        super().__init__(t, drift=0, scale=1)

    def __str__(self):
        return "Wiener process on [0, {t}]".format(t=str(self.t))

    def __repr__(self):
        return "WienerProcess(t={t})".format(t=str(self.t))

    def sample(self, n, zero=True):
        """Generate a realization of the Wiener process.

        :param int n: the number of increments to generate
        :param bool zero: if True, include :math:`t=0`
        """
        return self._sample_brownian_motion(n, zero)
