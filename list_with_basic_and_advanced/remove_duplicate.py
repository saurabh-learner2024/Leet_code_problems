def remove_duplicate(list_of_element):
    duplicate_sets = set()
    uniq_items = []
    for ele in list_of_element:
        if ele not in duplicate_sets:
            uniq_items.append(ele)
            duplicate_sets.add(ele)
    return (uniq_items)

list_of_element = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(remove_duplicate(list_of_element))