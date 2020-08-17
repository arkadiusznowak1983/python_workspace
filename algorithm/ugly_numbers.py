import sys
class UglyNumbers:
    '''
    https://www.geeksforgeeks.org/ugly-numbers/

    Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
    The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.
    Given a number n, the task is to find n’th Ugly number.

    Examples:
    Input  : n = 7
    Output : 8
    Input  : n = 10
    Output : 12
    Input  : n = 15
    Output : 24
    Input  : n = 150
    Output : 5832

    '''
    # def ugly_numbers_first_look(sel, n):
    #     # uglyNumbers = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
    #     uglyNumbers = [1]
    #     uglyPrimes = [2, 3, 5]
    #
    #     for licznik2 in uglyPrimes:
    #         uglyNumbers.append(licznik2)
    #         for licznik3 in uglyPrimes:
    #             uglyNumbers.append(licznik3)
    #             uglyNumbers.append(licznik2*licznik3)
    #             for licznik5 in uglyPrimes:
    #                 uglyNumbers.append(licznik5)
    #                 uglyNumbers.append(licznik2 * licznik3 * licznik5)
    #
    #     # ! method removing dup is set
    #     # uglyNumbers = list(set(uglyNumbers))
    #     # 2 method removing dup is list comprehetion
    #     uglyNumbers = [loopUglyNumber for key, loopUglyNumber in enumerate(uglyNumbers) if key == 0 or (loopUglyNumber not in uglyNumbers[:key])]
    #     uglyNumbers.sort()
    #     return uglyNumbers[n-1]

    def ugly_numbers_recurent(self, n):
        '''
        To check
            if a number is ugly,
                divide the number by greatest divisible powers of 2, 3 and 5,
        if the number becomes 1
            then it is an ugly number
            otherwise not.
        :param n:
        :return:
        '''
        uglyNumberCounter = 1
        for licznik in range(1, sys.maxsize):
            if self.isUgly(licznik):
                if uglyNumberCounter == n:
                    return licznik
                uglyNumberCounter = uglyNumberCounter + 1

    uglyPrimes = [2, 3, 5]
    def isUgly(self, n):
        if n <= 6:
            return 1
        for number in self.uglyPrimes:
            while(n % number == 0):
                n = int(n/number)
        return 1 if n == 1 else 0
