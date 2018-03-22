def insert_shift_list(list_input, val):
    list_output = []
    list_midpoint = len(list_input) // 2
    for i in range(len(list_input) + 1):
        if i < list_midpoint:
            list_output += [list_input[i]]
        elif i == list_midpoint:
            list_output += [val]
        else:
            list_output += [list_input[i - 1]]
    return list_output
