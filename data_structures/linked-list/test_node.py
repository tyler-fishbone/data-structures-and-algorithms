import pytest, conftest
from linked_list import LinkedList as LL
from node import Node

def test_node(node_val_1):
    """
    tests that single node with val one behaves as expected
    """
    assert node_val_1.val == 1

def test_node_next(node_val_1):
    """
    tests that _next of single node with val one is None
    """
    assert node_val_1.val == 1
