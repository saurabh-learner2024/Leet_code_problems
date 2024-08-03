# define a data_dictionary with key-value pairs
data_dictionary = {'a': 11, 'b': 13, 'c': 23, 'd': 34, 'e': 21, 'f': 12}
# define a variable sorted_data_dictionary, sorted function is used to sort the value
# here we use key attributes to sort the dictionary on the basis of their values
sorted_data_dictionary = sorted(data_dictionary.items(), key=lambda x: x[1])
# print the sorted_data_dictionary to see the output
print(sorted_data_dictionary)
