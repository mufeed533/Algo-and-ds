"https://leetcode.com/problems/longest-palindromic-substring/description/"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        res_length = 0

        for i in range(len(s)):
            # odd case
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res_length = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
            # even case
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_length:
                    res_length = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
        return res
