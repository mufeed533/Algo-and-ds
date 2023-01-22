"""
Write a python function with DP to count the number of subsets with given sum
"""


def count_subset(v: list, t: int) -> int:
    n = len(v)
    dp = []
    for _ in range(n + 1):
        temp = []
        for _ in range(t + 1):
            temp.append(0)
        dp.append(temp)

    for i in range(n + 1):
        for j in range(t + 1):
            if j == 0:
                dp[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if v[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - v[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][t]


print(count_subset([1, 2, 3, 4, 6], 8))
