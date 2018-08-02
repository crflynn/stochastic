"""Mixed poisson processes."""

from stochastic.continuous.poisson import PoissonProcess


class MixedPoissonProcess(PoissonProcess):
    r"""Mixed poisson process. Inherits from the PoissonProcess class.

    A mixed poisson process is a Poisson process for which the rate is
    a random variate, a sample taken from a random distribution.
    On every call of the sample method, a new random rate is generated,
    before drawing the sample. A Poisson process with rate :math:`\lambda`
    is a count of occurrences of i.i.d. exponential random
    variables with mean :math:`1/\lambda`. This class
    generates samples of times for which cumulative
    exponential random variables occur.

    :param function rate_dist: random distribution of the rate :math:`\lambda`
    :param rate_args: arguments to input into the rate_dist function
    :param rate_kwargs: keyword arguments to input into the rate_dist function
    """

    def __init__(self, rate_dist, rate_args=(), rate_kwargs={}):
        self.rate_dist = rate_dist
        self.rate_args = rate_args
        self.rate_kwargs = rate_kwargs
        self._gen_rate()

    def __str__(self):
        return "Mixed Poisson process with rate {r}.".format(r=str(self.rate))

    def __repr__(self):
        return "MixedPoissonProcess(rate={r})".format(r=str(self.rate))

    @property
    def rate_dist(self):
        """Current rate's random distribution."""
        return self._rate_dist

    @rate_dist.setter
    def rate_dist(self, value):
        self._rate_dist = value
        self._gen_rate()

    @property
    def rate_kwargs(self):
        """Keyword arguments for rate generation using
        given random distribution and parameters."""
        return self._rate_kwargs

    @rate_kwargs.setter
    def rate_kwargs(self, value):
        self._rate_kwargs = value
        self._gen_rate()

    @property
    def rate_args(self):
        """Arguments for rate generation using given random distribution."""
        return self._rate_args

    @rate_args.setter
    def rate_args(self, value):
        self._rate_args = value
        self._gen_rate()

    @property
    def rate(self):
        """Current rate."""
        return self._rate

    @rate.setter
    def rate(self, value):
        print('a')
        rate_dist, rate_args, rate_kwargs = value
        self._rate_dist = rate_dist
        self._rate_args = rate_args
        self._rate_kwargs = rate_kwargs
        self._gen_rate()

    def _gen_rate(self):
        """Generate a new rate. Called when any parameter is set,
        and upon each call for samples."""
        if (hasattr(self, '_rate_args') &
                hasattr(self, '_rate_dist') &
                hasattr(self, '_rate_kwargs')):
            self._rate = self.rate_dist(*self.rate_args, **self.rate_kwargs)
            self._check_nonnegative_number(self.rate, "Arrival rate")

    def sample(self, n=None, length=None, zero=True):
        """Generate a new random rate upon each realization."""
        self._gen_rate()
        return super(MixedPoissonProcess, self).sample(n, length, zero)
