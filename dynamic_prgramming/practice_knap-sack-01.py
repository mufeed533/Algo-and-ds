"""
Develop a solution for knap-sack problem
"""

dict = {}


def knap_sack(v: list, w: list, n: int, c) -> int:
    if c == 0 or n == 0:
        return 0
    if (n, c) in dict:
        return dict[(n, c)]

    if c < w[n - 1]:
        dict[(n, c)] = knap_sack(v, w, n - 1, c)
        return dict[(n, c)]
    else:
        dict[(n, c)] = max(v[n - 1] + knap_sack(v, w, n - 1, c - w[n - 1]),
                           knap_sack(v, w, n - 1, c))
        return dict[(n, c)]


def knap_sack_by_bottom_down_dp(v: list, w: list, n: int, c: int):
    dp = {}
    for i in range(n + 1):
        for j in range(c + 1):
            if i == 0 or j == 0:
                dp[(i, j)] = 0

    for i in range(1, n+1):
        for j in range(1, c+1):
            if w[i - 1] > j:
                dp[(i, j)] = dp[(i - 1, j)]
            else:
                dp[(i, j)] = max(v[i - 1] + dp[(i - 1, j - w[i - 1])], dp[(i - 1, j)])
    return dp[(n, c)]


"""
base condition:
 if c == 0 or n == 0
      return 0

Choice diagram:
            if wi > c:
              return func()
            else:
               return max()
"""

# result = knap_sack([1, 2, 3, 4], [2, 1, 1, 1], 4, 8)
result = knap_sack_by_bottom_down_dp([1, 2, 3, 4], [2, 1, 1, 1], 4, 8)
print(result)
