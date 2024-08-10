from itertools import product

list_of_combination = []


def combination_of_letter(dic):
    combos = product(*[value for value in dic.values()])
    for combo in combos:
        combination = ''.join(combo)
        list_of_combination.append(combination)
    return list_of_combination


input = {'1': ['a', 'b'], '2': ['c', 'd']}
print(combination_of_letter(input))
