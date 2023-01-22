"""
Write a python function to find minimum subset sum from an array using dynamic programming
"""
"""
find range -> 0 to sum(arr)

find if subset sum of each of these elements are possible

if possible, add the range into an array

iterate through the above array and if you can find the pair, calculate the minimum from the difference
"""


def find_subset_sum(v: list, t: int) -> bool:
    dp = []
    n = len(v)

    for _ in range(n + 1):
        temp = []
        for _ in range(t + 1):
            temp.append(False)
        dp.append(temp)

    for i in range(n + 1):
        for j in range(t + 1):
            if j == 0:
                dp[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, t + 1):
            if v[i - 1] <= t:
                dp[i][j] = dp[i - 1][j - v[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][t]


def minimum_subset_sum(v: list) -> int:
    subset_sum_range = sum(v)

    all_subset_sums = set()
    min_subset = subset_sum_range + 1
    for i in range(1, subset_sum_range):
        if find_subset_sum(v, i):
            if (subset_sum_range - i) in all_subset_sums:
                print(i, subset_sum_range - i)
                min_subset = min(min_subset, abs(i - (subset_sum_range - i)))
            all_subset_sums.add(i)
    return min_subset


print(minimum_subset_sum([1, 2, 3, 5]))
