def check_circularly_identical(list_1, list_2):
    return ''.join(map(str, list_2)) in ''.join(map(str, list_1 * 2))


list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print(check_circularly_identical(list1, list2))
print(check_circularly_identical(list2, list3))
print(check_circularly_identical(list1, list3))