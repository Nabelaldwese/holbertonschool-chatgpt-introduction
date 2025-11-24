#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
        n (int): The number for which the factorial is to be computed.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)

