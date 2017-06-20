"""Implement binary search tree."""


class Node(object):
    """Implement a node of a BST."""

    def __init__(self, val, left=None, right=None):
        """Instantiate a new BST."""
        self.val = val
        self.left = left
        self.right = right


class BinTree(object):
    """Implement a binary search tree."""

    def __init__(self, val):
        """Instantiate a new BST."""
        self._root = None
        self._size = 0
        if val is None:
            raise ValueError('Please enter an integer or iterable of integers')
        elif type(val) in [list, tuple]:
            for item in val:
                self.insert(item)

    def insert(self, val):
        """Insert a value into a BST."""
        if type(val) not in [int, float]:
            raise ValueError('Please insert only integers')
        if not self._root:
            self._root = Node(val)
            self._size += 1
        else:
            curr = self._root
            while curr:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        curr.right = Node(val)
                        self._size += 1
                        return
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(val)
                        self._size += 1
                        return
                else:
                    return

    def search(self, val):
        """Insert a value into a BST."""
        if type(val) not in [int, float]:
            raise ValueError('BST is only made of numbers')
        if not self._root:
            return None
        else:
            curr = self._root
            while curr:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        return None
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        return None
                elif val == curr.val:
                    return curr


if __name__ == '__main__':
    pass
