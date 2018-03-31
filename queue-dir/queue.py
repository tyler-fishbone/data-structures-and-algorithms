from node import Node

class Queue:
    """
    This class makes a queue data structure
    """
    def __init__(self, iter = []):
        """
        method which defines the newly created stack
        """
        self._back = None
        self._front = None
        self._size = 0

        for i in reversed(iter):
            self.enqueue(i)

    def __len__(self):
        """
        returns current number of nodes in queue
        """
        return self._size        

    def enqueue(self, val):
        """
        method which adds a value to the back of the queue
        """
        self._back = Node(val, self._back)
        self._size += 1
        return self._back

    def dequeue(self):
        """
        iterates through the queue to find front node, then removes/returns it
        """
        ## need to test for 0 and 1 node
        if self._size == 0:
            print('Queue is empty, nothing to dequeue')
            return False
        elif self._size == 1:
            current = self._back
            self._back = None
            self._size -= 1
            return current
        else:
            current = self._back
            while current._next is not None:
                prev = current
                current = current._next
            prev._next = None
            self._size -= 1
            return current

one_four_queue = Queue([1, 2, 3, 4, 'a'])
print(one_four_queue._size)
one_four_queue.enqueue(0)
one_four_queue.dequeue()
one_four_queue.dequeue()
one_four_queue.dequeue()
# test if it tries to dequeue when queue is empty
current = one_four_queue._back
print(one_four_queue._size)

while current is not None:
    print(current.val)
    current = current._next

print(one_four_queue.__len__)