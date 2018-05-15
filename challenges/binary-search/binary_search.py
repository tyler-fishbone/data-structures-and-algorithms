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


# def binary_search(sorted_array, search_key):
#     '''
#     This function searchs an input array for a key
#     If it is there it returns the index of the key
#     If not it returns -1
#     '''
#     def split(input_array, target_val):
#         middle_index = len(input_array) // 2
#         if input_array[middle_index] == target_val:
#             print('found value', target_val)
#             return True
#         elif len(input_array) == 0:
#             return -1
#         elif input_array[middle] < target_val:
#             split([middle:], target_val)
#         else:
#             split([:middle], target_val)

#     split(sorted_array, search_key)
