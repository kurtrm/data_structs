"""Test our self-balancing methods."""


import pytest


@pytest.fixture
def large_binary_tree():
    """For testing."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    return beast


@pytest.fixture
def smaller_binary_tree():
    """For more testing."""
    from bst import BinTree
    beast = BinTree([10, 5, 11, 13, 4, 6, 12, 20, 21, 7])
    return beast


@pytest.fixture
def empty_bst():
    """For more testing."""
    from bst import BinTree
    beast = BinTree()
    return beast


# initiated and balanced
# inserted and balanced
# - stays balanced
# - rebalances if conditions met
# deleted and balanced
# - stays balanced
# - rebalances if conditions met


def test_initiate_one():
    """."""
    from bst import BinTree
    beast = BinTree(10)
    assert beast.balance() == 0


def test_intiate_small():
    """."""
    from bst import BinTree
    beast = BinTree([10, 9, 8, 7, 6])
    assert beast.balance() == -1
    assert beast._root.left.val == 7
    assert beast.balance(beast._root.left) == 0


def test_initiate_big():
    """."""
    from bst import BinTree
    beast = BinTree([1, 2, 3, 4, 5, 6])
    assert beast.balance() == 0
    assert beast._root.val == 4
    assert beast.balance(beast._root.right) == 1
    assert beast._root.left.val == 2
    assert beast.balance(beast._root.left) == 0


def test_insert_into_empty(empty_bst):
    """."""


def test_insert_many_into_empty(empty_bst):
    """."""


def test_insert_into_balanced_small(smaller_binary_tree):
    """Ensure stays balanced when we expect it to."""


def test_insert_small_many_and_force_rebalance(smaller_binary_tree):
    """Ensure it rebalances correctly with a few nodes."""


def test_insert_into_balanced_large(large_binary_tree):
    """Ensure stays balanced when we expect a larger to to stay balnced."""


def test_insert_larger_many_and_force_rebalance(large_binary_tree):
    """Ensure rebalances correctly on larger binary tree."""


def test_delete_from_small_stay_balanced(smaller_binary_tree):
    """."""


def test_delete_from_small_rebalance(smaller_binary_tree):
    """Make sure the small bst  rebalances after deleting nodes."""


def test_delete_from_large_stay_balanced(large_binary_tree):
    """Ensure it stays balanced."""


def test_delete_from_large_rebalance(large_binary_tree):
    """Ensure it rebalances."""


def test_delete_many_from_small(smaller_binary_tree):
    """Ensure it passes after complex deletions."""


def test_delete_many_from_large(large_binary_tree):
    """Ensure it passes after complex deletions."""
