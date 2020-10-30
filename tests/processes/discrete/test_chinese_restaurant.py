"""Chinese restaurant tests."""
import pytest

from stochastic.processes.discrete import ChineseRestaurantProcess


def test_chinese_restaurant_str_repr(discount, strength):
    instance = ChineseRestaurantProcess(discount, strength)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)


def test_chinese_restaurant_sample_partition(discount, strength, n):
    instance = ChineseRestaurantProcess(discount, strength)
    s = instance.sample_partition(n)
    assert sum([len(t) for t in s]) == n
    customers = list(range(n))
    for table in s:
        for customer in table:
            assert customer in customers


def test_chinese_restaurant_sample(discount, strength, n):
    instance = ChineseRestaurantProcess(discount, strength)
    s = instance.sample(n)
    assert len(s) == n
    for c in s:
        assert c in range(n)


def test_chinese_restaurant_sequence_to_partition(discount, strength, n):
    instance = ChineseRestaurantProcess(discount, strength)
    s = instance.sample(n)
    p = instance.sequence_to_partition(s)
    print(p)
    assert sum([len(t) for t in p]) == n
    customers = list(range(n))
    for table in p:
        for customer in table:
            assert customer in customers


def test_chinese_restaurant_partition_to_sequence(discount, strength, n):
    instance = ChineseRestaurantProcess(discount, strength)
    p = instance.sample_partition(n)
    s = instance.partition_to_sequence(p)
    assert len(s) == n
    for c in s:
        assert c in range(n)


@pytest.mark.parametrize(
    "discount,strength",
    [
        (2, 0),  # bad discount
        (-1, 1.1),  # discount negative, strength not a multiple
        (0.7, -2),  # discount positive, strength not greater than its negative
    ],
)
def test_chinese_restaurant_probability(discount, strength):
    with pytest.raises(ValueError):
        instance = ChineseRestaurantProcess(discount, strength)
