from node import Node
from stack import Stack

def multi_bracket_validation(input_str):
    """ function which takes in string and returns a bool of if it is balanced
    Round Brackets : () | Square Brackets : [] | Curly Brackets : {}
    """
    bracket_dict = {'(': ')',
                    '[': ']',
                    '{': '}',
                    }
    opening_brackets = bracket_dict.keys()
    closing_brackets = bracket_dict.values()
    
    s = Stack()

    for i in input_str:
        if i in opening_brackets:
            s.push(i)
        elif i in closing_brackets:
            try:
                if i == bracket_dict[s.top.val]:
                    s.pop()
                else:
                    return False
            except AttributeError:
                return False

    return s._size == 0
