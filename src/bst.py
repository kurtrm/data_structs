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

    def __init__(self, val=None):
        """Instantiate a new BST."""
        self._root = None
        self._size = 0
        if type(val) in [list, tuple]:
            for item in val:
                self.insert(item)
        elif val:
            raise ValueError('BST only accepts optional parameter or a list or tuple')

    def insert(self, val):
        """Insert a value into a BST."""
        if type(val) not in [int, float]:
            raise ValueError('Please insert only integers or floats')
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

    def contains(self, val):
        """Check to see if the BST contains a value."""
        if self.search(val):
            return True
        return False

    def size(self):
        """Return the total number of nodes in the BST."""
        return self._size

    def depth(self, node=None):
        """Find the depth of a specified node."""
        if not node:
            node = self._root
            if not node:
                return 0

        l_depth = 0
        r_depth = 0

        if node.left:
            l_depth = self.depth(node.left)
        if node.right:
            r_depth = self.depth(node.right)

        if not node.left and not node.right:
            return 1
        elif l_depth >= r_depth:
            return l_depth + 1
        elif l_depth < r_depth:
            return r_depth + 1

    def balance(self):
        """Return an integer representing if the tree is balanced or not."""
        start = self._root
        if not start:
            return 0

        l_depth = 0
        r_depth = 0
        if start.left:
            l_depth = self.depth(start.left)
        if start.right:
            r_depth = self.depth(start.right)
        return l_depth - r_depth

    def in_order(self, node=None):
        """Traverse the list in order."""
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_val in self.in_order(node.left):
                yield each_val
        yield node.val
        if node.right:
            for each_val in self.in_order(node.right):
                yield each_val

    def pre_order(self, node=None):
        """Traverse the list in pre-order."""
        if not node:
            node = self._root
            if not node:
                yield None
        yield node.val
        if node.left:
            for each_val in self.in_order(node.left):
                yield each_val
        if node.right:
            for each_val in self.in_order(node.right):
                yield each_val

    def post_order(self, node=None):
        """Traverse the list in post-order."""
        if not node:
            node = self._root
            if not node:
                yield None
        if node.left:
            for each_val in self.in_order(node.left):
                yield each_val
        if node.right:
            for each_val in self.in_order(node.right):
                yield each_val
        yield node.val

    def breadth_first(self):
        """Perform a BFT on the BST."""
        if not self._root:
            yield None
        yield self._root.val
        traverse = []
        if self._root.left:
            traverse.append(self._root.left)
        if self._root.right:
            traverse.append(self._root.right)
        for node in traverse:
            yield node.val
            if node.left:
                traverse.append(node.left)
            if node.right:
                traverse.append(node.right)


if __name__ == '__main__':
    pass
