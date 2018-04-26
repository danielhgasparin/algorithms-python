"""Main module to execute algorithms.

Usage:
    python main.py <module> <function> [<argument>...]
"""

import sys
import importlib
import util.args as argsutil

package_name = "algorithms"
module_name = sys.argv[1]
function_name = sys.argv[2]
args_str = sys.argv[3:]

module = importlib.import_module(package_name + "." + module_name)
function = getattr(module, function_name)
args = argsutil.convert(args_str)

result = function(*args)

print(result)