def second_largest(list_of_number):
    if len(list_of_number) < 2:
        return
    if len(list_of_number) == 2 and list_of_number[0] == list_of_number[1]:
        return
    unique_items = []
    duplicate_items = set()
    for element in list_of_number:
        if element not in duplicate_items:
            unique_items.append(element)
            duplicate_items.add(element)
    unique_items.sort()
    return unique_items[-2]


print(second_largest([1, 2, 3, 4, 4]))
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_largest([2, 2]))
print(second_largest([1]))
