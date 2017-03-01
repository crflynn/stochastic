import numpy as np
from numbers import Number


class ChineseRestaurant(object):
    """

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

        """
        if not isinstance(n, int):
            raise TypeError('Sample length must be positive integer.')
        if n < 1:
            raise ValueError('Sample length must be at least 1.')

        s = [[1]]
        num_tables = 1
        table_range = [0, 1]

        for k in range(2, n + 1):
            table = np.random.randint(0, num_tables + 1)
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
