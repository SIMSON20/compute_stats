import unittest
import math

def compute_stats():
    """
    Docstring
    Displays statistics (count, sum, avg, min, and max)
    on a set of integers read from a txt file.
    """
    print(f'total = {count_numbers()}')
    print(f'summation = {summation()}')
    print(f'average = {round(average())}')
    print(f'Minimum = {minimum()}')
    print(f'Maximum = {maximum()}')

file = 'random_nums.txt'

def read_ints():
    
    f = open(file, 'r')

    lines = f.readlines()

    data = [int(x) for x in lines]

    return data

def count_numbers(data = None):
    if data == None:
        return len(read_ints())
    else:
        return len(data)

def summation(data=None):
    if data == None:
        return sum(read_ints())
    else:
        return sum(data)

def average(data=None):
    if data == None:
        return summation()/count_numbers()
    else:
        return sum(data)/len(data)

def minimum(data=None):
    if data == None:
        return min(read_ints())
    else:
        return min(data)

def maximum(data=None):
    if data == None:
        return max(read_ints())
    else:
        return max(data)

def harmonic_mean(data = None):
    if data == None:
        data = read_ints()
    inv_data = [1/x for x in data]
    return len(data)/sum(inv_data)


def variance(data=None):
    if data == None:
        data = read_ints()

    avg = sum(data)/len(data)

    return sum([(x-avg)**2 for x in data])/len(data)

def standard_dev(data=None):
    if data == None:
        data = read_ints()

    avg = sum(data)/len(data)

    return math.sqrt(sum([(x-avg)**2 for x in data])/len(data))


class Test_Additional_Stats(unittest.TestCase):
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
    compute_stats()
    unittest.main()