
arr = []


# ToDo: This code is unfinished
def subsets_string(s: str, index: int, results: list) -> list:
    if index == len(s):
        return []

    curr_char = s[index]
    prev_res = subsets_string(s, index + 1, results)
    for i in prev_res:
        results.append(i + curr_char)
    results.append(curr_char)
    return results


print(subsets_string("abc", 0, []))
