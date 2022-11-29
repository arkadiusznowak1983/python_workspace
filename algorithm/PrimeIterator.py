class Primes:
    def __init__(self, n: int, greater: int = 1):
        self.__n = n
        self.__greater = greater
        self.__all = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.__next_prime() <= self.__greater:
            pass
        return self.__all[-1]

    def __next_prime(self):
        if len(self.__all) == self.__n:
            raise StopIteration
        if not len(self.__all):
            self.__all.append(2)
            return 2

        new = self.__all[-1]
        while True:
            new += 1
            is_prime = True
            for prime in self.__all:
                if new % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                break
        self.__all.append(new)
        return new


# first 17 primes
assert [v for v in Primes(17)].__eq__([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), "Wrong for Pi(17)"

# first 17 primes greater than 10
assert [v for v in Primes(17, 10)].__eq__([11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]), "Wrong for Pi(17, 10)"

assert max(Primes(999)) == 7907, "Wrong 999 prime"
