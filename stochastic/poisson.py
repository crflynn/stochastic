import numpy as np
from numbers import Number


class Poisson(object):
    """
    A Poisson process with rate lambda is a count of occurrences of iid
    exponential random variables with mean 1/lambda. This class generates
    samples of times for which cumulative exponential random variables
    occur.

    args:
        rate (float) = the rate of occurrence;  1/rate is the mean of the
            associated exponential random variables

    methods:

    sample
        args:
            length (int or float) = int number of occurrences to generate
                or float end time for sample.
            time (boolean) = If true length is an end time for the sample, if
                false length is an integer count at which the sample should
                end. Default is False
        returns:
            (list of len length+1) of cumulative exponentials if time = False
            or (list of arbitrary len) if time = True
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
        """
        if not isinstance(time, bool):
            raise TypeError('Time must be boolean.')

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
