"""Fizzbuzz module.

Returns a sequence from 1 to n, replacing the numbers divisible by 3 for the word "fizz",
divisible by 5 for the word "buzz" and divisible by both 3 and 5 for the word "fizzbuzz".
"""

def fizzbuzz(n):
    """Return a sequence up to "n" using the fizzbuzz rule."""
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            value = "fizzbuzz"
        elif i % 3 == 0:
            value = "fizz"
        elif i % 5 == 0:
            value = "buzz"
        else:
            value = str(i)
        result.append(value)
    return result


def fizzbuzz_generator():
    """Generator of Fizzbuzz sequence."""
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield "fizzbuzz"
        elif i % 3 == 0:
            yield "fizz"
        elif i % 5 == 0:
            yield "buzz"
        else:
            yield str(i)
        i += 1


def run_fizzbuzz_generator(n):
    """Return Fizzbuzz sequence up to "n" using using "fizzbuzz_generator"."""
    result = []
    fizzbuzz_gen = fizzbuzz_generator()
    for _ in range(n):
        result.append(next(fizzbuzz_gen))
    return result