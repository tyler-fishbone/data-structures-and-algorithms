import pytest
# from node import Node
from fifo_animal_shelter import AnimalShelter

@pytest.fixture
def three_cats_two_dogs_queue():
    return AnimalShelter(['cat', 'dog', 'dog', 'cat', 'dog'])

@pytest.fixture
def empty_shelter_queue():
    return AnimalShelter([])

@pytest.fixture
def one_cat_queue():
    return AnimalShelter(['cat'])