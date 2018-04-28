"""Palindrome module

Palindromes are strings that form the same word if reversed
"""

def is_palindrome(value):
    """Check if a string is a palindrome."""
    return value == value[::-1]

def is_palindrome_functional(value):
    """Check if a string is a palindrome in a functional way using the "all" function."""
    return all(char == value[len(value) - i - 1] for i, char in enumerate(value) if i <= (len(value) / 2) - 1)