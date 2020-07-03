"""Constant elasticity of variance (CEV) process."""
from stochastic.diffusion.ornstein_uhlenbeck import OrnsteinUhlenbeckProcess


class ConstantElasticityVarianceProcess(OrnsteinUhlenbeckProcess):
    r"""Constant elasticity of variance process.

    .. image:: _static/constant_elasticity_variance_process.png
        :scale: 50%

    The process :math:`X_t` that satisfies the following stochastic
    differential equation with Wiener process :math:`W_t`:

    .. math::

        dX_t = \mu X_t dt + \sigma X_t^\gamma dW_t

    Realizations are generated using the Euler-Maruyama method.

    :param float mu: the drift coefficient, or :math:`\mu` above
    :param float sigma: the volatility coefficient, or :math:`\sigma` above
    :param float gamma: the volatility-price exponent, or :math:`\gamma` above
    :param float t: the right hand endpoint of the time interval :math:`[0,t]`
        for the process
    """

    def __init__(self, mu=1, sigma=1, gamma=1, t=1):
        super(ConstantElasticityVarianceProcess, self).__init__(-mu, 0, sigma, t)
        self.mu = mu
        self.sigma = sigma
        self.gamma = gamma

    def __str__(self):
        return (
            "Constant elasticity of variance process with drift={m}, volatility={v}, exponent={e} on [0, {t}]"
        ).format(m=str(self.mu), v=str(self.sigma), e=str(self.gamma), t=str(self.t))

    def __repr__(self):
        return "ConstantElasticityVarianceProcess(mu={m}, sigma={s}, gamma={g}, t={t})".format(
            s=str(self.sigma), m=str(self.mu), g=str(self.gamma), t=str(self.t)
        )

    @property
    def mu(self):
        """Mu."""
        return self._mu

    @mu.setter
    def mu(self, value):
        self._check_number(value, "Drift coefficient.")
        self._mu = value

    @property
    def sigma(self):
        """Sigma."""
        return self._sigma

    @sigma.setter
    def sigma(self, value):
        self._check_nonnegative_number(value, "Volatility coefficient")
        self._sigma = value

    @property
    def gamma(self):
        """Gamma."""
        return self._gamma

    @gamma.setter
    def gamma(self, value):
        self._check_nonnegative_number(value, "Exponent")
        self._gamma = value

    def _volatility(self, arg):
        """O-U Volatility coefficient."""
        return arg ** self.gamma


class CEVProcess(ConstantElasticityVarianceProcess):
    """Alias for ConstantElasticityVarianceProcess."""

    pass
