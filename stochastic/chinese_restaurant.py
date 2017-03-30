import numpy as np
from numbers import Number


class ChineseRestaurant(object):
    """
    A Chinese restaurant process consists of a sequence of arrivals of 
    customers to a Chinese restaurant. Customers may be seated either at an
    occupied table or a new table, there being infinitely many customers 
    and tables. 

    The first customer sits at the first table. The n-th customer
    sits at a new table with probability 1/n, and at each already occupied
    table with probability t_k/n, where t_k is the number of customers
    already seated at table k. This is the canonical process with discount=0
    and strength=1.

    The generalized process gives the n-th customer a probability of
    (strength + T * discount) / (n - 1 + strength) to sit at a new table
    and a probability of (t_k - discount) / (n - 1 + strength) of sitting at
    table k. T is the number of occupied tables.

    args:
        discount (float) = any real-valued number less than 1
        strength (float) = must be a negative multiple of discount if discount
            is less than 0 or a value greater than the opposite of discount
            if discount is non-negative and less than 1

    methods:

    sample
        args:
            n (int) = number of customers to simulate
        returns:
            (list of lists) representing the partition of customers among 
                different tables.

    """

    def __init__(self, discount=0, strength=1):
        self.discount = discount
        self.strength = strength

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, Number):
            raise TypeError(
                'Discount value must be a number.')
        if value >= 1:
            raise ValueError(
                'Discount value must be less than 1.')
        self._discount = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if not isinstance(value, Number):
            raise TypeError('Strength value must be a number.')
        if self.discount < 0:
            if value / -self.discount <= 0 or (value / -self.discount) % 1 != 0:
                raise ValueError(
                    'When discount is negative, strength value must be equal to a multiple of the discount value.')
        elif self.discount < 1:
            if value <= -self.discount:
                raise ValueError(
                    'When discount is between 0 and 1, strength value must be greater than the negative of the discount')
        self._strength = value

    def __str__(self):
        return 'Chinese restaurant process with discount {discount} and strength {strength}'.format(discount=self.discount, strength=self.strength)

    def __repr__(self):
        return self.__str__()

    def sample(self, n):
        """
        Generate a Chinese restaurant process with n customers
        """
        if not isinstance(n, int):
            raise TypeError('Sample length must be positive integer.')
        if n < 1:
            raise ValueError('Sample length must be at least 1.')

        s = [[1]]
        num_tables = 1
        table_range = [0, 1]

        for k in range(2, n + 1):
            p = [1.0 * (len(s[t]) - self.discount) / (k - 1 + self.strength)
                 for t in table_range[:-1]]
            p.append(1.0 * (self.strength + num_tables * self.discount) /
                     (k - 1 + self.strength))
            table = np.random.choice(table_range, p=p)
            if table == num_tables:
                num_tables += 1
                table_range.append(num_tables)
                s.append([])
            s[table].append(k)

        return np.array(s)
