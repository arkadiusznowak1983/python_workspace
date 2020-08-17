import unittest
from sum_of_consecutive_natural_numbers import SumOfConsecutiveNaturalNumbers


class MyTestCase(unittest.TestCase):
    def test_10(self):
        self.assertEqual( [{'A': 1, 'n': 4}], SumOfConsecutiveNaturalNumbers().f(10))
    def test_100(self):
        self.assertEqual( [{'A': 18, 'n': 5}, {'A': 9, 'n': 8}], SumOfConsecutiveNaturalNumbers().f(10))


if __name__ == '__main__':
    unittest.main()
