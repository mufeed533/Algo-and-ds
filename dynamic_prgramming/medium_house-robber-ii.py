"https://leetcode.com/problems/house-robber-ii/description/"

class Solution(object):
    def helper_function(self, nums):
        r1, r2 = 0, 0
        for i in nums:
            temp = max(r2, r1+i)
            r1 = r2
            r2 = temp
        return r2

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        return max(self.helper_function(nums[1:]), self.helper_function(nums[:len(nums)-1]))
