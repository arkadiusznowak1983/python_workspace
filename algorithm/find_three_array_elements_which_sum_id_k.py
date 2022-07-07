class Interview:
    def find(self, N: [], k: int):
        if len(N) < 3:
            raise Exception('bad array')
        N.sort(reverse=True)
        for firstIndex in range(len(N)-3):
            if N[firstIndex] < k - min(N):
                for secondIndex in range(firstIndex+1, len(N)-2):
                    for thirdIndex in range(secondIndex+1, len(N)-1):
                        if N[firstIndex] + N[secondIndex] + N[thirdIndex] == k:
                            return [N[firstIndex], N[secondIndex], N[thirdIndex]]
        return []

# print(Interview().find([5, 1, 6, 2, 4, 3], 10))