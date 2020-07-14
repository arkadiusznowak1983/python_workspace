diverse = [50, 25, 10, 5, 2, 1]
def num_coins(N, level=0):
    if N == 0 or level == len(diverse):
        return []
    if N >= diverse[level]:
        return num_coins(N - diverse[level], level) + [diverse[level]]
    return num_coins(N, level+1)

print(num_coins(48))
