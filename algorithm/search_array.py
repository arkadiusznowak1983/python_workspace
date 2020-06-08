class SearchArray:
    """ Class contains solutions for different search alghoritms """
    type = None
    def __init__(self, type):
        self.type = type

    def search(self, array=[], element=None):
        '''
        Search array indeks for element value. If array not contains that value ten returns -1
        :param array: searched array
        :param element: searched value
        :return: array index for element value
        '''

        if self.type == 'linear':
            return self.linear(array, element)
        elif self.type == 'binary':
            return self.binary(array, element)
        else:
            raise Exception('specify correct alghoritm: linear, binary, ...')

    def linear(self, array=[], element=None):
        '''
        Search array element using linear strategy
        time complexity is 0(n)
        :param array: using linear strategy array no need to be sorted
        :param element: searched element
        :return: index for element value
        '''

        indeks = 0
        while( len(array) > indeks and element != array[indeks] ):
            indeks+=1
        return indeks if indeks < len(array) else -1

    def binary(self, sortedArray=[], element=None):
        '''
        Search array element using binary "divide and conquer" strategy
        time complexity is 0(log_2(n))
        :param sortedArray: binary search can work only on sorted array
        :param element: searched element
        :return: index for element value
        '''

        leftPos = 0
        rightPos = len(sortedArray)
        while( leftPos < rightPos ):
            middlePos = (leftPos+rightPos)//2
            if sortedArray[middlePos] < element:
                leftPos = middlePos + 1
            elif sortedArray[middlePos] > element:
                rightPos = middlePos - 1
            else:
                return middlePos
        return -1