"https://leetcode.com/problems/palindrome-number/description/"

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        l,r = 0, len(x) - 1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True
