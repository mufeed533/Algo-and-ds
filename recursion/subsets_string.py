results = []


def subsets_string(s, curr):
    if len(s) == 0:
        return ""
    curr = s[-1] + subsets_string(s[:-1], curr)
    results.append(curr)
    curr = ""
    return curr


subsets_string("abc", "")
print(results)
