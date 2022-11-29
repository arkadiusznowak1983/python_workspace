from abc import ABC, abstractmethod


class Currency(ABC):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = float(round(value, 2))

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def convert(self, currency):
        pass

    def __float__(self):
        return float(self.value)


class PLN(Currency):
    def __str__(self):
        return f"{self.value:.2f} PLN"

    def convert(self, currency):
        return currency(float(self.value) * 4.5)


class EUR(Currency):
    def __str__(self):
        return f"{self.value:.2f} EUR"

    def convert(self, currency):
        return currency(float(self.value) / 4.5)


pln = PLN(0.6)
eur = EUR(0.7)
print(pln, ' => ', pln.convert(EUR))
print(eur, ' => ', eur.convert(PLN))
