import itertools


def permutation_of_list(list_of_elements):
    return list(itertools.permutations(list_of_elements))


list_of_element = [1, 2, 3]
print(permutation_of_list(list_of_element))
