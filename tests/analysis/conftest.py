"""Continuous-time process tests."""
# flake8: noqa
import numpy as np
import pytest


# NHPPLeemisEst
@pytest.fixture(params=[np.array([[0,1,2,3,4,5,6],[0,0.5,0.75,0,0,0,0],[0,10,20,50,100,0,0]]).T])
def AllReal2D(request):
    return request.param
    
# ks2d
@pytest.fixture(params=[np.array([[*np.arange(6),*np.arange(6),*np.arange(6),*np.arange(6),*np.arange(6),*np.arange(6)],[*([1]*6),*([2]*6),*([3]*6),*([4]*6),*([5]*6),*([6]*6)]])])
def points2d(request):
    return request.param
func=lambda x,y:x+y
@pytest.fixture(params=[func])
def distfunc2d(request):
    return request.param
    
dim=500
side=np.linspace(0,6,dim)
x,y = np.meshgrid(side,side)
z=6.*x-y**2.
    
@pytest.fixture(params=[z])
def distarr2d(request):
    return request.param