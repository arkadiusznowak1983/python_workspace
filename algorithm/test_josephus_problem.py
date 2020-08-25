import unittest
from josephus_problem import JosephusProblem
from print_as_log_writter import print


class JosephusProblemTestCase(unittest.TestCase):
    def test_safe(self):
        self.assertEqual(1, JosephusProblem().safe(1,1))
        self.assertEqual(2, JosephusProblem().safe(2,3))
        self.assertEqual(3, JosephusProblem().safe(3, 2))
        self.assertEqual(1, JosephusProblem().safe(5, 4))
        self.assertEqual(3, JosephusProblem().safe(5, 2))
    def test_linear(self):
        self.assertEqual(1, JosephusProblem().linear(1,1))
        self.assertEqual(2, JosephusProblem().linear(2,3))
        self.assertEqual(3, JosephusProblem().linear(3, 2))
        self.assertEqual(1, JosephusProblem().linear(5, 4))
        self.assertEqual(3, JosephusProblem().linear(5, 2))
        self.assertEqual(5, JosephusProblem().linear(10, 2))
    def test_fastest(self):
        self.assertEqual(1, JosephusProblem().fastest(1,1))
        self.assertEqual(2, JosephusProblem().fastest(2,3))
        self.assertEqual(3, JosephusProblem().fastest(3, 2))
        self.assertEqual(1, JosephusProblem().fastest(5, 4))
        self.assertEqual(3, JosephusProblem().fastest(5, 2))
        self.assertEqual(5, JosephusProblem().fastest(10, 2))
    def test_circle(self):
        pass
        # self.assertEqual(1, JosephusProblem().circle(1,1))
        # self.assertEqual(2, JosephusProblem().circle(2,3))
        # self.assertEqual(3, JosephusProblem().circle(3, 2))
        self.assertEqual(1, JosephusProblem().safe(5, 4))
        self.assertEqual(1, JosephusProblem().circle(5, 4))
        # self.assertEqual(3, JosephusProblem().circle(5, 2))
        # self.assertEqual(5, JosephusProblem().circle(10, 2))

if __name__ == '__main__':
    unittest.main()

