class Node:
    """
    Creating nodes for use in data structures
    """
    def __init__(self, val, next = None):
        """
        method called upon creation of node
        """
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        """
        string representation of node for dev
        """
        return 'Node.val = {}'.format(self.val)
    
    def __str__ (self):
        """
        string representation of node for user
        """
        return self.val

    