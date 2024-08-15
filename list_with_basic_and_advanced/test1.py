# # Define a list 'colors' containing sublists, each with a single color name
# colors = [['Red'], ['Green'], ['Black']]
#
# # Use a list comprehension to create a new list, where each sublist is converted to a string
# # The resulting list contains string representations of the sublists
# # The 'join' method is used to concatenate the strings with newline characters '\n' in between
# # This creates a multi-line string where each sublist is on a new line
# # Print the resulting multi-line string
# print('\n'.join(str(lst) for lst in colors))


# import ast
#
# string = "['Red', 'Green', 'Orange']"
# print(type(ast.literal_eval(string)))


# # Define two lists 'num1' and 'num2' containing integers
# num1 = [1, 3, 5, 7, 9, 10]
# num2 = [2, 4, 6, 8]
#
# # Update the last element of 'num1' (using slicing) to be the entire 'num2' list
# # This effectively replaces the last element of 'num1' with the elements of 'num2'
# num1[-1:] = num2
#
# # Print the modified 'num1' list, which now contains the elements of both 'num1' and 'num2'
# print(num1)


# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# print(max(lists, key=lambda x: sum(x)))


# list1 = [{}, {}, {}]
# print(all(not dic for dic in list1))



# # Import the 'groupby' function from the 'itertools' module
# from itertools import groupby
#
# # Define a function 'compress' that takes a list of numbers 'l_nums' as input
# def compress(l_nums):
#     # Use 'groupby' to group consecutive duplicates and return the unique keys
#     return [list(group) for key, group in groupby(l_nums)]
#
# # Define a list 'n_list' with consecutive duplicate elements
# n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
#
# # Print a message indicating the purpose of the following output
# print("Original list:")
#
# # Print the original list 'n_list'
# print(n_list)
#
# # Print a message indicating the purpose of the following output
# print("\nAfter removing consecutive duplicates:")
#
# # Call the 'compress' function with 'n_list' as an argument and print the result with consecutive duplicates removed
# print(compress(n_list))


# Define a function 'decode' that takes a list 'alist' as input
def decode(alist):
    # Define a nested function 'aux' that processes individual elements or sublists
    def aux(g):
        # Check if the element 'g' is a list
        if isinstance(g, list):
            # If it is a list, return a tuple with the element at index 1 and a range of length 'g[0]'
            return [(g[1], range(g[0]))]
        else:
            # If 'g' is not a list, return a tuple with 'g' and a range of length 1
            return [(g, [0])]

    # Use list comprehensions to decode the run-length encoded 'alist'
    return [x for g in alist for x, R in aux(g) for i in R]


# Create a list 'n_list' containing a run-length encoded representation
n_list = [[2, 1], 2, 3, [2, 4], 5, 1]

# Print a message indicating the original encoded list
print("Original encoded list:")
# Print the original encoded list
print(n_list)

# Print a message indicating the decoded list from the run-length encoded input
print("\nDecode a run-length encoded said list:")
# Call the 'decode' function with 'n_list' and print the result
print(decode(n_list))
