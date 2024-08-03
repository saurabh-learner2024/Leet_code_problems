import operator

def sort_dict_by_value(dic):
    """
    Sorts a dictionary by its values and returns a new dictionary.

    Args:
        dic (dict): The dictionary to sort.

    Returns:
        dict: A new dictionary sorted by values.
    """
    # Sort the dictionary items by values using operator.itemgetter
    sorted_items = sorted(dic.items(), key=operator.itemgetter(1))
    # Convert the sorted items back into a dictionary
    sorted_dict = dict(sorted_items)
    return sorted_dict

# Sample data dictionary
data_dictionary = {'c': 23, 'd': 34, 'e': 21, 'a': 11, 'b': 13, 'f': 12}

# Print the sorted dictionary
print(sort_dict_by_value(data_dictionary))
