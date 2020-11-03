"""Cox-Ingersoll-Ross process."""
from stochastic.processes.diffusion.diffusion import DiffusionProcess
from stochastic.utils import single_arg_constant_function


class CoxIngersollRossProcess(DiffusionProcess):
    r"""Cox-Ingersoll-Ross process.

    .. image:: _static/cox_ingersoll_ross_process.png
        :scale: 50%

    A model for instantaneous interest rate.

    The process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \theta (\mu - X_t) dt + \sigma \sqrt{X_t} dW_t

    Realizations are generated using the Euler-Maruyama method.

    .. note::

        Since the family of diffusion processes have parameters which
        generalize to functions of ``t``, parameter attributes will be returned
        as callables, even if they are initialized as constants. e.g. a
        ``speed`` parameter of 1 accessed from an instance attribute will return
        a function which accepts a single argument and always returns 1.

    :param float speed: the speed of reversion, or :math:`\theta` above
    :param float mean: the mean of the process, or :math:`\mu` above
    :param float vol: volatility coefficient of the process, or :math:`\sigma`
        above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, speed=1, mean=0, vol=1, t=1, rng=None):
        super().__init__(
            speed=single_arg_constant_function(speed),
            mean=single_arg_constant_function(mean),
            vol=single_arg_constant_function(vol),
            volexp=single_arg_constant_function(0.5),
            t=t,
            rng=rng,
        )

    def __str__(self):
        return "Cox-Ingersoll-Ross process with speed={s}, mean={m}, vol={v} on [0, {t}]".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )

    def __repr__(self):
        return "CoxIngersollRossProcess(speed={s}, mean={m}, vol={v}, t={t})".format(
            s=str(self.speed), m=str(self.mean), v=str(self.vol), t=str(self.t)
        )
