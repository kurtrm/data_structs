"""Test the trie tree."""
import pytest


with open('/usr/share/dict/words') as dictionary:
    words = dictionary.read()
list_words = words.split('\n')


@pytest.fixture
def test_trie():
    """Trie tree for testing."""
    from trie import Trie
    return Trie()


def test_insert(test_trie):
    """Test that the insert method works."""
    test_trie.insert('test')
    assert test_trie._base == {'t': {'e': {'s': {'t': {'$': {}}}}}}


def test_insert_adds(test_trie):
    """Test that insert manages words already present."""
    test_trie.insert('test')
    test_trie.insert('tests')
    assert test_trie._base == {'t': {'e': {'s': {'t': {'$': {}, 's': {'$': {}}}}}}}


def test_contains_multiple(test_trie):
    """Test the contains method."""
    test_trie.insert('test')
    test_trie.insert('tests')
    assert test_trie.contains('test')
    assert test_trie.contains('tests')


def test_does_not_contain(test_trie):
    """Test the contains method on something not in trie."""
    test_trie.insert('test')
    test_trie.insert('tests')
    assert not test_trie.contains('tes')


def test_size(test_trie):
    """Test the size of the trie."""
    test_trie.insert('test')
    test_trie.insert('tests')
    test_trie.insert('art')
    assert test_trie.size() == 3


def test_remove_method_long(test_trie):
    """Test the remove on a long string."""
    test_trie.insert('test')
    test_trie.insert('tests')
    test_trie.insert('art')
    test_trie.remove('tests')
    assert not test_trie.contains('tests')
    assert test_trie.contains('test')


def test_remove_method_short(test_trie):
    """Test the remove on a short string."""
    test_trie.insert('test')
    test_trie.insert('tests')
    test_trie.insert('art')
    test_trie.remove('test')
    assert test_trie.contains('tests')
    assert not test_trie.contains('test')


def test_traversal(test_trie):
    """Test the traversal method."""
    test_trie.insert('star')
    test_trie.insert('stars')
    test_trie.insert('start')
    test_trie.insert('starts')
    test_trie.insert('stairs')
    test_trie.insert('stair')
    ret_string = ''
    for char in test_trie.traversal('sta'):
        ret_string += char
    assert len(ret_string) == len('starstsirs')


def test_autocomplete(test_trie):
    """Test the autocomplete method."""
    test_trie.insert('star')
    test_trie.insert('stars')
    test_trie.insert('start')
    test_trie.insert('starts')
    test_trie.insert('stairs')
    test_trie.insert('stair')
    test_trie.insert('stop')
    ret_list = ['star', 'stars', 'start', 'starts', 'stairs', 'stair', 'stop']
    for word in ret_list:
        assert word in test_trie.autocomplete('st')


def test_autocomplete_does_not_return_non_words(test_trie):
    """Test that autocomplete does not return word stubs."""
    test_trie.insert('star')
    test_trie.insert('stars')
    test_trie.insert('start')
    test_trie.insert('starts')
    test_trie.insert('stairs')
    test_trie.insert('stair')
    test_trie.insert('stop')
    ret_list = ['st', 'sta', 'stai', 'sto']
    for word in ret_list:
        assert word not in test_trie.autocomplete('st')


def test_insert_not_string(test_trie):
    """Test that you can't put anything but a string in there."""
    with pytest.raises(TypeError):
        test_trie.insert(2)


def test_insert_empty_string(test_trie):
    """Test it won't accept empty string."""
    with pytest.raises(ValueError):
        test_trie.insert('')


def test_contain_not_string(test_trie):
    """Test that you can't pass anything but a string in there."""
    with pytest.raises(TypeError):
        test_trie.contains(345)


def test_contain_empty_string(test_trie):
    """Test it won't accept empty string."""
    with pytest.raises(ValueError):
        test_trie.contains('')


def test_remove_not_string(test_trie):
    """Test that you can't pass anything but a string in there."""
    with pytest.raises(TypeError):
        test_trie.remove(True)


def test_remove_empty_string(test_trie):
    """Test it won't accept empty string."""
    with pytest.raises(ValueError):
        test_trie.remove('')


def test_remove_checks_contains_word(test_trie):
    """Test that a value error is raised if word not in trie."""
    with pytest.raises(ValueError):
        test_trie.remove('banana')


def test_traversal_not_string(test_trie):
    """Test that you can't pass anything but a string in there."""
    with pytest.raises(TypeError):
        next(test_trie.traversal(True))


def test_traversal_empty_string(test_trie):
    """Test it won't accept empty string."""
    with pytest.raises(ValueError):
        next(test_trie.traversal(''))


def test_traversal_checks_contains_word(test_trie):
    """Test that a value error is raised if word not in trie."""
    test_trie.insert('starts')
    with pytest.raises(ValueError):
        next(test_trie.traversal('banana'))


def test_autocomplete_not_string(test_trie):
    """Test that you can't pass anything but a string in there."""
    with pytest.raises(TypeError):
        next(test_trie.autocomplete(True))


def test_autocomplete_empty_string(test_trie):
    """Test it won't accept empty string."""
    with pytest.raises(ValueError):
        next(test_trie.autocomplete(''))


def test_autocomplete_checks_contains_word(test_trie):
    """Test that a value error is raised if word not in trie."""
    test_trie.insert('starts')
    with pytest.raises(ValueError):
        next(test_trie.autocomplete('banana'))
