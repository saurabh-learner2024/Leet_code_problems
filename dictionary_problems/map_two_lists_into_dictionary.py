def create_student_dictionary(serial_no, students_name):
    """
    Creates a dictionary mapping student serial numbers to student names.

    :param serial_no: A list of serial numbers.
    :type serial_no: list
    :param students_name: A list of student names corresponding to the serial numbers.
    :type students_name: list
    :return: A dictionary mapping serial numbers to student names.
    :rtype: dict
    """
    # Use the map function to create tuples of (serial_no, student_name)
    pairs = map(lambda x: (x[0], x[1]), zip(serial_no, students_name))

    # Convert the map object to a dictionary
    return dict(pairs)


# Define the lists of serial numbers and student names
serial_no = [1, 2, 3, 4, 5, 6, 7]
students_name = ['Abhishek', 'Bulbul', 'Christina', 'David', 'Eris', 'Faizal', 'George']

# Create the dictionary mapping serial numbers to student names
final_dictionary = create_student_dictionary(serial_no, students_name)

# Print the resulting dictionary
print(final_dictionary)
