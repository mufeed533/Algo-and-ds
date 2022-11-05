"https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/837507470/"

class Solution(object):
    def kedans_algo(self, nums):
        max_sum = nums[0]
        curr_sum = 0
        for i in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += i
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_from_kedans_algo = self.kedans_algo(nums)

        max_from_other = sum(nums) -  (-1 * self.kedans_algo([-1 * i for i in nums]))
        if max_from_other == 0:
            return max_from_kedans_algo
        return max(max_from_kedans_algo, max_from_other)
