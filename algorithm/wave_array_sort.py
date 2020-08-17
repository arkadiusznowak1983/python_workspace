import operator
from pickle import encode_long


class WaveArraySort:
    '''
    https://www.geeksforgeeks.org/sort-array-wave-form-2/

    Given an unsorted array of integers, sort the array into a wave like array.
    An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

    Examples:
     Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
     Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                     {20, 5, 10, 2, 80, 6, 100, 3} OR
                     any other array that is in wave form

     Input:  arr[] = {20, 10, 8, 6, 4, 2}
     Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                     {10, 8, 20, 2, 6, 4} OR
                     any other array that is in wave form

     Input:  arr[] = {2, 4, 6, 8, 10, 20}
     Output: arr[] = {4, 2, 8, 6, 20, 10} OR
                     any other array that is in wave form

     Input:  arr[] = {3, 6, 5, 10, 7, 20}
     Output: arr[] = {6, 3, 10, 5, 20, 7} OR
                 any other array that is in wave form
    '''
    #
    # not working solution
    #
    # def nextOperator(self, op=operator.le):
    #     return operator.le if op==operator.ge else operator.ge

    # def waveSet(self, op, firstNum, secondNum):
    #     if op(firstNum, secondNum):
    #         return [firstNum, secondNum]
    #     else:
    #         return [secondNum, firstNum]
    #
    # def waveSet(self, op, num, waveArray):
    #     if not op(waveArray[num], waveArray[num+1]):
    #         tmpNum = waveArray[num+1]
    #         waveArray[num+1] = waveArray[num]
    #         waveArray[num] = tmpNum
    #
    # def waveSort(self, unsortedArray=[]):
    #     op = None
    #     for indeks in range(len(unsortedArray)-1):
    #         op = self.nextOperator(op)
    #         self.waveSet(op, indeks, unsortedArray)
    #         print( "{} {}".format( '>=' if op==operator.ge else '<=', unsortedArray) )

    def swap(self, waveArr, key):
        tmpNum = waveArr[key]
        waveArr[key] = waveArr[key + 1]
        waveArr[key + 1] = tmpNum

    def waveSortSwap(self, arr=[]):
        '''
        1) make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their adjacent odd elements
        2) Traverse all even positioned elements of input array, and do following.
        - If current element is smaller than previous odd element, swap previous and current.
        - If current element is smaller than next odd element, swap next and current.

        :param arr:
        :return:
        '''
        even = None
        odd = None
        for key, element in enumerate(arr):
            if (key == len(arr)-1 and key % 2 == 0) or (even is not None and even <= element):
                break
            if key % 2 == 0:
                even = element
            # print("{} {}".format(key, element))

        waveArr = arr.copy()
        for key, element in enumerate(arr):
            if (key % 2 == 0) and (odd is not None):
                if element < odd:
                    self.swap(self, waveArr, key - 1)
                elif (key != (len(arr)-1)) and (element < arr[key + 1]):
                    self.swap(self, waveArr, key)
            elif key % 2 == 1:
                odd = element
        return waveArr


    def waveSortSimple(self, arr=[]):
        '''
        working solution
        time complexity O(log(N)+N) if Merge Sort, Heap Sort, when sorting
        :param arr:
        :return:
        '''
        arr.sort()
        waveArray = []
        while(len(arr)):
            waveArray.append(arr.pop(-1))
            if not len(arr):
                break
            waveArray.append(arr.pop(0))
        return waveArray

    def dialer_sort_web(self, arr=[]):
        self.sort_web(arr)
        return arr
    def sort_web(self, arr=[]):
        '''
        time complexity is O(N)
        :param arr:
        :return:
        '''
        for indeks in range(0, len(arr)-1, 2):
            if indeks > 0 and arr[indeks] < arr[indeks - 1]:
                arr[indeks], arr[indeks - 1] = arr[indeks - 1], arr[indeks]
            if (indeks < len(arr) - 2 and arr[indeks] < arr[indeks + 1]):
                arr[indeks], arr[indeks + 1] = arr[indeks + 1], arr[indeks]

    def sort_wave_my_own(self, arr=[]):
        '''

        :param arr:
        :return:
        '''
        for indeks in range(0, len(arr)-1):
            if indeks % 2 == 0:
                if indeks > 0 and arr[indeks] < arr[indeks-1]:
                    arr[indeks], arr[indeks-1] = arr[indeks-1], arr[indeks]
                if indeks < (len(arr)-1) and arr[indeks] < arr[indeks+1]:
                    arr[indeks], arr[indeks+1] = arr[indeks+1], arr[indeks]
        return arr

if __name__ == '__main__':
    arr = [10, 5, 6, 3, 2, 20, 100, 80]
    WaveArraySort().sort_web(arr)
    print(arr)
    #print(WaveArraySort().waveSortSwap(arr=[10, 2, 5, 3]))

