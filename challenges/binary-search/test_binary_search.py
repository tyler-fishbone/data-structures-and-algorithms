from binary_search import binary_search
# import pytest

def test_binary_search_with_valid_input_in_list():
    assert binary_search([1,2,3,4,5,6,7], 6) == 5

def test_binary_search_with_valid_but_not_included_input_in_list():
    assert binary_search([1,2,3,4,5,6,7], 10) == -1

def test_binary_search_with_empty_list():
    assert binary_search([], 1) == -1
