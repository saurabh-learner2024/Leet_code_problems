def lists_to_list_of_dictionary(color_name, color_code):
    return [{'color_name': cn, 'color_code': cd} for cn, cd in zip(color_name, color_code)]


names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print(lists_to_list_of_dictionary(names, codes))