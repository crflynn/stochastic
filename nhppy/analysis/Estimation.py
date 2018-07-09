# Code créé par Gabriel Taillon le 7 Mai 2018

import os, sys, inspect, gc # standard library.
import numpy as np, sympy as sp, scipy
import matplotlib.pyplot as plt
import statsmodels.nonparametric.api as smnp
import analysisfunctions as func


def NHPPNonParamEst(AllRealizations):
    """ Non parametric estimation of the rate function of a NHPP.
    
    **Arguments:**  
        AllRealizations: 2d array
            'jagged' array containing all realizations, as columns of a 2d matrix. Contains all cumulative event occurences in time, padded with zeros to make columns of length equal to the realizations with the most events.
             
    **Returns:**
    Reference: 
    Leemis, L. M. (1991). Nonparametric estimation of the cumulative intensity function for a nonhomogeneous Poisson process. Management Science, 37(7), 886-900.
    """
    UnSortedTimes=AllRealizations[AllRealizations!=0]
    SortedTimes=np.sort(UnSortedTimes)
    n=len(SortedTimes)
    k=AllRealizations.shape[1]
    Sortedi=np.arange(0,len(SortedTimes))
    Interpoli=np.arange(0,len(SortedTimes)-1,1./NumbetweenTi)
    Arrayoft=np.interp(Interpoli,Sortedi,SortedTimes)
    Arrayofi=np.floor(Interpoli)+1
    ArrayofTi=np.repeat(SortedTimes[:-1],NumbetweenTi)
    ArrayofTi1=np.repeat(SortedTimes[1:],NumbetweenTi)
    np.seterr(invalid='ignore')
    GammaEst=Arrayofi*n/(n+1)/k+np.divide(n*(Arrayoft-ArrayofTi)/(n+1)/k,(ArrayofTi1-ArrayofTi))
    GammaEstNoNan=GammaEst[np.where(1-np.isnan(GammaEst))[0]]
    AllEventsT=Arrayoft[np.where(1-np.isnan(GammaEst))[0]]
    return AllEventsT, GammaEstNoNan
    