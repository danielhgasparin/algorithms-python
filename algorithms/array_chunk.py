"""Array chunk module.

Break an array into smaller arrays of the specified size.
"""

def array_chunk_slice(array, size):
    """Return an array containing chunks of the specified array with the specified size, using "slice"."""
    result = []
    for i in range(0, len(array), size):
        result.append(array[i: i + size])
    return result


def array_chunk_loop(array, size):
    """Return an array containing chunks of the specified array with the specified size, using a loop."""
    result = []
    chunk = []
    for i, value in enumerate(array):
        chunk.append(value)
        if len(chunk) == size or i + 1 == len(array):
            result.append(chunk[:])
            chunk.clear()
    return result