from collections import defaultdict

result = defaultdict(set)


def dict_from_two_list(list1, list2):
    for key, value in zip(list1, list2):
        result[key].add(value)
    return dict(result)


list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
list2 = [1, 2, 2, 3]
print(dict_from_two_list(list1, list2))
