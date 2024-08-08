def combine_add_sub(add, sub):
    return add(2, 3), sub(4, 3)


addition, subtraction = combine_add_sub((lambda x, y: x + y), (lambda x, y: x - y))
print(addition, subtraction)
