# Code créé par Gabriel Taillon le 7 Mai 2018
#  Test bench for the 2D Kolmogorov-Smyrnov Test.
import sys, os, numpy as np, scipy.stats
import KS2D

Scriptpath=os.path.dirname(os.path.abspath(__file__)) # Path of this script
Path2Res=os.path.join(Scriptpath,os.path.splitext(os.path.basename(__file__))[0])
if not os.path.exists(Path2Res): os.makedirs(Path2Res)

 
# Making phony data: 
testdata1=np.random.uniform(size=(100,2))
testdata2=np.random.uniform(size=(100,2))
testdata3=np.random.uniform(0.2,0.5,size=(100,2))
testlist1=np.random.uniform(size=(100,2)).tolist()
testlist2=np.random.uniform(size=(100,2)).T.tolist()    
    
# Test list:
print(KS2D.CountQuads(testdata1,[0.1,0.5],silent=1))

print(KS2D.CountQuads(testdata1,'a',silent=0))
print(KS2D.CountQuads('1',[0.1,0.5],silent=0)) 
print(KS2D.CountQuads(testlist1,[0.1,0.5],silent=0)) 
print(KS2D.CountQuads(testlist2,[0.1,0.5],silent=0)) 
# Test ndarray
print(KS2D.CountQuads(testdata1,np.array([0.1,0.5]),silent=0)) 
print(KS2D.CountQuads(testdata1.T,np.array([[0.1],[0.5]]),silent=0))
# Test Qks
print(KS2D.Qks(0))
print(KS2D.Qks(0.01))
print(KS2D.Qks(0.1))
print(KS2D.Qks(.5))
# Test the actual algo.
print(KS2D.ks2d2s(testdata1,testdata2))
print(KS2D.ks2d2s(testdata1,testdata3))