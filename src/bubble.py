"""Implementation of Bubble sort in Python."""


def bubble_sort(iter):
    """Sort the iterable using the Bubble sort method."""
    if not isinstance(iter, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    size = 0
    while size < (len(iter) - 1):
        size += 1
        for idx in range(len(iter) - size):
            if iter[idx] > iter[idx + 1]:
                tmp = iter[idx + 1]
                iter[idx + 1] = iter[idx]
                iter[idx] = tmp
    return iter


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'bubble_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import bubble_sort; from random import randint"
    )
    print("""
Bubble sort, sometimes referred to as sinking sort, is a simple
sorting algorithm that repeatedly steps through the list to be sorted,
compares each pair of adjacent items and swaps them if they are in the
wrong order.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
