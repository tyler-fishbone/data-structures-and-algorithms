import pytest
from linked_list import LinkedList as LL
from node import Node

@pytest.fixture
def node_val_1():
    """
    creates single node for testing
    """
    return Node(1)

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
def one_four_ll():
    """
    creates linked list with with values 1-4
    """
    return LL([1,2,3,4])

@pytest.fixture
def a_d_ll():
    """
    creates linked list with with values a, b, c, d
    """
    return LL(['a', 'b', 'c', 'd'])

@pytest.fixture
def a_b_cap_ll():
    """
    creates linked list with with values a, b, c, d
    """
    return LL(['A', 'B'])

