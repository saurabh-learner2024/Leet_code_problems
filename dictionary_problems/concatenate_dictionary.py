def concatenate_dicts(dicts):
    """
    Concatenates multiple dictionaries into one.

    :param dicts: A tuple or list of dictionaries to be concatenated.
    :type dicts: tuple or list
    :return: A single dictionary containing all key-value pairs from the input dictionaries.
    :rtype: dict
    """
    # Initialize an empty dictionary to hold the concatenated result
    concat_dict = {}
    # Iterate over each dictionary in the input collection
    for dic in dicts:
        # Update the result dictionary with key-value pairs from the current dictionary
        concat_dict.update(dic)
    # Return the concatenated dictionary
    return concat_dict


# Define sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate the sample dictionaries
final_dicts = concatenate_dicts((dic1, dic2, dic3))

# Print the resulting concatenated dictionary
print(final_dicts)


