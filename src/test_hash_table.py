"""Test our implementation of a hash table using a large dictionary of words."""
import pytest


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()
    list_words = words.split('\n')


@pytest.fixture
def naive_hash_table():
    """Hash table for testing."""
    from hash_table import HashTable
    hash_table = HashTable(hash='naive')
    for word in list_words:
        hash_table.set(word, word)
    return hash_table


@pytest.fixture
def complex_hash_table():
    """Hash table for testing."""
    from hash_table import HashTable
    hash_table = HashTable(hash='complex')
    # import pdb; pdb.set_trace()
    for word in list_words:
        hash_table.set(word, word)
    return hash_table


@pytest.mark.parametrize('word', list_words)
def test_parametrize_works_as_expected(word, complex_hash_table):
    """Test that parametrize works as expected."""
    assert complex_hash_table.get(word) == word
