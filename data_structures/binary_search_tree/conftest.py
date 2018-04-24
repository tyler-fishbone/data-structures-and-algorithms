import pytest
from .node import Node
from .bst import BST

@pytest.fixture
def bst_ten_values_random():
    """ returns a BST for a list of known values """
    return BST([5,8,3,4,1,2,9,6,7,0])

@pytest.fixture
def bst_empty():
    """ returns empty BST """
    return BST()