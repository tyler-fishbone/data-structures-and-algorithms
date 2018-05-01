from bst import BST, 
from hash_table import HashTable


def tree_intersection(bst_1, bst_2):
    """
    Take in two binary search trees and
    return a list of all the values in common.
    """

    def check_and_append(node):
        """Check if node.val is in hash table and if
        so append it to the output list."""
        if ht.get(node.val):
            output_list.append(node.val)

    output_list = []
    ht = HashTable(bst_1.size)

    bst_1.in_order_trav(lambda x: ht.set(x.val, x.val))

    bst_2.in_order_trav(lambda x: check_and_append(x))

    return output_list
