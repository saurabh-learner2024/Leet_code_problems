def count_distinct_words(words):
    """
    Counts the number of distinct words and their occurrences.

    Args:
    words (list): A list of words.

    Returns:
    tuple: Number of distinct words and a dictionary of word counts in the order of their appearance.
    """
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    number_of_distinct_word = len(word_count)
    return number_of_distinct_word, word_count


# Example usage
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'kiwi', 'kiwi', 'banana']
numbers_of_dist_word, word_with_count = count_distinct_words(words)

print(f"Number of distinct words is {numbers_of_dist_word}")

for word, count in word_with_count.items():
    print(f"{word} has count {count}")
