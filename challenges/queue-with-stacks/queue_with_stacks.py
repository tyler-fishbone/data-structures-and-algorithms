from node import Node
from stack import Stack

class Queue:
    """
    This class makes a queue data structure using stack methods?
    """
    def __init__(self, iter = []):
        """
        method which defines the newly create
        """
        # self._back = None
        # self._front = None
        self.stack_one = Stack()
        self.stack_two = Stack()

        for i in reversed(iter):
            self.enqueue(i)

    def enqueue(self, value):
        """
        method which adds a value to the back of the queue
        """
        self.stack_one.push(value)
        return self.stack_one

    def dequeue(self):
        """
        iterates through the queue to find front node, then removes/returns it
        """
        try:
            current = self.stack_one.top
            while current._next is not None:
                current = current._next
                self.stack_two.push(self.stack_one.pop())
            node_to_dequeue = self.stack_one.pop()
            current = self.stack_two.top
            while current is not None:
                current = current._next
                self.stack_one.push(self.stack_two.pop())
            return node_to_dequeue
        except AttributeError:
            print('Cannot dequeue from empty queue')
            return False


# # qwt = Queue([1, 2, 3, 4, 5, 6, 7, 8, 9])

# one_four_queue = Queue([10, 20, 30, 40, 'a'])
# print(one_four_queue.stack_one._size)
# # one_four_queue.enqueue(0)
# # one_four_queue.dequeue()
# # one_four_queue.dequeue()
# one_four_queue.dequeue()
# # test if it tries to dequeue when queue is empty
# current = one_four_queue.stack_one.top
# print(one_four_queue.stack_one._size)

# while current is not None:
#     print(current.val)
#     current = current._next

# print(one_four_queue.stack_one._size)