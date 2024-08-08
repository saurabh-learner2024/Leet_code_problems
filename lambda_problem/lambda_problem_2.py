def complex_operations_combiner(add_ops, sub_ops, conditions):
    """
    Combines operations based on given conditions.

    Parameters:
    add_ops (list of functions): A list of functions for addition operations.
    sub_ops (list of functions): A list of functions for subtraction operations.
    conditions (list of bool): A list of boolean values determining which operation to apply.

    Returns:
    list: A list of results from applying the appropriate operations based on conditions.
    """
    results = []  # Initialize an empty list to store results

    # Iterate over the conditions with their index
    for i, condition in enumerate(conditions):
        if condition:
            # If the condition is True, apply the corresponding addition operation
            results.append(add_ops[i](2, 3))
        else:
            # If the condition is False, apply the corresponding subtraction operation
            results.append(sub_ops[i](4, 3))

    return results  # Return the list of results


# Example usage:
add_ops = [
    lambda x, y: x + y,  # Addition function: x + y
    lambda x, y: x + y + 1,  # Addition function: x + y + 1
    lambda x, y: x + y + 2  # Addition function: x + y + 2
]

sub_ops = [
    lambda x, y: x - y,  # Subtraction function: x - y
    lambda x, y: x - y - 1,  # Subtraction function: x - y - 1
    lambda x, y: x - y - 2  # Subtraction function: x - y - 2
]

conditions = [True, False, True]  # List of conditions to decide which operations to apply

result = complex_operations_combiner(add_ops, sub_ops,
                                     conditions)  # Call the function with provided operations and conditions
print(result)  # Output should be [5, 2, 7]
