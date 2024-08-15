def split_every_nth_element_of_list(list_of_element, step):
    return [list_of_element[i::step] for i in range(step)]


elements_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(split_every_nth_element_of_list(elements_list, 5))