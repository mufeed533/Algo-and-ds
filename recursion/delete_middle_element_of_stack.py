"""
Write a function to delete middle element of stack
"""


def solve(sta: list, middle: int) -> list:
    if middle == 1:
        sta.pop()
        return sta

    temp = sta.pop()
    sta = solve(sta, middle - 1)
    sta.append(temp)
    return sta


def delete_middle(sta: list) -> list:
    middle = (len(sta) // 2) + 1
    result = solve(sta, middle)
    return result


print(delete_middle([1, 5]))
