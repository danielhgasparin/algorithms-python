"""Steps module.

Return a sequence of strings of "n" levels, representing the steps of a progression bar.

Like, for 4 levels: ["#   ", "##  ", "### ", "####"]
"""

def steps_just(n):
    """Return a list of "n" progression steps, using the "ljust" string method."""
    result = []
    for i in range(1, n + 1):
        result.append(("#" * i).ljust(n))
    return result


def steps_concat(n):
    """Return a list of "n" progression steps, concatenating the parts."""
    result = []
    for i in range(1, n + 1):
        result.append(("#" * i) + (" " * (n - i)))
    return result


def steps_loop(n):
    """Return a list of "n" progression steps, using loops."""
    result = []
    for i in range(n):
        line = ""
        for j in range(n):
            line += "#" if j <= i else " "
        result.append(line)
    return result


def steps_recursive(n, steps = None, line = ""):
    """Return a list of "n" progression steps, using recursion."""
    if steps is None:
        steps = []

    if len(steps) == n:
        return steps

    if len(line) == n:
        steps.append(line)
        return steps_recursive(n, steps)

    line += "#" if len(line) <= len(steps) else " "
    return steps_recursive(n, steps, line)