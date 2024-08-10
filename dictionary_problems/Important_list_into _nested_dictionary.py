# Initialize an empty dictionary that will be used to build the nested structure.
new_dict = current = {}

def nested_dictionary_list(name_list):
    """
    Creates a nested dictionary from a list of names.

    This function takes a list of names and creates a dictionary where each name
    is a key. The value of each key is another dictionary, creating a nested
    structure with the names.

    Args:
        name_list (list): A list of strings where each string is a name.

    Returns:
        dict: A nested dictionary structure based on the names in the list.
    """
    global current  # Use the global 'current' variable to track the current level in the dictionary.
    for name in name_list:
        current[name] = {}  # Create a new empty dictionary for the current name.
        current = current[name]  # Move the current pointer to the newly created dictionary.
    return new_dict  # Return the fully constructed nested dictionary.

# Example usage
list_of_names = ['Abhishek', 'Shanu', 'Saurabh']
print(nested_dictionary_list(list_of_names))
