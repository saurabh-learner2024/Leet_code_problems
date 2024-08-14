def common_data(list1, list2):
    common_elements = []
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                common_elements.append(num1)
    return common_elements


list_1 = [1, 2, 3, 4, 9, 6, 5]
list_2 = [5, 6, 7, 8, 9]
print(common_data(list_1, list_2))