"""Mixed poisson processes."""
from stochastic.processes.continuous.poisson import PoissonProcess
from stochastic.utils.validation import check_nonnegative_number


class MixedPoissonProcess(PoissonProcess):
    r"""Mixed poisson process.

    .. image:: _static/mixed_poisson_process.png
        :scale: 50%

    A mixed poisson process is a Poisson process for which the rate is
    a scalar random variate. The sample method will generate a random variate
    for the rate before generating a Poisson process realization with the rate.
    A Poisson process with rate :math:`\lambda`
    is a count of occurrences of i.i.d. exponential random
    variables with mean :math:`1/\lambda`. Use the ``rate`` attribute to get
    the most recently generated random rate.

    :param callable rate_func: a callable to generate variates of the random
        rate
    :param tuple rate_args: positional args for ``rate_func``
    :param dict rate_kwargs: keyword args for ``rate_func``
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, rate_func, rate_args=None, rate_kwargs=None, rng=None):
        self.rate_func = rate_func
        self.rate_args = rate_args if rate_args is not None else tuple()
        self.rate_kwargs = rate_kwargs if rate_kwargs is not None else dict()
        super().__init__(rate=1, rng=rng)

    def __str__(self):
        return "Mixed Poisson process with random rate."

    def __repr__(self):
        return "MixedPoissonProcess(rate_func={rf}, rate_args={ra}, rate_kwargs={rkw})".format(
            rf=str(self.rate_func), ra=str(self.rate_args), rkw=str(self.rate_kwargs)
        )

    @property
    def rate_func(self):
        """Current rate's distribution."""
        return self._rate_func

    @rate_func.setter
    def rate_func(self, value):
        if not callable(value):
            raise ValueError("Rate function must be a callable.")
        self._rate_func = value

    @property
    def rate_args(self):
        """Positional arguments for the rate function."""
        return self._rate_args

    @rate_args.setter
    def rate_args(self, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError("Rate args must be a list or tuple.")
        self._rate_args = value

    @property
    def rate_kwargs(self):
        """Keyword arguments for the rate function."""
        return self._rate_kwargs

    @rate_kwargs.setter
    def rate_kwargs(self, value):
        if not isinstance(value, dict):
            raise ValueError("Rate kwargs must be a dict.")
        self._rate_kwargs = value

    @property
    def rate(self):
        """The most recently generated rate.

        Attempting to get the rate prior to generating a sample will raise
        an ``AttributeError``."""
        return self._rate

    @rate.setter
    def rate(self, value):
        check_nonnegative_number(value, "Arrival rate")
        self._rate = value

    def _sample_rate(self):
        """Generate a rate variate."""
        return self.rate_func(*self.rate_args, **self.rate_kwargs)

    def sample(self, n=None, length=None):
        """Generate a realization.

        Exactly one of `n` and `length` must be provided. Generates a random
        variate for the rate, then generates a Poisson process realization
        using this rate.

        :param int n: the number of arrivals to simulate
        :param int length: the length of time to simulate; will generate
            arrivals until length is met or exceeded.
        """
        self.rate = self._sample_rate()
        return self._sample_poisson_process(n, length)
