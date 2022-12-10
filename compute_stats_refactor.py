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
    try:
        f = open(file, 'r')

        lines = f.readlines()

        data = [int(x) for x in lines]

        return data
    except FileNotFoundError:
        print("The file doesn't exist")

    

def count_numbers(data = None):
    if data == None:
        data = read_ints()
    try:
        return len(data)
    except TypeError:
        print(f"{data} has no attribute len: data passes should be of type list, tuple, or array")
    

def summation(data=None):
    if data == None:
        data = read_ints()
    try:
        return sum(data)
    except TypeError:
        print("data {data} should be iterable")

def average(data=None):
    if data == None:
        data = read_ints()
    try:
        return sum(data)/len(data)
    except ZeroDivisionError:
        print("ZeroDivisionError: It should have at least one integers in the data passed to compute average")
    except TypeError:
        print(f"data {data} should be iterable")
    


def minimum(data=None):
    if data == None:
        data = read_ints()

    try:
        return min(data)
    except TypeError:
        print(f"data {data} should be iterable")
    except ValueError:
        print(f"data {data} passed should have at least one element")


def maximum(data=None):
    if data == None:
        data = read_ints()

    try:
        return max(data)
    except TypeError:
        print(f"data {data} should be iterable")
    except ValueError:
        print(f"data {data} passed should have at least one element")

def harmonic_mean(data = None):
    if data == None:
        data = read_ints()
    
    inv_data = []
    for x in data:
        try:
            inv_data.append(1/x)
        except ZeroDivisionError:
            print("All integers passed should be different from 0")
    try:
        return len(data)/sum(inv_data)
    except TypeError:
        print("data passed should be iterable")
    


def variance(data=None):
    if data == None:
        data = read_ints()
    try:
        avg = sum(data)/len(data)

        return sum([(x-avg)**2 for x in data])/len(data)
    except TypeError:
        print("data passed should be iterable")
    except ZeroDivisionError:
        print("it should have at least one element in the data passed")
    

def standard_dev(data=None):
    if data == None:
        data = read_ints()
    try:
        avg = sum(data)/len(data)

        return math.sqrt(sum([(x-avg)**2 for x in data])/len(data))
    except TypeError:
        print("data passed should be iterable")
    except ZeroDivisionError:
        print("it should have at least one element in the data passed")




if __name__ == '__main__':
    compute_stats()