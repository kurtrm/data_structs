"""Implementation of quicksort in Python."""


def quick_sort(iter):
    """Sort the iterable using the merge sort method."""
    if not isinstance(iter, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if len(iter) < 2:
        return iter
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    small = []
    large = []
    pivot = iter[0]
    for idx in range(len(iter)):
        if iter[idx] < pivot and not idx == 0:
            small.append(iter[idx])
        elif iter[idx] >= pivot and not idx == 0:
            large.append(iter[idx])
    small = quick_sort(small)
    large = quick_sort(large)
    small.append(pivot)
    small.extend(large)
    return small


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'quick_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import quick_sort; from random import randint"
    )
    print("""
Quicksort is a divide and conquer algorithm. Quicksort first
divides a large array into two smaller sub-arrays: the low
elements and the high elements. Quicksort can then recursively
sort the sub-arrays.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
