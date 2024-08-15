def multiple_integer_into_one(list_of_numbers):
    return ''.join(map(str, list_of_numbers))


list_of_integers = [11, 22, 33]
print(multiple_integer_into_one(list_of_integers))
