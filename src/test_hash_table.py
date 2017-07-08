"""Test our implementation of a hash table using a large dictionary of words."""
import pytest


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()
    list_words = words.split('\n')[:5000]


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


def test_default_size_and_hash():
    """."""
    from hash_table import HashTable
    hash_table = HashTable()
    assert (hash_table.hash,
            len(hash_table.table)) == (1, 1024)


def test_size_not_float_or_int():
    """."""
    from hash_table import HashTable
    with pytest.raises(TypeError):
        hash_table = HashTable('word')


def test_size_less_thank_512():
    """."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        hash_table = HashTable(511.9)


def test_manual_assignment_of_hash():
    """."""
    from hash_table import HashTable
    complex_hash = HashTable(hash='complex')
    naive_hash = HashTable(hash='naive')
    assert (complex_hash.hash, naive_hash.hash) == (1, 2)


def test_improper_hash_specified():
    """."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        hash_table = HashTable(hash='piglatinhash')
# @pytest.mark.parametrize('word', list_words)
# def test_parametrize_works_as_expected(word, complex_hash_table):
#     """Test that parametrize works as expected."""
#     assert complex_hash_table.get(word) == word
