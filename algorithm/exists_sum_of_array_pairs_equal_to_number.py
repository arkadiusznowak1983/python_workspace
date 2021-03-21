class ExistsSumOfArrayPairsEqualToNumber:
    # https://www.youtube.com/watch?v=XKu_SEDAykw
    def linear(self, n, sum):
        if n is None or sum is None:
            raise Exception( "Bad input values. Try e.g. linear( n=[1, 2, 4, 4, 9, 11 ], s=8 )" )
        n.sort()                                                                                                        # O(nlogn)                              O=(n)
        lowest = n[0]                                                                                                   # O(1) get                              O=(1)
        biggest = n[-1]                                                                                                 # O(1) get                              O=(1)
        while len(n) > 1:                                                                                               # O((n-2) * 1) loop n-2 times, get
            pair_sum = lowest + biggest                                                                                 # O(1) add                              O=(1)
            if pair_sum > sum:                                                                                          # O(1) cmp
                del n[-1]                                                                                               # O(1) del
                biggest = n[-1]                                                                                         # O(1) get
            elif pair_sum < sum:                                                                                        # O((n-logn) * 1) else cmp
                del n[0]                                                                                                # O(1) del
                lowest = n[0]                                                                                           # O(1) get
            else:
                return True
        return False                                                                                                    # Time complexity                                                Space complexity
                                                                                                                        # O=( nlogn + 2+((n-2)*(1+1+1+(logn*(1+1))+((n-logn)*(1+1)))) )  O=(n +1 +1 +1)
                                                                                                                        # O=( nlogn + ((n-2)*(3+ 2logn +2n -2logn)) +2 )                 O=(n +3)
                                                                                                                        # O=( nlogn + ((n-2)*(3 + 2n)) +2 )
                                                                                                                        # O=( nlogn + (((3n+2n*n) -6 -4n)) +2 )
                                                                                                                        # O=( nlogn + 2n^2 -n -4 )
                                                                                                                        # O=( n * (logn + 2n + 1) )
                                                                                                                        # e.g. for array of 4 elements its: O(4*(log4+8+1)) => O=(~40)   O=(4 + 3) => 7