import pytest
# from node import Node
from queue import Queue

@pytest.fixture
def one_nine_queue():
    return Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])

@pytest.fixture
def empty_queue():
    return Queue([])

@pytest.fixture
def one_node_queue():
    return Queue([1])