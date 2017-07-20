"""Implementation of radix sort in Python."""


import math


def radix_sort(iter):
    """Sort the iterable using the radix sort method."""
    if not isinstance(iter, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    places = 0
    for num in iter:
        digits = num_digits(num)
        if digits > places:
            places = digits

    for place in range(1, places + 1):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for num in iter:
            digit = get_digit(num, place)
            bucket[digit].append(num)
        iter = []
        for sub in bucket:
            for number in sub:
                iter.append(number)
    return iter


def get_digit(num, place):  # found this on Stack Overflow, I think
    """Return the Place-th digit of num."""
    return int(num / 10 ** (place - 1)) % 10


def num_digits(num):
    """Give the length of a given number."""
    if num > 0:
        return int(math.log10(num)) + 1
    elif num == 0:
        return 1


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'radix_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import radix_sort; from random import randint"
    )
    print("""
Radix sort is a non-comparative integer sorting algorithm that sorts
data with integer keys by grouping keys by the individual digits
which share the same significant position and value.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
