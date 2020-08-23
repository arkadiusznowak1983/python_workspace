import unittest
from difference_between_heights import DifferenceBetweenHeights

class DifferenceBetweenHeightsTestCase(unittest.TestCase):
    def test_something(self):
        # Input: arr[] = {1, 5, 15, 10}
        # k = 3
        # Output: Maximum
        # difference is 8
        # arr[] = {4, 8, 12, 7}
        #
        self.assertEqual(8, DifferenceBetweenHeights().calc([1, 5, 15, 10], 3))
        self.assertEqual(5, DifferenceBetweenHeights().calc([1, 10, 14, 14, 14, 15], 6))

if __name__ == '__main__':
    unittest.main()
