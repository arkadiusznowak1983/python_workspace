import unittest
from wave_array_sort import WaveArraySort


class WaveArraySortTestCase(unittest.TestCase):
    # def test_sort_simple(self):
    #     self.assertEqual([3, 1, 2], WaveArraySort().waveSortSimple(arr=[2, 3, 1]))
    # def test_sort_swap(self):
    #     self.assertEqual([3, 1, 2], WaveArraySort().waveSortSwap(arr=[2, 3, 1]))
    def test_sort_web(self):
        # self.assertEqual([3, 1, 2], WaveArraySort().dialer_sort_web(arr=[2, 3, 1]))
        # self.assertEqual([90, 10, 49, 1, 5, 2, 23], WaveArraySort().dialer_sort_web(arr=[10, 90, 49, 2, 1, 5, 23]))
        self.assertEqual([90, 10, 49, 1, 5, 2, 23], WaveArraySort().sort_wave_my_own(arr=[10, 90, 49, 2, 1, 5, 23]))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WaveArraySortTestCase)
    unittest.TextTestRunner(verbosity=0).run(suite)
