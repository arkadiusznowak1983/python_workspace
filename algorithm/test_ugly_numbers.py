import unittest
from ugly_numbers import UglyNumbers


class UglyNumbersestCase(unittest.TestCase):
    # def test_ugly_numbers_first_look(self):
    #     '''
    #     Examples:
    #         Input  : n = 7
    #         Output : 8
    #         Input  : n = 10
    #         Output : 12
    #         Input  : n = 15
    #         Output : 24
    #         Input  : n = 150
    #         Output : 5832
    #
    #         1, 2, 3,
    #         4, 5, 6,
    #         8, 9, 10,
    #         12, 15
    #
    #     :return:
    #     '''
    #     print('test_ugly_numbers_first_look - i used bad solution')
    #     self.assertEqual(8, UglyNumbers().ugly_numbers_first_look(7))
    #     self.assertEqual(12, UglyNumbers().ugly_numbers_first_look(10))
    #     self.assertEqual(24, UglyNumbers().ugly_numbers_first_look(15))
    #     # self.assertEqual(5832, UglyNumbers().ugly_numbers_first_look(150))

    def test_ugly_numbers_recurent(self):
        print('test_ugly_numbers_recurent')
        '''
        Examples:
            Input  : n = 7
            Output : 8
            Input  : n = 10
            Output : 12
            Input  : n = 15
            Output : 24
            Input  : n = 150
            Output : 5832

            1, 2, 3,
            4, 5, 6,
            8, 9, 10,
            12, 15

        :return:
        '''
        self.assertEqual(5, UglyNumbers().ugly_numbers_recurent(5))
        self.assertEqual(6, UglyNumbers().ugly_numbers_recurent(6))
        self.assertEqual(8, UglyNumbers().ugly_numbers_recurent(7))
        self.assertEqual(12, UglyNumbers().ugly_numbers_recurent(10))
        self.assertEqual(24, UglyNumbers().ugly_numbers_recurent(15))
        self.assertEqual(5832, UglyNumbers().ugly_numbers_recurent(150))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(UglyNumbersestCase.test_ugly_numbers_recurent)
    unittest.TextTestRunner(verbosity=0).run(suite)