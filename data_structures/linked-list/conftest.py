import pytest
from linked_list import LinkedList as LL
from node import Node

@pytest.fixture
def empty_ll():
    """
    creates empty linked list for testing
    """
    return LL()

@pytest.fixture
def small_ll():
    """
    creates linked list with iter for testing
    """
    return LL([5,6,7,8])

@pytest.fixture
def node_val_1():
    """
    creates single node for testing
    """
    return Node(1)
