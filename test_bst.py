"""Test binary search tree."""
import pytest


@pytest.fixture
def binary_tree():
    """Binary tree for testing."""
    from bst import BinTree
    new_tree = BinTree(5)


@pytest.fixture
def bigger_binary_tree():
    """Larger binary tree for testing."""
    from bst import BinTree
    binary_tree.insert(8)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(7)
    binary_tree.insert(9)


def test_init_with_val():
    """."""
    from bst import BinTree
    new_tree = BinTree(5)
    assert new_tree.val == 5
    assert new_tree.left is None
    assert new_tree.right is None


def test_init_with_iter():
    """."""
    from bst import BinTree
    new_tree = BinTree([3, 2, 1, 4, 5])
    assert new_tree.val == 3
    assert new_tree.left.val == 2
    assert new_tree.right.val == 4
    assert new_tree.left.left.val == 1
    assert new_tree.right.right.val == 5


def test_init_with_non_int():
    """Must accept int or list of ints for now."""
    from bst import BinTree
    with pytest.raises(ValueError):
        new_tree = BinTree("new tree")


def test_init_with_none():
    """Cannot be initialized with nothing."""
    from bst import BinTree
    new_tree = BinTree()
    new_tree.val is None
    new_tree.left is None
    new_tree.right is None


def test_insert_smaller(binary_tree):
    """Test insertion success."""
    binary_tree.insert(4)
    assert binary_tree.left.val == 4
    assert binary_tree.right.val is None


def test_insert_larger(binary_tree):
    """Test insertion success."""
    binary_tree.insert(6)
    assert binary_tree.left.val is None
    assert binary_tree.right.val == 6


def test_insert_smaller_isolated(binary_tree):
    """Test insertion with a left node already there."""
    binary_tree.insert(4)
    binary_tree.insert(6)
    assert binary_tree.left.val == 4
    assert binary_tree.right.val == 6


def test_insert_larger_isolated(binary_tree):
    """Test insertion with a right node already there."""
    binary_tree.insert(6)
    binary_tree.insert(4)
    assert binary_tree.left.val == 4
    assert binary_tree.right.val == 6


def test_insert_depth(binary_tree):
    """Test insertion continues recursively down the tree."""
    binary_tree.insert(8)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(7)
    binary_tree.insert(9)
    assert binary_tree.left.left.val == 1
    assert binary_tree.left.right.val == 3
    assert binary_tree.right.left.val == 7
    assert binary_tree.right.right.val == 9


def test_no_inserting_non_numbers(binary_tree):
    """."""
    with pytest.raises(ValueError):
        binary_tree.insert('a tree')


def test_search(binary_tree):
    """Test that we are returned a node containing the value.

    Not really sure what we're actually returning here.
    """
    assert isinstance(binary_tree.search(5), BinTree)
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


def test_contains_given_none_raises_exception(bigger_binary_tree):
    """Test error raised."""
    with pytest.raises(ValueError):
        bigger_binary_tree.contains()


def test_balance(bigger_binary_tree, binary_tree):
    """Test correct balance."""
    assert bigger_binary_tree.balance() == 3
    assert binary_tree.balance() == 0


def test_balance_right(binary_tree):
    """Test balance right."""
    binary_tree.insert(10)
    binary_tree.insert(7)
    binary_tree.insert(2)
    binary_tree.insert(13)
    binary_tree.insert(9)
    assert binary_tree.balance() == -3
