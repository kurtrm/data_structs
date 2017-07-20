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
            raise TypeError('Insert takes in one param which must be a string')
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
            raise TypeError('Contains takes in one param which must be a string')
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
            raise TypeError('Remove takes in one param which must be a string')
        if not word or word == '':
            raise ValueError('Please enter a string')

        if not self.contains(word):
            raise ValueError('String not in trie')
        else:
            curr = self._base
            last_word = curr
            next_letter = word[0]
            for idx, char in enumerate(word):
                if '$' in curr[char] and not idx == (len(word) - 1):
                    last_word = curr[char]
                    next_letter = word[idx + 1]
                    curr = curr[char]
                elif idx == (len(word) - 1):
                    if len(curr[char]) > 1:
                        del curr[char]['$']
                    else:
                        del last_word[next_letter]
                        break
                else:
                    curr = curr[char]

    def traversal(self, start, last=None):
        """Perform a DFT of the trie from a specified start."""
        if not isinstance(start, str):
            raise TypeError('Traversal takes in one param which must be a string')
        if not start or start == '':
            raise ValueError('Please enter a string')
        if not last:
            curr = self._base
            for idx, char in enumerate(start):
                if idx == (len(start) - 1) and char in curr:
                    yield start
                    curr = curr[char]
                    for char in curr:
                        if not char == '$':
                            yield char
                            for each_char in self.traversal(start, curr[char]):
                                yield each_char
                elif char in curr:
                    curr = curr[char]
                else:
                    raise ValueError('String not in trie')
        else:
            for char in last:
                if not char == '$':
                    yield char
                    for each_char in self.traversal(start, last[char]):
                        yield each_char

    def autocomplete(self, start, last=None):
        """Autocomplete a string with all possible words."""
        if not isinstance(start, str):
            raise TypeError('Traversal takes in one param which must be a string')
        if not start or start == '':
            raise ValueError('Please enter a string')
        words = []
        if not last:
            curr = self._base
            for idx, char in enumerate(start):
                if idx == (len(start) - 1) and char in curr:
                    curr = curr[char]
                    for char in curr:
                        if char == '$':
                            words.append(start)
                        if not char == '$':
                            next = start + char
                            words.extend(self.autocomplete(next, curr[char]))
                elif char in curr:
                    curr = curr[char]
                else:
                    raise ValueError('String not in trie')
        else:
            for char in last:
                if char == '$':
                    words.append(start)
                if not char == '$':
                    next = start + char
                    words.extend(self.autocomplete(next, last[char]))
        return words
