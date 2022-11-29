class Primes:
    def __init__(self, n: int):
        self.__n = n
        self.__all = []

    def get(self):
        new = 2
        self.__all.append(new)
        yield new

        while len(self.__all) < self.__n:
            new += 1
            is_prime = True
            for prime in self.__all:
                if new % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                self.__all.append(new)
                yield new


assert [v for v in Primes(17).get()].__eq__([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), "Wrong for Pi(17)"
assert max(Primes(999).get()) == 7907, "Wrong 999 prime"

try:
    len(Primes(999).get())
except TypeError:
    pass
else:
    raise AssertionError("Generator should raise exception TypeError: object of type 'generator' has no len()")
