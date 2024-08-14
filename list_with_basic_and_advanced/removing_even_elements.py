def removing_even_position_element(list_of_names):
    odd_number_element = []
    for index, element in enumerate(list_of_names):
        if index % 2 != 0:
            odd_number_element.append(list_of_names[index])
    return odd_number_element


list_of_elements = ["Abhishek", "Shanu", "Shastri", "Tanuja", "Abhijeet"]
print(removing_even_position_element(list_of_elements))