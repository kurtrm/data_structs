"""Test our implementation of a hash table using a large dictionary of words."""
import pytest


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()
    list_words = words.split('\n')


@pytest.mark.parametrize('word', list_words)
def test_parametrize_works_as_expected(word):
    """Test that parametrize works as expected."""
    from hash_table import HashTable
    pass
