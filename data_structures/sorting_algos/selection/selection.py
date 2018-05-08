

def selection(input_list):
    """
    Sort a given list using selection sort algorithm
    and return a that list with the values ascending.
    """
    input_list_length = len(input_list)

    for i in range(input_list_length):
        current_smallest_index = i
        try:
            for j in range(i, input_list_length):
                if input_list[j] < input_list[current_smallest_index]:
                    current_smallest_index = j
            if current_smallest_index != i:
                input_list[current_smallest_index], input_list[i] = \
                    input_list[i], input_list[current_smallest_index]
        except TypeError:
            print('All data must be same type i.e. int, str, etc...')
            return None