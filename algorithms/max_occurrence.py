"""Max occurrence module."""

def max_occurrence(value):
    """Return the char that appears more times in a string."""
    occurrences = _dict_builder(value)
    return max(occurrences.items(), key=lambda item: item[1])[0]


def max_occurrence_loop(value):
    """Return the char that appears more times in a string using a loop to check the dictionary."""
    occurrences = _dict_builder(value)
    max_value = 0
    max_char = ""
    for item in occurrences.items():
        if item[1] > max_value:
            max_value = item[1]
            max_char = item[0]
    return max_char


def _dict_builder(string):
    """Return a dictionary containing the occurrence of each char."""
    occurrences = dict()
    for char in string:
        occurrences[char] = occurrences.get(char, 0) + 1
    return occurrences