import unittest
from pow_own_idea import PowOwnIdea


class PowOwnIdeaTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(1, PowOwnIdea().pow(2, 0, type='simple'))
        self.assertEqual(128, PowOwnIdea().pow(2, 7, type='simple'))
        self.assertEqual(512, PowOwnIdea().pow(2, 9, type='simple'))
    def test_own(self):
        self.assertEqual(1, PowOwnIdea().pow(2, 0, type='own'))
        self.assertEqual(128, PowOwnIdea().pow(2, 7, type='own'))
        self.assertEqual(512, PowOwnIdea().pow(2, 9, type='own'))
        self.assertEqual(125, PowOwnIdea().pow(5, 3, type='own'))
    def test_linear(self):
        self.assertEqual(1, PowOwnIdea().pow(2, 0, type='linear'))
        self.assertEqual(128, PowOwnIdea().pow(2, 7, type='linear'))
        self.assertEqual(512, PowOwnIdea().pow(2, 9, type='linear'))
        self.assertEqual(125, PowOwnIdea().pow(5, 3, type='linear'))

if __name__ == '__main__':
    unittest.main()
