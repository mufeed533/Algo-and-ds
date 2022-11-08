"https://leetcode.com/problems/valid-palindrome/submissions/839506855/"

class Solution(object):
    def is_alpha_numeric(self, c):
        if ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
            return True
        return False
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0, len(s)-1
        while l < r:
            while l < r and not self.is_alpha_numeric(s[l]):
                l += 1
            while r > l and not self.is_alpha_numeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
