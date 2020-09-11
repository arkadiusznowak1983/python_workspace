class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __bool__(self):
        print('aaaaa')
        print("(self.value if self.left is None else self.left) = {}".format((self.value if self.left.value is None else self.left.value)))
        print("(self.value if self.right is None else self.right) = {}".format((self.value if self.right.value is None else self.right.value)))
        print("((self.value if self.left is None else self.left) <= self.value <= (self.value if self.right is None else self.right)) = ".format(((self.value if self.left.value is None else self.left.value) <= self.value <= (self.value if self.right.value is None else self.right.value))))
        return self.value is not None and ((self.value if self.left.value is None else self.left.value) <= self.value <= (self.value if self.right.value is None else self.right.value))
