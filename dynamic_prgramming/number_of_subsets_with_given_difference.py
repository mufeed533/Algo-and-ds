"""
Write a python function to count the number of subsets with the given difference in sum
"""

"""
Find the range -> 0 - sum(arr)

iterate and look for subset with the given target sum
if found, add that into a set
find the number of subsets with given difference
"""


def check_subset_exists(v: list, t: int) -> bool:
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

    for i in range(n + 1):
        for j in range(t + 1):
            if v[i - 1] <= t:
                dp[i][j] = dp[i - 1][j - v[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][t]


def find_number_of_subsets(v: list, t: int) -> int:
    result = 0
    subset_sum = sum(v)

    subset_list = set()

    for i in range(subset_sum + 1):
        if check_subset_exists(v, i):
            difference = (subset_sum - i)
            if abs(i - difference) == t and difference in subset_list:
                print(i, difference)
                result += 1
            subset_list.add(i)
    return result


print(find_number_of_subsets([1, 2, 3, 4], 6))
