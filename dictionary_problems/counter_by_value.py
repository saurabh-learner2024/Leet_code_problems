# Import the 'Counter' class from the 'collections' module.
from collections import Counter

# Create a Counter object 'x' with subjects as keys and associated scores as values.
x = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})

# Print the most common elements in the 'x' Counter, which are subject-score pairs.
print(x.most_common())
