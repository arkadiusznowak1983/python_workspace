import unittest
from exists_sum_of_array_pairs_equal_to_number import ExistsSumOfArrayPairsEqualToNumber

class MyTestCase(unittest.TestCase):
    def test_linear(self):
        self.assertEqual(False, ExistsSumOfArrayPairsEqualToNumber().linear( [1, 2, 4, 9], 8 ))
        self.assertEqual(False, ExistsSumOfArrayPairsEqualToNumber().linear([1, 2, 4, 9, 11], 8))
        self.assertEqual(False, ExistsSumOfArrayPairsEqualToNumber().linear([3, 4], 6))
        self.assertEqual(True, ExistsSumOfArrayPairsEqualToNumber().linear([1, 2, 4, 4], 8))
        self.assertEqual(True, ExistsSumOfArrayPairsEqualToNumber().linear([1, 2, 3, 4], 4))
        self.assertEqual(True, ExistsSumOfArrayPairsEqualToNumber().linear([1, 1], 2))

if __name__ == '__main__':
    unittest.main()
