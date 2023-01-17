results = []

arr = []


# ToDo: This code is unfinished
def subsets_string(s, index, curr):
    if index == len(s):
        return []
    arr.append([s[index]] + subsets_string(s, index + 1, curr))
    arr.append(subsets_string(s, index + 1, curr))
    return []


print(subsets_string("abc", 0, ""))
