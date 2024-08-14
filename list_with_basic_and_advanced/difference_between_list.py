def difference_between_lists(list1, list2):
    difference_list1_list2 = list(set(list1) - set(list2))
    difference_list2_list1 = list(set(list2) - set(list1))
    difference_between_list = difference_list1_list2 + difference_list2_list1
    return difference_between_list


list_1 = [1, 3, 5, 7, 9]
list_2 = [1, 2, 4, 6, 7, 8]
print(difference_between_lists(list_1, list_2))
