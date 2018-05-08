import pytest


@pytest.fixture
def list_ten_values_random_order():
    """Return list of ten values which are in a randomized order."""
    return [54, 26, 93, 17, 77, 31, 44, 55, 20, 3]


@pytest.fixture
def list_ten_values_in_order():
    """Return list of ten values which are in ascending order."""
    return [3, 17, 20, 26, 31, 44, 54, 55, 77, 93]


@pytest.fixture
def list_eleven_values_random_order():
    """Return list of ten values which are in a randomized order."""
    return [54, 26, 93, 17, 77, 31, 44, 55, 20, 3, 16]


@pytest.fixture
def list_eleven_values_in_order():
    """Return list of ten values which are in ascending order."""
    return [3, 16, 17, 20, 26, 31, 44, 54, 55, 77, 93]


@pytest.fixture
def list_ten_values_reversed_order():
    """Return list of ten values which are in descending order."""
    return [93, 77, 55, 54, 44, 31, 26, 20, 17, 3]


@pytest.fixture
def list_ten_values_close_to_correct_order():
    """Return list of ten values which are already sorted correctly in order."""
    return [26, 20, 17, 3, 93, 77, 55, 54, 44, 31]


@pytest.fixture
def list_one_value():
    """Return list of one value."""
    return [31]


@pytest.fixture
def empty_list():
    """Return empty list."""
    return []


@pytest.fixture
def list_multiple_data_types():
    """Return list of ten values mutliple data types"""
    return [93, 77, 'fiftyfive', 54, 44, 31, 26, 20, 17, 3]


