import shift_list
import pytest

def test_insert_shift_list():
    assert insert_shift_list([1,2,3,4,5,6,7,8,9], 'X') == [1, 2, 3, 4, 5, 'X', 6, 7, 8, 9]
