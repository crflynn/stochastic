"""Poisson processes."""
import numpy as np

from stochastic.processes.base import BaseProcess
from stochastic.utils.validation import check_nonnegative_number
from stochastic.utils.validation import check_positive_integer
from stochastic.utils.validation import check_positive_number


class PoissonProcess(BaseProcess):
    r"""Poisson process.

    .. image:: _static/poisson_process.png
        :scale: 50%

    A Poisson process with rate :math:`\lambda` is a count of occurrences of
    i.i.d. exponential random variables with mean :math:`1/\lambda`. This class
    generates samples of times for which cumulative exponential random
    variables occur.

    :param float rate: the parameter :math:`\lambda` which defines the rate of
        occurrences of the process
    :param numpy.random.Generator rng: a custom random number generator
    """

    def __init__(self, rate=1, rng=None):
        super().__init__(rng=rng)
        self.rate = rate

    def __str__(self):
        return "Poisson process with rate {r}.".format(r=str(self.rate))

    def __repr__(self):
        return "PoissonProcess(rate={r})".format(r=str(self.rate))

    @property
    def rate(self):
        """Rate parameter."""
        return self._rate

    @rate.setter
    def rate(self, value):
        check_nonnegative_number(value, "Arrival rate")
        self._rate = value

    def _sample_poisson_process(self, n=None, length=None):
        """Generate a realization of a Poisson process.

        Generate a poisson process sample up to count of length if time=False,
        otherwise generate a sample up to time t=length if time=True
        """
        if n is not None:
            check_positive_integer(n)

            exponentials = self.rng.exponential(scale=1.0 / self.rate, size=n)

            s = np.array([0] + list(np.cumsum(exponentials)))
            return s
        elif length is not None:
            check_positive_number(length, "Sample length")

            t = 0
            times = [0]
            exp_rate = 1.0 / self.rate

            while t < length:
                t += self.rng.exponential(scale=exp_rate)
                times.append(t)

            return np.array(times)
        else:
            raise ValueError("Must provide either argument n or length.")

    def sample(self, n=None, length=None):
        """Generate a realization.

        Exactly one of `n` and `length` must be provided.

        :param int n: the number of arrivals to simulate
        :param int length: the length of time to simulate; will generate
            arrivals until length is met or exceeded.
        """
        return self._sample_poisson_process(n, length)
