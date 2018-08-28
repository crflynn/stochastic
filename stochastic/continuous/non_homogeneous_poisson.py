"""Poisson processes."""
import numpy as np
import scipy.optimize

from stochastic.base import Checks


class NonHomogeneousPoissonProcess(Checks):
    r"""Non-homogeneous Poisson process.
    
    .. image:: _static/non_homogeneous_poisson_process.png
    :scale: 50%

    A Poisson process whose rate :math:`\lambda` is a function of time or the
    underlying data space :math:`\lambda\to\lambda(t)`. This class also be
    used to generate multidimensional points, if multidimensional parameters
    are inputted. Uses the 'thinning' or 'acceptance/rejection' algorithm
    to generate the points. Returns data points inside `bounds` if a function
    is inputted, and indexes if a density array is inputted.

    1. Note: :math:`dim` is not an input parameter, but the methods crash
    unless the number of input argument of the function :math:`\lambda(t)`,
    or the number of dimensions of the matrix :math:`\lambda(t)` is not
    equal to the number :math:`dim` of sets of bounds.

    2. Note: This class can be used to create a Cox process by injecting a
    :math:`\lambda(t)` matrix generated using another stochastic process.

    :param rate_func: a function with :math:`dim` arguments representing a
        multidimensional density function, or a :math:`dim`-dimensional array
        representing the rate function in the data space.
    :param dict rate_kwargs: keyword args for ``rate_func``
    """

    def __init__(self, rate_func, rate_kwargs={}):
        self.rate_func = rate_func
        self.rate_kwargs = rate_kwargs
        self.bounds = bounds

    def __str__(self):
        return "Non-homogeneous Poisson process with rate function of time."

    def __repr__(self):
        return "NonHomogeneousPoissonProcess(" \
            "rate_func={rf}, bounds={bds}, rate_kwargs={rkw})".format(
                rf=str(self.rate_func),
                bds=str(self.bounds),
                rkw=str(self.rate_kwargs)
            )        
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
    def rate_func(self):
        """Rate function, or :math:`dim`-dimensional array."""
        return self._rate_func

    @rate_func.setter
    def rate_func(self, value):
        if (not callable(value)) & (not isinstance(value, (np.ndarray))):
            raise ValueError("Rate function must be a callable or ndarray.")
        self._rate_func = value

    @property
    def bounds(self):
        """Boundaries of the density function or array. 2D Array/List"""
        return self._bounds

    @bounds.setter
    def bounds(self, value):
        if not isinstance(value, (list, np.ndarray, tuple)):
            raise ValueError("Bounds must be a `(dim, 2)` list, `numpy` ndarray or tuple.")
        self._bounds = value

    def _get_rate_max(self):
        """Generate a new `rate_max` value. Used to generate uniformly distributed
        points in the data space before rejecting part of them."""
        if callable(self._rate_func):
            max = scipy.optimize.minimize(lambda x: -self.rate_func(*x, **self.rate_kwargs),
                                          x0 = 
                                          [np.mean(i) for i in self._bounds],
                                          bounds=self.bounds)
            self._rate_max = self._rate_func(*max.x, **self.rate_kwargs)
        else:
            self._rate_max = np.amax(self._rate_func)
            # self._check_nonnegative_number(self._rate_max, "Maximal rate")
    def _sample_nhpp_inversion(rate_func, n=None, length=None, zero=True):
        """Generate a realization of a Non-Homogeneous Poisson process using
        the inversion algorithm. Only 1D.
        
        :param array bounds: :math:`dim` number of bounds
        (temporal/spatial) in a :math:`(dim, 2)`-dimensional array between which
        the random points are generated.
        """
        if n is not None:
                times = np.array(list(np.cumsum(np.random.exponential(size=n))))
                means = np.array([0])
                for time in times:
                    mean = 0
                    while (mean == means[-1]) | (mean == 0):
                        inversion = lambda x : np.abs(time - scipy.integrate.quad(rate_func, 0, x)[0])
                        mean = scipy.optimize.minimize(inversion, time, bounds = ((means[-1],np.inf),)).x
                    means = np.append(means, mean)
        if length is not None:
            times = np.array([0])
            means = np.array([0])   
            while means[-1] < length:
                mean = 0
                while (mean == means[-1]) | (mean == 0):
                    inversion = lambda x : np.abs(times[-1] - scipy.integrate.quad(rate_func, 0, x)[0])
                    mean = scipy.optimize.minimize(inversion, times[-1], bounds = ((means[-1],np.inf),)).x
                    times = np.append(times, times[-1]+np.random.exponential())
                means = np.append(means, mean)
        return(means[1-zero:])
    def _sample_nhpp_thinning(self, n=None, bounds=None zero=True):
        """Generate a realization of a Non-Homogeneous Poisson process using
        the thinning or acceptance/rejection algorithm. Points are generated
        uniformly inside the `bounds`, and accepted with a probability
        proportional to the rate function. Instead of accepting/rejecting
        points one at a time, this algorithm compares numpy ndarrays of length
        `block`, until `n` samples are generated.
        
        :param array bounds: :math:`dim` number of bounds
        (temporal/spatial) in a :math:`(dim, 2)`-dimensional array between which
        the random points are generated.
        """
        thinned = []
        if n is not None:
            self._check_increments(n)
            while len(thinned) < n:
                unthinned = np.zeros(block)
                if callable(self.rate_func):
                    for boundary in self.bounds:# unthinned->data points
                        unthinned
                else:
                    for dim_len in self.rate_func.shape:# unthinned->indexes
                        unthinned = np.vstack((unthinned,
                            np.random.randint(0, dim_len, block)))

            if zero:
                return(np.vstack((np.zeros((1, thinned.shape[1])), thinned[:n, :])))
            else:
                return thinned[:n, :]
        else:
            raise ValueError("Must provide argument n.")
            
    def sample(self, n=None, zero=True, algo='thinning'):
        """Generate a realization.

        :param int n: the number of points to simulate
        """
        self._get_rate_max()
        if algo == 'thinning':
            return self._sample_nhpp_thinning(n, zero, block)
        elif: algo == 'inversion':
            return
        elif: algo == 'order':
            return
    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError(
        "NonHomogeneousPoissonProcess object has no attribute times.")

def lambdatest1D(x1):
return(6*x1)
Intervals1D = np.array([[0, 3]])
def lambdatest2D(x1,x2):
    return(6.*x1*x2**2.)
Intervals2D = np.array([[0,3], [0,2]])
def lambdatest3D(x1,x2,x3):
    return(x1+2*x2**2+3*x3**3)
Intervals3D = np.array([[0,1], [0,2], [0,3]])

A = NonHomogeneousPoissonProcess(lambdatest3D, Intervals3D)
print(A.sample(n=10,))