# Code créé par Gabriel Taillon le 7 Mai 2018
#  Test bench for the 2D Kolmogorov-Smyrnov Test.
import unittest
import sys
import os
import numpy as np
import scipy.stats
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
testArr3D=np.random.uniform(size=(100,3))
testArr1D=np.random.uniform(size=(100,1))
def f2d3arg(x,y,k): return(x**2+y)
def f2d2arg(x,y): return(x**2+y)
def f2d1arg(x): return(x**2)
def f2d1(x,y): return(x+y)
def f2d2(x,y): return(x**2)
def f2d3(x,y): return(y**2)
def f2d4(x,y): return(y)
def f2d5(x,y): return(x)
class TestKS2D(unittest.TestCase):
    def test_FuncQuads_funcargs(self):
        self.assertIsNone(KS2D.FuncQuads(f2d3arg,[0.1,0.1],[0,1],[0,1]))
        self.assertIsNone(KS2D.FuncQuads(f2d1arg,[0.1,0.1],[0,1],[0,1]))
        self.assertEqual(sum(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[0,1],[0,1])),1.0)
    def test_FuncQuads_limargs(self):
        self.assertEqual(sum(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[1,0],[0,1])),1.0)
        self.assertEqual(sum(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[0,1],[1,0])),1.0)
        self.assertIsNone(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[1,0],[1,1]))
        self.assertIsNone(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[1,1],[1,0]))
        self.assertIsNone(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[1,0,1],[1,0]))
        self.assertIsNone(KS2D.FuncQuads(f2d2arg,[0.1,0.1],[1,0],[1,0,1]))
    def test_FuncQuads_manyfuncs(self):
        self.assertEqual(sum(KS2D.FuncQuads(f2d1,[0.5,0.1],[0,1],[1,0])),1.0)
        self.assertEqual(round(sum(KS2D.FuncQuads(f2d2,[0.5,0.1],[0,1],[1,0])),4),1.0)
        # This test consistently presents floating point error with 0,9999999... Rounding seems to solve most problems.
        self.assertEqual(sum(KS2D.FuncQuads(f2d3,[0.5,0.1],[0,1],[1,0])),1.0)
        self.assertEqual(sum(KS2D.FuncQuads(f2d4,[0.5,0.1],[0,1],[1,0])),1.0)
        self.assertEqual(sum(KS2D.FuncQuads(f2d5,[0.5,0.1],[0,1],[1,0])),1.0)
    def test_CountQuads_ArrList(self):
        self.assertEqual(sum(KS2D.CountQuads(testdata1,[0.1,0.5])),1.0)
    def test_CountQuads_ArrWrongDim(self):
        self.assertIsNone(KS2D.CountQuads(testArr1D,[0.1,0.5]))
        self.assertIsNone(KS2D.CountQuads(testArr1D.T,[0.1,0.5]))
        self.assertIsNone(KS2D.CountQuads(testArr3D,[0.1,0.5]))
        self.assertIsNone(KS2D.CountQuads(testArr3D.T,[0.1,0.5]))
    def test_CountQuads_PointWrongDim(self):
        self.assertIsNone(KS2D.CountQuads(testdata1,[0.1,0.1,0.5]))
        self.assertIsNone(KS2D.CountQuads(testdata1,[0.5]))
        self.assertIsNone(KS2D.CountQuads(testdata1,[0.5,1,1,1,1,1,1,1,1,1,1]))
        # self.assertIsNone(KS2D.CountQuads(testdata1,[[0.1],[1,1,1]]))  # lists of lists that have different lengths
    def test_CountQuads_ArrArr(self):
        self.assertEqual(sum(KS2D.CountQuads(testdata1,np.asarray([0.5,0.1]))),1.0)
    def test_CountQuads_ListArr(self):
        self.assertEqual(sum(KS2D.CountQuads(testlist1,np.asarray([0.9,0.9]))),1.0)
    def test_CountQuads_ListList(self):
        self.assertEqual(sum(KS2D.CountQuads(testlist1,[0.1,0.01])),1.0)
    def test_CountQuads_StrArr(self):
        self.assertIsNone(KS2D.CountQuads('arr',[0.1,0.01]))
    def test_CountQuads_ArrStr(self):
        self.assertIsNone(KS2D.CountQuads(testdata1,'arr'))
    def test_CountQuads_Arrfunc(self):
        self.assertIsNone(KS2D.CountQuads(testdata1,KS2D.ks2d2s))
    def test_CountQuads_funcArr(self):
        self.assertIsNone(KS2D.CountQuads(KS2D.ks2d2s,np.asarray([0.9,0.4])))
    def test_Qks_Edge0(self):
        self.assertEqual(KS2D.Qks(0.),1.0)
        self.assertEqual(KS2D.Qks(0.01),1.0)
        self.assertEqual(KS2D.Qks(0.0001),1.0)
        self.assertEqual(KS2D.Qks(0.000001),1.0)
    def test_Qks_EdgeInf(self):
        self.assertEqual(KS2D.Qks(10),0.)
        self.assertEqual(KS2D.Qks(10.),0.)
        self.assertEqual(KS2D.Qks(100.),0.)
        self.assertEqual(KS2D.Qks(100000),0.)
    def test_Qks_ManyValues(self):
        self.assertTrue(1>=KS2D.Qks(0.01)>=0)
        self.assertTrue(1>=KS2D.Qks(0.1)>=0)
        self.assertTrue(1>=KS2D.Qks(0.2)>=0)
        self.assertTrue(1>=KS2D.Qks(0.4)>=0)
        self.assertTrue(1>=KS2D.Qks(0.8)>=0)
        self.assertTrue(1>=KS2D.Qks(2)>=0)
    def test_Qks_str(self):
        self.assertIsNone(KS2D.Qks('a'))
        self.assertIsNone(KS2D.Qks([1,0]))
        self.assertIsNone(KS2D.Qks(np.asarray([1,0])))
    def test_ks2d2s_ArgSize(self):
        self.assertIsNone(KS2D.ks2d2s(testdata1,testArr3D))
        self.assertIsNone(KS2D.ks2d2s(testdata1,testArr1D))
        self.assertIsNone(KS2D.ks2d2s(testdata1,testlist1))
        self.assertIsNone(KS2D.ks2d2s(testArr3D,testdata1))
        self.assertIsNone(KS2D.ks2d2s(testArr1D,testdata1))
        self.assertIsNone(KS2D.ks2d2s(testlist1,testdata1))
    def test_ks2d2s_ArgSize(self):
        self.assertIsNone(KS2D.ks2d2s(testdata1,'a'))
        self.assertIsNone(KS2D.ks2d2s('a',testdata1))
        self.assertIsNone(KS2D.ks2d2s(testdata1,1))
        self.assertIsNone(KS2D.ks2d2s(1,testdata1))

if __name__=='__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)