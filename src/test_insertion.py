"""Test insertion sort."""


import pytest
from random import randint


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 17, 6, 300, 4, 3, 2, 11], [2, 3, 4, 6, 8, 9, 10, 11, 17, 300])
]


def test_insertion_non_list_raises_error():
    """Entering a non-list/tuple param raises an error."""
    from insertion import insertion_sort
    with pytest.raises(TypeError):
        insertion_sort('Hello')


def test_insertion_non_int_raises_error():
    """Entering an iterable containing non-integers raises an error."""
    from insertion import insertion_sort
    with pytest.raises(ValueError):
        insertion_sort([1, 2, 3, 5, 'burp'])


@pytest.mark.parametrize('input, expected', to_sort)
def test_insertion_sort_returns_ordered_list(input, expected):
    """Insertion sort returns an ordered list."""
    from insertion import insertion_sort
    assert insertion_sort(input) == expected


def test_insertion_sort_sorts_random_list():
    """Insertion sort returns an ordered list."""
    from insertion import insertion_sort
    input = [randint(0, 1000) for i in range(100)]
    expected = sorted(input)
    assert insertion_sort(input) == expected
