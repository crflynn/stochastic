import numpy as np
import pytest

from stochastic import random

# def test_random_default():
#     assert isinstance(random.generator, np.random.Generator)


def test_random_use_randomstate():
    random.use_generator()
    assert isinstance(random.generator, np.random.Generator)
    random.use_randomstate()
    assert random.generator == np.random
    with pytest.raises(TypeError):
        random.use_randomstate("something")
    random.use_generator()
    assert isinstance(random.generator, np.random.Generator)


def test_random_use_generator():
    random.use_randomstate()
    assert random.generator == np.random
    random.use_generator()
    assert isinstance(random.generator, np.random.Generator)
    with pytest.raises(TypeError):
        random.use_generator("something")


def test_random_seed():
    random.use_randomstate()
    random.seed(42)
    before = np.random.uniform()
    random.seed(42)
    after = np.random.uniform()
    assert before == after

    random.use_generator()
    random.seed(42)
    before = random.generator.uniform()
    random.seed(42)
    after = random.generator.uniform()
    assert before == after
