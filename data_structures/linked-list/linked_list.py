from node import Node

class LinkedList:
    '''
    This class creates a linked list using using our Nodes from node.py
    It can be passed a list and will create the beginning of the LL from that list
    '''
    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0

        for item in reversed(iter):
            self.insert(item)
        
    def __repr__(self):
        # this assumes head will have a value
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size
    
    def insert(self, val):
        # steps one by one
        # node = Node(val)
        # node._next = self.head
        # self.head = node
        self.head = Node(val, self.head)
        self._size += 1
        