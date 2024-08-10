from collections import Counter

result = Counter()


def combine_values(lst):
    for dic in lst:
        result[dic['item']] += dic['amount']
    return dict(result)


input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combine_values(input))
