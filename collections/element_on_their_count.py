def iterate_elements(elements_counts):
    """
    Generator function to iterate over elements as many times as their count.

    Args:
    elements_counts (dict): A dictionary where keys are elements and values are counts.

    Yields:
    element: Each element repeated according to its count.
    """
    # Iterate over each element and its count in the dictionary
    for element, count in elements_counts.items():
        # Repeat the element 'count' times
        for _ in range(count):
            yield element


# Dictionary of elements and their counts
elements_counts = {'a': 3, 'b': 2, 'c': 1}

# Convert the generator to a list to collect the results
result = list(iterate_elements(elements_counts))

# Print the result
print(result)


# # Import the Counter class from the collections module
# from collections import Counter
#
# # Create a Counter object 'c' with specified initial counts for keys 'p', 'q', 'r', and 's'
# c = Counter(p=4, q=2, r=0, s=-2)
#
# # Print the elements in the Counter 'c' as a list
# print(list(c.elements()))