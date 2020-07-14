# import math

def findMissing(A, B):
    A.sort()
    B.sort()
    for i in range(0, len(A)-1):
        if A[i] != B[i]:
            return A[i]
    return A[i+1]

def findMissingBySum(A, B):
    return sum(A) - sum(B)

print( findMissingBySum([1, 3, 5, 8, 9], [1, 3, 8, 9]) )