"""Test our implementation of a hash table using a large dictionary of words."""
import pytest
import random


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()
list_words = words.split('\n')


random_words = random.sample(list_words, 500)


@pytest.fixture
def complex_hash_table():
    """Hash table for testing."""
    from hash_table import HashTable
    hash_table = HashTable(hash_function='complex')
    for word in random_words:
        hash_table.set(word, word)
    return hash_table


def test_default_size_and_hash():
    """."""
    from hash_table import HashTable
    hash_table = HashTable()
    assert (hash_table.hash_function,
            len(hash_table.table)) == (1, 1024)


def test_size_not_float_or_int():
    """."""
    from hash_table import HashTable
    with pytest.raises(TypeError):
        hash_table = HashTable('word')


def test_size_less_than_512():
    """."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        hash_table = HashTable(511.9)


def test_manual_assignment_of_hash():
    """."""
    from hash_table import HashTable
    complex_hash = HashTable(hash_function='complex')
    naive_hash = HashTable(hash_function='naive')
    assert (complex_hash.hash_function, naive_hash.hash_function) == (1, 2)


def test_improper_hash_specified():
    """."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        hash_table = HashTable(hash_function='piglatinhash')


def test_naive_hash_is_dumb():
    """."""
    from hash_table import HashTable
    hash_table = HashTable(hash_function='naive')
    hash_table._hash('Apollo') == hash_table._hash('Bunker')


def test_naive_hash_causes_many_collisions():
    """."""
    from hash_table import HashTable
    hash_table = HashTable(hash_function='naive')
    equal = True
    while equal is True:
        sample_words = random.sample(list_words, 50)
        for word in sample_words:
            hash_table.set(word, word)
        hash_table_words = [hash_table.get(word) for word in sample_words]
        equal = hash_table_words == sample_words
    assert not equal


@pytest.mark.parametrize('word', random_words)
def test_that_we_get_correct_words(word, complex_hash_table):
    """."""
    assert complex_hash_table.get(word) == word


def test_that_we_get_none_if_key_not_found(complex_hash_table):
    """Test that parametrize works as expected."""
    assert complex_hash_table.get("Supercalifragilistic") is None
