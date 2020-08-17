import unittest
from sort_merge import SortMerge

class SortMergeTestCase(unittest.TestCase):
    def test_SortMerge(self):
        print('test_SortMerge')
        self.assertEqual( [1, 2, 3, 5, 7, 9]
                         ,SortMerge().sort_own([2, 3, 5, 7, 9, 1]))
    def test_SortMergeAlternative(self):
        print('test_SortMergeAlternative')
        self.assertEqual( [1, 2, 3, 5, 7, 9]
                         ,SortMerge().merge_sort([2, 3, 5, 7, 9, 1]))


if __name__ == '__main__':
    unittest.main()

