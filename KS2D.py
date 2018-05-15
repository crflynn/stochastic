# Code créé par Gabriel Taillon le 7 Mai 2018
#  2D Kolmogorov-Smyrnov Test.
# References: #  [1] Peacock, J. A. (1983). Two-dimensional goodness-of-fit testing in astronomy. Monthly Notices of the Royal Astronomical Society, 202(3), 615-627.
#  [2] Fasano, G., & Franceschini, A. (1987). A multidimensional version of the Kolmogorov–Smirnov test. Monthly Notices of the Royal Astronomical Society, 225(1), 155-170.
#  [3]  Flannery, B. P., Press, W. H., Teukolsky, S. A., & Vetterling, W. (1992). Numerical recipes in C. Press Syndicate of the University of Cambridge, New York, 24, 78.
import sys, os, inspect, logging
import numpy as np, scipy.stats
import matplotlib.pyplot as plt

def CountQuads(Arr2D,point):
    # Counts the number of points of Arr2D in each 4 quadrant defined by a vertical and horizontal line crossing the point.
    # Then computes the proportion of points in each quadrant.
    
    # A bit of checking. If Arr2D and point are not lists or ndarray, exit.
    if isinstance(point, list):
        logging.info('point is a list')
        point=np.asarray((np.ravel(point)))
        pass
    elif type(point).__module__+type(point).__name__=='numpyndarray':
        point=np.ravel(point.copy())
        logging.info('point is a numpy.ndarray')
    else:
        logging.error('point is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(point)!=2:
        logging.error('2 elements should be in point. Exiting.')
        return
    if isinstance(Arr2D, list):
        logging.info('Arr2D is a list')
        Arr2D=np.asarray((Arr2D))
    elif type(Arr2D).__module__+type(Arr2D).__name__=='numpyndarray':
        logging.info('Arr2D is a ndarray')
    else:
        logging.error('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D.shape[1]>Arr2D.shape[0]: # Reshape so that A[row,column] is achieved.
        Arr2D=Arr2D.copy().T
    if Arr2D.shape[1]!=2: 
        logging.error('2 columns should be in Arr2D. Exiting.')
        return
    # The pp of Qpp refer to p for 'positive' and n for 'negative' quadrants. In order. first subscript is x, second is y.
    Qpp=Arr2D[(Arr2D[:,0]>=point[0])&(Arr2D[:,1]>=point[1]),:]
    Qnp=Arr2D[(Arr2D[:,0]<=point[0])&(Arr2D[:,1]>=point[1]),:]
    Qpn=Arr2D[(Arr2D[:,0]>=point[0])&(Arr2D[:,1]<=point[1]),:]
    Qnn=Arr2D[(Arr2D[:,0]<=point[0])&(Arr2D[:,1]<=point[1]),:]
    logging.info('Same number of points in Arr2D as in all Quadrants: '+str((len(Qpp)+len(Qnp)+len(Qpn)+len(Qnn))==len(Arr2D)))
    logging.info('Number of points in each quadrant: Qpp='+str(Qpp)+'Qnp='+str(Qnp)+'Qpn='+str(Qpn)+'Qnn='+str(Qnn))
    # Normalized fractions:
    ff=1./len(Arr2D)
    fpp=len(Qpp)*ff
    fnp=len(Qnp)*ff
    fpn=len(Qpn)*ff
    fnn=len(Qnn)*ff
    logging.info('Probabilities of finding points in each quadrant: fpp='+str(fpp)+'fnp='+str(fnp)+'fpn='+str(fpn)+'fnn='+str(fnn))
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
        xlim=np.asarray((np.sort(np.ravel(xlim))))
        pass
    elif type(xlim).__module__+type(xlim).__name__=='numpyndarray':
        xlim=np.sort(np.ravel(xlim.copy()))
        if not silent: print('xlim is a numpy.ndarray')
    else:
        if not silent: print('xlim is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(xlim)!=2:
        if not silent: print('2 elements should be in xlim. Exiting.')
        return
    if xlim[0]==xlim[1]:
        if not silent: print('limits in xlim should not be the same. Exiting.')
        return
    if isinstance(ylim, list):
        if not silent: print('ylim is a list')
        ylim=np.asarray((np.sort(np.ravel(ylim))))
        pass
    elif type(ylim).__module__+type(ylim).__name__=='numpyndarray':
        ylim=np.sort(np.ravel(ylim.copy()))
        if not silent: print('ylim is a numpy.ndarray')
    else:
        if not silent: print('ylim is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(ylim)!=2:
        if not silent: print('2 elements should be in ylim. Exiting.')
        return
    if ylim[0]==ylim[1]:
        if not silent: print('limits in ylim should not be the same. Exiting.')
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
        if not silent: print('Arr2D1 is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D1.shape[1]>Arr2D1.shape[0]:
        Arr2D1=Arr2D1.copy().T
        
    if type(Arr2D2).__module__+type(Arr2D2).__name__=='numpyndarray':
        if not silent: print('Arr2D2 is a ndarray')
    else:
        if not silent: print('Arr2D2 is neither a list not a numpy.ndarray. Exiting.')
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
    # d and prob :two-sample K-S statistic as d, and its significance level as prob Small values of prob show that the two samples are significantly different
    return(d,prob)
    
def ks2d1s(Arr2D,func2D,xlim=[],ylim=[],silent=1):
    # ks2d1s: ks stands for Kolmogorov-smirnov, 2dfor  2 dimensional, 1s for 1 samples, compared to a function.
    # Executes the KS test for goodness-of-fit on one samples in a 2D plane: tests if the hypothesis that the sample is from the given distribution can be rejected.
    if callable(func2D):
        if not silent:print('func2D is a function')
        if len(inspect.getfullargspec(func2D)[0])!=2:
            if not silent:print('func2D function has not 2 arguments. Exiting.')
            return
        pass
    else:
        if not silent:print('func2D is not a function. Exiting.')
        return  
    if type(Arr2D).__module__+type(Arr2D).__name__=='numpyndarray':
        if not silent: print('Arr2D is a ndarray')
    else:
        if not silent: print('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D.shape[1]>Arr2D.shape[0]:
        Arr2D=Arr2D.copy().T   
    if Arr2D.shape[1]!=2:
        if not silent: print('2 columns should be in Arr2D1. Exiting.')
        return
    if xlim==[]:
        xlim.append(np.amin(Arr2D[:,0]))
        xlim.append(np.amax(Arr2D[:,0]))
        xlim[0]=xlim[0]-(abs(xlim[1]-xlim[0]))/10
        xlim[1]=xlim[1]+(abs(xlim[1]-xlim[0]))/10
    if ylim==[]:
        ylim.append(np.amin(Arr2D[:,1]))
        ylim.append(np.amax(Arr2D[:,1]))
        ylim[0]=ylim[0]-(abs(ylim[1]-ylim[0]))/10
        ylim[1]=ylim[1]+(abs(ylim[1]-ylim[0]))/10
    d=0
    for point in Arr2D:
        fpp1,fmp1,fpm1,fmm1=FuncQuads(func2D,point,xlim,ylim)
        fpp2,fmp2,fpm2,fmm2=CountQuads(Arr2D,point)
        d=max(d,abs(fpp1-fpp2))
        d=max(d,abs(fpm1-fpm2))
        d=max(d,abs(fmp1-fmp2))
        d=max(d,abs(fmm1-fmm2))
    sqen=np.sqrt(len(Arr2D))
    R1=scipy.stats.pearsonr(Arr2D[:,0],Arr2D[:,1])[0]
    RR=np.sqrt(1.0-R1**2)
    prob=Qks(d*sqen/(1.+RR*(0.25-0.75/sqen)))
    return(d,prob)
# while len(Thinned)<Samples:
def MultiVarNHPPThinSamples(lambdaa,Intervals,Samples=100,blocksize=1000,silent=0): 
    # Utility function: genreate spatial data by thinning. Intervals is a np array of 2 lenght lists. lambdaa is a function or 2d matrix.Iterate over blocksize uniformlly generated points until Samples number of samples are created.
    if not silent: print('NHPP samples in space by thinning. lambda can be a 2D matrix or function')
    # This algorithm acts as if events do not happen outside the Intervals.
    if callable(lambdaa):
        boundstuple=[]
        for i in Intervals: boundstuple+=(tuple(i),)
        max = scipy.optimize.minimize(lambda x: -lambdaa(*x),x0=[np.mean(i) for i in Intervals],bounds = boundstuple)
        lmax=lambdaa(*max.x)
    else:
        lmax=np.amax(lambdaa)
    Thinned=[]
    while len(Thinned)<Samples:
        for i in Intervals:
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
def f2d2arg(x,y): return(x*y)
testdata1=np.random.uniform(size=(100,2))
dim=500
sidex=np.linspace(0,2,dim)
sidey=np.linspace(0,1,dim)
x,y = np.meshgrid(sidex,sidey)
thin=MultiVarNHPPThinSamples(f2d2arg,np.array([[0,2],[0,1]]),1000)
print(ks2d1s(thin,f2d2arg,xlim=[0,2],ylim=[0,1]))
print(ks2d2s(thin,testdata1))
plt.contourf(x,y,f2d2arg(x,y))
plt.plot(thin[:,0],thin[:,1],'.b')
plt.show()
sys.exit()  

testdata2=np.random.uniform(size=(100,2))
def f2d2arg(x,y): return(x+y)    
print(ks2d1s(testdata2,f2d2arg,silent=0))




    
