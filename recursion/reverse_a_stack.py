"""
Write a recursive python function to reverse a stack
"""


def merge_stack(i: int, sta: list) -> list:
    temp_stack = []
    for _ in range(len(sta)):
        temp_stack.append(sta.pop())
    sta.append(i)
    for _ in range(len(temp_stack)):
        sta.append(temp_stack.pop())
    return sta


def reverse_stack(sta: list) -> list:
    if len(sta) == 1 or not len(sta):
        return sta

    temp = sta.pop()
    return merge_stack(temp, reverse_stack(sta))


print(reverse_stack([]))

"""
Hypothesis:
reverse_stack([3, 1, 4, 6, 7]) -> [7,6,4,1,3]
reverse_stack([3, 1, 4, 6]) -> [6,4,1,3]
reverse_stack([3, 1, 4]) -> [4,1,3]

induction:
val = stack.pop()
stack = reverse_stack(stack)

base condition:
if len(sta) == 1:
   return sta
   
merge_stack()
"""
