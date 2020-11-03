"""Constant elasticity of variance (CEV) process."""
from stochastic.processes.diffusion.diffusion import DiffusionProcess
from stochastic.utils import ensure_single_arg_constant_function
from stochastic.utils import single_arg_constant_function
from stochastic.utils.validation import check_numeric


class ConstantElasticityVarianceProcess(DiffusionProcess):
    r"""Constant elasticity of variance process.

    .. image:: _static/constant_elasticity_variance_process.png
        :scale: 50%

    The process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \mu X_t dt + \sigma X_t^\gamma dW_t

    Realizations are generated using the Euler-Maruyama method.

    .. note::

        Since the family of diffusion processes have parameters which
        generalize to functions of ``t``, parameter attributes will be returned
        as callables, even if they are initialized as constants. e.g. a
        ``speed`` parameter of 1 accessed from an instance attribute will return
        a function which accepts a single argument and always returns 1.

    :param float drift: the drift coefficient, or :math:`\mu` above
    :param float vol: the volatility coefficient, or :math:`\sigma` above
    :param float volexp: the volatility-price exponent, or :math:`\gamma` above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, drift=1, vol=1, volexp=1, t=1, rng=None):
        super().__init__(
            speed=single_arg_constant_function(-drift),
            mean=single_arg_constant_function(1),
            vol=single_arg_constant_function(vol),
            volexp=single_arg_constant_function(volexp),
            t=t,
            rng=rng,
        )
        self.drift = drift

    def __str__(self):
        return "Constant elasticity of variance process with drift={m}, vol={v}, volexp={e} on [0, {t}]".format(
            m=str(self.drift), v=str(self.vol), e=str(self.volexp), t=str(self.t)
        )

    def __repr__(self):
        return "ConstantElasticityVarianceProcess(drift={d}, vol={v}, volexp={e}, t={t})".format(
            v=str(self.vol), d=str(self.drift), e=str(self.volexp), t=str(self.t)
        )

    @property
    def drift(self):
        """Drift, or Mu."""
        return self._drift

    @drift.setter
    def drift(self, value):
        check_numeric(value, "Drift coefficient.")
        self._drift = ensure_single_arg_constant_function(value)
        self.speed = ensure_single_arg_constant_function(-value)
