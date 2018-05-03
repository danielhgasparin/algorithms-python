"""Pyramid steps module.

Return a sequence of strings of "n" levels, representing the steps of a progression in a pyramid shape.

Like, for 4 levels: ["   #   ", "  ###  ", " ##### ", "#######"]
"""

def pyramid_steps_concat(n):
    """Return a list of "n" progression pyramid steps, concatenating the parts."""
    result = []
    for i in range(1, n + 1):
        result.append((" " * (n - i)) + ("#" * (i * 2 - 1)) + (" " * (n - i)))
    return result


def pyramid_steps_loop(n):
    """Return a list of "n" progression pyramid steps, using loops."""
    import math
    result = []
    line_size = n * 2 - 1
    line_mid = math.floor(line_size / 2)
    for i in range(n):
        line = ""
        for j in range(line_size):
            line += "#" if j >= line_mid - i and j <= line_mid + i else " "
        result.append(line)
    return result


def pyramid_steps_recursive(n, steps = None, line = ""):
    """Return a list of "n" progression pyramid steps, using recursion."""
    import math

    if steps is None:
        steps = []

    if len(steps) == n:
        return steps

    line_size = n * 2 - 1

    if len(line) == line_size:
        steps.append(line)
        return pyramid_steps_recursive(n, steps)

    line_mid = math.floor(line_size / 2)

    line += "#" if len(line) >= line_mid - len(steps) and len(line) <= line_mid + len(steps) else " "
    return pyramid_steps_recursive(n, steps, line)