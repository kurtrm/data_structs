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

#  Left off wondering why test with no arguments is equal to self.root

# Also, exploring post and pre order test failures

def test_in_order_only_accepts_node(small_bst):
    """Ensure each test only accepts an integer or float."""
    with pytest.raises(TypeError):
        next(small_bst.in_order('stringy'))


def test_in_order_yields_none_if_empty(empty_bst):
    """Ensure we get None if empty."""
    assert next(empty_bst.in_order()) is None


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
    small_bst.insert(7)
    small_bst.insert(12)
    generator = small_bst.in_order()
    assert list(generator) == sorted([10, 5, 11, 13, 2, 0, 20, 7, 12])


# ===== Pre-Order Traversal =====


def test_pre_order_only_accepts_node(small_bst):
    """Ensure each test only accepts an integer or float."""
    with pytest.raises(TypeError):
        next(small_bst.pre_order('stringy'))


def test_pre_order_yields_none_if_empty(empty_bst):
    """Ensure we get None if empty."""
    assert next(empty_bst.pre_order()) is None


def test_pre_order_yields_root_if_no_left_and_right(empty_bst):
    """."""
    empty_bst.insert(5)
    generator = empty_bst.pre_order()
    assert next(generator) == 5


def test_pre_order_yields_left_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(4)
    empty_bst.insert(3)
    empty_bst.insert(2)
    empty_bst.insert(1)
    empty_bst.insert(0)
    generator = empty_bst.pre_order()
    assert list(generator) == [5, 4, 3, 2, 1, 0]


def test_pre_order_yields_right_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(6)
    empty_bst.insert(7)
    empty_bst.insert(8)
    empty_bst.insert(9)
    empty_bst.insert(10)
    generator = empty_bst.pre_order()
    assert list(generator) == [5, 6, 7, 8, 9, 10]


