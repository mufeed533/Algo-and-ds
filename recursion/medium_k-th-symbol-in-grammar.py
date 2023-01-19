"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
"""


def find_kth_symbol(n: int, k: int) -> int:
    # base condition
    if n == 1 and k == 1:
        return 0
    mid = pow(2, n - 1) // 2
    if k <= mid:
        return find_kth_symbol(n - 1, k)
    else:
        return 0 if find_kth_symbol(n - 1, k - mid) == 1 else 1


"""
n = 1,     0
n = 2,     01
n = 3,     0110
n = 4,     01101001
n = 5,     0110100110010110

n == 1? return 0

kthsymbol(n) = kthsymbol(n-1) + insert() 
"""

print(find_kth_symbol(30, 434991989))
