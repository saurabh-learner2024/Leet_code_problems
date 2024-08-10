from collections import deque

# Initialize an empty deque
dq = deque()

# Add elements to the deque
dq.append(1)        # Add to the right side
dq.append(2)
dq.appendleft(0)    # Add to the left side

print(f"Initial deque: {dq}")

# Remove elements from the deque
dq.pop()            # Remove from the right side
print(f"After pop: {dq}")

dq.popleft()        # Remove from the left side
print(f"After popleft: {dq}")

# Access elements in the deque
print(f"First element: {dq[0]}")   # Access the first element
print(f"Last element: {dq[-1]}")   # Access the last element

# Rotate the deque
dq.append(3)
dq.append(4)
print(f"Before rotation: {dq}")
dq.rotate(1)        # Rotate to the right by 1
print(f"After rotating right by 1: {dq}")
dq.rotate(-2)       # Rotate to the left by 2
print(f"After rotating left by 2: {dq}")

# Extend the deque with iterable
dq.extend([5, 6, 7])         # Add elements to the right side
print(f"After extend right: {dq}")
dq.extendleft([-1, -2, -3])  # Add elements to the left side
print(f"After extend left: {dq}")

# Remove specific element
dq.remove(3)  # Remove the first occurrence of 3
print(f"After removing element 3: {dq}")

# Get the length of the deque
print(f"Length of deque: {len(dq)}")

# Clear all elements
dq.clear()
print(f"After clearing deque: {dq}")

# Create a deque with a fixed size
fixed_dq = deque(maxlen=3)
fixed_dq.extend([1, 2, 3])
print(f"Fixed size deque: {fixed_dq}")

# Adding more elements when deque is full
fixed_dq.append(4)  # Oldest element (1) will be removed
print(f"After appending to full deque: {fixed_dq}")
