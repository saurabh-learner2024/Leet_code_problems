# Create a nested list 'l' using a list comprehension
# This list comprehension generates a 5x5 matrix with elements calculated using the formula 5*i + j
l = [[10*i + j for j in range(1, 11) if (10*i + j) % 2 == 0] for i in range(5)]

# Print the resulting 5x5 matrix 'l'
print(l)
