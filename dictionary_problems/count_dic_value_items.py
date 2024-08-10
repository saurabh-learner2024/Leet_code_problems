
def count_dict_values_item(my_dict):
    ctr = sum(map(len,my_dict.values()))
    return ctr

dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
print(count_dict_values_item(dict1))