from collections import deque

# Original dictionary
data = {'a': 1, 'b': 2, 'c': 3}

# Passing the items to a deque (as tuples)
items_deque = deque(data.items())
items_deque.rotate(2)

print(items_deque)
