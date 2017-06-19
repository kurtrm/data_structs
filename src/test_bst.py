"""Test binary search tree."""
import pytest


def test_init_with_val():
    """."""
    from binary_search_tree import BinTree
    new_tree = BinTree(5)
    assert new_tree.val == 5
    assert new_tree.left is None
    assert new_tree.right is None


def test_init_with_iter():
    """."""
    from binary_search_tree import BinTree
    new_tree = BinTree([3, 2, 1, 4, 5])
    assert new_tree.val == 3
    assert new_tree.left.val == 2
    assert new_tree.right.val == 4
    assert new_tree.left.left.val == 1
    assert new_tree.right.right.val == 5


def test_