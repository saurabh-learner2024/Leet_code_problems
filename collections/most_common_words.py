from collections import Counter
import re


def most_common_elements(text, n=10):
    """
    Finds the most common elements (words) and their counts in the given text.

    Args:
    text (str): The input text to analyze.
    n (int): The number of most common elements to return. Default is 10.

    Returns:
    list of tuples: A list of tuples where each tuple contains a word and its count.
    """
    # Use a regular expression to find all words in the text
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the n most common elements
    most_common = word_counts.most_common(n)

    return most_common


# Example usage
text = """
Python is an interpreted, high-level and general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable use of significant indentation.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""

# Find the 5 most common words
common_elements = most_common_elements(text, n=5)

# Print the results
print(common_elements)
