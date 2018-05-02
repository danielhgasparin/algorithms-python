"""Anagram module.

Anagrams are strings that uses the same characters in the same quantity, disregarding spaces, punctuation and character case.
"""

def anagram_sort(a, b):
    """Check if the strings are anagrams of each other."""
    return _clean_sort(a) == _clean_sort(b)


def _clean_sort(string):
    """Clean non-alphanumeric characteres and sort into a list."""
    return sorted(char.casefold() for char in string if char.isalnum())


def anagram_sort_regex(a, b):
    """Check if the strings are anagrams of each other using regular expression."""
    return _clean_sort_regex(a) == _clean_sort_regex(b)


def _clean_sort_regex(string):
    """Clean non-alphanumeric characteres using regular expression and sort into a list."""
    import re
    return sorted(re.sub(r"\W", "", string).casefold())


def anagram_dict(a, b):
    """Check if the strings are anagrams of each other using dictionaries."""
    dict_a = _build_dict(a)
    dict_b = _build_dict(b)
    return dict_a == dict_b


def anagram_dict_loop(a, b):
    """Check if the strings are anagrams of each other using dictionaries and comparing then with a loop."""
    dict_a = _build_dict(a)
    dict_b = _build_dict(b)
    if len(dict_a) != len(dict_b):
        return False
    for key in dict_a:
        if dict_a[key] != dict_b.get(key):
            return False
    return True


def _build_dict(string):
    """Return a dictionary containing the occurrence of each alphanumeric, case-insensitive, char."""
    occurrences = dict()
    for char in string:
        if char.isalnum():
            char = char.casefold()
            occurrences[char] = occurrences.get(char, 0) + 1
    return occurrences