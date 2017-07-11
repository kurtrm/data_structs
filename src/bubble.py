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
