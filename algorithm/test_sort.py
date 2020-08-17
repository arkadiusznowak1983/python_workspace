import unittest
from sort import Sort


class SortTestCase(unittest.TestCase):
    def test_sort_merge(self):
        print("test {}".format(SortTestCase.test_sort_merge.__name__))
        self.assertEqual( [1, 2, 3, 5, 7, 9]
                         ,Sort().merge([2, 3, 5, 7, 9, 1]))
    def test_sort_merge_linked_list(self):
        print("test {}".format(SortTestCase.test_sort_merge.__name__))
        self.assertEqual( [1, 2, 3, 5, 7, 9]
                         ,Sort().merge_linked_list([2, 3, 5, 7, 9, 1]))


if __name__ == '__main__':
    unittest.main()
