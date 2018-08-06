# Code créé par Gabriel Taillon le 7 Mai 2018
#  Kolmogorov-Smyrnov Test extended to two dimensions.
# References:s#  [1] Peacock, J. A. (1983). Two-dimensional goodness-of-fit testing
#  in astronomy. Monthly Notices of the Royal Astronomical Society,
#  202(3), 615-627.
#  [2] Fasano, G., & Franceschini, A. (1987). A multidimensional version of
#  the Kolmogorov–Smirnov test. Monthly Notices of the Royal Astronomical
#  Society, 225(1), 155-170.
#  [3] Flannery, B. P., Press, W. H., Teukolsky, S. A., & Vetterling, W.
#  (1992). Numerical recipes in C. Press Syndicate of the University
#  of Cambridge, New York, 24, 78.
import sys, os, inspect, logging # standard library.
import numpy as np, scipy.stats # Non standard packages.

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
datefmt='%Y/%m/%d %H:%M:%S', filename='example.log', level=logging.DEBUG)

def CountQuads(Arr2D, point):
    """ Computes the probabilities of finding points in each 4 quadrant
	defined by a vertical and horizontal lines crossing the point, by counting
	the proportion of points in Arr2D in each quadrant.

	:param list Arr2D: Array of points to be counted.
	:param array point: A 2 element list, point, which is the center of 
	4 square quadrants.
	:returns: a tuple of 4 floats.  The probabilities of finding a point in
	each quadrants, with point as the origin.  p stands for positive, n for
	negative, with the first and second positions meaning the x and y
	directions respectively.
	"""
    logging.info('CountQuads function. Counts points in quadrants that surround a point using with an array of 2D points.')
    # A bit of checking. If Arr2D and point are not lists or ndarray, exit.
    if isinstance(point, list):
        logging.info('point is a list')
        point = np.asarray((np.ravel(point)))
    elif type(point).__module__+type(point).__name__ == 'numpyndarray':
        point = np.ravel(point.copy())
        logging.info('point is a numpy.ndarray')
    else:
        logging.error('point is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(point) != 2:
        logging.error('2 elements should be in point. Exiting.')
        return
    if isinstance(Arr2D, list):
        logging.info('Arr2D is a list')
        Arr2D = np.asarray((Arr2D))
    elif type(Arr2D).__module__+type(Arr2D).__name__ == 'numpyndarray':
        logging.info('Arr2D is a ndarray')
    else:
        logging.error('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D.shape[1] > Arr2D.shape[0]: # Reshape to A[row,column]
        Arr2D = Arr2D.copy().T
    if Arr2D.shape[1] != 2:
        logging.error('2 columns should be in Arr2D. Exiting.')
        return
    # The pp of Qpp refer to p for 'positive' and n for 'negative' quadrants. In order. first subscript is x, second is y.
    Qpp = Arr2D[(Arr2D[:, 0] > point[0]) & (Arr2D[:, 1] > point[1]), :]
    Qnp = Arr2D[(Arr2D[:, 0] < point[0]) & (Arr2D[:, 1] > point[1]), :]
    Qpn = Arr2D[(Arr2D[:, 0] > point[0]) & (Arr2D[:, 1] < point[1]), :]
    Qnn = Arr2D[(Arr2D[:, 0] < point[0]) & (Arr2D[:, 1] < point[1]), :]
    logging.info('Same number of points in Arr2D as in all Quadrants: '+str((len(Qpp)+len(Qnp)+len(Qpn)+len(Qnn)) == len(Arr2D)))
    logging.debug('Number of points in each quadrant: Qpp='+str(len(Qpp))+'Qnp='+str(len(Qnp))+'Qpn='+str(len(Qpn))+'Qnn='+str(len(Qnn)))
    # Normalized fractions:
    ff = 1./len(Arr2D)
    fpp = len(Qpp)*ff
    fnp = len(Qnp)*ff
    fpn = len(Qpn)*ff
    fnn = len(Qnn)*ff
    logging.debug('Probabilities of finding points in each quadrant: fpp='+str(fpp)+'fnp='+str(fnp)+'fpn='+str(fpn)+'fnn='+str(fnn))
    logging.debug('Total probability, which should be equal to one:'+str(fpp+fnp+fpn+fnn))
    # NOTE:  all the f's are supposed to sum to 1.0. Float representation cause SOMETIMES sum to 1.000000002 or something. I don't know how to test for that reliably, OR what to do about it yet. Keep in mind.
    logging.debug('CountQuads: exiting')
    return(fpp, fnp, fpn, fnn)
    
def FuncQuads(func2D, point, xlim, ylim, rounddig=4):
    """ Computes the probabilities of finding points in each 4 quadrant defined by a vertical and horizontal lines crossing the point, by integrating the density function func2D in each quadrant.
    
    :param array func2D: Density function that takes 2 arguments: x and y.
    :param list point: A 2 element list, point, which is the center of 4 square quadrants.
    :param array xlim,ylim: Domain of numerical integration necessary to compute the quadrant probabilities.
    :returns: a tuple of 4 floats. The probabilities of finding a point in each quadrants, with point as the origin.  p stands for positive, n for negative, with the first and second positions meaning the x and y directions respectively.
    """
    logging.info('FuncQuads function. Computes the probability of finding points in quadrants around a point using a 2D density function.')
    # If func2D is not a function with 2 arguments, exit.
    if callable(func2D):
        logging.info('func2D is a function')
        if len(inspect.getfullargspec(func2D)[0]) != 2:
            logging.error('func2D function has not 2 arguments. Exiting.')
            return
        pass
    else:
        logging.error('func2D is not a function. Exiting.')
        return
    # If xlim, ylim and point are not lists or ndarray, exit.
    if isinstance(point, list):
        logging.info('point is a list')
        point = np.asarray((np.ravel(point)))
    elif type(point).__module__+type(point).__name__ == 'numpyndarray':
        point = np.ravel(point.copy())
        logging.info('point is a numpy.ndarray')
    else:
        logging.error('point is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(point) != 2:
        logging.error('2 elements should be in point. Exiting.')
        return
    if isinstance(xlim, list):
        logging.info('xlim is a list')
        xlim = np.asarray((np.sort(np.ravel(xlim))))
    elif type(xlim).__module__+type(xlim).__name__ == 'numpyndarray':
        xlim = np.sort(np.ravel(xlim.copy()))
        logging.info('xlim is a numpy.ndarray')
    else:
        logging.info('xlim is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(xlim) != 2:
        logging.error('2 elements should be in xlim. Exiting.')
        return
    if xlim[0] == xlim[1]:
        logging.error('limits in xlim should not be the same. Exiting.')
        return
    if isinstance(ylim, list):
        logging.info('ylim is a list')
        ylim = np.asarray((np.sort(np.ravel(ylim))))
    elif type(ylim).__module__+type(ylim).__name__ == 'numpyndarray':
        ylim = np.sort(np.ravel(ylim.copy()))
        logging.info('ylim is a numpy.ndarray')
    else:
        logging.error('ylim is neither a list not a numpy.ndarray. Exiting.')
        return
    if len(ylim) != 2:
        logging.error('2 elements should be in ylim. Exiting.')
        return
    if ylim[0] == ylim[1]:
        logging.error('limits in ylim should not be the same. Exiting.')
        return
    # Numerical integration to find the quadrant probabilities.
    totInt = scipy.integrate.dblquad(func2D, *xlim, lambda x: np.amin(ylim),  lambda x: np.amax(ylim))[0]
    Qpp = scipy.integrate.dblquad(func2D, point[0], np.amax(xlim), lambda x: point[1],  lambda x: np.amax(ylim))[0]
    Qpn = scipy.integrate.dblquad(func2D, point[0], np.amax(xlim), lambda x: np.amin(ylim),  lambda x: point[1])[0]
    Qnp = scipy.integrate.dblquad(func2D, np.amin(xlim), point[0], lambda x: point[1],  lambda x: np.amax(ylim))[0]
    Qnn = scipy.integrate.dblquad(func2D, np.amin(xlim), point[0], lambda x: np.amin(ylim),  lambda x: point[1])[0]
    fpp = round(Qpp/totInt, rounddig)
    fnp = round(Qnp/totInt, rounddig)
    fpn = round(Qpn/totInt, rounddig)
    fnn = round(Qnn/totInt, rounddig)
    logging.info('Probabilities of finding points in each quadrant: fpp='+str(fpp)+' fnp='+str(fnp)+' fpn='+str(fpn)+' fnn='+str(fnn))
    logging.debug('Total probability, which should be equal to one: '+str(fpp+fnp+fpn+fnn))
    logging.debug('FuncQuads: exiting')
    return(fpp, fnp, fpn, fnn)

def Qks(alam, iter=100, prec=1e-6):
    """ Computes the value of the KS probability function, as a function of alam, the D statistic. From *Numerical recipes in C* page 623: '[...] the K–S statistic useful is that its distribution in the case of the null hypothesis (data sets drawn from the same distribution) can be calculated, at least to useful approximation, thus giving the significance of any observed nonzero value of D.' (D being the KS statistic).

    :param float alam: D statistic.
    :param int iter: Number of iterations to be perfomed. On non-convergence, returns 1.0.
    :param float prec: Convergence criteria of the qks. Stops converging if that precision is attained.
    :returns: a float. The significance level of the observed D statistic.
    """
    # If j iterations are performed, meaning that toadd is still 2 times larger than the precision.
    logging.info('Qks function. Value of the KS probability function using a float.')
    if isinstance(alam, int) | isinstance(alam, float):
        pass
    else:
        logging.error('alam is not an integer or float. Exiting.')
        return
    toadd = [1]
    qks = 0.
    j = 1
    while (j < iter) & (abs(toadd[-1]) > prec*2):
        toadd.append(2.*(-1.)**(j-1.)*np.exp(-2.*j**2.*alam**2.))
        qks += toadd[-1]
        j += 1
    if (j == iter) | (qks > 1): #  If no convergence after the j iterations, return 1.0.
        logging.info('No convergence. Returning 1.')
        return(1.0)
    if qks < prec:
        logging.info('Computed value lower than precision. returning 0.')
        return(0.)
    else:
        logging.info('Qks: Returning computed value qks= '+str(qks))
        return(qks)

def ks2d2s(Arr2D1, Arr2D2):
    """ ks stands for Kolmogorov-Smirnov, 2d for 2 dimensional, 2s for 2 samples.
    KS test for goodness-of-fit on two 2D samples. Tests the hypothesis that the two samples are from the same distribution.

    :param array Arr2D1: 2D array of points/samples.
    :param array Arr2D2: 2D array of points/samples.
    :returns: a tuple of two floats. First, the two-sample K-S statistic. If this value is higher than the significance level of the hypothesis, it is rejected. Second, the significance level of *d*. Small values of prob show that the two samples are significantly different.
    """
    logging.info('ks2d2s function: Computes the KS statistic on a 2D plane for two samples of points.')
    if type(Arr2D1).__module__+type(Arr2D1).__name__ == 'numpyndarray':
        logging.info('Arr2D1 is a ndarray')
    else:
        logging.error('Arr2D1 is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D1.shape[1] > Arr2D1.shape[0]:
        Arr2D1 = Arr2D1.copy().T
    if type(Arr2D2).__module__+type(Arr2D2).__name__ == 'numpyndarray':
        logging.info('Arr2D2 is a ndarray')
    else:
        logging.error('Arr2D2 is neither a list not a numpy.ndarray. Exiting.')
        return
    if Arr2D2.shape[1] > Arr2D2.shape[0]:
        Arr2D2 = Arr2D2.copy().T
    if Arr2D1.shape[1] != 2:
        logging.error('2 columns should be in Arr2D1. Exiting.')
        return
    if Arr2D2.shape[1] != 2:
        logging.error('2 columns should be in Arr2D2. Exiting.')
        return
    d1, d2 = 0., 0.
    for point1 in Arr2D1:
        fpp1, fmp1, fpm1, fmm1 = CountQuads(Arr2D1, point1)
        fpp2, fmp2, fpm2, fmm2 = CountQuads(Arr2D2, point1)
        d1 = max(d1, abs(fpp1-fpp2))
        d1 = max(d1, abs(fpm1-fpm2))
        d1 = max(d1, abs(fmp1-fmp2))
        d1 = max(d1, abs(fmm1-fmm2))
    for point2 in Arr2D2:
        fpp1, fmp1, fpm1, fmm1 = CountQuads(Arr2D1, point2)
        fpp2, fmp2, fpm2, fmm2 = CountQuads(Arr2D2, point2)
        d2 = max(d2, abs(fpp1-fpp2))
        d2 = max(d2, abs(fpm1-fpm2))
        d2 = max(d2, abs(fmp1-fmp2))
        d2 = max(d2, abs(fmm1-fmm2))
    d = (d1+d2)/2.
    logging.debug('d='+str(d))
    sqen = np.sqrt(len(Arr2D1)*len(Arr2D2)/(len(Arr2D1)+len(Arr2D2)))
    logging.debug('sqen='+str(sqen))
    R1 = scipy.stats.pearsonr(Arr2D1[:, 0], Arr2D1[:, 1])[0]
    logging.debug('R1='+str(R1))
    R2 = scipy.stats.pearsonr(Arr2D2[:, 0], Arr2D2[:, 1])[0]
    logging.debug('R2='+str(R2))
    RR = np.sqrt(1.-(R1*R1+R2*R2)/2.)
    logging.debug('RR='+str(RR))
    prob = Qks(d*sqen/(1.+RR*(0.25-0.75/sqen)))
    # Small values of prob show that the two samples are significantly different. Prob is the significance level of an observed value of d. NOT the same as the significance level that ou set and compare to D.
    logging.debug(' ks2d2s, exiting: Output=d, prob= '+str(d)+', '+str(prob))
    return(d, prob)

def ks2d1s(Arr2D, func2D, xlim=[], ylim=[]):
    """ ks stands for Kolmogorov-Smirnov, 2d for 2 dimensional, 1s for 1 sample.
    KS test for goodness-of-fit on one 2D sample and one 2D density distribution. Tests the hypothesis that the data was generated from the density distribution.

    :param array Arr2D: 2D array of points/samples.
    :param func2D: Density distribution. Could implement a function for arrays in the future...
    :param array xlim, ylim: Defines the domain for the numerical integration necessary to compute the quadrant probabilities.
    :returns: tuple of two floats. First, the two-sample K-S statistic. If this value is higher than the significance level of the hypothesis, it is rejected. Second, the significance level of *d*. Small values of prob show that the two samples are significantly different.
    """
    logging.info('ks2d1s function: Computes the KS statistic on a 2D plane for one sample and one density function.')
    if callable(func2D):
        logging.info('func2D is a function')
        if len(inspect.getfullargspec(func2D)[0]) != 2:
            logging.error('func2D function has not 2 arguments. Exiting.')
            return
        pass
    else:
        logging.error('func2D is not a function. Exiting.')
        return
    if type(Arr2D).__module__+type(Arr2D).__name__ == 'numpyndarray':
        logging.info('Arr2D is a ndarray')
    else:
        logging.error('Arr2D is neither a list not a numpy.ndarray. Exiting.')
        return
    print(Arr2D.shape)
    if Arr2D.shape[1] > Arr2D.shape[0]:
        Arr2D = Arr2D.copy().T
    if Arr2D.shape[1] != 2:
        logging.error('2 columns should be in Arr2D1. Exiting.')
        return
    if xlim == []:
        logging.debug('No xlim given. Computing xlim using given data.')
        xlim.append(np.amin(Arr2D[:, 0])-abs(np.amin(Arr2D[:, 0])-np.amax(Arr2D[:, 0]))/10)
        xlim.append(np.amax(Arr2D[:, 0])-abs(np.amin(Arr2D[:, 0])-np.amax(Arr2D[:, 0]))/10)
        logging.debug('Computed xlim: '+str(xlim))
    if ylim == []:
        logging.debug('No ylim given. Computing ylim using given data.')
        ylim.append(np.amin(Arr2D[:, 1])-abs(np.amin(Arr2D[:, 1])-np.amax(Arr2D[:, 1]))/10)
      
	ylim.append(np.amax(Arr2D[:, 1])-abs(np.amin(Arr2D[:, 1])-np.amax(Arr2D[:, 1]))/10)
        logging.debug('Computed ylim: '+str(ylim))
    d=0
    for point in Arr2D:
        fpp1, fmp1, fpm1, fmm1 = FuncQuads(func2D, point, xlim, ylim)
        fpp2, fmp2, fpm2, fmm2 = CountQuads(Arr2D, point)
        d = max(d, abs(fpp1-fpp2))
        d = max(d, abs(fpm1-fpm2))
        d = max(d, abs(fmp1-fmp2))
        d = max(d, abs(fmm1-fmm2))
    sqen = np.sqrt(len(Arr2D))
    logging.debug('sqen= '+str(sqen))
    R1 = scipy.stats.pearsonr(Arr2D[:, 0], Arr2D[:, 1])[0]
    logging.debug('R1= '+str(R1))
    RR = np.sqrt(1.0-R1**2)
    logging.debug('RR= '+str(RR))
    prob = Qks(d*sqen/(1.+RR*(0.25-0.75/sqen)))
    logging.debug(' ks2d2s, exiting: Output=d, prob= '+str(d)+', '+str(prob))
    print(d)
    return d, prob
