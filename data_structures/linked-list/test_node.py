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

# def test_node_without_val_invalid(empty_ll):
#     """
#     test that adding an empty node throws the correct error and handles it
#     """
#     with pytest.raises(AssertionError) as err:
#         empty_ll.insert()

#     assert str(err.value) == 'Must insert a value to use .insert'

# def test_check_insert_not_none(empty_ll):
#     """
#     check if iterable valid
#     """
#     # assert empty_ll.insert() == False
#     with pytest.raises(TypeError) as err:
#         empty_ll.insert()

#     assert str(err.value) == 'Must insert a value to use .insert'

# class Node:
#     '''
#     Node class for use in our linked lists
#     '''
#     def __init__(self, val, next=None):
#         self.val = val
#         self._next = next
    
#     def __repr__(self):
#         return '{val}'.format(val=self.val)
