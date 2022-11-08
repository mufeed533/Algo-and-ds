"https://leetcode.com/problems/longest-repeating-character-replacement/description/"

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0

        frequency = {}
        max_sub_array = 0

        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            max_frequency = frequency[max(frequency, key=frequency.get)]
            if ((r - l + 1) - max_frequency) > k:
                frequency[s[l]] -= 1
                l += 1
                
            max_sub_array = max(max_sub_array, r - l + 1)
        return max_sub_array
