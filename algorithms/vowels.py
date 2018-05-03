"""Vowels module."""

def vowels(value):
    """Count the number of vowels in a string."""
    return sum(1 for char in value.lower() if char in "aeiou")

def vowels_loop(value):
    """Count the number of vowels in a string, using a loop."""
    count = 0
    for char in value.lower():
        if char in "aeiou":
            count += 1
    return count