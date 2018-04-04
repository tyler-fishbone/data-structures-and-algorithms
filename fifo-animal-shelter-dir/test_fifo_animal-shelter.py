import pytest


def test_a_s_for_size(three_cats_two_dogs_queue):
    """check size of initial queue passed in"""
    assert three_cats_two_dogs_queue.animal_queue._size == 5

def test_empty_a_s_for_sise(empty_shelter_queue):
    """check size of initial queue passed in"""
    assert empty_shelter_queue.animal_queue._size == 0

def test_enqueue_new_animal(three_cats_two_dogs_queue):
    """ tests adding new animal to queue """
    three_cats_two_dogs_queue.enqueue('dog')
    assert three_cats_two_dogs_queue.animal_queue._size == 6

def test_enqueue_incorrent_new_animal(three_cats_two_dogs_queue):
    """ tests adding new animal to queue """
    assert three_cats_two_dogs_queue.enqueue('gorrila') is False

def test_dequeue_with_no_input(three_cats_two_dogs_queue):
    """ tests for correct dequeueing of front animal when noe is input"""
    assert three_cats_two_dogs_queue.dequeue().val == 'cat'
    

def test_dequeue_with_same_animal_as_front(three_cats_two_dogs_queue):
    """ test for correct dequeueing of front animal when input matches front """
    assert three_cats_two_dogs_queue.dequeue('cat').val == 'cat'


def test_dequeue_with_no_front_animal(three_cats_two_dogs_queue):
    """ test for correct dequeueing for input animal when different from front"""
    assert three_cats_two_dogs_queue.dequeue('dog').val == 'dog'
    assert three_cats_two_dogs_queue.animal_queue._size == 4


def test_dequeue_with_empty_shelter(empty_shelter_queue):
    """ tests for correct return when checking empty shelter """
    assert empty_shelter_queue.dequeue('dog') is False

def test_dequeue_when_shelter_has_only_one_pet(one_cat_queue):
    """ tests dequeue with just one pet in queue """
    assert one_cat_queue.dequeue('cat').val == 'cat'