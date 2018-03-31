import pytest
from stack import Stack
from node import Node

# init

def test_empty_stack_has_no_top(empty_stack):
    """
    check top of empty string is 0
    """
    assert empty_stack.top is None

def test_full_stack_top_is_correct_valid(one_nine_stack):
    """
    tests top of valid stack is expected value
    """
    assert one_nine_stack.top.val == 1

def test_full_stack_second_value_valid(one_nine_stack):
    """
    tests next value after top for expected value
    """
    assert one_nine_stack.top._next.val == 2


# len

def test_len_on_empty(empty_stack):
    """
    asserts correct size of empty stack is 0
    """
    assert empty_stack._size == 0

def test_len_on_populated_stack(one_nine_stack):
    """
    asserts correct size of populated stack
    """
    assert one_nine_stack._size == 9

# push

def test_insertion(empty_stack):
    """
    asserts pushed value is now top of stack
    """
    assert empty_stack.top is None
    assert empty_stack.push(1).val == 1

def test_push_for_str(one_nine_stack):
    """
    adds a str to a stack to check type consitency
    """
    assert one_nine_stack.push('a').val == 'a'

def test_push_for_bool(one_nine_stack):
    """
    adds a str to a stack to check type consitency
    """
    assert one_nine_stack.push(True).val == True

# pop

def test_pop_returns_valid(one_nine_stack):
    """
    checks return ppopped value to be correct
    """
    assert one_nine_stack.pop().val == 1

def test_pop_from_empty_stack(empty_stack):
    """
    checks return ppopped value to be correct
    """
    assert empty_stack.pop() is False

# peek

def test_peek_populated_stack(one_nine_stack):
    """
    tests top of populated stack is as expected int
    """
    assert one_nine_stack.peek().val == 1

def test_peek_empty_stack(empty_stack):
    """
    tests top of empty stack is as expected None
    """
    assert empty_stack.peek() is False

def test_peek_after_push_diff_type(one_nine_stack):
    """
    tests for expected repsonse after str type is pushed to
    array
    """
    one_nine_stack.push('a')
    one_nine_stack.peek().val = 'a'