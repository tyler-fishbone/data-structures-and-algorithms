import pytest

from bst import BST

@pytest.fixture
def bst_ten_values_random():
    """ returns a BST for a list of known values """
    return BST([5,3,1,4,10,7,12])

@pytest.fixture
def bst_one_val():
    """ returns a BST for one value """
    return BST([5])

@pytest.fixture
def bst_empty():
    """ returns empty BST """
    return BST()