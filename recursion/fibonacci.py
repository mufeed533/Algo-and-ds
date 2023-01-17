"""
Create a recursive function for fibonacci series
"""


def fib(n):
    if n == 0 or n == 1:
        return n

    val = fib(n - 2) + fib(n - 1)
    return val


print(fib(15))
