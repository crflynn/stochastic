import numpy as np
from numbers import Number


class PoissonProcess(object):
    """
    A Poisson process with rate lambda is a count of occurrences of iid
    exponential random variables with mean 1/lambda. This class generates
    samples of times for which cumulative exponential random variables
    occur.

    args:
        rate (float) = the rate of occurrence;  1/rate is the mean of the
            associated exponential random variables
    """

    def __init__(self, rate=1):
        self.rate = rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if not isinstance(value, Number):
            raise TypeError('Arrival rate must be a positive number.')
        if value < 0:
            raise ValueError(
                'Arrival rate must be positive')
        self._rate = value

    def __str__(self):
        return 'Poisson process with rate = %s.' % self._rate

    def __repr__(self):
        return self.__str__()

    def sample(self, length, time=False):
        """
        Generate a poisson process sample up to count of length if time=False,
        otherwise generate a sample up to time t=length if time=True

        args:
            length (int or float) = If time=False, generates a Poisson process
                sample where length is the number of jumps. If time=True,
                length is the end time for the sample.
            time (bool) = Flag for generating a sample where length is number
                of jumps if False or length is end time of the sample if True.
                Default: False. 
        """
        if not isinstance(time, bool):
            raise TypeError('Time flag must be boolean.')

        if time:

            t_end = length
            if not isinstance(length, (int, float)):
                raise TypeError('Sample length must be a positive number.')
            if t_end <= 0:
                raise ValueError('Sample length must be positive.')

            t = 0
            times = []
            exp_rate = 1.0 / self.rate

            while t < t_end:
                times.append(t)
                t += np.random.exponential(scale=exp_rate)

            return times

        else:

            if not isinstance(length, int):
                raise TypeError('Count value must be an integer.')
            if length < 1:
                raise ValueError('Count value must be positive.')

            exponentials = np.random.exponential(
                scale=1.0 / self.rate, size=length)

            return np.array([0] + list(np.cumsum(exponentials)))
