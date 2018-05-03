"""Capitalization module.

Converts the first letter of each word in a string to upper case, that is, title case.

Obviously the string methods "capitalize" and "title" will not be used.
"""

def title_case(value):
    """Return the specified string in title case."""
    return " ".join(word[0].upper() + word[1:] for word in value.split())

def title_case_loop(value):
    """Return the specified string in title case using a loop."""
    result = ""
    for i, word in enumerate(value):
        if(i == 0 or value[i - 1] == " "):
            result += word.upper()
        else:
            result += word
    return result