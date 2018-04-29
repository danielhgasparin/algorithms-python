"""Max occurrence module."""

def max_occurrence(value):
    """Return the char that appears more times in a string."""
    occurrences = dict()
    for char in value:
        occurrences[char] = occurrences.get(char, 0) + 1
    return max(occurrences.items(), key=lambda item: item[1])[0]

def max_occurrence_loop(value):
    """Return the char that appears more times in a string using a loop to check the dictionary."""
    occurrences = dict()
    for char in value:
        occurrences[char] = occurrences.get(char, 0) + 1
    max_value = 0
    max_char = ""
    for item in occurrences.items():
        if item[1] > max_value:
            max_value = item[1]
            max_char = item[0]
    return max_char