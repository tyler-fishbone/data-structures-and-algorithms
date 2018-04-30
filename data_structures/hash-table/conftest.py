import pytest

@pytest.fixture
def hash_table_empty_size_ten():
    """Create hash table with 10 buckets."""
    return HashTable(10)