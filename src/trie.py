"""Implement a trie in Python."""


class Trie(object):
    """Define a trie and its methods."""

    def __init__(self):
        """Initialize a trie."""
        self._base = {}
        self._size = 0

    def insert(self, word):
        """Insert an input string into the trie."""
        if not isinstance(word, str):
            raise TypeError('Insert takes in one parameter which must be a string')
        if not word or word == '':
            raise ValueError('Please enter a string')

        curr = self._base
        for idx, char in enumerate(word):
            if idx == (len(word) - 1) and char not in curr:
                curr[char] = {}
                curr[char]['$'] = {}
                self._size += 1
            elif idx == (len(word) - 1) and char in curr and '$' not in curr[char]:
                curr[char]['$'] = {}
                self._size += 1
            elif char in curr:
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]

    def contains(self, word):
        """Check to see if a given word is contained in the trie."""
        if not isinstance(word, str):
            raise TypeError('Contains takes in one parameter which must be a string')
        if not word or word == '':
            raise ValueError('Please enter a string')

        curr = self._base
        for idx, char in enumerate(word):
            if idx == (len(word) - 1) and char in curr and '$' in curr[char]:
                return True
            elif char in curr:
                curr = curr[char]
            else:
                return False
        return False

    def size(self):
        """Return the total number of words in the trie."""
        return self._size

    def remove(self, word):
        """Remove the specified word from the trie."""
        if not isinstance(word, str):
            raise TypeError('Remove takes in one parameter which must be a string')
        if not word or word == '':
            raise ValueError('Please enter a string')

        if not self.contains(word):
            raise ValueError('String not in trie')
        else:
            pass
