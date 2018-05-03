from hash_table import HashTable
from left_join import left_join


def test_left_join_valid_output(ht_syn_one, ht_ant_one, left_join_list_one):
    """Test valid case."""
    # print(ht_ant_one)
    left_join_result = left_join(ht_syn_one, ht_ant_one)
    # print(left_join_result)
    assert left_join_result == left_join_list_one


def test_left_join_valid_input_ant_empty(ht_syn_one, ht_ant_empty, left_join_list_two):
    """Test valid case."""
    left_join_result = left_join(ht_syn_one, ht_ant_empty)
    assert left_join_result == left_join_list_two
