# Code créé par Gabriel Taillon le 7 Mai 2018
#  2D Kolmogorov-Smyrnov Test. Exclusively Data-Data for now.
# References: 
#  [1] Peacock, J. A. (1983). Two-dimensional goodness-of-fit testing in astronomy. Monthly Notices of the Royal Astronomical Society, 202(3), 615-627.
#  [2] Fasano, G., & Franceschini, A. (1987). A multidimensional version of the Kolmogorov–Smirnov test. Monthly Notices of the Royal Astronomical Society, 225(1), 155-170.
#  [3]  Flannery, B. P., Press, W. H., Teukolsky, S. A., & Vetterling, W. (1992). Numerical recipes in C. Press Syndicate of the University of Cambridge, New York, 24, 78.
import sys, os, inspect
import numpy as np, scipy.stats

def CountQuads(Arr2D,point,silent=1):
    # Counts the number of points of Arr2D in each 4 quadrant defined by a vertical and horizontal line crossing the point.
    # Then computes the proportion of points in each quadrant.
    # A bit of checking. If Arr2D and point are not lists or ndarray, exit.
    if isinstance(point, list):
        if not silent: print('point is a list')
        point=np.asarray((np.ravel(point)))
        pass
    elif type(point).__module__+type(point).__name__=='numpyndarray':
        point=np.ravel(point.copy())
        if not silent: print('point is a numpy.ndarray')
    else:
        if not silent: print('point is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(point)!=2:
        if not silent: print('2 elements should be in point. Exiting.')
        return
    if isinstance(Arr2D, list):
        if not silent: print('Arr2D is a list')
        Arr2D=np.asarray((Arr2D))
    elif type(Arr2D).__module__+type(Arr2D).__name__=='numpyndarray':
        if not silent: print('Arr2D is a ndarray')
    else:
        if not silent: print('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D.shape[1]>Arr2D.shape[0]: # Reshape so that A[row,column] is achieved.
        Arr2D=Arr2D.copy().T
    if Arr2D.shape[1]!=2: 
        if not silent: print('2 columns should be in Arr2D. Exiting.')
        return
    # The pp of Qpp refer to p for 'positive' and m for 'negative' quadrants. In order. first subscript is x, second is y.
    Qpp=Arr2D[(Arr2D[:,0]>=point[0])&(Arr2D[:,1]>=point[1]),:]
    Qmp=Arr2D[(Arr2D[:,0]<=point[0])&(Arr2D[:,1]>=point[1]),:]
    Qpm=Arr2D[(Arr2D[:,0]>=point[0])&(Arr2D[:,1]<=point[1]),:]
    Qmm=Arr2D[(Arr2D[:,0]<=point[0])&(Arr2D[:,1]<=point[1]),:]
    if not silent: print('Same number of points in Arr2D as in all Quadrants: '+str((len(Qpp)+len(Qmp)+len(Qpm)+len(Qmm))==len(Arr2D)))
    # Normalized fractions:
    ff=1./len(Arr2D)
    fpp=len(Qpp)*ff
    fmp=len(Qmp)*ff
    fpm=len(Qpm)*ff
    fmm=len(Qmm)*ff
    # NOTE:  all the f's are supposed to sum to 1.0. Float representation cause SOMETIMES sum to 1.000000002 or something. I don't know how to test for that reliably, OR what to do about it yet. Keep in mind.
    return(fpp,fmp,fpm,fmm)
def FuncQuads(func2D,point,xlim,ylim,rounddig=4,silent=1):
    # Computes the proportion of func2D in each 4 quadrant defined by a vertical and horizontal lines crossing the point.
    # func2D must be a function that takes 2 arguments.
    # uses numerical integration based on scipy to compute the fpp's
    # A bit of checking. 
    # If func2D is not a function with 2 arguments, exit.
    if callable(func2D):
        if not silent:print('func2D is a function')
        if len(inspect.getfullargspec(func2D)[0])!=2:
            if not silent:print('func2D function has not 2 arguments. Exiting.')
            return
        pass
    else:
        if not silent:print('func2D is not a function. Exiting.')
        return
    # If xlim, ylim and point are not lists or ndarray, exit.
    if isinstance(point, list):
        if not silent: print('point is a list')
        point=np.asarray((np.ravel(point)))
        pass
    elif type(point).__module__+type(point).__name__=='numpyndarray':
        point=np.ravel(point.copy())
        if not silent: print('point is a numpy.ndarray')
    else:
        if not silent: print('point is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(point)!=2:
        if not silent: print('2 elements should be in point. Exiting.')
        return
    if isinstance(xlim, list):
        if not silent: print('xlim is a list')
        xlim=np.asarray((np.ravel(xlim)))
        pass
    elif type(xlim).__module__+type(xlim).__name__=='numpyndarray':
        xlim=np.ravel(xlim.copy())
        if not silent: print('xlim is a numpy.ndarray')
    else:
        if not silent: print('xlim is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(xlim)!=2:
        if not silent: print('2 elements should be in xlim. Exiting.')
        return
    if isinstance(ylim, list):
        if not silent: print('ylim is a list')
        ylim=np.asarray((np.ravel(ylim)))
        pass
    elif type(ylim).__module__+type(ylim).__name__=='numpyndarray':
        ylim=np.ravel(ylim.copy())
        if not silent: print('ylim is a numpy.ndarray')
    else:
        if not silent: print('ylim is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(ylim)!=2:
        if not silent: print('2 elements should be in ylim. Exiting.')
        return
    # Numerical integration to find the quadrant probabilities.
    totInt=scipy.integrate.dblquad(func2D,*xlim, lambda x: np.amin(ylim),  lambda x: np.amax(ylim))[0]
    Qpp=scipy.integrate.dblquad(func2D,point[0],np.amax(xlim), lambda x: point[1],  lambda x: np.amax(ylim))[0]
    Qpm=scipy.integrate.dblquad(func2D,point[0],np.amax(xlim), lambda x: np.amin(ylim),  lambda x: point[1])[0]
    Qmp=scipy.integrate.dblquad(func2D,np.amin(xlim),point[0], lambda x: point[1],  lambda x: np.amax(ylim))[0]
    Qmm=scipy.integrate.dblquad(func2D,np.amin(xlim),point[0], lambda x: np.amin(ylim),  lambda x: point[1])[0]
    fpp=round(Qpp/totInt,rounddig)
    fmp=round(Qmp/totInt,rounddig)
    fpm=round(Qpm/totInt,rounddig)
    fmm=round(Qmm/totInt,rounddig)    
    return(fpp,fmp,fpm,fmm)
def f2d(x,y,k):
    return(x**2+y)
print(FuncQuads(f2d,[0.5,0.5,0],[0,1,1],[0,1,1],silent=0))
sys.exit()

def Qks(alam,iter=101,prec=1e-6,silent=1):
    # Computes the value of the KS probability function, as a function of alam, a float. What is this function? Complicated: 
    # From Numerical recipes in C page 623: '[...] the K–S statistic useful is that its distribution in the case of the null hypothesis (data sets drawn from the same distribution) can be calculated, at least to useful approximation, thus giving the significance of any observed nonzero value of D.' (D being the maximum value of the absolute difference between two cumulative distribution functions)
    # Anyhow, the equation is pretty straightforward: sum of terms as defined below.
    # 100 iterations are more than sufficient to converge. No convergence here: if j iterations are performed, meaning that toadd is still 2 times larger than the precision.
    if isinstance(alam,int)|isinstance(alam,float):
        pass
    else:
        if not silent: print('alam is not an integer or float. Exiting.')
        return
    toadd=[1]
    qks=0.
    j=1
    while (j<iter) & (abs(toadd[-1])>prec*2):
        toadd.append(2.*(-1.)**(j-1.)*np.exp(-2.*j**2.*alam**2.))
        qks+=toadd[-1]
        j+=1
    if (j==iter) | (qks>1): #  If no convergence after the j iterations, return 1.0.
        return(1.0)
    if qks<prec:    
        return(0.)
    else:
        return(qks)
        
def ks2d2s(Arr2D1,Arr2D2,silent=1):
    # ks2d2s: ks stands for Kolmogorov-smirnov, 2dfor  2 dimensional, 2s for 2 samples.
    # Executes the KS test for goodness-of-fit on two samples in a 2D plane: tests if the hypothesis that the two samples are from the same distribution can be rejected.
    if type(Arr2D1).__module__+type(Arr2D1).__name__=='numpyndarray':
        if not silent: print('Arr2D1 is a ndarray')
    else:
        if not silent: print('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D1.shape[1]>Arr2D1.shape[0]:
        Arr2D1=Arr2D1.copy().T
        
    if type(Arr2D2).__module__+type(Arr2D2).__name__=='numpyndarray':
        if not silent: print('Arr2D1 is a ndarray')
    else:
        if not silent: print('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D2.shape[1]>Arr2D2.shape[0]:
        Arr2D2=Arr2D2.copy().T   
    if Arr2D1.shape[1]!=2:
        if not silent: print('2 columns should be in Arr2D1. Exiting.')
        return
    if Arr2D2.shape[1]!=2:
        if not silent: print('2 columns should be in Arr2D2. Exiting.')
        return
    d1,d2=0.,0.
    for point1 in Arr2D1:
        fpp1,fmp1,fpm1,fmm1=CountQuads(Arr2D1,point1)
        fpp2,fmp2,fpm2,fmm2=CountQuads(Arr2D2,point1)
        d1=max(d1,abs(fpp1-fpp2))
        d1=max(d1,abs(fpm1-fpm2))
        d1=max(d1,abs(fmp1-fmp2))
        d1=max(d1,abs(fmm1-fmm2))
    for point2 in Arr2D2:
        fpp1,fmp1,fpm1,fmm1=CountQuads(Arr2D1,point2)
        fpp2,fmp2,fpm2,fmm2=CountQuads(Arr2D2,point2)
        d2=max(d2,abs(fpp1-fpp2))
        d2=max(d2,abs(fpm1-fpm2))
        d2=max(d2,abs(fmp1-fmp2))
        d2=max(d2,abs(fmm1-fmm2))
    d=(d1+d2)/2.
    sqen=np.sqrt(len(Arr2D1)*len(Arr2D2)/(len(Arr2D1)+len(Arr2D2)))
    R1=scipy.stats.pearsonr(Arr2D1[:,0],Arr2D1[:,1])[0]
    R2=scipy.stats.pearsonr(Arr2D2[:,0],Arr2D2[:,1])[0]
    RR=np.sqrt(1.-(R1*R1+R2*R2)/2.)
    prob=Qks(d*sqen/(1.+RR*(0.25-0.75/sqen)))
    # d and prob significance: if d is lowe than you significance level, cannot reject the hypothesis that the 2 datasets come form the same functions. Higher prob is better. From numerical recipes in C: When the indicated probability is > 0.20, its value may not be accurate, but the implication that the data and model (or two data sets) are not significantly different is certainly correct.
    return(d,prob)
    
