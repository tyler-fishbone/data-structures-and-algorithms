from bst import BST

def fizz_buzz_tree(input_tree):
    """ traverses a tree and performs fizz buzz on each element, agumenting the val """
    input_tree.in_order_trav(lambda x: fizzbuzz(x))
    return input_tree


def fizzbuzz(node):
    """ takes a value and returns fizz is divisible by 3,
        buzz if divisible by 5, fizzbuzz if divisble by both,
        or just the value if none of the conditions are met """
    if node.val % 3 == 0 and node.val % 5 == 0:
        node.val = 'fizzbuzz'
        return node
    elif node.val % 3 == 0:
        node.val = 'fizz'
        return node
    elif node.val % 5 == 0:
        node.val = 'buzz'
        return node
    return