"""
Write a recursive function to check a subset sum is possible from an array of integers
"""


def subset_sum(v: list, n: int, s: int) -> bool:
    if s == 0:
        return True

    if n == 0:
        return False

    if v[n - 1] > s:
        return subset_sum(v, n - 1, s)
    else:
        return subset_sum(v, n - 1, s - (v[n - 1])) or subset_sum(v, n - 1, s)


print(subset_sum([1, 2, 3, 4], 4, 11))
"""

"""
