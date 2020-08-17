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

    def ugly_numbers_simple(self, n):
        '''
        time complexity: O(nlog(n)) ???
        space complexity: O(1)
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

    def ugly_numbers_dynamic(self, n):
        '''
        dynamic method
        time complexity: O(n)
        space complexity: O(n)
        '''
        uglyNumbers = [0] * n
        uglyNumbers[0] = 1
        primary2 = primary3 = primary5 = 0
        nextMultiplePrimary2 = 2
        nextMultiplePrimary3 = 3
        nextMultiplePrimary5 = 5

        for indeks in range(1, len(uglyNumbers)):
            uglyNumbers[indeks] = min( nextMultiplePrimary2
                                      ,nextMultiplePrimary3
                                      ,nextMultiplePrimary5)
            if (uglyNumbers[indeks] == nextMultiplePrimary2):
                    primary2 = primary2 + 1
                    nextMultiplePrimary2 = uglyNumbers[primary2] * 2
            if (uglyNumbers[indeks] == nextMultiplePrimary3):
                    primary3 = primary3 + 1
                    nextMultiplePrimary3 = uglyNumbers[primary3] * 3
            if (uglyNumbers[indeks] == nextMultiplePrimary5):
                    primary5 = primary5 + 1
                    nextMultiplePrimary5 = uglyNumbers[primary5] * 5

        return uglyNumbers[-1]
