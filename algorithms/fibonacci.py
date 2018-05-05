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


def run_fib_generator(n):
    """Return Fibonacci sequence with length "n" using "fib_generator".
    
    Args:
        n: The length of the sequence to return.

    Returns:
        A list containing the Fibonacci sequence.
    """
    result = []
    fib_gen = _fib_generator()
    for _ in range(n):
        result.append(next(fib_gen))
    return result


def _fib_generator():
    """Generator of Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


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

    if len(acc) < 2:
        acc.append(1)
    else:
        acc.append(acc[-1] + acc[-2])
    return fib_recursive(n - 1, acc)


def fib_recursive_mathy(n):
    """Return the number in Fibonacci sequence at position "n" using recursion in a more mathematical way.
    
    Very slow solution without cache!

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The Number in Fibonacci sequence at the specified position.
    """
    if n < 2:
        return n

    return fib_recursive_mathy(n - 1) + fib_recursive_mathy(n - 2)


def run_fib_recursive_mathy(n):
    """Return Fibonacci sequence with length "n" using "fib_recursive_mathy".
    
    Args:
        n: The length of the sequence to return.

    Returns:
        A list containing the Fibonacci sequence.
    """
    return [fib_recursive_mathy(i + 1) for i in range(n)]


def fib_recursive_mathy_memoized(n):
    """Same function as "fib_recursive_mathy", but this will be memoized."""
    if n < 2:
        return n

    return fib_recursive_mathy_memoized(n - 1) + fib_recursive_mathy_memoized(n - 2)


def _memoize(func):
    """Memoizer to store cache of calls to "fib_recursive_mathy"."""
    cache = {}
    def memoizer (n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return memoizer

# Replace the function "fib_recursive_mathy_memoized" with its memoized version.
fib_recursive_mathy_memoized = _memoize(fib_recursive_mathy_memoized)


def run_fib_recursive_mathy_memoized(n):
    """Return Fibonacci sequence with length "n" using "fib_recursive_mathy_memoized".

    Args:
        n: The position in the Fibonacci sequence.

    Returns:
        The Number in Fibonacci sequence at the specified position.
    """
    return [fib_recursive_mathy_memoized(i + 1) for i in range(n)]


from util.cache import memoize
@memoize
def fib_recursive_mathy_cached(n):
    """Same function as "fib_recursive_mathy", but this is cached using a generic memoizer as decorator.
    
    The decorator is implemented in "./util/cache.py".
    """
    if n < 2:
        return n

    return fib_recursive_mathy_cached(n - 1) + fib_recursive_mathy_cached(n - 2)


def run_fib_recursive_mathy_cached(n):
    """Return Fibonacci sequence with length "n" using "fib_recursive_mathy_cached".
    
    Args:
        n: The length of the sequence to return.

    Returns:
        A list containing the Fibonacci sequence.
    """
    return [fib_recursive_mathy_cached(i + 1) for i in range(n)]