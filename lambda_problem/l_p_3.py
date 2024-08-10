def dynamic_operation_selector(op_list1, op_list2, conditions, params1, params2):
    """
    Select and apply operations from two lists of lambda functions based on conditions.

    Parameters:
    op_list1 (list): A list of lambda functions for the first type of operations.
    op_list2 (list): A list of lambda functions for the second type of operations.
    conditions (list): A list of boolean values indicating which list of operations to use.
    params1 (list): A list of tuples containing parameters for the operations in op_list1.
    params2 (list): A list of tuples containing parameters for the operations in op_list2.

    Returns:
    list: A list of results obtained by applying the corresponding operations based on the conditions and parameters.
    """
    results = []  # Initialize an empty list to store the results

    # Iterate over the conditions along with their index
    for i, condition in enumerate(conditions):
        # Check if the condition is True
        if condition:
            # Apply the corresponding lambda function from op_list1 using params1 and append the result
            results.append(op_list1[i](*params1[i]))
        else:
            # Apply the corresponding lambda function from op_list2 using params2 and append the result
            results.append(op_list2[i](*params2[i]))

    return results  # Return the list of results


# Example usage:
op_list1 = [
    lambda x, y: x * y,  # Operation for index 0
    lambda x, y: x ** y,  # Operation for index 1
    lambda x, y: x + y  # Operation for index 2
]

op_list2 = [
    lambda x, y: x / y,  # Operation for index 0
    lambda x, y: x - y,  # Operation for index 1
    lambda x, y: x % y  # Operation for index 2
]

conditions = [True, False, True]  # Conditions determining which list of operations to use
params1 = [(2, 3), (4, 2), (1, 5)]  # Parameters for the operations in op_list1
params2 = [(8, 2), (7, 4), (10, 3)]  # Parameters for the operations in op_list2

result = dynamic_operation_selector(op_list1, op_list2, conditions, params1, params2)
print(result)  # Output should be [6, 3, 6]
