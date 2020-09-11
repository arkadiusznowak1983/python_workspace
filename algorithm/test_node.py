import unittest
from node import Node


class NodeTestCase(unittest.TestCase):
    def test_bool(self):
        if Node(value=2, left=Node(1), right=Node(3)):
            self.fail('to nie jest drzewo binarne')


if __name__ == '__main__':
    unittest.main()
