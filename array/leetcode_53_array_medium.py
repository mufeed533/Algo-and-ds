"https://leetcode.com/problems/maximum-subarray/submissions/837434565/"

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsum = nums[0]
        currSum = 0

        for i in nums:
            currSum = max(currSum, 0)
            currSum += i
            maxsum = max(currSum, maxsum)
        return maxsum
