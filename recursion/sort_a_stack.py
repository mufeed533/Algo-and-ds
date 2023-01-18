"""
Write a function to sort a stack using recursion
"""


def merge_stack(i: int, sta: list) -> list:
    new_stack = list()
    for _ in range(len(sta)):
        curr_val = sta.pop()
        if curr_val <= i:
            sta.append(curr_val)
            sta.append(i)
            break
        new_stack.append(curr_val)

    if not sta:
        sta.append(i)

    for _ in range(len(new_stack)):
        sta.append(new_stack.pop())
    return sta


def sort_stack(sta: list) -> list:
    if len(sta) == 1:
        return sta

    stack_item = sta.pop()
    return merge_stack(stack_item, sort_stack(sta))


print(sort_stack([5, 7, 1, 3, 2]))
