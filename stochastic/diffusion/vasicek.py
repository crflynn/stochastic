"""Vasicek process."""
from stochastic.diffusion.ornstein_uhlenbeck import OrnsteinUhlenbeckProcess


class VasicekProcess(OrnsteinUhlenbeckProcess):
    r"""Vasicek process.

    A model for instantaneous interest rate.

    .. image:: _static/vasicek_process.png
        :scale: 50%

    The Vasicek process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \theta X_t (\mu - t) dt + \sigma dW_t

    Realizations are generated using the Euler-Maruyama method.

    :param float speed: the speed of reversion, or :math:`\theta` above
    :param float mean: the mean of the process, or :math:`\mu` above
    :param float vol: volatility coefficient of the process, or :math:`\sigma`
        above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __str__(self):
        return "Vasicek process with speed={s}, mean={m}, vol={v} on [0, {t}]".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )

    def __repr__(self):
        return "VasicekProcess(speed={s}, mean={m}, vol={v}, t={t})".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )
