"https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/837969935/:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        m = set()
        subsring_length = 0

        for r in range(len(s)):
            if s[r] in m: 
                while l < r and s[l] != s[r]:
                    m.remove(s[l])
                    l += 1
                m.remove(s[l])
                l += 1

            m.add(s[r])
            subsring_length = max(subsring_length, r - l + 1)
        return subsring_length

