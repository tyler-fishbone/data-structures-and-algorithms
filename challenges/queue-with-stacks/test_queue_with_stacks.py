import pytest
from queue_with_stacks import Queue

# # enqueue

def test_empty_queue_has_no_back(empty_queue):
    """
    check size of empty queue is 0
    """
    assert len(empty_queue.stack_one) == 0

def test_full_queue__back_is_correct_valid(one_nine_queue):
    """
    tests size of valid queue is expected value
    """
    assert len(one_nine_queue.stack_one) == 9
    one_nine_queue.enqueue('a')
    assert len(one_nine_queue.stack_one) == 10

def test_insertion(empty_queue):
    """
    asserts enqueued value is now _back of queue
    """
    assert len(empty_queue.enqueue(1)) == 1

# # dequeue

def test_dequeue_returns_valid(one_nine_queue):
    """
    checks return dequeued value to be correct, final val at front of queue
    """
    assert one_nine_queue.dequeue() == 9
    assert len(one_nine_queue.stack_one) == 8

def test_dequeue_from_empty_queue(empty_queue):
    """
    checks return dequeued value of empty queue is expected response False
    """
    assert empty_queue.dequeue() is False

def test_dequeue_single_node_queue(one_node_queue):
    """
    checks returns dequeued value for queue with onld node in it
    """
    assert len(one_node_queue.stack_one) == 1