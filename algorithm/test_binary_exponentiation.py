import unittest
from binary_exponentiation import  BinaryExponentiation

class BinaryExponentiationTestCase(unittest.TestCase):
    def test_recurent_pow_5_2(self):
        self.assertEqual( BinaryExponentiation( 5 ).calc(), 25 )
        self.assertEqual( BinaryExponentiation( 5, 2 ).calc(), 25 )
    def test_recurent__7_13(self):
        self.assertEqual( BinaryExponentiation( 7, 9 ).calc(), 40353607 )

    def test_linear_pow_5_2(self):
        self.assertEqual( BinaryExponentiation( 5 ).calc(type='linear'), 25 )
        self.assertEqual( BinaryExponentiation( 5, 2 ).calc(type='linear'), 25 )
    def test_linear__7_13(self):
        self.assertEqual( BinaryExponentiation( 7, 9 ).calc(type='linear'), 40353607 )

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BinaryExponentiationTestCase)
    #suite = unittest.TestLoader().loadTestsFromName('test_linear__7_13', BinaryExponentiationTestCase)
    unittest.TextTestRunner(verbosity=5).run(suite)