from .queue import Queue
from .k_tree import Node, KTree

def print_level_order(input_tree):
    """ 
    takes in a k-ary tree and returns a string that contains 
    a listing of all values in the tree, with new lines in-between 
    each level of the tree
    """
    
    output_lst = []
    queue = Queue()

    queue.enqueue(input_tree.root)
    queue.enqueue(Node('/n'))
    
    while len(queue) > 0:
        current = queue.dequeue()
        if current.val == '/n':
            queue.enqueue(Node('/n')
        else:
            for child in current.children:
                queue.enqueue(child)
        output_lst.append(current.val)
    
    output_string = ''.join(output_lst)
    return output_string