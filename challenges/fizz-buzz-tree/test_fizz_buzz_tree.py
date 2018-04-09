import pytest
from bst import BST
from fizz_buzz_tree import fizz_buzz_tree

def test_fbt_valid_output(bst_ten_values_random):
    """ 
    tests fizzbuzz tree on valid tree with fizz, buzz, fizzbuzz,
    and none cases """
    check_list = []
    # bst_ten_values_random.in_order_trav(lambda x: print(x))
    fizz_buzz_tree(bst_ten_values_random)
    bst_ten_values_random.in_order_trav(lambda x: check_list.append(x.val))
    assert check_list == [1,2,'buzz','buzz','fizz',7,'fizz','fizzbuzz']

def test_fbt_empty_bst(bst_empty):
    """ tests fizzbuzztree function on empty tree"""
    check_list = []
    fizz_buzz_tree(bst_empty)
    bst_empty.in_order_trav(lambda x: check_list.append(x.val))
    assert check_list == []

def test_single_node_before_and_after(bst_empty):
    """ tests fizzbuzz tree function on empty and single node tree"""
    assert bst_empty.root is None
    bst_empty.insert(9)
    bst_empty.insert(5)
    fizz_buzz_tree(bst_empty)
    assert bst_empty.root.left.val == 'buzz'