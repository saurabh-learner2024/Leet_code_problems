def dynamic_composer(function_selectors, params):
    """
    Compose and apply a series of lambda functions based on the provided function selectors and parameters.

    Parameters:
    function_selectors (list): A list of lambda functions to be applied.
    params (list): A list of tuples containing parameters for the corresponding lambda functions.

    Returns:
    The result of applying the composed functions to their respective parameters.
    """
    result = None  # Initialize the result to None

    for func, param in zip(function_selectors, params):
        if result is None:
            result = func(*param)  # Apply the first function to its parameters
        else:
            result = func(result)  # Apply subsequent functions to the result of the previous function

    return result

# Define a list of lambda functions (function selectors)
function_selectors = [
    lambda x, y: x + y,    # Function to add two numbers
    lambda z: z * 2,       # Function to double a number
    lambda w: f"{w} is divisible by 5" if (w % 5) == 0 else "Not divisible by 5"  # Function to check divisibility by 5
]

# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Define a list of tuples (parameters for the corresponding functions)
params = [
    (a, b),  # Parameters for the first lambda function (a + b)
    (None,),  # Parameters for the second lambda function (apply to result of first function)
    (None,)   # Parameters for the third lambda function (apply to result of second function)
]

result = dynamic_composer(function_selectors, params)
print(result)  # Output will be based on the user's input
