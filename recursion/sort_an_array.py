"""
Write a recursive function to sort an array
"""


def merge(i: int, arr: list) -> list:
    # [1,2,5,7], 3
    for index, value in enumerate(arr):
        if value > i:
            arr.insert(index, i)
            return arr
    arr.append(i)
    return arr


def sort_arr(arr: list) -> list:
    # base condition
    if len(arr) == 1:
        return arr

    # induction
    return merge(arr[-1], sort_arr(arr[:-1]))


print(sort_arr([5, 7, 0, 2, 3, 3]))

"""
Hypothesis : 

sort_arr([1,5,2,0]) -> [0,1,2,5]
sort_arr([1,5,2]) -> [1,2,5]

merge(int, arr) -> arr


induction:
base conditio:
if sizeArr == 1:
   return [1]

return merge(arr[:-1], sort_arr(arr[:-1)))
"""
