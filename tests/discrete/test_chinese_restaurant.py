"""Chinese restaurant tests."""
# flake8: noqa
import pytest

from stochastic.discrete import ChineseRestaurantProcess


def test_chinese_restaurant_str_repr(discount, strength):
    instance = ChineseRestaurantProcess(discount, strength)
    assert isinstance(repr(instance), str)
    assert isinstance(str(instance), str)

def test_chinese_restaurant_sample(discount, strength, n):
    instance = ChineseRestaurantProcess(discount, strength)
    s = instance.sample(n)
    assert sum([len(t) for t in s]) == n
    customers = list(range(1, n+1))
    for table in s:
        for customer in table:
            assert customer in customers

@pytest.mark.parametrize("discount,strength", [
    (2, 0), # bad discount
    (-1, 1.1), # discount negative, strength not a multiple
    (0.7, -2), # discount positive, strength not greater than its negative
])
def test_chinese_restaurant_probability(discount, strength):
    with pytest.raises(ValueError):
        instance = ChineseRestaurantProcess(discount, strength)
