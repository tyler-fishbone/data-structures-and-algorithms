import pytest
from mergesort import mergesort


def test_list_ten_values_random_order(list_ten_values_random_order, list_ten_values_in_order):
    """Test list of ten values which are in a randomized order."""
    mergesort(list_ten_values_random_order) 
    assert list_ten_values_random_order == list_ten_values_in_order


def test_list_eleven_values_random_order(list_eleven_values_random_order, list_eleven_values_in_order):
    """Test list of eleven values which are in a randomized order."""
    mergesort(list_eleven_values_random_order) 
    assert list_eleven_values_random_order == list_eleven_values_in_order


def test_list_ten_values_in_order(list_ten_values_in_order):
    """Test list of ten values which are in ascending order."""
    mergesort(list_ten_values_in_order)
    assert list_ten_values_in_order == list_ten_values_in_order


def test_list_ten_values_reversed_order(list_ten_values_reversed_order, list_ten_values_in_order):
    """Test list of ten values which are in descending order."""
    mergesort(list_ten_values_reversed_order)
    assert list_ten_values_reversed_order == list_ten_values_in_order


def test_list_ten_values_close_to_correct_order(list_ten_values_close_to_correct_order, list_ten_values_in_order):
    """Test list of ten values which are already sorted correctly in order."""
    mergesort(list_ten_values_close_to_correct_order)
    assert list_ten_values_close_to_correct_order == list_ten_values_in_order


def test_list_one_value(list_one_value):
    """Test list of one value."""
    mergesort(list_one_value)
    assert list_one_value == [31]


def test_empty_list(empty_list):
    """Test list of one value."""
    mergesort(empty_list)
    assert empty_list == []


def test_mutiple_data_types(list_multiple_data_types):
    """Test list containing mutliple datatypes."""
    assert mergesort(list_multiple_data_types) is None
