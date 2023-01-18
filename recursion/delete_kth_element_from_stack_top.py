"""
Write a recursive function to delete kth element from stack top
"""


def solve(sta: list, k: int) -> list:
    if k == 1:
        sta.pop()
        return sta
    temp = sta.pop()
    sta = solve(sta, k - 1)
    sta.append(temp)
    return sta


def delete_kth_element(sta: list, k: int) -> list:
    if k > len(sta) or k == 0 or not sta:
        return sta
    return solve(sta, k)


print(delete_kth_element([1, 5, 7, 2, 3], 5))
