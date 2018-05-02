import pytest
from bst import BST


@pytest.fixture
def bst_ten_vals():
    """ returns a BST for a list of known values """
    return BST([5, 8, 3, 4, 1, 2, 9, 6, 7])


@pytest.fixture
def bst_nine_vals():
    """ returns a BST for a list of known values """
    return BST([5, 12, 3, 0, 14, 1, 3, 9, 33])


@pytest.fixture
def bst_nine_vals_negs():
    """ returns a BST for a list of known values """
    return BST([5, 12, 3, -14, 0, 1, 3, -9, 33])


@pytest.fixture
def bst_empty():
    """ returns empty BST """
    return BST()