class PowOwnIdea:
    def simple(self, base, exp):
        # print('SIMPLE')
        result = 1
        for counter in range(exp):
            result = result * base
        return result
    def own(self, base, exp):
        # print("OWN exp=", exp)
        if exp == 0:
            return 1;
        result = self.own(base, int(exp/2))
        return (1 if exp % 2 == 0 else base) * result * result
    def linear(self, base, exp):
        result = 1
        while exp:
            if exp % 2 == 1:
                result = result * base
            base = base * base
            exp = int(exp / 2)
        return result
    # 7 => 111 => 2^0 + 2^1 + 2^2
    # 9 => 1001 => 2^0 + 2^3
    # 13 => 1101 => 2^0 + 2^2 + 2^3
    def pow(self, base, exp, type='simple'):
        if type == 'simple':
            return self.simple(base, exp)
        elif type == 'own':
            return self.own(base, exp)
        elif type == 'linear':
            return self.linear(base, exp)
        return self.simple(base, exp)
