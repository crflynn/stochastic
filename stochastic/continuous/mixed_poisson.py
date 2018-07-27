"""Mixed poisson processes."""
import numpy as np

from stochastic.base import Checks

class MixedPoissonProcess(Checks):
    r"""Mixed poisson process.

    A mixed poisson process is a Poisson process for which the rate is a random variate, 
    a sample taken from a random distribution. On every call of the sample, a new random rate is generated.
    A Poisson process with rate :math:`\lambda` is a count of occurrences of
    i.i.d. exponential random variables with mean :math:`1/\lambda`. This class
    generates samples of times for which cumulative exponential random variables occur. 

    :param function info: random distribution of the rate :math:`\lambda`
    :param list params: parameters to input into the info function
    """

    def __init__(self, info, params):
        self.info = info
        self.params = params
        self.rate=(info,params)

    def __str__(self):
        return "Mixed Poisson process with rate {r}.".format(r=str(self.rate))

    def __repr__(self):
        return "PoissonProcess(rate={r})".format(r=str(self.rate))

    @property
    def info(self):
        """Current rate's random distribution."""
        return self._info
        
    @info.setter
    def info(self, value):
        self._info = value
        if (hasattr(self,'_params')) & (hasattr(self,'_info')) : 
            self.rate = self._info,self._params
        if (hasattr(self,'_rate')) : self._check_nonnegative_number(self._rate, "Arrival rate")

    @property
    def params(self):
        """Parameters for rate generation using given random distribution."""
        return self._params
        
    @params.setter
    def params(self, value):
        self._params = value
        if (hasattr(self,'_params')) & (hasattr(self,'_info')) : 
            self.rate = self._info,self._params
            self._check_nonnegative_number(self._rate, "Arrival rate")
        
    @property
    def rate(self):
        """Current rate."""
        return self._rate
        
    @rate.setter
    def rate(self, value):
        info, params= value 
        self._info=info
        self._params=params
        self._rate = self._info(*self._params)
        self._check_nonnegative_number(self._rate, "Arrival rate")
        
    def genrate(self):
        self._rate=self.info(*self.params)

    def _sample_poisson_process(self, n=None, length=None, zero=True):
        """Generate a realization of a Mixed Poisson process.

        Generate a poisson process sample up to count of length if time=False,
        otherwise generate a sample up to time t=length if time=True
        """
        
        if n is not None:
            self._check_increments(n)

            exponentials = np.random.exponential(
                scale=1.0 / self.rate, size=n)

            s = np.array([0] + list(np.cumsum(exponentials)))
            if zero:
                return s
            else:
                return s[1:]
        elif length is not None:
            self._check_positive_number(length, "Sample length")

            t = 0
            times = []
            if zero:
                times.append(0)
            exp_rate = 1.0 / self.rate

            while t < length:
                t += np.random.exponential(scale=exp_rate)
                times.append(t)
            return np.array(times)
            
        else:
            raise ValueError(
                "Must provide either argument n or length.")

    def sample(self, n=None, length=None, zero=True):
        """Generate a realization.

        Exactly one of the following parameters must be provided.

        :param int n: the number of arrivals to simulate
        :param int length: the length of time to simulate; will generate
            arrivals until length is met or exceeded.
        :param bool zero: if True, include :math:`t=0`
        """
        out=self._sample_poisson_process(n, length, zero)
        self._rate = self._info(*self._params) 
        """Generate a new random rate upon each realization."""
        self._check_nonnegative_number(self._rate, "Arrival rate")
        return out

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError("MixedPoissonProcess object has no attribute times.")