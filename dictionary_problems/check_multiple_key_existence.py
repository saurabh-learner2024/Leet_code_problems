# Create a dictionary 'student' with key-value pairs representing a student's information.
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

# Check if the set of keys in 'student' contains the keys 'class' and 'name'.
print(student.keys() >= {'class', 'name'})

# Check if the set of keys in 'student' contains the keys 'name' and 'Alex'.
# Note that 'Alex' is not a key, so this check will always be False.
print(student.keys() >= {'name', 'Alex'})

# Check if the set of keys in 'student' contains the keys 'roll_id' and 'name'.
print(student.keys() >= {'roll_id', 'name'})
