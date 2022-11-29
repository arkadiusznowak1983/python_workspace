# Prevent float incermentation problems like, 0.6 + 0.7 = 1.2999999999999998
#
class Money(float):
    precision = 4
    multiplication = 10**precision

    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return float(self._value / self.multiplication)

    @value.setter
    def value(self, value):
        self._value = int(value * self.multiplication)

    def __float__(self):
        return self.value

    def __int__(self):
        return int(self._value)

    def __add__(self, other):
        return float((int(self) + int(other)) / self.multiplication)


print('Incorrect ', 0.6+0.7)
print('Fixed', Money(0.6) + Money(0.7))


#  simplest solution
class Float(float):
    def __add__(self, other):
        return float((int(float(self) * 10**4) + int(float(other) * 10**4)) / 10**4)


print('Simple float __add__ overload', Float(0.6) + Float(0.7))

