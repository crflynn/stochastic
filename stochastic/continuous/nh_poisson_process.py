"""Poisson processes."""
import numpy as np
import scipy.optimize

from stochastic.base import Checks

class NHPP(Checks):
    r"""Non-homogeneous Poisson process.

    A Poisson process whose rate function varies with time/the underlying data space. Can also be used to generate multidimensional points, if multidimensional parameters are inputted.
    
        NOTE 1: :math:`dim` is not an input parameter, but this class crashes unless the number of input argument of the function lambdaa, or the number of dimensions of the matrix lambdaa is not equal to the :math:`dim` of the boundaries parameters.
        
        NOTE 2: This class can be used to create a Cox process by injecting a lambdaa matrix generated using another stochastic process.
    
    :param lambdaa: function with :math:`dim` arguments representing a multidimensional equation, or :math:`dim`-dimensional array representing the rate function in the data space.
    :param array boundaries: dim number of boundaries (temporal/spatial) in a :math:`(dim,2)`-dimensional array between which to generate random points.
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

    def _sample_poisson_process(self, n=None,blocksize=1000):
        """Generate a realization of a Non-homogeneous Poisson process using the Thinning/acceptance-rejection algorithm.

        Generate a poisson process sample up to count of length if time=False,
        otherwise generate a sample up to time t=length if time=True
        """
        Thinned=[]
        if n is not None:
            self._check_increments(n)
            while len(Thinned)<n:
                for i in self.boundaries:
                    if 'Unthin' not in locals():
                        Unthin=np.random.uniform(*i,size=(blocksize))
                    else:
                        Unthin=np.vstack((Unthin,np.random.uniform(*i,size=(blocksize))))
                Unthin.T
                if len(Unthin.shape)==1:
                    Unthin=np.reshape(Unthin,(1,len(Unthin)))
                U=np.random.uniform(size=(blocksize))
                if callable(self.lambdaa): 
                    Criteria=self.lambdaa(*Unthin)/self.lmax
                else:
                    Criteria2D=self.lambdaa/self.lmax
                    Indx=(Unthinx*self.lambdaa.shape[0]).astype(int)
                    Indy=(Unthiny*self.lambdaa.shape[1]).astype(int)
                    Criteria=Criteria2D[Indx,Indy]
                    Unthin=np.transpose(np.vstack((Unthinx,Unthiny)))
                if Thinned==[]: 
                    Thinned=Unthin.T[U<Criteria,:]
                else:
                    Unthin=np.vstack((Unthin,np.random.uniform(*i,size=(blocksize))))
            Unthin.T
            U=np.random.uniform(size=(blocksize))
            if callable(self.lambdaa): 
                Criteria=self.lambdaa(*Unthin)/self.lmax
            else:
                Criteria2D=self.lambdaa/self.lmax
                Indx=(Unthinx*self.lambdaa.shape[0]).astype(int)
                Indy=(Unthiny*self.lambdaa.shape[1]).astype(int)
                Criteria=Criteria2D[Indx,Indy]
                Unthin=np.transpose(np.vstack((Unthinx,Unthiny)))
            if Thinned==[]: 
                Thinned=Unthin.T[U<Criteria,:]
            else:
                Thinned=np.vstack((Thinned,Unthin.T[U<Criteria,:]))
            del Unthin
            return Thinned[:n,:]
        else:
            raise ValueError(
                "Must provide either argument n.")
               
    def sample(self, n=None):
        """Generate a realization.

        :param int n: the number of points to simulate
        """
        return self._sample_poisson_process(n)

    def times(self, *args, **kwargs):
        """Disallow times for this process."""
        raise AttributeError("MixedPoissonProcess object has no attribute times.")