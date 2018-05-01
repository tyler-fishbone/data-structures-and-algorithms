import pytest
from bst import BST


@pytest.fixture
def bst_ten_values():
    """ returns a BST for a list of known values """
    return BST([5, 8, 3, 4, 1, 2, 9, 6, 7, 0])


@pytest.fixture
def bst_nine_values():
    """ returns a BST for a list of known values """
    return BST([5, 12, 3, 14, 1, 3, 9, 33, 0])


@pytest.fixture
def bst_empty():
    """ returns empty BST """
    return BST()