def remove_element_at_specified_position(list_of_colors):
    updated_list = []
    for index, element in enumerate(list_of_colors):
        if index not in (0, 4, 5):
            updated_list.append(list_of_colors[index])
    return updated_list


list_of_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_element_at_specified_position(list_of_colors))
