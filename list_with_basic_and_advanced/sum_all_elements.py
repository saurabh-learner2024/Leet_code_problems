def sum_list_element(list_num):
    total = 0
    """
    'A function that adds all the elements of the list'.
    
    :param list_num: Containing a list of integer elements
    :return total: total of all elements
    """
    for ele in list_num:
        total = total + ele
    return total


list1 = [11, 12, 13, 14, 15]
print(sum_list_element(list1))
print(sum_list_element.__doc__)
