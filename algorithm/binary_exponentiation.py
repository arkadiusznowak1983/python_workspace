class BinaryExponentiation:
    def __init__(self, base=1, exp=2):
        self.base = 1 if base is None else base
        self.exp = 2 if exp is None else exp

    def calc(self, type='recurent'):
        if type=='recurent':
            return self.calc_recurent()
        return self.calc_linear()

    def calc_recurent(self):
        '''
        time complexity is O(log(n)) but recursive function will extend the execution time
        :return: base multiplication by exp in recursive mode
        '''
        if self.exp == 0:
            return 1
        duplicated = BinaryExponentiation( self.base, int(self.exp / 2) ).calc()
        duplicated = duplicated * duplicated
        if self.exp % 2 == 1:
            duplicated = duplicated * self.base
        return duplicated

    def calc_linear(self):
        '''
        time complexity is O(log(n)) and the linear algorithm is better solution
        :return: base multiplication by exp in linear mode (fastest way)
        '''
        result = 1
        while(self.exp):
            if self.exp % 2 == 1:
                result = result * self.base
            self.base = self.base * self.base
            self.exp = int(self.exp / 2)
        return result
