import pytest
from tree_intersection import tree_intersection


def test_tree_intersetion_on_two_valid_filled_binary_search_trees(bst_ten_vals, bst_nine_vals):
    '''test tree intersetion on two valid binary search trees'''
    assert tree_intersection(bst_ten_vals, bst_nine_vals) == {1, 3, 5, 9}


def test_tree_intersetion_bsts_one_filled_one_empty(bst_ten_vals, bst_empty):
    '''test tree intersetion on two valid binary search trees'''
    assert tree_intersection(bst_ten_vals, bst_empty) == set()


def test_func_on_two_valid_filled_binary_search_trees_with_negative_vals(bst_ten_vals, bst_nine_vals_negs):
    '''test tree intersetion on two valid binary search trees'''
    assert tree_intersection(bst_ten_vals, bst_nine_vals_negs) == {1, 3, 5}


def test_func_two_binary_search_trees_with_negative_vals_and_zero(bst_nine_vals, bst_nine_vals_negs):
    '''test tree intersetion on two valid binary search trees'''
    assert tree_intersection(bst_nine_vals, bst_nine_vals_negs) == {1, 3, 5}

