from linked_list import LinkedList, NodeList

class Sort:
    def merge(self, arr=[]):
        '''
        time complexity: O(n*log(n))
        space complexity: O(n)
        '''
        if len(arr) <= 1:
            return arr

        # Divide And Conquer
        half = len(arr) // 2
        arrL = self.merge(arr[:half])
        arrR = self.merge(arr[half:])

        # sort & add left elements
        arr = []
        while(len(arrL) and len(arrR)):
            arr.append( arrL.pop(0) if arrL[0] < arrR[0] else arrR.pop(0) )
        [arr.append(item) for item in arrL + arrR]

        return arr

    def merge_linked_list(self, arr=[]):
        linkedList = LinkedList()
        [linkedList.append(data) for data in arr]
        linkedList.head = linkedList.sort(linkedList.head)
        result = []
        current = linkedList.head
        while(current is not None):
            result.append(current.data)
            current = current.next
        return result
