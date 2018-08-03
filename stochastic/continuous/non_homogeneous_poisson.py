"""Poisson processes."""
import numpy as np
import scipy.optimize

from stochastic.base import Checks


class NonHomogeneousPoissonProcess(Checks):
    r"""Non-homogeneous Poisson process.

    A Poisson process whose rate :math:`\lambda` is a function of time or the
    underlying data space :math:`\lambda\to\lambda(t)`. This class also be
    used to generate multidimensional points, if multidimensional parameters
    are inputted. Uses the 'thinning' or 'acceptance/rejection' algorithm
    to generate the points. Returns data points if a function is inputted,
    and indexes if a density array is inputted.

    1. Note: :math:`dim` is not an input parameter, but the methods crash
    unless the number of input argument of the function :math:`\lambda(t)`,
    or the number of dimensions of the matrix :math:`\lambda(t)` is not
    equal to the number :math:`dim` of sets of boundaries.

    2. Note: This class can be used to create a Cox process by injecting a
    :math:`\lambda(t)` matrix generated using another stochastic process.
    
    

    :param lambdaa: function with :math:`dim` arguments representing a
        multidimensional equation, or :math:`dim`-dimensional array
        representing the rate function in the data space.

    :param array boundaries: :math:`dim` number of boundaries
        (temporal/spatial) in a :math:`(dim,2)`-dimensional array between which
        to generate random points.
    """

    def __init__(self, lambdaa, boundaries):
        self.lambdaa = lambdaa
        self.boundaries = boundaries
        self._gen_lmax()

    @property
    def lambdaa(self):
        """Rate function, or :math:`dim`-dimensional matrix."""
        return self._lambdaa

    @lambdaa.setter
    def lambdaa(self, value):
        self._lambdaa = value
        self._gen_lmax()

    @property
    def boundaries(self):
        """boundaries of the rate function."""
        return self._boundaries

    @boundaries.setter
    def boundaries(self, value):
        self._boundaries = value
        self._gen_lmax()

    def _gen_lmax(self):
        """Generate a new lmax value. Used to generate uniformly distributed
        points in the data space before rejecting part of them."""
        if (hasattr(self, '_lambdaa')) & (hasattr(self, '_boundaries')):
            if callable(self._lambdaa):
                boundstuple = []
                for i in self.boundaries:
                    boundstuple += (tuple(i),)
                max = scipy.optimize.minimize(lambda x: -self.lambdaa(*x),
                 x0=[np.mean(i) for i in self._boundaries],
                 bounds=boundstuple)
                self._lmax = self._lambdaa(*max.x)
            else:
                self._lmax = np.amax(self._lambdaa)
            # self._check_nonnegative_number(self._lmax, "Maximal rate")

    def _sample_nhpp_thinning(self, n=None, block=1000):
        """Generate a realization of a Non-homogeneous Poisson process using
        the thinning or acceptance/rejection algorithm. Instead of
        accepting/rejecting points one at a time, this algorithm compares
        numpy ndarray of length block, until n samples are generated.
        """
        thinned = []
        if n is not None:
            self._check_increments(n)
            while len(thinned) < n:
                unthinned = np.zeros(block)
                if callable(self.lambdaa):
                    for boundary in self.boundaries:# unthinned->data points
                        unthinned = np.vstack((unthinned,
                            np.random.uniform(*boundary, size=(block))))
                else:
                    for dim_len in self.lambdaa.shape:# unthinned->indexes
                        unthinned = np.vstack((unthinned,
                            np.random.randint(0, dim_len, block)))
                unthinned = unthinned[1:]
                if len(unthinned.shape) == 1:
                    unthinned = np.reshape(unthinned, (1, len(unthinned)))
                uniform = np.random.uniform(size=(block))
                if callable(self.lambdaa):
                    criteria = self.lambdaa(*unthinned)/self._lmax
                else:
                    prob_arr = self.lambdaa/self._lmax
                    criteria = np.array([])
                    for point in unthinned.T.astype(int):
                        criteria = np.append(criteria, prob_arr[tuple(point)])
                if len(thinned) == 0:
                    thinned = unthinned.T[uniform < criteria, :]
                else:
                    unthinned = np.vstack((unthinned,
                    np.random.uniform(*i, size=(block))))
            return thinned[:n, :]
        else:
            raise ValueError(
                "Must provide either argument n.")

    def sample(self, n=None):
        """Generate a realization.

        :param int n: the number of points to simulate
        """
        return self._sample_nhpp_thinning(n)

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError("MixedPoissonProcess object has no attribute times.")
        
        
def lambdatest1D(x1):
    return(6.*x1)
Intervals1D = np.array([[0, 3]])
def lambdatest2D(x1,x2):
    return(6.*x1*x2**2.)
Intervals2D = np.array([[0,3], [0,2]])
def lambdatest3D(x1,x2,x3):
    return(x1+2*x2**2+3*x3**3)
Intervals3D = np.array([[0,1], [0,2], [0,3]])
print(Intervals3D.shape)

A=NonHomogeneousPoissonProcess(lambdatest1D,Intervals1D)
print(A.sample(10))
B=NonHomogeneousPoissonProcess(np.array([[[1, 2, 3, 4], [4, 5, 6, 7], [5, 6, 7, 8]],
    [[7, 8, 9, 5], [10, 11, 12, 5], [5, 6, 7, 8]]]),Intervals3D)
print(B.sample(10))
