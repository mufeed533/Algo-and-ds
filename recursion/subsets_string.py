
arr = []


def subsets_string(s: str) -> list:
    if len(s) == 0:
        return ['']

    curr_char = s[-1]
    prev_res = subsets_string(s[:-1])
    results = []
    for i in prev_res:
        results.append(i)
        results.append(i + curr_char)
    return results


print(subsets_string("abc"))
