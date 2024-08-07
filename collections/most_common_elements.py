from collections import Counter


def most_common_elements(string):
    elements_with_their_count = Counter(string)
    three_most_common_elements = elements_with_their_count.most_common(3)
    return three_most_common_elements


string_of_elements = 'lkseropewdssafsdfafkpwe'
print(dict(most_common_elements(string_of_elements)))