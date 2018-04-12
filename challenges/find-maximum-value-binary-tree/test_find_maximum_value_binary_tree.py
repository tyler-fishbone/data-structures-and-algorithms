import pytest
from bst import BST
from find_maximum_value_binary_tree import find_maximum_value_binary_tree


def test_normal_BFT_valid(bst_ten_values_random):
    """ tests normal behavior of function """
    assert find_maximum_value_binary_tree(bst_ten_values_random) == 12

def test_bft_with_one_val(bst_one_val):
    """ asserts good behavior with tree that only has root """
    assert find_maximum_value_binary_tree(bst_one_val) == 5

def test_bft_with_empty_tree(bst_empty):
    """ asserts good behavior with empty tree """
    assert find_maximum_value_binary_tree(bst_empty) == False