# Define a list 'colors' containing sublists, each with a single color name
colors = [['Red'], ['Green'], ['Black']]

# Use a list comprehension to create a new list, where each sublist is converted to a string
# The resulting list contains string representations of the sublists
# The 'join' method is used to concatenate the strings with newline characters '\n' in between
# This creates a multi-line string where each sublist is on a new line
# Print the resulting multi-line string
print('\n'.join(str(lst) for lst in colors))
