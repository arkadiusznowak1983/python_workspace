class isPrime:
    def is_prime(self, n):
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i = i + 1
        return True