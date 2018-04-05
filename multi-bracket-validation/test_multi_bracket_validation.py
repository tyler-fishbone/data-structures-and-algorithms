import pytest
from multi_bracket_validation import multi_bracket_validation

def test_mbv_true_case_simple():
    """test function on balanced str"""
    assert multi_bracket_validation('[{()}]') == True

def test_mbv_true_case_empty_str():
    """test function with empty string"""
    assert multi_bracket_validation('') == True

def test_mbv_true_complex():
    """ tests function with complex but balanced string"""
    assert  multi_bracket_validation('{{[[asdf]]}a}()') == True

def test_mbv_false_simple():
    """ tests function returns false on unbalanced case"""
    assert multi_bracket_validation('(') == False

def test_mbv_false_complex():
    """ tests function returns false on complex unbalanced str"""
    assert multi_bracket_validation('{asd{[asdf[]aasdf]}}())') == False

# str1 = '{[}]'
# str2 = '{{[[asdf]]}a}()'
# str3 = '{asd{[asdf[]aasdf]}}())'
# str4 = 'a'

# print(multi_bracket_validation(str1))
# print(multi_bracket_validation(str2))
# print(multi_bracket_validation(str3))
# print(multi_bracket_validation(str4))