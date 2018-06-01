from node_bst import Node
from queue import Queue
from bst import BST

def breadth_first_traversal(binary_search_tree):
    """ function for traversing through bst
    in left to right breadth first order """

    array_for_testing = []
    current_bst = binary_search_tree.root
    q = Queue([current_bst])

    # current_q = q._front

    while q._size > 0:
        try:
            if current_bst.left is not None:
                q.enqueue(current_bst.left)

            if current_bst.right is not None:
                q.enqueue(current_bst.right)
        except AttributeError:
            print('Cannot traverse empty tree')
            return False

        print(q._front.val.val)
        array_for_testing.append(q._front.val.val)

        q.dequeue()
        if q._size <= 0:
            break
        else:
            current_bst = q._front.val

    return array_for_testing
