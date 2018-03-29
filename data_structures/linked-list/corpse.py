

    # def insert_before(self, value, newVal):
    #     """
    #     inserts a node before a specified node
    #     """
    #     # new_node = Node(newVal, value)
    #     # temp = self.head
    #     # while temp:
    #     #     if temp._next == value:
    #     #         temp._next = new_node
    #     #         self._size += 1
    #     #         return self._size
    #     #     temp = temp._next
    #     new_node = Node(newVal)
    #     temp = self.head._next
    #     while temp._next is not None:
    #         if temp._next.val == value:
    #             new_node._next = temp._next
    #             temp._next = new_node
    #             self._size += 1
    #             return self._size
    #         temp = temp._next
    #     # if temp._next is None:
    #     #     raise ValueError("Data not in list")s
