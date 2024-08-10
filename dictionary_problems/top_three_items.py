# Import the 'nlargest' function from the 'heapq' module.
# This will be used to find the top n items from an iterable.
from heapq import nlargest

# Import the 'itemgetter' function from the 'operator' module.
# This will be used to extract the value from a tuple for comparison.
from operator import itemgetter

# Initialize an empty dictionary to store the top three items.
top_three = {}


def top_three_items(my_dict):
    """
    Finds the top three items with the highest values in a dictionary.

    This function takes a dictionary where keys are items and values are
    numerical values (e.g., prices). It returns a dictionary containing the
    top three items with the highest values.

    Args:
        my_dict (dict): A dictionary where keys are items and values are
                        numerical values (e.g., prices).

    Returns:
        dict: A dictionary containing the top three items with the highest values.
    """
    # Iterate over the top three items with the highest values in 'my_dict'.
    # 'nlargest' returns the largest 'n' items, using 'itemgetter(1)' to sort
    # by the dictionary values (which are at index 1 in the (key, value) tuple).
    for name, value in nlargest(3, my_dict.items(), key=itemgetter(1)):
        # Add the item and its value to the 'top_three' dictionary.
        top_three[name] = value

    # Return the 'top_three' dictionary containing the top three items.
    return top_three


# Define a dictionary of items with their corresponding values.
items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# Print the result of the 'top_three_items' function applied to the 'items' dictionary.
print(top_three_items(items))
