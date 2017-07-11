"""Implementation of Bubble sort in Python."""


def bubble_sort(iter):
    """Sort the iterable using the Bubble sort method."""
    try:
        size = 0
        while size < (len(iter) - 1):
            size += 1
            for idx in range(len(iter) - size):
                if iter[idx] > iter[idx + 1]:
                    tmp = iter[idx + 1]
                    iter[idx + 1] = iter[idx]
                    iter[idx] = tmp
        return iter
    except TypeError:
        raise TypeError("Input only a list/tuple of integers")
