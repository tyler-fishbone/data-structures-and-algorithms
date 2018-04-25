from node import Node

class Stack():
    """
    creating a Stack class for use in data structures
    """
    def __init__(self, iter = []):
        """
        initiatilizes the stack with default properties unless specific
        """
        self.top = None
        self._size = 0

        for i in reversed(iter):
            self.push(i)
               
    def __len__(self):
        """
        returns length of stack
        """
        return self._size
    
    def __str__(self):
        """
        returns a formatted string for info about stack
        """
        return 'This stack is {} nodes'.format(self._size)
    
    def push(self, val):
        """
        places a new node on top of the stack and sets it as the new top
        """
        node = Node(val)
        node._next = self.top
        self.top = node
        # self.top = Node(val, self.top) <- is dryer way to do this
        self._size += 1
        return self.top
    
    def pop(self):
        """
        removes the top node on the array and returns it
        """
        if self.top is not None:
            node_to_remove = self.top
            self.top = self.top._next
            self._size -= 1
            return node_to_remove.val
        else:
            print('Cannot pop from empty stack')
            return False
    
    def peek(self):
        """
        returns the node at the top of the stack
        """
        if self.top is not None:
            return self.top
        else:
            return False
            

# one_four_stack = Stack([1, 2, 3, 4, 'a'])
# one_four_stack.push(0)
# one_four_stack.pop()
# one_four_stack.pop()
# one_four_stack.pop()
# # test if it tries to pop when stack is empty
# current = one_four_stack.top

# while current is not None:
#     print(current.val)
#     current = current._next

# print(one_four_stack.peek())
