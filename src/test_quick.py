"""Test quicksort."""


import pytest
from random import randint


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 17, 6, 300, 4, 3, 2, 11], [2, 3, 4, 6, 8, 9, 10, 11, 17, 300])
]


def test_quick_non_list_raises_error():
    """Entering a non-list/tuple param raises an error."""
    from quick import quick_sort
    with pytest.raises(TypeError):
        quick_sort('Hello')


def test_quick_non_int_raises_error():
    """Entering an iterable containing non-integers raises an error."""
    from quick import quick_sort
    with pytest.raises(ValueError):
        quick_sort([1, 2, 3, 5, 'burp'])


@pytest.mark.parametrize('input, expected', to_sort)
def test_quick_sort_returns_ordered_list(input, expected):
    """Quick sort returns an ordered list."""
    from quick import quick_sort
    assert quick_sort(input) == expected


def test_quick_sort_sorts_random_list():
    """Quick sort returns an ordered list."""
    from quick import quick_sort
    input = [randint(0, 1000) for i in range(100)]
    expected = sorted(input)
    assert quick_sort(input) == expected
