import unittest
from find_three_array_elements_which_sum_id_k import Interview

class InterviewTestCase(unittest.TestCase):
    def test_exception(self):
        try:
            Interview().find([1, 2], 3)
        except Exception:
            return
        self.fail('no exception appears')
    def test_correct(self):
        self.assertEqual( [5, 3, 2], Interview().find([5, 1, 6, 2, 4, 3], 10) )



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InterviewTestCase)
    unittest.TextTestRunner(verbosity=0).run(suite)
