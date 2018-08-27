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
    to generate the points. Returns data points if a function is inputted,
    and indexes if a density array is inputted.

    1. Note: :math:`dim` is not an input parameter, but the methods crash
    unless the number of input argument of the function :math:`\lambda(t)`,
    or the number of dimensions of the matrix :math:`\lambda(t)` is not
    equal to the number :math:`dim` of sets of bounds.

    2. Note: This class can be used to create a Cox process by injecting a
    :math:`\lambda(t)` matrix generated using another stochastic process.

    :param rate_func: a function with :math:`dim` arguments representing a
        multidimensional density function, or a :math:`dim`-dimensional array
        representing the rate function in the data space.

    :param array bounds: :math:`dim` number of bounds
        (temporal/spatial) in a :math:`(dim, 2)`-dimensional array between which
        the random points are generated.
    """

    def __init__(self, rate_func, bounds):
        self.rate_func = rate_func
        self.bounds = bounds

    def __str__(self):
        return "Non-homogeneous Poisson process with rate function of time."

    def __repr__(self):
        return "NonHomogeneousPoissonProcess(" \
            "rate_func={rf}, rate_args={ra}, rate_kwargs={rkw})".format(
                rf=str(self.rate_func),
                ra=str(self.rate_args),
                rkw=str(self.rate_kwargs)
            )        
          
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
            max = scipy.optimize.minimize(lambda x: -self.rate_func(*x),
            x0 = [np.mean(i) for i in self._bounds],
            bounds=self.bounds)
            self._rate_max = self._rate_func(*max.x)
        else:
            self._rate_max = np.amax(self._rate_func)
            # self._check_nonnegative_number(self._rate_max, "Maximal rate")

    def _sample_nhpp_thinning(self, n=None, block=1000):
        """Generate a realization of a Non-Homogeneous Poisson process using
        the thinning or acceptance/rejection algorithm. Instead of
        accepting/rejecting points one at a time, this algorithm compares
        numpy ndarrays of length `block`, until `n` samples are generated.
        """
        thinned = []
        if n is not None:
            self._check_increments(n)
            while len(thinned) < n:
                unthinned = np.zeros(block)
                if callable(self.rate_func):
                    for boundary in self.bounds:# unthinned->data points
                        unthinned = np.vstack((unthinned,
                        np.random.uniform(*boundary, size=(block))))
                else:
                    for dim_len in self.rate_func.shape:# unthinned->indexes
                        unthinned = np.vstack((unthinned,
                            np.random.randint(0, dim_len, block)))
                unthinned = unthinned[1:]
                uniform = np.random.uniform(size=(block))
                if callable(self.rate_func):
                    criteria = self.rate_func(*unthinned)/self._rate_max
                else:
                    prob_arr = self.rate_func/self._rate_max
                    criteria = np.array([])
                    for point in unthinned.T.astype(int):
                        criteria = np.append(criteria, prob_arr[tuple(point)])
                if len(thinned) == 0:
                    thinned = unthinned.T[uniform < criteria, :]
                else:
                    thinned = np.vstack((thinned,
                    unthinned.T[uniform < criteria, :]))
            return thinned[:n, :]
        else:
            raise ValueError("Must provide argument n.")

    def sample(self, n=None):
        """Generate a realization.

        :param int n: the number of points to simulate
        """
        self._get_rate_max()
        return self._sample_nhpp_thinning(n)

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError(
        "NonHomogeneousPoissonProcess object has no attribute times.")
