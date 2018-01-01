"""Constant elasticity of variance (CEV) process."""
from stochastic.diffusion.ornstein_uhlenbeck import OrnsteinUhlenbeckProcess


class ConstantElasticityVarianceProcess(OrnsteinUhlenbeckProcess):
    """Constant elasticity of variance process."""

    def __init__(self, t=1, mu=1, sigma=1, gamma=1):
        super().__init__(t, -mu, 0, sigma)
        self.mu = mu
        self.sigma = sigma
        self.gamma = gamma

    @property
    def mu(self):
        """Mu."""
        return self._mu

    @mu.setter
    def mu(self, value):
        self._check_number(value)
        self._mu = value

    @property
    def sigma(self):
        """Sigma."""
        return self._sigma

    @sigma.setter
    def sigma(self, value):
        self._check_nonnegative_number(value)
        self._sigma = value

    @property
    def gamma(self):
        """Gamma."""
        return self._gamma

    @gamma.setter
    def gamma(self, value):
        self._check_nonnegative_number(value)
        self._gamma = value

    def _volatility(self, arg):
        """O-U Volatility coefficient."""
        return arg ** self.gamma


class CEVProcess(ConstantElasticityVarianceProcess):
    """Alias for ConstantElasticityVarianceProcess."""

    pass
