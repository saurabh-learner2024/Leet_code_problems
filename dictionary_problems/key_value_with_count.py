def key_value_count(my_dict):
    """
    Prints each key-value pair in a dictionary along with its position.

    This function iterates over a dictionary, printing each key, its associated
    value, and the position (count) of the key-value pair in the dictionary.

    Args:
        my_dict (dict): A dictionary where keys are paired with values.

    Returns:
        None
    """
    # Iterate over each key-value pair in the dictionary 'my_dict'.
    # 'enumerate' is used to get a count (starting from 1) along with the key-value pair.
    for count, (key, value) in enumerate(my_dict.items(), 1):
        # Print the key, value, and count (position) in a formatted way.
        print(key, '   ', value, '    ', count)
        # The 'pass' statement is not necessary here, but it indicates that
        # there is no further action to be taken within this loop.
        pass


# Define a dictionary 'dict_num' with integer keys and values.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Call the 'key_value_count' function with 'dict_num' as the argument.
key_value_count(dict_num)
