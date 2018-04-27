"""Fibonacci sequence module."""

def fib(n):
    """Return Fibonacci sequence with length "n".

    Args:
        n: The length of the sequence to return.

    Returns:
        A list containing the Fibonacci sequence.
    """
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(b)
        a, b = b, a + b
    return result


def fib_up_to(n):
    """Return Fibonacci sequence up to "n".
    
    Args:
        n: An integer up to wich calculate Fibonacci sequence.

    Returns:
        A list containing the Fibonacci sequence.
    """
    result = []
    a, b = 0, 1
    while b <= n:
        result.append(b)
        a, b = b, a + b
    return result


def fib_generator():
    """Generator of Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def run_fib_generator(n):
    """Return Fibonacci sequence with length "n" using a generator.
    
    Args:
        n: The length of the sequence to return.

    Returns:
        A list containing the Fibonacci sequence.
    """
    result = []
    fib_seq = fib_generator()
    for _ in range(n):
        result.append(next(fib_seq))
    return result


def fib_recursive(n, acc = None):
    """Return Fibonacci sequence with length "n" using recursion.

    Note that since Python have no Tail Call Optimization, using recursion will result in less performance than a simple loop.

    Args:
        n: The length of the sequence to return.
        acc: Acumulator used for the recursive construction of the result list.

    Returns:
        A list containing the Fibonacci sequence.
    """
    if acc is None:
        acc = []
    if n <= 0:
        return acc
    else:
        if len(acc) < 2:
            acc.append(1)
        else:
            acc.append(acc[-1] + acc[-2])
        return fib_recursive(n - 1, acc)


def fib_recursive_mathy(n):
    """Return the number in Fibonacci sequence at position "n" using recursion in a more mathematical way.
    
    Note that this will result in the worst performance of all the other methods in this module.

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The Number in Fibonacci sequence at the specified position.
    """
    if n < 2:
        return n
    else:
        return fib_recursive_mathy(n - 1) + fib_recursive_mathy(n - 2)


def run_fib_recursive_mathy(n):
    """Return Fibonacci sequence with length "n" using a mathematical recursive function.
    
    Args:
        n: The length of the sequence to return.

    Returns:
        A list containing the Fibonacci sequence.
    """
    return [fib_recursive_mathy(i + 1) for i in range(n)]