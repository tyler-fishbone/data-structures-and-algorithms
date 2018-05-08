def mergesort(input_list):
    """
    Given an list of values, sort the list into
    ascending order and return it.
    """
    # recurse following function until input is single elements
    if len(input_list) > 1:
        # split list
        mid = len(input_list) // 2
        left_side = input_list[:mid]
        right_side = input_list[mid:]
        
        # recursive calls
        mergesort(left_side)
        mergesort(right_side)

        # counters
        i = 0  # left side
        j = 0  # right side
        k = 0  # input list

        # place items back into input list in correct order
        try:
            while i < len(left_side) and j < len(right_side):
                if left_side[i] < right_side[j]:
                    input_list[k] = left_side[i]
                    i = i + 1
                else:
                    input_list[k] = right_side[j]
                    j = j + 1
                k = k + 1
            
            # when one list has been exhausted place items
            # from other list into it in order
            while i < len(left_side):
                input_list[k] = left_side[i]
                i = i + 1
                k = k + 1
            
            while j < len(right_side):
                input_list[k] = right_side[j]
                j = j + 1
                k = k + 1
        except TypeError:
            print('All data must be same type i.e. int, str, etc...')
            return None
