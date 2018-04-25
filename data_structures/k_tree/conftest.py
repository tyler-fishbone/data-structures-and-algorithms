import pytest
from .k_tree import Node, KTree

@pytest.fixture
def ktree_four_nodes():
    """ returns a ktree with a list of known values """
    # node_1 = Node(1)
    # node_2 = Node(2)
    # node_3 = Node(3)
    # node_4 = Node(4)
    ktree = KTree()
    ktree.insert(None, 1)
    ktree.insert(1, 2)
    ktree.insert(1, 3)
    ktree.insert(1, 4)
    return ktree

@pytest.fixture
def ktree_empty():
    """ returns empty ktree """
    return KTree()