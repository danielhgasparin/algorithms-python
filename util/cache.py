"""Functions to cache data in memory."""

import functools

def memoize(obj):
    """A decorator to cache functions or classes."""
    cache = {}

    @functools.wraps(obj) 
    # Decorator to store name and docstring of original obj to be used in place of those of memoizer.
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]

    return memoizer