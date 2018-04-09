import pytest

from bst import BST

@pytest.fixture
def bst_ten_values_random():
    """ returns a BST for a list of known values """
    return BST([5,1,15,9,6,7,5,2])

@pytest.fixture
def bst_empty():
    """ returns empty BST """
    return BST()