def test_pre_order_v_shaped_bst():
    """Test odd shape."""
    from bst import BinTree
    beast = BinTree([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
    generator = beast.pre_order()
    assert list(generator) == [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]


def test_pre_order_big():
    """."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    generator = beast.pre_order()
    assert list(generator) == [45, 33, 1, 0, 8, 4, 7, 10, 16, 14, 11, 44, 93, 63, 54, 49, 79, 69, 100, 94]


def test_pre_order_small():
    """."""
    from bst import BinTree
    beast = BinTree([10, 5, 11, 13, 4, 6, 12, 20, 21, 7])
    generator = beast.pre_order()
    assert list(generator) == [10, 5, 4, 6, 7, 11, 13, 12, 20, 21]


# ===== Post-Order Traversal =====


def test_post_order_only_accepts_node(small_bst):
    """Ensure each test only accepts an integer or float."""
    with pytest.raises(TypeError):
        next(small_bst.post_order('stringy'))


def test_post_order_yields_none_if_empty(empty_bst):
    """Ensure we get None if empty."""
    assert next(empty_bst.post_order()) is None


def test_post_order_yields_root_if_no_left_and_right(empty_bst):
    """."""
    empty_bst.insert(5)
    generator = empty_bst.post_order()
    assert next(generator) == 5


def test_post_order_yields_left_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(4)
    empty_bst.insert(3)
    empty_bst.insert(2)
    empty_bst.insert(1)
    empty_bst.insert(0)
    generator = empty_bst.post_order()
    assert list(generator) == [0, 1, 2, 3, 4, 5]


def test_post_order_yields_right_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(6)
    empty_bst.insert(7)
    empty_bst.insert(8)
    empty_bst.insert(9)
    empty_bst.insert(10)
    generator = empty_bst.post_order()
    assert list(generator) == [10, 9, 8, 7, 6, 5]


def test_post_order_v_shaped_bst():
    """Test odd shape."""
    from bst import BinTree
    beast = BinTree([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
    generator = beast.post_order()
    assert list(generator) == [1, 2, 3, 4, 10, 9, 8, 7, 6, 5]


def test_post_order_big():
    """."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    generator = beast.post_order()
    assert list(generator) == [0, 7, 4, 11, 14, 16, 10, 8, 1, 44, 33, 49, 54, 69, 79, 63, 94, 100, 93, 45]


def test_post_order_small():
    """."""
    from bst import BinTree
    beast = BinTree([10, 5, 11, 13, 4, 6, 12, 20, 21, 7])
    generator = beast.post_order()
    assert list(generator) == [4, 7, 6, 5, 12, 21, 20, 13, 11, 10]


# ===== Breadth-First Traversal =====


def test_breadth_yields_none_if_empty(empty_bst):
    """Ensure we get None if empty."""
    assert next(empty_bst.breadth_first()) is None


def test_breadth_yields_root_if_no_left_and_right(empty_bst):
    """."""
    empty_bst.insert(5)
    generator = empty_bst.breadth_first()
    assert next(generator) == 5


def test_breadth_first_yields_left_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(4)
    empty_bst.insert(3)
    empty_bst.insert(2)
    empty_bst.insert(1)
    empty_bst.insert(0)
    generator = empty_bst.breadth_first()
    assert list(generator) == [5, 4, 3, 2, 1, 0]


def test_breadth_first_yields_right_nodes(empty_bst):
    """."""
    empty_bst.insert(5)
    empty_bst.insert(6)
    empty_bst.insert(7)
    empty_bst.insert(8)
    empty_bst.insert(9)
    empty_bst.insert(10)
    generator = empty_bst.breadth_first()
    assert list(generator) == [5, 6, 7, 8, 9, 10]


def test_breadth_firwt_v_shaped_bst():
    """Test odd shape."""
    from bst import BinTree
    beast = BinTree([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
    generator = beast.breadth_first()
    assert list(generator) == [5, 4, 6, 3, 7, 2, 8, 1, 9, 10]


def test_breadth_first_big():
    """."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    generator = beast.breadth_first()
    assert list(generator) == [45, 33, 93, 1, 44, 63, 100, 0, 8, 54, 79, 94, 4, 10, 49, 69, 7, 16, 14, 11]


def test_breadth_first_small():
    """."""
    from bst import BinTree
    beast = BinTree([10, 5, 11, 13, 4, 6, 12, 20, 21, 7])
    generator = beast.breadth_first()
    assert list(generator) == [10, 5, 11, 4, 6, 13, 7, 12, 20, 21]


# ===== Delete =====


def test_delete_returns_none(empty_bst):
    """Ensure that delete returns None."""
    assert empty_bst.delete(1000) is None
    assert empty_bst.size() == 0


def test_delete_root(empty_bst):
    """Ensure delete can work on the root."""
    empty_bst.insert(5)
    empty_bst.insert(10)
    assert empty_bst.contains(5) is True
    assert empty_bst.size() == 2
    empty_bst.delete(5)
    assert empty_bst.contains(5) is False
    assert empty_bst.contains(10) is True
    assert empty_bst._root.val == 10
    assert empty_bst.size() == 1


def test_delete_no_children():
    """Delete works on a node with no children."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    assert beast.size() == 20
    beast.delete(11)
    assert beast.size() == 19
    assert not beast.contains(11)
    assert beast.search(14).left is None


def test_delete_one_child():
    """Delete works on a node with one child."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    assert beast.size() == 20
    beast.delete(16)
    assert beast.size() == 19
    assert not beast.contains(16)
    assert beast.search(10).right.val == 14


def test_delete_two_children():
    """Delete works on a node with one child."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    assert beast.size() == 20
    beast.delete(93)
    assert beast.size() == 19
    assert not beast.contains(93)
    assert beast._root.right.val == 79
    assert beast.search(63).right.val == 69
    assert beast.search(79).right.val == 100


def test_delete_complex_root():
    """Delete works on a node with one child."""
    from bst import BinTree
    beast = BinTree([45, 33, 1, 8, 93, 10, 63, 44, 100, 4, 79, 69, 7, 54, 0, 16, 94, 14, 49, 11])
    assert beast.size() == 20
    beast.delete(45)
    assert beast.size() == 19
    assert not beast.contains(45)
    assert beast._root.val == 44
    assert beast._root.right.val == 93
    assert beast._root.left.val == 33
    generator = beast.in_order()
    assert list(generator) == [0, 1, 4, 7, 8, 10, 11, 14, 16, 33, 44, 49, 54, 63, 69, 79, 93, 94, 100]
