"""Poisson processes."""
import numpy as np
import scipy.optimize

from stochastic.base import Checks

def MultiVarNHPPThinSamples(lambdaa,boundaries,Samples=100,blocksize=1000,silent=0): 
    """ Computes sample random points in a multidimensional space, using a multidimensional rate function/rate matrix. Use the thinning/acceptance-rejection algorithm.
    
    **Arguments:**  
        lambdaa : function or n-d matrix
            Rate function. For now, the multidimensional rate cannot be constant.
        boundaries : (2,n) matrix
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
    # This algorithm acts as if events do not happen outside the boundaries.
    if callable(lambdaa):
        boundstuple=[]
        for i in boundaries: boundstuple+=(tuple(i),)
        max = scipy.optimize.minimize(lambda x: -lambdaa(*x),x0=[np.mean(i) for i in boundaries],bounds = boundstuple)
        lmax=lambdaa(*max.x)
    else:
        lmax=np.amax(lambdaa)
    Thinned=[]
    while len(Thinned)<Samples:
        for i in boundaries:
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
    :param matrix of shape (dim,2) boundaries: Parameters to input into the RateDistFunction
    """

    def __init__(self,lambdaa,boundaries):
        self.lambdaa=lambdaa
        self.boundaries=boundaries
        self.lmax=(lambdaa,boundaries)
        
    @property
    def lambdaa(self):
        """Rate function, or n-dimensional matrix."""
        return self._lambdaa

    @lambdaa.setter
    def lambdaa(self, value):
        self._lambdaa = value
        if (hasattr(self,'_lambdaa')) & (hasattr(self,'_boundaries')) : 
            self.lmax=self.lambdaa,self.boundaries
            self._check_nonnegative_number(self._lmax, "Maximal rate")
        # if (hasattr(self,'_rate')) : self._check_nonnegative_number(self._rate, "Arrival rate")

    @property
    def boundaries(self):
        """boundaries of the rate function."""
        return self._boundaries

    @boundaries.setter
    def boundaries(self, value):
        self._boundaries = value
        if (hasattr(self,'_lambdaa')) & (hasattr(self,'_boundaries')) : 
            self.lmax=self.lambdaa,self.boundaries
            self._check_nonnegative_number(self._lmax, "Maximal rate")

    @property
    def lmax(self):
        """Current rate."""

        return self._lmax
        """Maximal rate."""

    @lmax.setter
    def lmax(self, value):
        lambdaa,boundaries = value 
        if callable(lambdaa):
            boundstuple=[]
            for i in boundaries: boundstuple+=(tuple(i),)
            max = scipy.optimize.minimize(lambda x: -lambdaa(*x),x0=[np.mean(i) for i in boundaries],bounds = boundstuple)
            self._lmax=lambdaa(*max.x)
        else:
            self._lmax=np.amax(lambdaa)
        self._check_nonnegative_number(self._lmax, "Maximal rate")
         
        # self.__init__(lambdaa,boundaries)


    def _sample_poisson_process(self, n=None, length=None, zero=True):
        """Generate a realization of a Non-homogeneous Poisson process using the Thinning/acceptance-rejection algorithm.

        Generate a poisson process sample up to count of length if time=False,
        otherwise generate a sample up to time t=length if time=True
        """
        
        Thinned=[]
        while len(Thinned)<Samples:
            for i in boundaries:
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
import sys
def lambdatest2D(x1,x2):
    return(6.*x1*x2**2.)
Intervals2D=np.array([[0,3],[0,2]])
def lambdatest3D1(x1,x2,x3):
    return(x1+2*x2**2+3*x3**3)
def lambdatest3D2(x1,x2,x3):
    return(x1+x2**2-x3**3)
Intervals3D1=np.array([[0,1],[0,2],[0,3]])
Intervals3D2=np.array([[0,2],[0,2],[0,5]])
A=NHPP(lambdatest3D1,Intervals3D1)
print(A.lmax)
A.boundaries=Intervals3D2
print(A.lmax)
A.lambdaa=lambdatest3D2
print(A.lmax)
sys.exit()
NHPP.lmax=lambdatest3D,Intervals3D1
print(NHPP.lmax)