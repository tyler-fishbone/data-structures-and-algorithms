import pytest
from bst import BST
from breadth_first_traversal import breadth_first_traversal

# bst_ten_values_random
# bst_empty

def test_normal_BFT_valid(bst_ten_values_random):
    """ tests normal behavior of function """
    assert breadth_first_traversal(bst_ten_values_random) == [5,3,10,1,4,7,12]

def test_bft_with_one_val(bst_one_val):
    """ asserts good behavior with tree that only has root """
    assert breadth_first_traversal(bst_one_val) == [5]

def test_bft_with_empty_tree(bst_empty):
    """ asserts good behavior with empty tree """
    assert breadth_first_traversal(bst_empty) == False