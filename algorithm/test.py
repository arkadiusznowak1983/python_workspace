'''
joseph problem
'''
def joseph(n, k):
    if n == 1:
        return 1
    return ((joseph(n-1, k) + k - 1) % n) + 1

# print(joseph(10, 2), joseph(10, 2) == 5)
# print(joseph(5, 4), joseph(5, 4) == 1)
#################################################

'''
is prime
'''
def isPrime(n, depth = None):
    if depth is None:
        depth = n // 3
    if depth >= 2:
        if n % depth == 0:
            return False
        else:
            return isPrime(n, depth - 1)
    return True

# print("is prime(n={}): {}  ".format(83, isPrime(n=83)))
# print("is prime(n={}): {}  ".format(87, isPrime(n=87)))
# print("is prime(n={}): {}  ".format(89, isPrime(n=89)))
#################################################

'''
generate list of primes
'''
def getPrimes(n):
    primes = { 2: True
              ,3: True
              ,5: True }
    counter = 0
    while True:
        try:
            k = sorted(list(primes))[counter]
        except:
            for k in range(2, n):
                if primes.get(k) is None:
                    primes[k] = True
                    break
            if k > n // 3:
                break
        counter = counter + 1
        ind = 2
        while ind * k <= n:
            primes[ind * k] = False if primes.get(ind * k) is None else primes.get(ind * k)
            ind = ind + 1
    return {i: False if primes.get(i) == False else True for i in range(2, n)}

print(getPrimes(50))
# print(list({2: True, 3: True, 4: False})[0])
# print({2: True, 3: True, 4: False}.get(2))
# print({2: True, 3: True, 4: False}.get(1))