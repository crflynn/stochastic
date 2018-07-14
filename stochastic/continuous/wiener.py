"""Wiener process."""
from stochastic.continuous.brownian_motion import BrownianMotion


class WienerProcess(BrownianMotion):
    """Wiener process, or standard Brownian motion.

    .. image:: _static/wiener_process.png
        :scale: 50%

    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, t=1):
        super(WienerProcess, self).__init__(drift=0, scale=1, t=t)

    def __str__(self):
        return "Wiener process on [0, {t}]".format(t=str(self.t))

    def __repr__(self):
        return "WienerProcess(t={t})".format(t=str(self.t))
