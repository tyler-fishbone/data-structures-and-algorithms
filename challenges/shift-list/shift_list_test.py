import shift_list
import pytest

def test_insert_shift_list_with_valid_list():
    assert shift_list.insert_shift_list([1,2,3,4,5,6,7,8,9], 'X') == [1, 2, 3, 4, 5, 'X', 6, 7, 8, 9]

# def test_insert_shift_list_with_non_list():
#     with pytest.raises(TypeError) as err:
#         shift_list.insert_shift_list(True, 'X')

#     assert str(err.value) == 'Argument invalid. Must be valid list.'
