from .node import Node
import pytest
from .bst import BST

def test_bst_root(bst_ten_values_random):
    """tests self.root on passed in iter """
    assert bst_ten_values_random.root.val == 5

def test_bst_empty_root(bst_empty):
    """tests for self.root on passed empty bst """
    assert bst_empty.root == None

def test_bst_single_node():
    """ tests creation of bst with only one node """
    assert BST(1).root is None

def test_bst_insert(bst_empty):
    """ tests instert method """
    bst_empty.insert(5)
    assert bst_empty.root.val == 5
    bst_empty.insert(6)
    assert bst_empty.root.right.val == 6

def test_bst_in_order_normal(bst_ten_values_random):
    """ tests bst comes out in correct order"""
    check_list = []
    bst_ten_values_random.in_order_trav(lambda x: check_list.append(x.val))
    assert check_list == [0,1,2,3,4,5,6,7,8,9]

def test_bst_empty_in_order(bst_empty):
    """ tests bst in order method on empty bst"""
    check_list = []
    bst_empty.in_order_trav(lambda x: check_list.append(x.val))
    assert check_list == []

def test_bst_pre_order_normal(bst_ten_values_random):
    """ tests bst comes out in correct order"""
    check_list = []
    bst_ten_values_random.pre_order_trav(lambda x: check_list.append(x.val))
    assert check_list == [5,3,1,0,2,4,8,6,7,9]

def test_bst_empty_pre_order(bst_empty):
    """ tests bst pre order method on empty bst"""
    check_list = []
    bst_empty.pre_order_trav(lambda x: check_list.append(x.val))
    assert check_list == []

def test_bst_post_order_normal(bst_ten_values_random):
    """ tests bst comes out in correct order"""
    check_list = []
    bst_ten_values_random.post_order_trav(lambda x: check_list.append(x.val))
    assert check_list == [0,2,1,4,3,7,6,9,8,5]

def test_bst_empty_post_order(bst_empty):
    """ tests bst post order method on empty bst"""
    check_list = []
    bst_empty.post_order_trav(lambda x: check_list.append(x.val))
    assert check_list == []

# def test_bst_pre_order_traversal(bst_)