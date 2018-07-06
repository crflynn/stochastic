"""Poisson processes."""
import numpy as np

from stochastic.base import Checks

def MultiVarNHPPThinSamples(lambdaa,Boundaries,Samples=100,blocksize=1000,silent=0): 
    """ Computes sample random points in a multidimensional space, using a multidimensional rate function/rate matrix. Use the thinning/acceptance-rejection algorithm.
    
    **Arguments:**  
        lambdaa : function or n-d matrix
            Rate function. For now, the multidimensional rate cannot be constant.
        Boundaries : (2,n) matrix
            Contains the spatial boundaries in which to generate the points. Data space boundaries.
        Samples: integer
            Number of samples to generate
        blocksize: integer
            Number of points to generate before thinning, rejection. Instead of generating points one by one, a blocksize length array is generated. I think this makes the algo faster.
        silent: bool
            Prints debug if equal to one. TO BE REMOVED. REPLACED WITH CORRECT LOGGING.
    **Returns:**
        Thinned : (samples,n) matrix
            Generated samples.
    """ 
    if not silent: print('NHPP samples in space by thinning. lambda can be a 2D matrix or function')
    # This algorithm acts as if events do not happen outside the Boundaries.
    if callable(lambdaa):
        boundstuple=[]
        for i in Boundaries: boundstuple+=(tuple(i),)
        max = scipy.optimize.minimize(lambda x: -lambdaa(*x),x0=[np.mean(i) for i in Boundaries],bounds = boundstuple)
        lmax=lambdaa(*max.x)
    else:
        lmax=np.amax(lambdaa)
    Thinned=[]
    while len(Thinned)<Samples:
        for i in Boundaries:
            if 'Unthin' not in locals():
                Unthin=np.random.uniform(*i,size=(blocksize))
            else:
                Unthin=np.vstack((Unthin,np.random.uniform(*i,size=(blocksize))))
        Unthin.T
        U=np.random.uniform(size=(blocksize))
        if callable(lambdaa): 
            Criteria=lambdaa(*Unthin)/lmax
        else:
            Criteria2D=lambdaa/lmax
            Indx=(Unthinx*lambdaa.shape[0]).astype(int)
            Indy=(Unthiny*lambdaa.shape[1]).astype(int)
            Criteria=Criteria2D[Indx,Indy]
            Unthin=np.transpose(np.vstack((Unthinx,Unthiny)))
        if Thinned==[]: 
            Thinned=Unthin.T[U<Criteria,:]
        else:
            Thinned=np.vstack((Thinned,Unthin.T[U<Criteria,:]))
        del Unthin
    Thinned=Thinned[:Samples,:]
    return(Thinned)


class NHPP(Checks):
    r"""Non-homogeneous Poisson process.

    # .. image:: _static/poisson_process.png
        # :scale: 50%
    A Poisson process whose rate function varies with time/the underlying data space. Can also be used to generate multidimensional points.

    :param function or nd Matrix lambda: n-dimensional rate function, or n-dimensional matrix representing the rate function in the data space.
    :param list of floats RateDistParams: Parameters to input into the RateDistFunction
    :param matrix of shape (dim,2) Boundaries: Parameters to input into the RateDistFunction
    """

    def __init__(self, lambdaa,Boundaries):
        self.lambdaa=lambdaa
        self.Boundaries=Boundaries
        if callable(lambdaa):
            boundstuple=[]
            for i in Boundaries: boundstuple+=(tuple(i),)
            max = scipy.optimize.minimize(lambda x: -lambdaa(*x),x0=[np.mean(i) for i in Boundaries],bounds = boundstuple)
            self.lmax=lambdaa(*max.x)
        else:
            self.lmax=np.amax(lambdaa)
         

    @property
    def rate(self):
        """Current rate."""
        return self._rate
        """Current rate random distribution and parameters."""
        

    @rate.setter
    def rate(self, lambdaa,Boundaries):
        self.__init__(lambdaa,Boundaries)


    def _sample_poisson_process(self, n=None, length=None, zero=True):
        """Generate a realization of a Non-homogeneous Poisson process using the Thinning/acceptance-rejection algorithm.

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
        return self._sample_poisson_process(n, length, zero)

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError("MixedPoissonProcess object has no attribute times.")