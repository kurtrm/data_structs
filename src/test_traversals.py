"""Test our traversal functions."""

import pytest

# in order, pre_order, post_order, breadth_first


@pytest.fixture
def binary_tree():
    """For testing."""
    from bst import BinTree
    bst = [5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11]
    bin_tree = BinTree(bst)
    return bin_tree


@pytest.fixture
def empty_bst():
    """For more testing."""
    from bst import BinTree
    bst = BinTree()
    return bst


@pytest.fixture
def small_bst():
    """For small testing."""
    from bst import BinTree
    bst = BinTree([10, 5, 11, 13, 2, 0, 20])
    return bst


# ===== In Order Traversals =====


def test_only_accepts_number(small_bst):
    """Ensure each test only accepts an integer or float."""
    with pytest.raises(TypeError):
        small_bst.in_order('stringy')


def test_node_must_be_in_binary_tree_to_start_traversal(binary_tree):
    """Ensure a node not in the tree can't be passed into the method."""
    with pytest.raises(ValueError):
        binary_tree.in_order(1000)


def test_yields_none_if_empty(empty_bst):
    """Ensure we get None if empty."""
    assert next(empty_bst.in_order()) is None


def test_starts_at_root_with_no_arguments(binary_tree):
    """starts at root."""
    generator = binary_tree.in_order()
    assert next(generator) == binary_tree._root


def test_yields_root_if_no_left_and_right(empty_bst):
    """."""
    empty_bst.insert(5)
    generator = empty_bst.in_order()
    assert next(generator) == 5


def test_yields_left_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(4)
    empty_bst.insert(3)
    empty_bst.insert(2)
    empty_bst.insert(1)
    empty_bst.insert(0)
    generator = empty_bst.in_order()
    assert list(generator) == [0, 1, 2, 3, 4, 5]


def test_yields_right_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(6)
    empty_bst.insert(7)
    empty_bst.insert(8)
    empty_bst.insert(9)
    empty_bst.insert(10)
    generator = empty_bst.in_order()
    assert list(generator) == [5, 6, 7, 8, 9, 10]


def test_v_shaped_bst():
    """Test odd shape."""
    from bst import BinTree
    beast = BinTree([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
    generator = beast.in_order()
    assert list(generator) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_big(binary_tree):
    """."""
    generator = binary_tree.in_order()
    assert list(generator) == sorted([5, -1, 1, 8, 9, 10, 17, -3, -10, 4, 2, -100, 7, -5, 0, 16, -22, 14, 3, 11])


def test_small(small_bst):
    """."""
    generator = small_bst.in_order()
    assert list(generator) == sorted([10, 5, 11, 13, 2, 0, 20])


# ===== Pre-Order Traversal =====





# ===== Post-Order Traversal =====



# ===== Breadth-First Traversal =====

