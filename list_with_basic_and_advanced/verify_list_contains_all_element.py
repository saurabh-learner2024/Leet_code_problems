def check_all_element_of_list(color):
    return all(c == 'blue' for c in color)


color1 = ["green", "orange", "black", "white"]
color2 = ["blue", "blue", "blue", "blue", "blue"]
print(check_all_element_of_list(color1))
print(check_all_element_of_list(color2))