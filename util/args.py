"""Functions to work with lists of arguments."""

def convert(args_list):
    """Convert a list of arguments from string to whatever type it can be converted.

    Args:
        args_list: A list of string arguments.

    Returns:
        A list of arguments, each of the type that could be converted.
    """
    result = []
    for item in args_list:
        try:
            result.append(int(item))
            continue
        except ValueError:
            pass
        
        try:
            result.append(float(item))
            continue
        except ValueError:
            pass

        result.append(str(item))

    return result