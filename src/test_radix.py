"""Test radixsort."""


import pytest
from random import randint


to_sort = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([10, 9, 8, 17, 6, 300, 4, 3, 2, 11], [2, 3, 4, 6, 8, 9, 10, 11, 17, 300])
]


to_get = [
    (713, 1, 3),
    (713, 2, 1),
    (713, 3, 7),
    (713, 4, 0),
    (518973, 5, 1)
]


to_count = [
    (713, 3),
    (518973, 6),
    (1, 1),
    (1, 1),
    (0, 1),
    (00, 1)
]


@pytest.mark.parametrize('num, place, expected', to_get)
def test_get_digit(num, place, expected):
    """Check if it returns the correct digit."""
    from radix import get_digit
    assert get_digit(num, place) == expected


@pytest.mark.parametrize('num, digits', to_count)
def test_num_digits(num, digits):
    """Return the number of digits in the number."""
    from radix import num_digits
    assert num_digits(num) == digits


def test_radix_non_list_raises_error():
    """Entering a non-list/tuple param raises an error."""
    from radix import radix_sort
    with pytest.raises(TypeError):
        radix_sort('Hello')


def test_radix_non_int_raises_error():
    """Entering an iterable containing non-integers raises an error."""
    from radix import radix_sort
    with pytest.raises(ValueError):
        radix_sort([1, 2, 3, 5, 'burp'])


@pytest.mark.parametrize('input, expected', to_sort)
def test_radix_sort_returns_ordered_list(input, expected):
    """Radix sort returns an ordered list."""
    from radix import radix_sort
    assert radix_sort(input) == expected


def test_radix_sort_sorts_random_list():
    """Radix sort returns an ordered list."""
    from radix import radix_sort
    input = [randint(0, 1000) for i in range(100)]
    expected = sorted(input)
    assert radix_sort(input) == expected
