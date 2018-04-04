from queue import Queue

class AnimalShelter:
    """ animal shelter class """
    def __init__(self, iter = []):
        """ makes animal shelter class """
        self.animal_queue = Queue()

        for i in iter:
            self.enqueue(i)
    
    def enqueue(self, animal):
        """ puts new animal in the back of the queue """
        if animal == 'cat' or animal == 'dog':
            self.animal_queue.enqueue(animal)
            return self.animal_queue._back
        else:
            print('You must only add cat or dog.')
            return False
    
    def dequeue(self, animal = None):
        """ takes first dog or cat animal off the front of the queue """
        adopted_animal = False
        current = self.animal_queue._front
        print('input animal: {}'.format(animal))
        print('self.front:   {}'.format(current))
        if self.animal_queue._size == 0:
            print('We are all out of animals')
            return False
        if animal == None:
            return self.animal_queue.dequeue()
        elif animal == current.val:
            return self.animal_queue.dequeue()
        else:
            while current._next is not None:
                if current._next.val == animal:
                    adopted_animal = current._next
                    current._next = current._next._next
                    self.animal_queue._size -= 1
                    return adopted_animal
                current = current._next
            print('Sorry we do not have one of those')
            return False
        
    


# def print_shelter():
#     current = shelter_one.animal_queue._front
#     counter = 1
#     while current is not None:
#         print('{}. {}'.format(counter, current.val))
#         counter += 1
#         current = current._next
#     print()

# # qwt = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])

# shelter_one = AnimalShelter(['cat', 'dog', 'dog', 'cat', 'cat'])

# print_shelter() #

# shelter_one.dequeue('d')

# print_shelter() #

# shelter_one.enqueue('do')

# print_shelter() #

# shelter_one.dequeue()

# print_shelter() #

# shelter_one.dequeue('d')

# print_shelter() #

# shelter_one.dequeue('cat')

# print_shelter() #
