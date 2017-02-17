from unittest import TestCase
import numpy as np

from .. import Bernoulli, Poisson, RandomWalk, MarkovChain, Moran


class BernoulliTest(TestCase):

    def test_create_bernoulli(self):
        with self.assertRaises(ValueError):
            bernoulli = Bernoulli(p=-1)

        with self.assertRaises(ValueError):
            bernoulli = Bernoulli(p=1.1)

        with self.assertRaises(TypeError):
            bernoulli = Bernoulli(p='hi')

        with self.assertRaises(ValueError):
            bernoulli = Bernoulli(states=1)

        with self.assertRaises(ValueError):
            bernoulli = Bernoulli(states=[1, 2, 3])

    def test_sample_bernoulli(self):
        bernoulli = Bernoulli()

        with self.assertRaises(TypeError):
            bernoulli.sample(1.5)

        with self.assertRaises(ValueError):
            bernoulli.sample(0)

        np.random.seed(42)
        b = np.all(bernoulli.sample(10) ==
                   np.array([0, 1, 1, 1, 0, 0, 0, 1, 1, 1]))
        self.assertTrue(b)


class PoissonTest(TestCase):

    def test_create_poisson(self):
        with self.assertRaises(ValueError):
            poisson = Poisson(rate=-1)

        with self.assertRaises(TypeError):
            poisson = Poisson(rate='hi')

    def test_sample_poisson(self):
        poisson = Poisson()

        with self.assertRaises(TypeError):
            poisson.sample('hi', time=True)

        with self.assertRaises(ValueError):
            poisson.sample(-1, time=True)

        with self.assertRaises(TypeError):
            poisson.sample(1.0)

        with self.assertRaises(ValueError):
            poisson.sample(-1)

        with self.assertRaises(TypeError):
            poisson.sample(10, time='hi')

        np.random.seed(42)
        p = np.all(poisson.sample(10) ==
                   np.array([0, 0.46926808997685909, 3.4793895208943804,
                             4.7961352144398299, 5.7090777682157832,
                             5.8787026386781296, 6.0482989305927344,
                             6.1081376992014151, 8.1193685636813555,
                             9.0384507173086206, 10.269700779013212]))
        self.assertTrue(p)

        np.random.seed(42)
        p = np.all(poisson.sample(10, time=True) ==
                   np.array([0, 0.4692680899768591, 3.4793895208943804,
                             4.79613521443983, 5.709077768215783,
                             5.87870263867813, 6.048298930592734,
                             6.108137699201415, 8.119368563681356,
                             9.03845071730862]))
        self.assertTrue(p)


class RandomWalkTest(TestCase):

    def test_create_randomwalk(self):
        with self.assertRaises(ValueError):
            randomwalk = RandomWalk(steps=[-1, 1], p=[0])

        with self.assertRaises(TypeError):
            randomwalk = RandomWalk(steps=1)

        with self.assertRaises(ValueError):
            randomwalk = RandomWalk(steps=[-1, 1], p=[1, 2, 3])

        with self.assertRaises(TypeError):
            randomwalk = RandomWalk(steps=[-1, 1], p=[0, 'as'])

        with self.assertRaises(ValueError):
            randomwalk = RandomWalk(steps=[-1, 1], p=[-1, 2])

        with self.assertRaises(ValueError):
            randomwalk = RandomWalk(steps=[-1, 1], p=[0.25, 0.25])

    def test_sample_randomwalk(self):
        randomwalk = RandomWalk()

        with self.assertRaises(TypeError):
            randomwalk.sample(1.5)

        with self.assertRaises(ValueError):
            randomwalk.sample(-1)

        with self.assertRaises(TypeError):
            randomwalk.sample('hi')

        with self.assertRaises(TypeError):
            randomwalk.sample_increments(1.5)

        with self.assertRaises(ValueError):
            randomwalk.sample_increments(-1)

        with self.assertRaises(TypeError):
            randomwalk.sample_increments('hi')

        np.random.seed(42)
        p = np.all(randomwalk.sample(10) ==
                   np.array([0, -1, 0, 1, 2, 1, 0, -1, 0, 1, 2]))
        self.assertTrue(p)

        np.random.seed(42)
        p = np.all(randomwalk.sample_increments(10) ==
                   np.array([-1,  1,  1,  1, -1, -1, -1,  1,  1,  1]))
        self.assertTrue(p)


class MarkovChainTest(TestCase):

    def test_create_markovchain(self):
        with self.assertRaises(ValueError):
            markovchain = MarkovChain(transition=[0.5, 0.5])

        with self.assertRaises(ValueError):
            markovchain = MarkovChain(
                transition=[[0.5, 0.5, 0], [0.2, 0.2, 0.6]])

        with self.assertRaises(ValueError):
            markovchain = MarkovChain(transition=[[0.5, 0.5], [0.5, 0.4]])

        with self.assertRaises(ValueError):
            markovchain = MarkovChain(initial=[0.3, 0.3, 0.4])

        with self.assertRaises(ValueError):
            markovchain = MarkovChain(initial=[0.3, 0.5])

        with self.assertRaises(ValueError):
            markovchain = MarkovChain(states=[[1, 2], [3, 4]])

        with self.assertRaises(ValueError):
            markovchain = MarkovChain(states=[1, 2, 3])

    def test_sample_markovchain(self):
        markovchain = MarkovChain()

        with self.assertRaises(TypeError):
            markovchain.sample(1.5)

        with self.assertRaises(TypeError):
            markovchain.sample('hi')

        with self.assertRaises(ValueError):
            markovchain.sample(-1)

        np.random.seed(42)
        p = np.all(markovchain.sample(10) ==
                   np.array([0, 1, 1, 1, 0, 0, 0, 1, 1, 1]))
        self.assertTrue(p)


class MoranTest(TestCase):

    def test_create_moran(self):
        with self.assertRaises(TypeError):
            moran = Moran(1.4)

        with self.assertRaises(ValueError):
            moran = Moran(-5)

    def test_sample_moran(self):
        moran = Moran(20)

        with self.assertRaises(TypeError):
            moran.sample(5.6)

        with self.assertRaises(ValueError):
            moran.sample(-1)

        with self.assertRaises(TypeError):
            moran.sample(20, 5.5)

        with self.assertRaises(ValueError):
            moran.sample(20, 0)

        np.random.seed(42)
        p = np.all(moran.sample(10) ==
                   np.array([10, 10, 11, 11, 11, 10,  9,  8,  9,  9,
                            9,  8,  9, 10,  9,  8,  7,  7,  7,  7,
                            7,  7,  6,  6,  6,  6,  6,  5,  5,  5,
                            4,  4,  4,  3,  4,  5,  5,  5,  4,  4,
                            4,  3,  3,  2,  2,  2,  2,  2,  2,  2,
                            2,  3,  3,  4,  5,  5,  6,  5,  5,  4,
                            4,  4,  4,  4,  4,  4,  4,  3,  3,  2,
                            3,  3,  3,  2,  2,  2,  2,  2,  1,  1,
                            1,  1,  1,  1,  1,  1,  1,  1,  1,  1,
                            1,  1,  1,  1,  1,  1,  1,  1,  1,  0]))
        self.assertTrue(p)
