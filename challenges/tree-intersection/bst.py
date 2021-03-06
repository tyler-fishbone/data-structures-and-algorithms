class Node:
    """
    Creating nodes for use in data structures
    """
    def __init__(self, val, next=None):
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

    def __str__(self):
        """String representation of node for user."""
        return self.val


class BST:
    """ creates a binary search tree (from scratch!) """
    def __init__(self, iter = []):
        """ initialises bst """
        self.root = None
        self.size = 0

        try:
            for i in iter:
                self.insert(i)
        except TypeError:
            print("input value must be iterable")
            return None
        
    def __repr__(self):
        """ string representation of bst root for dev """
        return '<BST Root {}'.format(self.root.val)
    
    def __str__(self):
        """ string representation of bst root for user """
        return self.root.val
    
    def insert(self, val):
        """ places a node at the correctly sorted position in a bst """
        current = self.root

        self.size += 1

        if self.root is None:
            self.root = Node(val)
            return self.root
        
        while True:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = Node(val)
                    return current.right
                
            else:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = Node(val)
                    return current.left
    
    def in_order_trav(self, function_lambda):
        """ function for going through bst in order from smallest to largest """
        def _walk(node=None):
            if node is None:
                return
            
            if node.left is not None:
                _walk(node.left)
            
            print(node.val)
            function_lambda(node)
            
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)
    
    def pre_order_trav(self, function_lambda):
        """ function for going through bst in pre order """
        def _walk(node=None):
            if node is None:
                return
            
            function_lambda(node)

            if node.left is not None:
                _walk(node.left)
            
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)
    
    def post_order_trav(self, function_lambda):
        """ function for going through bst in pre order """
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)
            
            if node.right is not None:
                _walk(node.right)
            
            function_lambda(node)

        _walk(self.root)
