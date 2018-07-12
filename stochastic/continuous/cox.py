"""Cox processes. Doubly stochastic poisson processes."""
import inspect
import sys
import numpy as np

from stochastic.base import Checks

class CoxProcess(Checks):
    r"""Cox process, or doubly stochastic Poisson process (DSPP).

    # .. image:: _static/poisson_process.png
        # :scale: 50%
    A Poisson process whose rate function is another stochastic process. If lambdaa is a NHPPy/stochastic class, it automatically creates a new lambdaa on every sample generation. Otherwise, if lambda is a list, it has to be generated manually every iteration. and this class would be functionally identical to the NHPP class.

    :param class infoprocess: class from the NHPPy/stochastic that enables the sampling of a stochastic process. Normally, one that outputs
    :param list of floats infoparams: Parameters to input into the information process
    """

    def __init__(self, infoprocess,infoparams):
        self.infoprocess=infoprocess
        self.infoparams=infoparams
        self._check_child(self.infoprocess)

    @property
    def infoprocess(self):
        """Current rate's random distribution."""
        return self._infoprocess
        
    @infoprocess.setter
    def infoprocess(self, value):
        self._infoprocess = value
        if (hasattr(self,'_infoprocess')) & (hasattr(self,'_infoparams')) : 
            currentprocess=self._infoprocess(self._infoparams)
            self.lambdaa =currentprocess.sample(n)

    @property
    def infoparams(self):
        """Parameters for rate generation using given random distribution."""
        return self._ratedistparams
        
    @infoparams.setter
    def infoparams(self, value):
        self._infoparams = value
        if (hasattr(self,'_infoprocess')) & (hasattr(self,'_infoparams')) : 
            if inspect.isclass(self._infoprocess):
                self._infoprocess=self._infoprocess(self._infoparams)
            else:
                self.lambdaa =self._infoprocess(self._infoparams).sample(n)
        
    @property
    def lambdaa(self):
        """Current stochastically generated rate."""
        return self._lambdaa
        
    @lambdaa.setter
    def lambdaa(self, value):
        infoprocess, infoparams= value 
        self._infoprocess= infoprocess
        currentprocess=self._infoprocess(self._infoparams)
        self.lambdaa =currentprocess.sample(n)
        
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
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
from poisson import PoissonProcess
from stochastic.base import Continuous
A=CoxProcess(PoissonProcess,1)
sys.exit()
# A=PoissonProcess(2)
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
