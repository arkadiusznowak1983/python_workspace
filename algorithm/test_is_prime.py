import unittest
from is_prime import isPrime


class isPrimeTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, isPrime().is_prime(7))
        self.assertEqual(False, isPrime().is_prime(49))
        self.assertEqual(False, isPrime().is_prime(81))
        self.assertEqual(True, isPrime().is_prime(83))


if __name__ == '__main__':
    unittest.main()
