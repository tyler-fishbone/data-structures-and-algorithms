"""Hash Table Class"""
from linked_list import LinkedList


class HashTable:
    """Hash table class."""
    def __init__(self, max_size=1024):
        if type(max_size) is not int:
            raise TypeError
        self.max_size = max_size
        self.buckets = [LinkedList()] * self.max_size

    def hash_key(self, key):
        """Hash key."""
        if type(key) is not str:
            raise TypeError
        
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """Set new value in hash table."""
        if type(key) is not str:
            raise TypeError

        self.buckets[self.hash_key(key)].insert({key: val})

    def get(self, key):
        """Get value in hash table."""
        if type(key) is not str:
            raise TypeError

        current = self.buckets[self.hash_key(key)].head
        while current:
            if key in current.val:
                return current.val[key]
            current = current._next

        print('The key {} in this hash table'.format(key))
        return False


    def remove(self, key):
        """Remove value in hash table."""
        if type(key) is not str:
            raise TypeError

        current = self.buckets[self.hash_key(key)].head
        while current:
            if key in current.val:
                return current.val[key]
            current = current._next

        print('The key {} in this hash table'.format(key))
        return False

        # temp = self.buckets[self.hash_key(key)]
        # self.buckets[self.hash_key(key)] = None
        # return temp
