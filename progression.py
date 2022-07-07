def licz(S):
    result = []
    for n in range(1,S*2+1):
        a=(S/n)-((n-1)/2)
        if a%1==0 and (a+a+n-1)*(n/2) == S:
            result.append([a, n])
    return result

print( licz(134638) )