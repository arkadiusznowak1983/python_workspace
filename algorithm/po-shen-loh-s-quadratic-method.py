from math import sqrt
from functools import lru_cache


class QuadraticMethod:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def a_equal_zero(self):
        return [-self.c / self.b]

    @lru_cache(maxsize=None)
    def delta(self):
        return (self.b * self.b) - (4 * self.a * self.c)

    def calculate(self):
        """  y = ax**2 + bx + c  """
        if self.a == 0:
            return self.a_equal_zero()

        self.b = -self.b
        if self.delta() > 0:
            sq = sqrt(self.delta())
            return [(self.b-sq) / (2 * self.a), (self.b + sq) / (2 * self.a)]
        if self.delta() == 0:
            return [self.delta() / (2 * self.a)]
        r = self.b / (2 * self.a)
        i = sqrt(-self.delta()) / (2 * self.a)
        return [complex(r, -i), complex(r, i)]


class PoShenLohs(QuadraticMethod):
    def delta_below_zero(self):
        sq = sqrt(-self.delta())
        return [complex(self.avg(), -sq), complex(self.avg(), sq)]

    def delta_equal_zero(self):
        return [self.avg()]

    def delta_above_zero(self):
        sq = sqrt(self.delta())
        return [self.avg() - sq, self.avg() + sq]

    @lru_cache(maxsize=None)
    def avg(self):
        return -self.b / (2 * self.a)

    @lru_cache(maxsize=None)
    def delta(self):
        return (self.avg() * self.avg()) - (self.c / self.a)

    def calculate(self):
        """  y = ax**2 + bx + c  """
        if self.a == 0:
            return self.a_equal_zero()
        if self.delta() > 0:
            return self.delta_above_zero()
        if self.delta() == 0:
            return self.delta_equal_zero()
        return self.delta_below_zero()


class PoShenLohsAosS(PoShenLohs):
    """ UNDER CONSTRUCTION"""
    @lru_cache(maxsize=None)
    def avg(self):
        return -self.b / 2

    def calculate(self):
        """  y = ax**2 + bx + c  """
        if self.a == 0:
            return self.a_equal_zero()
        if self.a != 1:
            self.b /= self.a
            self.c /= self.a

        square_avg = sqrt(self.avg() * self.avg())
        if not self.c > square_avg:
            delta_square = square_avg - self.c
            return [self.avg() - delta_square, self.avg() + delta_square]


if __name__ == "__main__":
    for test in [[(0, -3, 3), [1]],
                 [(1, -4, 4), [0], [2]],  # two different and both correct results
                 [(2, -6, 22.5), [(1.5 - 3j), (1.5 + 3j)]],
                 [(2, -14, 24), [3, 4]],
                 [(3, 0, -27), [-3, 3]]
                 ]:
        for method in [QuadraticMethod, PoShenLohs]:  # , PoShenLohsAosS]:
            try:
                assert method(*test[0]).calculate() == test[1], "a={}, b={}, c={} => {}".format(*test[0], test[1])
            except:
                assert method(*test[0]).calculate() == test[len(test)-1], "a={}, b={}, c={} => {}".format(*test[0], test[len(test)-1])
