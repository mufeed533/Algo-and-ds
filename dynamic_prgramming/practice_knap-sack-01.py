"""
Develop a solution for knap-sack problem
"""


def knap_sack(weights: list, values: list, n: int, capacity: int) -> int:
    # base condition
    if n == 0 or capacity == 0:
        return 0

    # choice diagram
    if weights[n - 1] > capacity:
        # can not add
        return knap_sack(weights, values, n - 1, capacity)
    else:
        # we can add
        return max(values[n - 1] + knap_sack(weights, values, n - 1, capacity - values[n - 1]),
                   knap_sack(weights, values, n - 1, capacity))


w = [1, 2, 3, 4]
v = [2, 4, 1, 3]
c = 8

result = knap_sack(w, v, len(w), c)
print(result)
