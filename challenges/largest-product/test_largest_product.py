from largest_product import largest_product


def test_largest_product_with_valid_input_in_list():
    assert largest_product([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56


def test_largest_product_with_invalid_input_not_list():
    assert largest_product([]) is None


def test_largest_product_with_invalid_type_bool():
    assert largest_product(False) is None
