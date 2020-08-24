class JosephusProblem:
    '''
    https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/

    https://rosettacode.org/wiki/Josephus_problem#Faster_way

    i got this on GS interview as first question
    '''
    def safe(self, n, k):
        '''
        josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
        josephus(1, k) = 1

        O(n)
        '''
        if n == 1:
            return 1
        return (self.safe(n - 1, k) + k - 1) % n + 1

    def linear(self, n, k):
        '''
        O(n)
        '''
        r = 0
        for i in range(1, n + 1):
            r = (r + k) % i
        return r + 1

    def fastest(self, n, k):
        return self.best(n, k) + 1

    def best(self, n, k):
        '''
        O(k*log(n))
        '''
        if n == 1:
            return 0
        if k == 1:
            return n - 1
        if k > n:
            return (self.best(n - 1, k) + k) % n

        res = self.best(n - int(n / k), k) - (n % k)
        if (res < 0):
            return res + n
        else:
            return res + int(res / (k - 1))