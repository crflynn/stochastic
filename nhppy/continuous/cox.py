"""Cox processes. Doubly stochastic poisson processes."""
import sys
import numpy as np

from nhppy.base import Checks

class CoxProcess(Checks):
    r"""Cox process, or doubly stochastic Poisson process (DSPP).

    # .. image:: _static/poisson_process.png
        # :scale: 50%
    A Poisson process whose rate function is another stochastic process. If lambdaa is a NHPPy/stochastic class, it automatically creates a new lambdaa on every sample generation. Otherwise, if lambda is a list, it has to be generated manually every iteration. and this class would be functionally identical to the NHPP class.

    :param class infoprocess: class from the NHPPy/stochastic that enables the sampling of a stochastic process. Normally, one that outputs
    :param list of floats infoparams: Parameters to input into the information process
    """

    def __init__(self, infoprocess,infoparams):
        self._check_zero
        self._check_child(infoprocess)
        sys.exit()

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
            self._check_nonnegative_number(self._rate, "Arrival rate")
        
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
# logic to checking if the passed instance to the cox process is legit: Checks OR continuous are parents of all process. Checks is parents of all processes. So just checking isinstance of checks SHOULD be enough.
# hat to do about instances of non continuous processes
from poisson import PoissonProcess
from nhppy.base import Continuous
A=CoxProcess(PoissonProcess)
sys.exit()
A=PoissonProcess(2)
print(isinstance(A,Continuous))
print(isinstance(A,Checks))
print(isinstance(A,Checks))
print(issubclass(A.__class__,Continuous))
print(issubclass(A.__class__,Checks))
print(issubclass(PoissonProcess,Continuous))
print(issubclass(PoissonProcess,Checks))
print(issubclass(Continuous,Checks))
print(isinstance(A,PoissonProcess))
sys.exit()
