"""Implement binary search tree."""


class Node(object):
    """Implement a binary search tree."""

    def __init__(self, val, left=None, right=None):
        """."""
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """."""

    def __int__(self, iterable=None):
        """."""
        self.root = None
        if iterable:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.insert(element)

    def insert(self, val):
        """."""
        if type(val) not in [float, int]:
            raise TypeError('Hey dude, you can only insert numbers.')

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
        """."""
        if type(val) not in [float, int]:
            raise TypeError('Hey dude, you can only insert numbers.')

        curr = self._root
        while curr:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                    continue
                else:
                    return
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                    continue
                else:
                    return
            else:
                return curr


if __name__ == '__main__':
    pass
