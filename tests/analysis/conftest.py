"""Continuous-time process tests."""
# flake8: noqa
import numpy as np
import pytest
    
# ks2d
points=np.array([[*np.arange(6),*np.arange(6),*np.arange(6),*np.arange(6),*np.arange(6),*np.arange(6)],[*([1]*6),*([2]*6),*([3]*6),*([4]*6),*([5]*6),*([6]*6)]])
@pytest.fixture(params=[points])
def points2d(request):
    return request.param

@pytest.fixture(params=[lambda x,y:x+y])
def distfunc2d(request):
    return request.param
    
dim=500
side=np.linspace(0,6,dim)
x,y = np.meshgrid(side,side)
z=6.*x-y**2.
    
@pytest.fixture(params=[z])
def distarr2d(request):
    return request.param