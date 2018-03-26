from node import Node

class LinkedList:
    '''
    This class creates a linked list using our Nodes from node.py
    It can be passed a list and will create the beginning of the LL from that list
    '''

    def __init__(self, iter=[]):
        self._current = None
        self.head = None
        self._size = 0
        if type(iter) is not list:
            raise TypeError('Invalid iterable')
        for item in reversed(iter):
            self.insert(item)
        
    def __repr__(self):
        return '<head> => {}'.format(self.head.val)

    def __len__(self):
        return self._size
    
    def insert(self, val):
        """
        inserts value at the beginning of the linked list
        """
        # if val is None:
        #     raise AssertionError('Must insert a value to use .insert')
        # try:
        self.head = Node(val, self.head)
        self._size += 1
        # except (AssertionError, TypeError):
        #     print('Must insert a value to use .insert')
        #     return False
    
    def find(self, val):
        """
        returns true of false if inputted value is in linked list - 0(n)
        """
        temp = self.head
        while(temp):
            if temp.val == val:
                return True
            temp = temp._next
        return False
