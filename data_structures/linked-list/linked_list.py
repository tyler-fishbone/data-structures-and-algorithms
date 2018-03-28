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
        self.head = Node(val, self.head)
        self._size += 1
    
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
    
    def append(self, val):
        """
        appends a value at the end of the linked list
        """
        temp = self.head
        while temp:
            temp = temp._next
        self.insert(val)
        self._size += 1
        return self._size

    def insert_before(self, value, newVal):
        """
        inserts a node before a specified node
        """
        # new_node = Node(newVal, value)
        # temp = self.head
        # while temp:
        #     if temp._next == value:
        #         temp._next = new_node
        #         self._size += 1
        #         return self._size
        #     temp = temp._next
        new_node = Node(newVal)
        temp = self.head._next
        while temp._next is not None:
            if temp._next.val == value:
                new_node._next = temp._next
                temp._next = new_node
                self._size += 1
                return self._size
            temp = temp._next
        if temp._next is None:
            raise ValueError("Data not in list")
    
    def insert_after(self, value, newVal):
        """
        inserts a node after a specified node
        """
        temp = self.head
        while temp:
            if temp.val == value:
                temp._next = Node('X', temp._next)
                self._size += 1
                return self._size
            temp = temp._next
        if temp._next is None:
            raise ValueError("Data not in list")

    def kth_from_end(self, k):
        """
        takes in a value k and returns in the reverse 
        index position of that element in the array
        """
        if k <= self._size:
            r = self._size - k - 1
            temp = self.head
            while r > 0:
                temp = temp._next
                r -= 1
            return temp
        else:
            raise AttributeError('Your input value is larger than the linked list')
