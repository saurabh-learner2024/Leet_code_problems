def distinct_values(dic):
    distinct_values = set([value for data in dic for value in data.values()])
    return distinct_values


input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
print(distinct_values(input))