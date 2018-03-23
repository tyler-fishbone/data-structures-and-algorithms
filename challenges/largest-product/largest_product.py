def largest_product(lst):
    '''
    This function takes in an array of arrays and returns the largest product of any two elements that are adjeacent to each other. Adjacent is defined as in the same nested array, or having the same second index as element in an adjacent array.
    '''
    try:    
        largest_product = lst[0][0] * lst[0][1]
        for i in range(len(lst)-1):
            prod_1 = lst[i][0] * lst[i + 1][0]
            prod_2 = lst[i][1] * lst[i + 1][1]
            prod_3 = lst[i + 1][0] * lst[i + 1][1]
            if largest_product < prod_1:
                largest_product = prod_1
            if largest_product < prod_2:
                largest_product = prod_2
            if largest_product < prod_3:
                largest_product = prod_3
        return largest_product
    except (IndexError, TypeError):
        print('\n Invalid input. Must be 2D array of values')
