import unittest
from compute_stats_refactor import *

class Test_Compute_Stats(unittest.TestCase):
    def test_read_ints(self):
        self.assertNotEqual(len(read_ints()), 0)

    def test_count_numbers(self):
        self.assertEqual(count_numbers([2, 3, 9]), 3)

    def test_summation(self):
        self.assertEqual(summation([1, 2, 3, 4, 5]), 15)

    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)

    def test_maximum(self):
        self.assertEqual(maximum([5, 8, 9]), 9)

    def test_harmonic_mean(self):
        self.assertEqual(harmonic_mean([4, 1]), 8/5)

    def test_variance(self):
        self.assertEqual(variance([2, 4]), 1)

    def test_standard_dev(self):
        self.assertEqual(standard_dev([2, 4]), 1)

if __name__ == '__main__':
    unittest.main()