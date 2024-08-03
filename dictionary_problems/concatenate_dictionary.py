def concatenate_dicts(dicts):
    concat_dict = {}
    for dic in dicts:
        concat_dict.update(dic)
    return concat_dict


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
final_dicts = concatenate_dicts((dic1, dic2, dic3))
print(final_dicts)
