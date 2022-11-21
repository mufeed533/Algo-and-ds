"https://leetcode.com/problems/house-robber/description/"

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1, r2 = 0, 0

        for i in nums:
            temp = max(r1+i, r2)
            r1 = r2
            r2 = temp
        
        return r2
