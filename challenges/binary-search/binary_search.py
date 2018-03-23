def binary_search(sorted_array, search_key):
    '''
    This function searchs an input array for a key
    If it is there it returns the index of the key
    If not it returns -1
    '''
    for i in range(len(sorted_array)):
        if sorted_array[i] == search_key:
            return i
    return -1
