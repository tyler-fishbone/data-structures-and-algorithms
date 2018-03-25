import pytest, conftest
from linked_list import LinkedList as LL

def test_empty_ll(empty_ll):
    """
    tests that an empty linked lists head value returns none
    tests that LL with an inserted 1 now has 1 as it's head val
    """
    assert empty_ll.head is None

def test_insert_first_node(empty_ll):
    """
    tests that an empty linked lists head value returns none
    tests that LL with an inserted 1 now has 1 as it's head val
    """
    empty_ll.insert(1)
    assert empty_ll.head.val == 1

def test_make_ll_by_passing_in_iter(small_ll):
    """
    tests that a LL instantiated with an iter returns first val of head as iter
    """
    assert small_ll.head.val == 5

def test_check_valid_iterable():
    """
    check if iterable valid
    """
    with pytest.raises(TypeError) as err:
        LL(2)

    assert str(err.value) == 'Invalid iterable'


def test_inserting_node_after_iter(small_ll):
    """
    tests that a LL instantiated with an iter returns first val of head as iter
    """
    small_ll.insert('new item')
    assert small_ll.head.val == 'new item'
    assert small_ll.head._next.val == 5

# def test_check_insert_not_none(empty_ll):
#     """
#     check if iterable valid
#     """
#     assert empty_ll.insert() == False
    # with pytest.raises(TypeError) as err:
    #     empty_ll.insert()

    # assert str(err.value) == 'Must insert a value to use .insert'

def test_find_method_val_at_head_position_valid(small_ll):
    """
    tests that find method returns true when given a val that is in the LL at the head
    """
    assert small_ll.find(5) == True

def test_find_method_val_not_at_head_valid(small_ll):
    """
    tests that find method returns true when given a val that is in the LL but
    not at the first node
    """
    assert small_ll.find(7) == True

def test_find_method_inserted_value_valid(small_ll):
    """
    tests that find method returns true when given a val that has just been inserted
    """
    small_ll.insert('test insert')
    assert small_ll.find('test insert') == True

def test_find_method_val_invalid(small_ll):
    """
    tests that find method returns false when not in the LL
    """
    assert small_ll.find(100) == False
