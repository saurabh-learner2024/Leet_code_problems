from collections import Counter


def combine_two_dictionary_by_adding_common_key_values(dic1, dic2):
    """
    Combine two dictionaries by adding the values of common keys.

    This function takes two dictionaries as input and returns a new dictionary.
    For each key that appears in both input dictionaries, its value in the resulting
    dictionary is the sum of its values from both input dictionaries. Keys that appear
    only in one dictionary will be included in the resulting dictionary with their
    corresponding values.

    Args:
        dic1 (dict): The first dictionary.
        dic2 (dict): The second dictionary.

    Returns:
        dict: A dictionary with combined values for common keys.
    """
    return dict(Counter(dic1) + Counter(dic2))


# Sample dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries and print the result
print(combine_two_dictionary_by_adding_common_key_values(d1, d2))
