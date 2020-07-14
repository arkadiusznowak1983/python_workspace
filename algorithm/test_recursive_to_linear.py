import unittest
from recursive_to_linear import RecursiveToLinear


class RecursiveToLinearTestCase(unittest.TestCase):
    def test_sample_recursive(self):
        self.assertEqual( RecursiveToLinear().sample_recursive( [1, 2, [9, 8, [1, 1]], [1, 1, 2, 5], 3] ), True )

    def test_sample_linear(self):
        self.assertEqual(RecursiveToLinear().sample_linear([1, 2, [9, 8, [1, 1]], [1, 1, 2, 5], 3]), True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RecursiveToLinearTestCase)
    suite = unittest.TestLoader().loadTestsFromName('test_sample_linear', RecursiveToLinearTestCase)
    unittest.TextTestRunner(verbosity=0).run(suite)
