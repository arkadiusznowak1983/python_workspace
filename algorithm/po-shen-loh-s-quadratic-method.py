from math import sqrt


class QuadraticMethod:
    def calculate(self, a, b, c):
        """  y = ax**2 + bx + c  """
        if a == 0:
            return [-c / b]

        d = b * b - 4 * a * c
        b = -b
        a2 = 2 * a
        if d > 0:
            sq = sqrt(d)
            return [(b - sq) / a2, (b + sq) / a2]
        if d == 0:
            return [d / a2]
        r = b / a2
        i = sqrt(-d) / a2
        return [complex(r, -i), complex(r, i)]


class PoShenLohs(QuadraticMethod):
    def calculate(self, a, b, c):
        """  y = ax**2 + bx + c  """
        if a == 0:
            return [-c / b]

        a2 = 2*a
        avg = -b / a2
        d = avg*avg - c/a
        if d > 0:
            sq = sqrt(d)
            return [avg - sq, avg + sq]
        if d == 0:
            return [avg]
        sq = sqrt(-d)
        return [complex(avg, -sq), complex(avg, sq)]


if __name__ == "__main__":
    for test in [[(0, -3, 3), [1]],
                 [(1, -4, 4), [0], [2]],  # two different and both correct results
                 [(2, -6, 22.5), [(1.5 - 3j), (1.5 + 3j)]],
                 [(2, -14, 24), [3, 4]],
                 [(3, 0, -27), [-3, 3]]]:
        for method in [QuadraticMethod, PoShenLohs]:
            try:
                assert method().calculate(*test[0]) == test[1], "a={}, b={}, c={} => {}".format(*test[0], test[1])
            except:
                assert method().calculate(*test[0]) == test[len(test)-1], "a={}, b={}, c={} => {}".format(*test[0], test[len(test)-1])
