"""Test merge sort."""


import pytest
from random import randint


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 17, 6, 300, 4, 3, 2, 11], [2, 3, 4, 6, 8, 9, 10, 11, 17, 300])
]


def test_merge_non_list_raises_error():
    """Entering a non-list/tuple param raises an error."""
    from merge import merge_sort
    with pytest.raises(TypeError):
        merge_sort('Hello')


def test_merge_non_int_raises_error():
    """Entering an iterable containing non-integers raises an error."""
    from merge import merge_sort
    with pytest.raises(ValueError):
        merge_sort([1, 2, 3, 5, 'burp'])


@pytest.mark.parametrize('input, expected', to_sort)
def test_merge_sort_returns_ordered_list(input, expected):
    """Merge sort returns an ordered list."""
    from merge import merge_sort
    assert merge_sort(input) == expected


def test_merge_sort_sorts_random_list():
    """Merge sort returns an ordered list."""
    from merge import merge_sort
    input = [randint(0, 1000) for i in range(100)]
    expected = sorted(input)
    assert merge_sort(input) == expected
