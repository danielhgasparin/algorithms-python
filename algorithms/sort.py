"""Sort module."""

from math import floor

def bubble_sort(vals):
    """Sort the given array using bubble sort."""
    for i in range(len(vals) - 1):
        for j in range(len(vals) - i - 1):
            if vals[j] > vals[j + 1]:
                vals[j], vals[j + 1] = vals[j + 1], vals[j]
    return vals


def selection_sort(vals):
    """Sort the given array using selection sort."""
    for i in range(len(vals) - 1):
        min_index = i
        for j in range(i + 1, len(vals)):
            if vals[j] < vals[min_index]:
                min_index = j
        if min_index != i:
            vals[i], vals[min_index] = vals[min_index], vals[i]
    return vals


def merge_sort(vals):
    """Sort the given array using merge sort."""
    if len(vals) == 1:
        return vals
    
    mid = floor(len(vals) / 2)

    return _merge(merge_sort(vals[:mid]), merge_sort(vals[mid:]))


def _merge(a, b):
    """Used by "merge_sort" function to merge two sorted arrays into one sorted array."""
    result = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            result.append(a[0])
            del a[0]
        else:
            result.append(b[0])
            del b[0]

    return [*result, *a, *b]