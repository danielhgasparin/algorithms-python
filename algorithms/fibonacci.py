"""Fibonacci sequence module."""

def fib_up_to(n):
    """Return Fibonacci sequence up to "n".
    
    Args:
        n: An integer up to wich calculate Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence.
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
