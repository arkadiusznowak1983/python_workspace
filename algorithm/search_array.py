class SearchArrayNode:
    def __init__(self):
        self.character = None
        self.nodes = []

    def insert_word(self, word, index):
        # validate & set current node letter
        if index >= len(word):
            return None
        if self.character is None:
            self.character = word[index]

        # validate next letter
        if len(word) <= index+1:
            return self

        # use or create node for letter
        sub_node = None
        if len(self.nodes):
            for node in self.nodes:
                if node.character == word[index+1]:
                    sub_node = node.insert_word(word, index+1)
                    break
        if sub_node is None:
            sub_node = SearchArrayNode().insert_word(word, index+1)
        if not sub_node is None:
            self.nodes.append(sub_node)

        return self

    def compile(self, elements=[]):
        for word in elements:
            node = None
            if not len(self.nodes):
                node = SearchArrayNode()
            else:
                for node in self.nodes:
                    if node.character == word[0]:
                        break
            self.nodes.append(node)
            node.insert_word(word, 0)

    def search(self, word, node=None):
        matches = []
        matches.append( node if not node is None else self )
        if len(self.nodes):
            for node in self.nodes:
                if node.character == word[0]:
                    matches.append( self.search(word[1:], node) )
        return matches

    # FINISH printing paths !!!!
    def show(self, nodes):
        print(nodes)
        pass

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
        elif self.type == 'like_bintree':
            return self.like_bintree(array, element)
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

    def like_bintree(self, elements, word):
        treeObject = SearchArrayNode()
        treeObject.compile(elements)
        treeObject.show(treeObject.search("lor"))