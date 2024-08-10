def max_min_value(dic):
    max_value = max(dic.keys(), key=lambda x: dic[x])
    min_value = min(dic.keys(), key=lambda x: dic[x])
    return max_value, min_value


dic1 = {'a': 2, 'b': 5, 'c': 8, 'd': 1}
maximum, minimum = max_min_value(dic1)
print(dic1[maximum], dic1[minimum])
