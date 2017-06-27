"""Test our self-balancing methods."""


import pytest


@pytest.fixture
def large_binary_tree():
    """For testing."""
    from balance_bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 99, 34, 79, 69, 25, 54, 83, 16, 94, 14, 49, 11])
    return beast


@pytest.fixture
def smaller_binary_tree():
    """For more testing."""
    from balance_bst import BinTree
    beast = BinTree([10, 5, 11, 13, 4, 6, 12, 20, 21, 7])
    return beast


@pytest.fixture
def empty_bst():
    """For more testing."""
    from balance_bst import BinTree
    beast = BinTree()
    return beast


def test_initiate_one(empty_bst):
    """."""
    empty_bst.insert(10)
    assert empty_bst.balance() == 0


def test_intiate_small():
    """."""
    from balance_bst import BinTree
    beast = BinTree([10, 9, 8, 7, 6])
    assert beast.balance() == 1
    assert beast._root.left.val == 7
    assert beast.balance(beast._root.left) == 0


# def test_initiate_big():
#     """."""
#     from balance_bst import BinTree
#     beast = BinTree([1, 2, 3, 4, 5, 6])
#     assert beast.balance() == 0
#     assert beast._root.val == 4
#     assert beast.balance(beast._root.right) == -1
#     assert beast._root.left.val == 2
#     assert beast.balance(beast._root.left) == 0


def test_insert_into_empty(empty_bst):
    """."""
    empty_bst.insert(5)
    assert empty_bst._root.val == 5
    assert empty_bst.balance() == 0


def test_insert_many_into_empty_right(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(6)
    assert empty_bst.balance() == -1
    empty_bst.insert(7)
    assert empty_bst.balance() == 0
    assert empty_bst._root.val == 6


def test_insert_many_into_empty_left(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(4)
    assert empty_bst.balance() == 1
    empty_bst.insert(3)
    assert empty_bst.balance() == 0
    assert empty_bst._root.val == 4


def test_insert_into_balanced_small(smaller_binary_tree):
    """Ensure stays balanced when we expect it to."""
    assert smaller_binary_tree.balance(smaller_binary_tree._root.left.left) == 0
    smaller_binary_tree.insert(3)
    assert smaller_binary_tree.balance(smaller_binary_tree._root.left.left) == 1
    assert smaller_binary_tree.balance() == 0
    smaller_binary_tree.insert(9)
    assert smaller_binary_tree.balance() == 0


def test_insert_small_many_and_force_rebalance(smaller_binary_tree):
    """Ensure it rebalances correctly with a few nodes."""
    assert smaller_binary_tree.balance(smaller_binary_tree._root.left.left) == 0
    smaller_binary_tree.insert(3)
    smaller_binary_tree.insert(2)
    smaller_binary_tree.insert(1)
    assert smaller_binary_tree.balance() == 1
    assert smaller_binary_tree._root.left.left.val == 3


def test_insert_small_many_and_force_rebalance_hard_right(smaller_binary_tree):
    """Ensure it rebalances correctly with a few nodes."""
    assert smaller_binary_tree.balance(smaller_binary_tree._root.left.left) == 0
    smaller_binary_tree.insert(50)
    smaller_binary_tree.insert(60)
    smaller_binary_tree.insert(70)
    smaller_binary_tree.insert(80)
    smaller_binary_tree.insert(90)
    smaller_binary_tree.insert(91)
    smaller_binary_tree.insert(92)
    smaller_binary_tree.insert(93)
    smaller_binary_tree.insert(94)
    smaller_binary_tree.insert(95)
    smaller_binary_tree.insert(35)
    assert smaller_binary_tree.balance() == 0
    assert smaller_binary_tree._root.val == 20
    assert smaller_binary_tree._root.left.val == 10
    assert smaller_binary_tree.balance(smaller_binary_tree._root.left.left) == -1
    assert smaller_binary_tree.balance(smaller_binary_tree._root.left.right) == 0
    assert smaller_binary_tree._root.left.right.val == 12
    assert smaller_binary_tree._root.right.val == 70


def test_insert_into_balanced_large(large_binary_tree):
    """Ensure stays balanced when we expect a larger to to stay balnced."""
    assert large_binary_tree.balance(large_binary_tree._root.left.left) == 1
    large_binary_tree.insert(27)
    large_binary_tree.insert(9)
    large_binary_tree.insert(15)
    assert large_binary_tree.balance() == 0
    assert large_binary_tree.balance(large_binary_tree._root.left) == -1
    large_binary_tree._root.left.right.left.val == 14
    large_binary_tree.balance(large_binary_tree._root.left.right.right) == -1


def test_insert_larger_many_and_force_rebalance(large_binary_tree):
    """Ensure rebalances correctly on larger binary tree."""
    large_binary_tree.delete(11)
    assert large_binary_tree.balance(large_binary_tree._root.left.left) == 1
    large_binary_tree.insert(55)
    large_binary_tree.insert(53)
    large_binary_tree.insert(52)
    assert large_binary_tree.balance() == 0
    assert large_binary_tree.balance(large_binary_tree._root.left.left) == 0


def test_delete_from_small_stay_balanced(smaller_binary_tree):
    """."""
    smaller_binary_tree.delete(7)
    assert smaller_binary_tree.balance() == -1
    smaller_binary_tree.delete(13)
    smaller_binary_tree.delete(21)
    assert smaller_binary_tree.balance() == 0


def test_delete_from_small_rebalance(smaller_binary_tree):
    """Make sure the small bst  rebalances after deleting nodes."""
    smaller_binary_tree.delete(12)
    smaller_binary_tree.delete(13)
    smaller_binary_tree.delete(20)
    smaller_binary_tree.delete(21)
    assert smaller_binary_tree._root.val == 6
    assert smaller_binary_tree.balance(smaller_binary_tree._root.right) == 0
    assert smaller_binary_tree._root.right.val == 10
    assert smaller_binary_tree._root.left.val == 5


def test_delete_from_large_stay_balanced(large_binary_tree):
    """Ensure it stays balanced."""
    assert large_binary_tree.balance() == 0
    large_binary_tree.delete(45)
    large_binary_tree.delete(79)
    large_binary_tree.delete(99)
    large_binary_tree.delete(44)
    large_binary_tree.delete(63)
    assert large_binary_tree.balance() == 1


def test_delete_from_large_rebalance(large_binary_tree):
    """Ensure it rebalances."""
    large_binary_tree.delete(11)
    large_binary_tree.delete(1)
    large_binary_tree.delete(14)
    large_binary_tree.delete(25)
    assert large_binary_tree._root.val == 63
    assert large_binary_tree.balance() == 1
    assert large_binary_tree.balance(large_binary_tree._root.left.right) == -1
