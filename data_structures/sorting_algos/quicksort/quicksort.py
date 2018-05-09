"""Quicksort function."""


def quicksort(input_list):
    """
    Quicksort sorting method.

    Sorts a given list using the quicksort sort algorithm
    and return that list with the values ascending.
    """
    if len(input_list) > 1:
        left_side = []
        equal = []
        right_side = []
        temp = input_list[0]

        for i in range(len(input_list)):
            try:
                if input_list[i] < temp:
                    left_side.append(input_list[i])
                elif input_list[i] == temp:
                    equal.append(input_list[i])
                else:
                    right_side.append(input_list[i])
            except TypeError:
                print('All data must be same type i.e. int, str, etc...')
                return None

        return quicksort(left_side) + equal + quicksort(right_side)
    else:
        return input_list
