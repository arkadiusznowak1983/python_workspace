# object oriented structure version
########################################################################

#
class LinkedListClass:
    next = None
    value = None
    def reverse(self):
        head = self
        last = None
        while head is not None:
            next = head.next
            head.next = last
            last = head
            head = next
        return last
    #
    def print(self):
        head = self
        while head is not None:
            print(head.value)
            head = head.next

#
headC=LinkedListClass()
headC.value = 'C'
headB=LinkedListClass()
headB.value = 'B'
headB.next = headC
headA=LinkedListClass()
headA.value = 'A'
headA.next = headB
headA.print()
reversed_head=headA.reverse()
reversed_head.print()


#############################################################################################################
# simple dict struct version
# ###################################################################
LinkedList = {'next': None, 'value': None}
# O(N), O(3)
def reverseLinkedList(head):
    last = None
    while head is not None:
        next = head.get('next')
        head['next'] = last
        last = head
        head = next
    return last

#
def printLinkedList(head):
    while not head is None:
        print(head.get('value'))
        head = head.get('next')

#
nodeC=LinkedList.copy()
nodeC['value']='C'
nodeB=LinkedList.copy()
nodeB['value']='B'
nodeB['next']=nodeC
nodeA=LinkedList.copy()
nodeA['value']='A'
nodeA['next']=nodeB
printLinkedList(head=nodeA)

#
printLinkedList(head=reverseLinkedList(head=nodeA))
