from copy import deepcopy

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + (str(self.next) if self.next is not None else str())

    def reverse(self, next = None):
        node = self.next
        self.next = next
        if node is None:
            return self
        return node.reverse(self)

    def __reversed__(self):
        node = deepcopy(self)
        return node.reverse()


list = Node(0, Node(5, Node(3, Node(2, Node(1, None)))))
print("list = ", list)
print("reversed list = ", reversed(list))
print("original list = ", list)