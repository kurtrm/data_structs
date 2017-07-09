"""Test binary search tree."""
import pytest


@pytest.fixture
def binary_tree():
    """Binary tree for testing."""
    from bst import BinTree
    new_tree = BinTree()
    new_tree.insert(5)
    return new_tree


@pytest.fixture
def bigger_binary_tree():
    """Larger binary tree for testing."""
    from bst import BinTree
    new_tree = BinTree([8, 2, 3, 1, 7, 9, 10])
    return new_tree


def test_init_with_empty_bst():
    """Test to see if an empty BST has a root or size."""
    from bst import BinTree
    new_tree = BinTree()
    assert new_tree._root is None
    assert new_tree._size == 0


def test_init_with_val(binary_tree):
    """Test to see if a single depth BST has a root."""
    assert binary_tree._root.val == 5
    assert binary_tree._root.left is None
    assert binary_tree._root.right is None
    assert binary_tree._size == 1


def test_init_with_iter():
    """Test to see if instantiating with an iterable works."""
    from bst import BinTree
    new_tree = BinTree([3, 2, 1, 4, 5])
    assert new_tree._root.val == 3
    assert new_tree._root.left.val == 2
    assert new_tree._root.right.val == 4
    assert new_tree._root.left.left.val == 1
    assert new_tree._root.right.right.val == 5


def test_insert_with_non_int():
    """Test that it only accepts a list or tuple as the optional param."""
    from bst import BinTree
    with pytest.raises(ValueError):
        BinTree('this should break it')


def test_insert_smaller(binary_tree):
    """Test insertion success."""
    binary_tree.insert(4)
    assert binary_tree._root.left.val == 4
    assert binary_tree._root.right is None


def test_insert_larger(binary_tree):
    """Test insertion success."""
    binary_tree.insert(6)
    assert binary_tree._root.left is None
    assert binary_tree._root.right.val == 6


def test_insert_smaller_isolated(binary_tree):
    """Test insertion with a left node already there."""
    binary_tree.insert(4)
    binary_tree.insert(6)
    assert binary_tree._root.left.val == 4
    assert binary_tree._root.right.val == 6


def test_insert_larger_isolated(binary_tree):
    """Test insertion with a right node already there."""
    binary_tree.insert(6)
    binary_tree.insert(4)
    assert binary_tree._root.left.val == 4
    assert binary_tree._root.right.val == 6


def test_insert_depth(binary_tree):
    """Test insertion continues recursively down the tree."""
    binary_tree.insert(8)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(7)
    binary_tree.insert(9)
    assert binary_tree._root.left.left.val == 1
    assert binary_tree._root.left.right.val == 3
    assert binary_tree._root.right.left.val == 7
    assert binary_tree._root.right.right.val == 9


def test_no_inserting_non_numbers(binary_tree):
    """Test to see if the insert method only accepts numbers."""
    with pytest.raises(ValueError):
        binary_tree.insert('a tree')


def test_search_with_non_number(binary_tree):
    """Test to see if searching for a string returns an error."""
    with pytest.raises(ValueError):
        binary_tree.search('a tree')


def test_search(binary_tree):
    """Test that we are returned a node containing the value.

    Not really sure what we're actually returning here.
    """
    from bst import Node
    assert isinstance(binary_tree.search(5), Node)
    assert binary_tree.search(0) is None


def test_search_more(binary_tree):
    """Test that search can navigate multiple BinTrees."""
    binary_tree.insert(8)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(7)
    binary_tree.insert(9)
    assert binary_tree.search(7)  # True
    assert binary_tree.search(3)  # True
    assert binary_tree.search(15) is None


def test_size(binary_tree):
    """Test that we get the correct size."""
    binary_tree.size() == 1
    binary_tree.insert(3)
    binary_tree.size() == 2


def test_depth(binary_tree):
    """Test thatt get the correct depth."""
    binary_tree.insert(8)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(7)
    binary_tree.insert(9)
    assert binary_tree.depth() == 3
    binary_tree.insert(11)
    assert binary_tree.depth() == 4


def test_depth_left(binary_tree):
    """Test that we go deep left."""
    binary_tree.insert(4)
    binary_tree.insert(3)
    binary_tree.insert(2)
    binary_tree.insert(1)
    assert binary_tree.depth() == 5


def test_depth_right(binary_tree):
    """Test that we go deep right."""
    binary_tree.insert(6)
    binary_tree.insert(7)
    binary_tree.insert(8)
    binary_tree.insert(9)
    binary_tree.insert(10)
    assert binary_tree.depth() == 6


def test_depth_none():
    """Test that we get none back if empty bst."""
    from bst import BinTree
    binary_tree = BinTree()
    binary_tree.depth() == 0


def test_contains(bigger_binary_tree):
    """Test value is either in there or not."""
    bigger_binary_tree.contains(8) is True
    bigger_binary_tree.contains(3) is True
    bigger_binary_tree.contains(17) is False


def test_balance(bigger_binary_tree, binary_tree):
    """Test correct balance."""
    assert bigger_binary_tree.balance() == 1
    assert binary_tree.balance() == 0


def test_balance_right(binary_tree):
    """Test balance right."""
    binary_tree.insert(10)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(13)
    binary_tree.insert(9)
    assert binary_tree.balance() == -2
