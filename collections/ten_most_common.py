# Import the Counter class from the collections module
from collections import Counter

# Import the re module for regular expressions
import re

# Define a multi-line text string containing information about Python
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python-related development with our grants program and by funding 
special projects."""

# Use a regular expression to extract words from the text
words = re.findall(r'\b\w+\b', text)

# Use Counter to count the occurrences of each word in the text and find the 10 most common words
print(Counter(words).most_common(10))
