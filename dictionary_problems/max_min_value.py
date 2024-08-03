def find_max_min_by_value(dics):
    """
    Find the keys with the maximum and minimum values in a dictionary.

    Parameters:
    dics (dict): A dictionary where the keys are the items and the values are comparable values.

    Returns:
    tuple: A tuple containing two elements:
           - The key with the maximum value.
           - The key with the minimum value.
    """
    # Find the key with the maximum value
    max_value = max(dics.keys(), key=lambda k: dics[k])

    # Find the key with the minimum value
    min_value = min(dics.keys(), key=lambda k: dics[k])

    return max_value, min_value


# Example dictionary
dics = {'a': 200, 'b': 300, 'c': 400, 'd': 230}

# Get the keys with the maximum and minimum values
max_key, min_key = find_max_min_by_value(dics)

# Print the results
print(f"Maximum element is '{max_key}' with value {dics[max_key]}")
print(f"Minimum element is '{min_key}' with value {dics[min_key]}")
