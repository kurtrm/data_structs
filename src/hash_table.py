"""Implement a hash table in Python."""


from store_bst import BinTree


class HashTable(object):
    """Define a hash table and its methods."""

    def __init__(self, size=None, hash=None):
        """Initialize a hash table."""
        if not size:
            size = 1024
        if not hash:
            hash = 'complex'

        if type(size) not in (float, int):
            raise ValueError("Size of hash must be a positive integer, larger than 512.")
        elif size < 512:
            raise ValueError("Size must be 512 or greater.")
        else:
            self.table = [None] * size

        if hash == 'complex':
            self.hash = 1
        if hash == 'naive':
            self.hash = 2
        else:
            raise ValueError("Specified hash must be either 'complex' or 'naive'.")

    def _naive_hash(self, key):
        """Additive hash function."""
        hash = 0
        for char in key:
            hash += ord(char)
        return hash

    def _complex_hash(self, key):
        """One-at-a-time hash function."""
        hash = 0
        for char in key:
            hash += ord(char)
            hash += (hash << 10)
            hash ^= (hash >> 6)
        hash += (hash << 3)
        hash ^= (hash >> 11)
        hash += (hash << 15)

        return hash

    def get(self, key):
        """Return the value associated with the key."""
        hash = self._hash(key)
        idx = hash % len(self.table)
        the_val = self.table[idx]
        if not the_val:
            return None
        if isinstance(the_val, tuple):
            return the_val[1]
        else:
            return the_val.search(hash).store

    def set(self, key, val):
        """Store the value using the key."""
        hash = self._hash(key)
        idx = hash % len(self.table)
        if not self.table[idx]:
            self.table[idx] = (hash, val)
        else:
            existing = self.table[idx]
            if isinstance(existing, BinTree):
                existing.insert(hash, val)
            else:
                tree = BinTree()
                tree.insert(existing[0], existing[1])
                tree.insert(hash, val)
                self.table[idx] = tree

    def _hash(self, key):
        """Hash the provided key and return the hash."""
        if self.hash == 1:
            return self._complex_hash(key)
        else:
            return self._naive_hash(key)
