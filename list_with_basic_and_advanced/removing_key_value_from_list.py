def remove_key_value_from_list(my_list):
    return [{key: value for key, value in dic.items() if key != 'key1'} for dic in my_list]


original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
print(remove_key_value_from_list(original_list))