import pytest
from queue import Queue

# init

def test_empty_queue_has_no_back(empty_queue):
    """
    check _back of empty queue is 0
    """
    assert empty_queue._back is None

def test_full_queue__back_is_correct_valid(one_nine_queue):
    """
    tests _back of valid queue is expected value
    """
    assert one_nine_queue._back.val == 1

def test_full_queue_second_value_valid(one_nine_queue):
    """
    tests next value after _back for expected value
    """
    assert one_nine_queue._back._next.val == 2


# # len

def test_len_on_empty(empty_queue):
    """
    asserts correct size of empty queue is 0
    """
    assert empty_queue._size == 0

def test_len_on_populated_queue(one_nine_queue):
    """
    asserts correct size of populated queue
    """
    assert one_nine_queue._size == 9

# enqueue

def test_insertion(empty_queue):
    """
    asserts enqueued value is now _back of queue
    """
    assert empty_queue._back is None
    assert empty_queue.enqueue(1).val == 1

def test_enqueue_for_str(one_nine_queue):
    """
    adds a str to a queue to check type consitency
    """
    assert one_nine_queue.enqueue('a').val == 'a'

def test_enqueue_for_bool(one_nine_queue):
    """
    adds a str to a queue to check type consitency
    """
    assert one_nine_queue.enqueue(True).val == True

# # dequeue

def test_dequeue_returns_valid(one_nine_queue):
    """
    checks return dequeued value to be correct, final val at front of queue
    """
    assert one_nine_queue.dequeue().val == 9

def test_dequeue_from_empty_queue(empty_queue):
    """
    checks return dequeued value of empty queue is expected response False
    """
    assert empty_queue.dequeue() is False

def test_dequeue_single_node_queue(one_node_queue):
    """
    checks returns dequeued value for queue with onld node in it
    """
    assert one_node_queue.dequeue().val == 1