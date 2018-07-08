"""Poisson processes."""
import numpy as np

from stochastic.base import Checks

class MixedPoissonProcess(Checks):
    r"""Mixed Poisson process.

    # .. image:: _static/poisson_process.png
        # :scale: 50%
    A mixed poisson process is a Poisson process for which the rate is a random variate, 
    a sample taken from a random distribution. On every call of the sample, a new random rate is generated.
    A Poisson process with rate :math:`\lambda` is a count of occurrences of
    i.i.d. exponential random variables with mean :math:`1/\lambda`. This class
    generates samples of times for which cumulative exponential random     variables occur. 

    :param function ratedist: random distribution of the rate :math:`\lambda` which defines the rate of
        occurrences of the process
    :param list of floats ratedistparams: Parameters to input into the ratedistFunction
    """

    def __init__(self, ratedist,ratedistparams):
        self.ratedist = ratedist
        self.ratedistparams = ratedistparams
        self.rate=(ratedist,ratedistparams)

    def __str__(self):
        return "Mixed Poisson process with rate {r}.".format(r=str(self.rate))

    def __repr__(self):
        return "PoissonProcess(rate={r})".format(r=str(self.rate))

    @property
    def ratedist(self):
        """Current rate's random distribution."""
        return self._ratedist
        
    @ratedist.setter
    def ratedist(self, value):
        self._ratedist = value
        if (hasattr(self,'_ratedistparams')) & (hasattr(self,'_ratedist')) : 
            self.rate = self._ratedist,self._ratedistparams
        if (hasattr(self,'_rate')) : self._check_nonnegative_number(self._rate, "Arrival rate")

    @property
    def ratedistparams(self):
        """Parameters for rate generation using given random distribution."""
        return self._ratedistparams
        
    @ratedistparams.setter
    def ratedistparams(self, value):
        self._ratedistparams = value
        if (hasattr(self,'_ratedistparams')) & (hasattr(self,'_ratedist')) : 
            self.rate = self._ratedist,self._ratedistparams
        if (hasattr(self,'_rate')) : self._check_nonnegative_number(self._rate, "Arrival rate")
        
    @property
    def rate(self):
        """Current rate."""
        return self._rate
        
    @rate.setter
    def rate(self, value):
        print('setter')
        ratedist, ratedistparams= value 
        self._ratedist=ratedist
        self._ratedistparams=ratedistparams
        self._rate = self._ratedist(*self._ratedistparams)
        self._check_nonnegative_number(self._rate, "Arrival rate")
        
    def genrate(self):
        self._rate=self.ratedist(*self.ratedistparams)

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
        self._rate = self._ratedist(*self._ratedistparams) 
        """Generate a new random rate upon each realization."""
        self._check_nonnegative_number(self._rate, "Arrival rate")
        return out

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError("MixedPoissonProcess object has no attribute times.")
        

InfoProcessparams=[0,100]
InfoProcess1=np.random.uniform
InfoProcess2=np.random.normal
A=MixedPoissonProcess(InfoProcess1,InfoProcessparams)
import sys
print(A.rate)
print(A.ratedist)
print(A.ratedistparams)
A.ratedist=InfoProcess1
print(A.rate)
print(A.ratedist)
print(A.ratedistparams)
A.ratedistparams=[0,10]
print(A.rate)
print(A.ratedist)
print(A.ratedistparams)

print(A.rate)
A.sample(n=100)
print(A.rate)
sys.exit()
