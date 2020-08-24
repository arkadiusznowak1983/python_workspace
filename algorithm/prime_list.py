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