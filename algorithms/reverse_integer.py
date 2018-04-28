"""Reverse integer module

Reversed integers must keep their original sign.
"""

def reverse_slice(value):
    str_value = str(value)
    if value >= 0:
        str_reverse = str_value[::-1]
    else:
        str_reverse = "-" + str_value[:0:-1]
    return int(str_reverse)
