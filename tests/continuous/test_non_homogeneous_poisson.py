"""Test NonHomogeneousPoissonProcess."""
# flake8: noqa
import pytest

from stochastic.continuous import NonHomogeneousPoissonProcess

def test_non_homogeneous_poisson_process_str_repr(
        lambda_func1D, lambda_arr1D, boundaries1D, 
        lambda_func2D, lambda_arr2D, boundaries2D, 
        lambda_func3D, lambda_arr3D, boundaries3D):
    instance_func1D = NonHomogeneousPoissonProcess(lambda_func1D,boundaries1D)
    instance_func2D = NonHomogeneousPoissonProcess(lambda_func2D,boundaries2D)
    instance_func3D = NonHomogeneousPoissonProcess(lambda_func3D,boundaries3D)
    instance_arr1D = NonHomogeneousPoissonProcess(lambda_arr1D,boundaries1D)
    instance_arr2D = NonHomogeneousPoissonProcess(lambda_arr2D,boundaries2D)
    instance_arr3D = NonHomogeneousPoissonProcess(lambda_arr3D,boundaries3D)
    instances=(instance_func1D, instance_func2D, instance_func3D,
        instance_arr1D, instance_arr2D, instance_arr3D)
    for instance in instances:
        assert isinstance(repr(instance), str)
        assert isinstance(str(instance), str)

def test_non_homogeneous_poisson_process_sample(
        lambda_func1D, lambda_arr1D, boundaries1D, 
        lambda_func2D, lambda_arr2D, boundaries2D, 
        lambda_func3D, lambda_arr3D, boundaries3D,
        n_fixture):
    instance_func1D = NonHomogeneousPoissonProcess(lambda_func1D,boundaries1D)
    instance_func2D = NonHomogeneousPoissonProcess(lambda_func2D,boundaries2D)
    instance_func3D = NonHomogeneousPoissonProcess(lambda_func3D,boundaries3D)
    instance_arr1D = NonHomogeneousPoissonProcess(lambda_arr1D,boundaries1D)
    instance_arr2D = NonHomogeneousPoissonProcess(lambda_arr2D,boundaries2D)
    instance_arr3D = NonHomogeneousPoissonProcess(lambda_arr3D,boundaries3D)
    instances=(instance_func1D, instance_func2D, instance_func3D,
        instance_arr1D, instance_arr2D, instance_arr3D)
    for instance in instances:
        if n_fixture is None:
            with pytest.raises(ValueError):
                s = instance.sample(n_fixture)
        else:  # n_fixture is not None:
            s = instance.sample(n_fixture)
            assert len(s) == n_fixture 
        
def test_non_homogeneous_poisson_process_times(
        lambda_func1D, lambda_arr1D, boundaries1D, 
        lambda_func2D, lambda_arr2D, boundaries2D, 
        lambda_func3D, lambda_arr3D, boundaries3D,
        n):
    instance_func1D = NonHomogeneousPoissonProcess(lambda_func1D,boundaries1D)
    instance_func2D = NonHomogeneousPoissonProcess(lambda_func2D,boundaries2D)
    instance_func3D = NonHomogeneousPoissonProcess(lambda_func3D,boundaries3D)
    instance_arr1D = NonHomogeneousPoissonProcess(lambda_arr1D,boundaries1D)
    instance_arr2D = NonHomogeneousPoissonProcess(lambda_arr2D,boundaries2D)
    instance_arr3D = NonHomogeneousPoissonProcess(lambda_arr3D,boundaries3D)
    instances=(instance_func1D, instance_func2D, instance_func3D,
        instance_arr1D, instance_arr2D, instance_arr3D)
    for instance in instances:
        with pytest.raises(AttributeError):
            times = instance.times(n)
