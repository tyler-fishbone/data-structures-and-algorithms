from binary_search import binary_search
# import pytest

def test_binary_search_with_valid_input_in_list():
    '''
    tests array with a valid case of search key being in array
    '''
    assert binary_search([1,2,3,4,5,6,7], 6) == 5

def test_binary_search_with_valid_but_not_included_input_in_list():
    '''
    tests array with valid case of search key not being in array and 
    returning -1
    '''
    assert binary_search([1,2,3,4,5,6,7], 10) == -1

def test_binary_search_with_empty_list():
    '''
    tests array with a valid case of empty array
    '''
    assert binary_search([], 1) == -1
