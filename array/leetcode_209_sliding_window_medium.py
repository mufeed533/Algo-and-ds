"https://leetcode.com/problems/minimum-size-subarray-sum/submissions/837849435/"

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0 
        totalSum = 0
        minarrayLength = len(nums)

        while l <= r and r < len(nums):
            if totalSum >= target:
                minarrayLength = min(minarrayLength, r - l + 1)
                totalSum -= nums[l]
                l += 1
            
            totalSum += nums[r]
            r += 1
        return minarrayLength
