import unittest
from search_pairs import SearchPairs


class SearchPairsCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3, SearchPairs().search([1, 5, 3, 4, 2], 2))
        self.assertEqual(3, SearchPairs().search([1, 2, 3, 4], 1))
        pass
    def test_somethingSecond(self):
        self.assertEqual(3, SearchPairs().searchSecond([1, 5, 3, 4, 2], 2))
        self.assertEqual(3, SearchPairs().searchSecond([1, 2, 3, 4], 1))
    def test_somethingThird(self):
        self.assertEqual(3, SearchPairs().searchThird([1, 5, 3, 4, 2], 2))
        self.assertEqual(3, SearchPairs().searchThird([1, 2, 3, 4], 1))
        self.assertEqual(0, SearchPairs().searchThird([363374326,364147530,61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793], 1))
    def test_somethingFourth(self):
        self.assertEqual(3, SearchPairs().searchFourth([1, 5, 3, 4, 2], 2))
        self.assertEqual(3, SearchPairs().searchFourth([1, 2, 3, 4], 1))
        self.assertEqual(0, SearchPairs().searchFourth([363374326,364147530,61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254, 879792181, 1069262793], 1))


if __name__ == '__main__':
    unittest.main()
