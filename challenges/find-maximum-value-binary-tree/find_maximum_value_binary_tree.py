from node_bst import Node
from queue import Queue
from bst import BST

def find_maximum_value_binary_tree(binary_search_tree):
    """ function for traversing through bst 
    in left to right breadth first order """
    try:
        current_max = binary_search_tree.root.val
    except AttributeError:
        print('Cannot traverse empty tree')
        return False
    current_bst = binary_search_tree.root
    q = Queue([current_bst])

    while q._size > 0:
        try:
            if current_bst.left is not None:
                q.enqueue(current_bst.left)
            
            if current_bst.right is not None:
                q.enqueue(current_bst.right)
        except AttributeError:
            print('Cannot traverse empty tree')
            return False
        
        if q._front.val.val > current_max:
            current_max = q._front.val.val
        
        q.dequeue()
        if q._size <= 0:
            break
        else:
            current_bst = q._front.val
            
    return current_max


# lil_bst = BST([5,3,1,4,10,7,12,5])
# print(find_maximum_value_binary_tree(lil_bst))