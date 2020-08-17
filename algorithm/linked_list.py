class NodeList:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = NodeList(data)
            return

        current = self.head
        while(current.next is not None):
            current = current.next
        current.next = NodeList(data)

    def merge(self, node1, node2):
        if node1 is None:
            return node2
        elif node2 is None:
            return node1

        if node1.data < node2.data:
            result = node1
            result.next = self.merge(node1.next, node2)
        else:
            result = node2
            result.next = self.merge(node1, node2.next)

        return result

    def sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.half(head)
        after_half = middle.next
        middle.next = None
        left = self.sort(head)
        right = self.sort(after_half)

        return self.merge(left, right)

    def half(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def print(self, head):
        while(head is not None):
            print("node_data={}".format(head.data))
            head = head.next