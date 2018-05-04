import pytest
from hash_table import HashTable

@pytest.fixture
def ht_syn_one():
    """Hash table of words and their synonyms."""
    ht = HashTable(10)
    # import pdb; pdb.set_trace()
    ht.set('fond', 'enamored')
    ht.set('wrath', 'anger')
    ht.set('diligent', 'employed')
    ht.set('outfit', 'garb')
    ht.set('guide', 'usher')
    return ht


@pytest.fixture
def ht_ant_one():
    """Hash table of words and their antonyms."""
    ht = HashTable(10)
    ht.set('fond', 'averse')
    ht.set('wrath', 'delight')
    ht.set('diligent', 'idle')
    ht.set('outfit', 'follow')
    ht.set('guide', 'jam')
    return ht


@pytest.fixture
def ht_ant_two():
    """Hash table of words and their antonyms."""
    ht = HashTable(10)
    ht.set('fond', 'averse')
    ht.set('diligent', 'idle')
    ht.set('guide', 'jam')
    return ht


@pytest.fixture
def left_join_list_one():
    """Resulting list from first hashtables."""
    return[
            ['wrath', 'anger', 'delight'],
            ['fond', 'enamored', 'averse'],
            ['guide', 'usher', 'jam'],
            ['outfit', 'garb', 'follow'],
            ['diligent', 'employed', 'idle'],
    ]


@pytest.fixture
def left_join_list_two():
    """Resulting list from first hashtables."""
    return[
            ['wrath', 'anger', None],
            ['fond', 'enamored', 'averse'],
            ['guide', 'usher', 'jam'],
            ['outfit', 'garb', None],
            ['diligent', 'employed', 'idle'],
    ]


@pytest.fixture
def left_join_list_three():
    """Resulting list from first hashtables."""
    return[
            ['wrath', 'anger', None],
            ['fond', 'enamored', None],
            ['guide', 'usher', None],
            ['outfit', 'garb', None],
            ['diligent', 'employed', None],
    ]

@pytest.fixture
def ht_empty():
    """Empty hash table."""
    ht = HashTable(10)
    return ht

