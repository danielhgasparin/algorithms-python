"""Reverse string module."""

def reverse_slice(value):
    """Reverse string using slice with a negative step."""
    return value[::-1]


def reverse_functional(value):
    """Reverse string in a functional way using the "reduce" function."""
    from functools import reduce
    return reduce((lambda result, char: char + result), value, "")


def reverse_builtin(value):
    """Reverse string using the built-in function "reversed"."""
    return "".join(reversed(value))


def reverse_loop(value):
    """Reverse string using a loop."""
    result = ""
    for char in value:
        result = char + result
    return result