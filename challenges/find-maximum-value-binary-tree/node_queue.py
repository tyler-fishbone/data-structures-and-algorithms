class Node:
    """
    Creating nodes for use in data structures
    """
    def __init__(self, val, next = None):
        """
        method called upon creation of node
        """
        self.val = val
        self._next = next
        # self._prev = prev

    def __repr__(self):
        """
        string representation of node
        """
        return self.val
    
    def __str__(self):
        """
        string representation of node
        """
        return self.val