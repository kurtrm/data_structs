"""Implementation of insertion sort in Python."""


def insertion_sort(iter):
    """Sort the iterable using the insertion sort method."""
    if not isinstance(iter, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    for idx in range(len(iter)):
        move = iter[idx]
        countdown = idx
        next_largest = idx
        while countdown > 0:
            if iter[countdown - 1] > move:
                next_largest = countdown - 1
            countdown -= 1
        del iter[idx]
        iter.insert(next_largest, move)
    return iter


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'insertion_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import insertion_sort; from random import randint"
    )
    print("""
Insertion sort iterates, consuming one input element each repetition,
and growing a sorted output list. At each iteration, insertion sort
removes one element from the input data, finds the location it belongs
within the sorted list, and inserts it there. It repeats until no input
elements remain.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
