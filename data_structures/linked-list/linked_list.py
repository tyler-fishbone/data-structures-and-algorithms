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

    def insert_before(self, val, newVal):
        """
        Add a new node with the given newValue immediately before the first value node
        """
        current = self.head
        previous = None
        while current:
            if current.val == val:
                if previous is None:
                    self.insert(newVal)
                else:
                    new_node = Node(newVal)
                    new_node._next = current
                    previous._next = new_node
                    self._size += 1
                break
            previous = current
            current = current._next

    
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
        # if temp._next is None:
        #     raise ValueError("Data not in list")

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


def merge_lists(a, b):
    """
    a function to zip together two linked lists augmenting the first linked list
    passed in to have the second LL values in it alternating
    """
    if b.head == None:
        return a
    if a.head == None:
        return b


    if a._size >= b._size:
        temp1, temp2 = a.head, b.head
        while temp2 is not None:
            a.insert_before(temp1.val, temp2)
            temp1, temp2 = temp1._next, temp2._next
        return a
    else:
        temp1, temp2 = a.head, b.head
        while temp1 is not None:
            b.insert_before(temp2.val, temp1)
            temp1, temp2 = temp1._next, temp2._next
        return b