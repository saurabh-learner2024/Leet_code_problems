def sort_list_of_tuple(list_of_tuple):
    sort_by_last_element = sorted(list_of_tuple, key=lambda x: x[-1])
    return sort_by_last_element


list_of_tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_list_of_tuple(list_of_tuple))