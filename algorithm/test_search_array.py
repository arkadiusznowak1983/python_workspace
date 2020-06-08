import unittest
from search_array import SearchArray

class SearchArrayTestCase(unittest.TestCase):

    def test_linear(self):
        self.assertEqual( (SearchArray('linear')).search([1, 2, 3, 5, 6, 74, 23, 435, 2, 3, 55, 64], 1 ), 0 )
        self.assertEqual( (SearchArray('linear')).search([1, 2, 3, 5, 6, 74, 23, 435, 2, 3, 55, 64], 2 ), 1 )
        self.assertEqual( (SearchArray('linear')).search([1, 2, 3, 5, 6, 74, 23, 435, 2, 3, 55, 64], 23 ), 6 )
        self.assertEqual((SearchArray('linear')).search([1, 2, 3, 5, 6, 74, 23, 435, 2, 3, 55, 64], 64 ), 11 )
        self.assertEqual((SearchArray('linear')).search([1, 2, 3, 5, 6, 74, 23, 435, 2, 3, 55, 64], 4 ), -1 )
        self.assertEqual((SearchArray('linear')).search([1, 2, 3, 5, 6, 74, 23, 435, 2, 3, 55, 64], 34 ), -1 )

    def test_binary(self):
        self.assertEqual( (SearchArray('binary')).search([1, 2, 2, 3, 3, 5, 6, 23, 55, 64, 74, 435], 1 ), 0 )
        self.assertEqual( (SearchArray('binary')).search([1, 2, 2, 3, 3, 5, 6, 23, 55, 64, 74, 435], 2 ), 2 )
        self.assertEqual((SearchArray('binary')).search([1, 2, 2, 3, 3, 5, 6, 23, 55, 64, 74, 435], 64 ), 9 )
        self.assertEqual((SearchArray('binary')).search([1, 2, 2, 3, 3, 5, 6, 23, 55, 64, 74, 435], 4 ), -1 )
        self.assertEqual((SearchArray('binary')).search([1, 2, 2, 3, 3, 5, 6, 23, 55, 64, 74, 435], 34 ), -1 )

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchArrayTestCase)
    #suite = unittest.TestLoader().loadTestsFromName( 'test_binary', SearchArrayTestCase )
    unittest.TextTestRunner(verbosity=2).run(suite)