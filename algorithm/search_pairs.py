class SearchPairs:
    '''
    https://www.hackerrank.com/challenges/pairs/problem
    '''
    def search(self, arr, k):
        arr.sort(reverse=True)
        indexBig = 0
        counter = 0
        while arr[indexBig] > k and indexBig < len(arr) - 1:
            indexSmall = len(arr) - 1
            while arr[indexBig] - arr[indexSmall] >= k:
                if arr[indexBig] - arr[indexSmall] == k:
                    counter = counter + 1
                    # print(arr[indexBig], arr[indexSmall])
                indexSmall = indexSmall - 1
            indexBig = indexBig + 1
        return counter

    def searchSecond(self, arr, k):
        counter = 0
        for i in range(len(arr)):
            if arr[i] >= k and arr[i] - k in arr:
                counter = counter + 1
        return counter

    def searchThird(self, arr, k):
        counter = 0
        smallArray = {}
        bigArray = []
        highest = None
        for elem in arr:
            if elem > k:
                highest = elem if highest is None or elem > highest else highest
                bigArray.append(elem - k)
            elif elem <= k:
                smallArray[elem] = True

        for elem in bigArray:
            if elem <= highest - k:
                smallArray[elem + k] = True

        for i in range(len(bigArray)):
            if smallArray.get(bigArray[i]) == True:
                counter = counter + 1
        return counter

    def searchFourth(self, arr, k):
        '''
        fastest way
        :param arr:
        :param k:
        :return:
        '''
        counter = 0
        smallArray = {}
        mediumArray = {}
        bigArray = []
        highest = None
        for elem in arr:
            if elem > k:
                highest = elem if highest is None or elem > highest else highest
                bigArray.append(elem - k)
            else:
                smallArray[elem] = True

        print('big=', bigArray)
        print('small=', smallArray)
        # [1, 5, 3, 4, 2], 2
        ind = 0
        while len(bigArray) > ind:
            if smallArray.get(bigArray[ind]):
                counter = counter + 1
                bigArray.pop(ind)
                print('smallGet=', smallArray)
                continue

            elif bigArray[ind] <= highest - k:
                mediumArray[bigArray[ind] + k] = True

            ind = ind + 1
        print('big=', bigArray)
        print('medium=', mediumArray)
        print('counter=', counter)

        for elem in bigArray:
            if smallArray.get(elem):
                counter = counter + 1
                print('smalGet=', smallArray)
            if mediumArray.get(elem):
                counter = counter + 1
                print('mediumGet=', mediumArray)
        return counter