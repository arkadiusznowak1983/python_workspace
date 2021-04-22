class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + (str(self.next) if self.next is not None else str())

    def __add__(self, other):
        if self.data is None or other is None or other.data is None:
            return Node()
        node = Node(data=self.data + other.data,
                    next=self.next + other.next if other.next is not None else None)
        if node.next is not None and node.next.data is not None and node.next.data > 9:
            node.data = node.data + 1
            node.next.data = node.next.data - 10
        return node


class SumLinkedLists:
    def __init__(self, lists=[]):
        self.lists = lists

    def __str__(self):
        if not len(self.lists):
            return str()
        node = self.lists[0]
        if len(self.lists) == 1:
            return str(node.data)
        for other in self.lists[1:]:
            node = node + other
        return str(node)


listA = Node(3, Node(2, Node(1, None)))  # 3->2->1->null
listB = Node(4, Node(5, Node(9, None)))  # 4->5->9->null

print("listA is ", listA)
print("listB is ", listB)
print("listA + listB is ", listA + listB)
print("sum lists is ", str(SumLinkedLists([listA, listB])))
