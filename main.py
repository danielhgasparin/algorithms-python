"""Main module to execute algorithms.

Usage:
    python main.py <function-name> [<argument>...]
"""

import sys

function_name = sys.argv[1]
args = sys.argv[2:]

if function_name == "fib_up_to":
    from algorithms.fibonacci import fib_up_to
    result = fib_up_to(int(args[0]))
    print(result)