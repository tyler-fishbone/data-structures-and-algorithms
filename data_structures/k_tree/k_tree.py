class Node:
    """
    Creating nodes for use in data structures
    """
    def __init__(self, val, children = []):
        """
        method called upon creation of node
        """
        self.val = val
        self.children = children

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

    
class KTree:
    """ 
    class for the k-ary tree 
    """
    def __init__(self, ):
        """ initialization of the k-ary tree """
        self.root = None
        self._size = 0
    
    def __repr__(self):
        """
        string representation of root for dev
        """
        return 'Node.val = {}'.format(self.root.val)
    
    def __str__ (self):
        """
        string representation of node for user
        """
        return self.root.val

    
    def insert(self, node, parent_node_val = None):
        """
        method for inserting new nodes into k-ary tree 
        """
        if parent_node_val is None and self.root is None:
            self.root = node
            self._size += 1
            return

        breadth_first_list = self.breadth_first_traversal()

        for i in breadth_first_list:
            if i.val == parent_node_val:
                i.children.append(node)
                self._size += 1
                return
    
    def breadth_first_traversal(self, function_lambda = None):
        """ 
        defines a method for traversing a k-ary tree from shallowest 
        to deepest level
        """
        breadth_first_list = [self.root]

        for i in range(self._size):
            function_lambda
            breadth_first_list += breadth_first_list[i-1].children       
        
        return breadth_first_list
        

    def pre_order_traversal(self, function_lambda = None):
        """
        defines a method for traversing a k-ary tree, perfomring
        operations on each node as it is first reached
        """
        def _walk(node = None):
            if len(node.children) < 1:
                return
            
            function_lambda(node)

            if len(node.children) > 0:
                for node in node.children:
                    _walk(node)
            
        _walk(self.root)


    def post_order_traversal(self, function_lambda = None):
        """
        defines a method for traversing a k-ary tree, performing
        operations on each node as it is last passed by
        """
        def _walk(node = None):
            if len(node.children) < 1:
                return

            if len(node.children) > 0:
                for node in node.children:
                    _walk(node)
            
            function_lambda(node)
            
        _walk(self.root)