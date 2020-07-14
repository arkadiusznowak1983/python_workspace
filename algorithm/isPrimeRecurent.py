
def isPrime(n, level=None):
    if level is None:
        level = n // 3
    if level>=2:
        if n%level == 0:
            print(n//level,' x ',level)
            return True
        else:
            return isPrime(n, level-1)
    else:
        print("prime")
        return True

isPrime(2245)