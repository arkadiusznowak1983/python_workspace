class SumOfConsecutiveNaturalNumbers:
    '''
    X = A + A+1 + A+2 + ... + A+n-1
    X = (A + A + n - 1)*(n/2)
    A = (2X + n - n**2)/2n
    '''
    def f(self, X):
        '''
        time complexity is O(n)
        :param X:
        :return:
        '''
        result = []
        n = 2
        while( (2*X + n - n**2) > 0):
            A = (2*X + n - n**2)/(2*n)
            if A - int(A) == 0:
                # print( "A={A} n={n}".format(A=A, n=n) )
                # result.append( "A={A} n={n}".format(A=A, n=n) )
                result.append( {'A': int(A), 'n': n} )
            n = n + 1
        return result

print(SumOfConsecutiveNaturalNumbers().f(100))