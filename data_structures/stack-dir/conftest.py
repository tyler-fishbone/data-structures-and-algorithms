import pytest
# from node import Node
from stack import Stack

@pytest.fixture
def one_nine_stack():
    return Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])

@pytest.fixture
def empty_stack():
    return Stack([])

