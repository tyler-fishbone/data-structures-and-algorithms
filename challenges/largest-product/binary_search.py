def binary_search(sorted_array, search_key):
    for i in range(len(sorted_array)):
        if sorted_array[i] == search_key:
            return i
    return -1
