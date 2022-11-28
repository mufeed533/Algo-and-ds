"https://leetcode.com/problems/word-break/description/"

class Solution:
    def wordBreak(self, s, wordDict):
        i = 0
        dp = [True] + [False] * len(s)

        for indx in range(len(s)+1):
            for word in wordDict:
                if len(word) <= len(s) and dp[indx - len(word)] and s[:indx].endswith(word):
                    dp[indx] = True
        return dp[-1]


