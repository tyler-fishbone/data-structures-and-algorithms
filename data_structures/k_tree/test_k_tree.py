from .k_tree import Node, KTree
import pytest


def test_ktree_root(ktree_four_nodes):
    """tests self.root of the ktree """
    assert ktree_four_nodes.root.val == 1

def test_ktree_empty_root(ktree_empty):
    """tests for self.root on passed empty ktree """
    assert ktree_empty.root == None

def test__repr__(ktree_four_nodes):
    """ tests repr for tree """
    assert ktree_four_nodes.root.val == 1


def test_ktree_insert(ktree_empty):
    """ tests instert method """
    node_1 = Node(1)
    node_3 = Node(3)
    ktree_empty.insert(node_1)
    assert ktree_empty.root.val == 1
    ktree_empty.insert(node_3, 1)
    assert ktree_empty.root.children[0].val == 3

# def test_ktree_in_breadthfirst(ktree_four_nodes):
#     """ tests ktree comes out in breadth first"""

#     assert ktree_four_nodes.breadth_first_traversal() == [1,2,3,4]

# def test_ktree_empty_in_order(ktree_empty):
#     """ tests ktree in order method on empty ktree"""
#     check_list = []
#     ktree_empty.in_order_trav(lambda x: check_list.append(x.val))
#     assert check_list == []

def test_ktree_pre_order_normal(ktree_four_nodes):
    """ tests ktree comes out in correct order"""
    check_list = []
    ktree_four_nodes.pre_order_traversal(lambda x: check_list.append(x.val))
    assert check_list == [1,2,3,4]

# def test_ktree_empty_pre_order(ktree_empty):
#     """ tests ktree pre order method on empty ktree"""
#     check_list = []
#     ktree_empty.pre_order_trav(lambda x: check_list.append(x.val))
#     assert check_list == []

# def test_ktree_post_order_normal(ktree_four_nodes):
#     """ tests ktree comes out in correct order"""
#     check_list = []
#     ktree_four_nodes.post_order_trav(lambda x: check_list.append(x.val))
#     assert check_list == [0,2,1,4,3,7,6,9,8,5]

# def test_ktree_empty_post_order(ktree_empty):
#     """ tests ktree post order method on empty ktree"""
#     check_list = []
#     ktree_empty.post_order_trav(lambda x: check_list.append(x.val))
#     assert check_list == []

# # def test_ktree_pre_order_traversal(ktree_)