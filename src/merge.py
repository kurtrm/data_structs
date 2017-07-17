"""Implementation of merge sort in Python."""


def merge_sort(iter):
    """Sort the iterable using the merge sort method."""
    if not isinstance(iter, (list, tuple)):
        raise TypeError("Input only a list/tuple of integers")
    if not all(isinstance(x, (int, float)) for x in iter):
        raise ValueError("Input only a list/tuple of integers")

    if len(iter) == 1:
        return iter
    if len(iter) == 2:
        if iter[0] > iter[1]:
            tmp = iter[0]
            iter[0] = iter[1]
            iter[1] = tmp
        return iter

    mid = len(iter) // 2
    left = merge_sort(iter[:mid])
    right = merge_sort(iter[mid:])

    ret_list = []
    while left or right:
        if left and right and left[0] < right[0]:
            ret_list.append(left.pop(0))
        elif left and right and left[0] >= right[0]:
            ret_list.append(right.pop(0))
        elif left and not right:
            ret_list.extend(left)
            break
        elif right and not left:
            ret_list.extend(right)
            break
    return ret_list


if __name__ == '__main__':  # pragma: no cover
    from timeit import Timer
    random = Timer(
        'merge_sort([randint(0, 1000) for x in range(100)][::-1])',
        "from __main__ import merge_sort; from random import randint"
    )
    print("""
Conceptually, a merge sort works as follows:

1. Divide the unsorted list into n sublists, each containing 1 element (a
list of 1 element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is
only 1 sublist remaining. This will be the sorted list.
""")
    print("Random input (100 numbers from 0-1000 sorted) over 1000 trials:")
    print(random.timeit(number=1000))
