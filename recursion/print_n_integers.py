"""
Print up to n integers from 1, using recursion
"""

arr = []


def print_n(n):
    # base condition
    if n == 1:
        arr.append(1)
        return
    arr.append(n)
    print_n(n - 1)


print_n(10)
print(arr)
