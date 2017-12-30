import numpy as np

from stochastic.base import Sequence


class PoissonProcess(Sequence):
    """Poisson process.

    A Poisson process with rate lambda is a count of occurrences of iid
    exponential random variables with mean 1/lambda. This class generates
    samples of times for which cumulative exponential random variables
    occur.
    """

    def __init__(self, rate=1):
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
        self._check_nonnegative_number(value, "Arrival rate")
        self._rate = value

    def _sample_poisson_process(self, n=None, length=None):
        """Generate a realization of a Poisson process.

        Generate a poisson process sample up to count of length if time=False,
        otherwise generate a sample up to time t=length if time=True
        """
        if n is not None:
            self._check_increments(n)

            exponentials = np.random.exponential(
                scale=1.0 / self.rate, size=length)

            return np.array([0] + list(np.cumsum(exponentials)))
        elif length is not None:
            self._check_positive_number(length, "Sample length")

            t = 0
            times = []
            exp_rate = 1.0 / self.rate

            while t < length:
                times.append(t)
                t += np.random.exponential(scale=exp_rate)

            return times
        else:
            raise ValueError(
                "Must provide either process increments or length.")

    def sample(self, n=None, length=None):
        """Generate a realization of a Poisson process."""
        self._sample_poisson_process(n, length)

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError("PoissonProcess object has no attribute times.")
