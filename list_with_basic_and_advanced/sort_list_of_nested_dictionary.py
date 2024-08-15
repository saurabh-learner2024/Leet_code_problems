def sort_list_of_nested_dictionary(my_list):
    return sorted(my_list, key=lambda x: x['key']['subkey'], reverse=True)


my_dict = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print(sort_list_of_nested_dictionary(my_dict))