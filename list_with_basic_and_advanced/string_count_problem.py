def string_count_of_list(list_string):
    count = 0
    for ele in list_string:
        if len(ele) >= 2 and ele[0] == ele[-1]:
            count = count + 1
    return count


list_of_string = ['abc', 'xyz', 'aba', '1221']
print(string_count_of_list(list_of_string))
