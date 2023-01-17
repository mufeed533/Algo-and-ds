"""
Write a recursive function to reverse a string
"""


def reverse_string(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_string(s[:-1])


print(reverse_string("abcdef"))
