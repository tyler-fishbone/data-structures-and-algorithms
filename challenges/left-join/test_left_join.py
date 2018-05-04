from hash_table import HashTable
from left_join import left_join


def test_left_join_valid_output_one(ht_syn_one, ht_ant_one, left_join_list_one):
    """Test valid case."""
    left_join_result = left_join(ht_syn_one, ht_ant_one)
    assert left_join_result == left_join_list_one


def test_left_join_valid_input_ant_empty_two(ht_syn_one, ht_ant_two, left_join_list_two):
    """Test valid case."""
    left_join_result = left_join(ht_syn_one, ht_ant_two)
    assert left_join_result == left_join_list_two


def test_left_join_valid_input_ant_empty_three(ht_syn_one, ht_empty, left_join_list_three):
    """Test valid case."""
    left_join_result = left_join(ht_syn_one, ht_empty)
    assert left_join_result == left_join_list_three
