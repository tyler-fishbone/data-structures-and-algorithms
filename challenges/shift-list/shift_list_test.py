import shift_list
import pytest

def test_insert_shift_list_with_valid_list_odd():
    assert shift_list.insert_shift_list([1,2,3,4,5,6,7,8,9], 'X') == [1, 2, 3, 4, 'X', 5, 6, 7, 8, 9]

def test_insert_shift_list_with_valid_list_even():
    assert shift_list.insert_shift_list([1,2,3,4,5,6,7,8], 'X') == [1, 2, 3, 4, 'X', 5, 6, 7, 8]

def test_insert_shift_list_with_valid_list_empty():
    assert shift_list.insert_shift_list([], 'X') == ['X']
