# Code créé par Gabriel Taillon le 7 Mai 2018
import numpy as np


def NHPPLeemisEst(AllRealizations):
    """ Non parametric estimation of the rate function of a NHPP.
    
    **Arguments:**  
        AllRealizations: 2d array
            'jagged' array containing all realizations, as columns of a 2d matrix. Contains all cumulative event occurences in time, padded with zeros to make columns of length equal to the realizations with the most events.
             
    **Returns:**
        AllEventsT: list
            All times where the estimated rate function was evaluated
        GammaEst: list
            All values of the estimated rate function evaluated between 0 and the maximal 
    Reference: 
    Leemis, L. M. (1991). Nonparametric estimation of the cumulative intensity function for a nonhomogeneous Poisson process. Management Science, 37(7), 886-900.
    """
    SortedTimes=np.sort(AllRealizations[AllRealizations!=0])
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
    
def NHPPMangkuEst(AllEventsT, LowerEstBound=40e-6, UpperEstBound=60e-6,silent=0):
    """ Parametric estimation of the rate function of a NHPP.
    
    **Arguments:**  
        AllEventsT: 2d array
            'jagged' array containing all realizations, as columns of a 2d matrix. Contains all cumulative event occurences in time, padded with zeros to make columns of length equal to the realizations with the most events.
             
    **Returns:**
        periodest: float
            Estimation of the period.
    Reference: 
    Helmers, R., Mangku, I. W., & Zitikis, R. (2003). Consistent estimation of the intensity function of a cyclic Poisson process. Journal of Multivariate Analysis, 84(1), 19-39.
    Belitser, E., Serra, P., & ZANTEN, H. V. (2013). Estimating the Period of a Cyclic Non‐Homogeneous Poisson Process. Scandinavian Journal of Statistics, 40(2), 204-218.
    """
    AllEventsT=Dataa[:,0]*TimeStep
    AllHarmonics=np.linspace(1, 10, 10)  # Also known as a harmonic spectrum.
    for Harmonic in AllHarmonics:
        AllGrosT=np.linspace(LowerEstBound*Harmonic, UpperEstBound*Harmonic, 5000)
        AllQ=[]
        periodest=[]
        for GrosT in AllGrosT:
            AllQ=np.append(AllQ, QforPeriodEst(AllEventsT,GrosT, TimeLength))
        periodest=np.append(periodest, AllGrosT[np.min(np.where(AllQ==np.min(AllQ))[0])]/Harmonic)
    return periodest
    