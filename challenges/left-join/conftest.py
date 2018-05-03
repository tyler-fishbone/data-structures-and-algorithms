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
def left_join_list_one():
    """Resulting list from first hashtables."""
    return[
            ['fond', 'enamored', 'averse'],
            ['wrath', 'anger', 'delight'],
            ['diligent', 'employed', 'idle'],
            ['outfit', 'garb', 'follow'],
            ['guide', 'usher', 'jam']
    ]


@pytest.fixture
def left_join_list_two():
    """Resulting list from first hashtables."""
    return[
            ['fond', 'enamored', None],
            ['wrath', 'anger', None],
            ['diligent', 'employed', None],
            ['outfit', 'garb', None],
            ['guide', 'usher', None]
    ]

@pytest.fixture
def ht_empty():
    """Empty hash table."""
    ht = HashTable()
    return ht

