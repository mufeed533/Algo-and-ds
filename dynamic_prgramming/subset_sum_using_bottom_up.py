"""
Write a python function using Dynamic Programming for subset sum problem.
Problem :  Given ar array of integers, find if it is possible to find a target sum from subsets of the array.
Output will be True or False
"""


def subset_sum(v: list, t: int) -> bool:
    dp = {}
    n = len(v)
    for i in range(n + 1):
        for j in range(t + 1):
            if i == 0:
                dp[(i, j)] = False
            if j == 0:
                dp[(i, j)] = True

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if v[i - 1] > j:
                dp[(i, j)] = dp[(i - 1, j)]
            else:
                dp[(i, j)] = dp[(i - 1, j - v[i - 1])] or dp[(i - 1, j)]

    return dp[(n, t)]


print(subset_sum([1, 1, 3, 4, 6], 8))
