import pytest
from queue import Queue
from print_level_order import print_level_order
from k_tree import Node, KTree

def test_correct_behavior_with_four_node_ktree(ktree_four_nodes):
    """
    tests for correct behavior with a ktree of 4 nodes
    """
    assert print_level_order(ktree_four_nodes) == '1/n234'

def test_correct_behavior_with_six_node_ktree(ktree_six_nodes):
    """
    tests for correct behavior with a ktree of 6 nodes
    """
    assert print_level_order(ktree_six_nodes) == '1/n234/n56'

def test_correct_behavior_with_empty_ktree(ktree_empty):
    """
    tests for correct behavior with an empty tree
    """
    assert print_level_order(ktree_empty) == ''