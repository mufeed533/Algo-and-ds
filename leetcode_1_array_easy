Link : https://leetcode.com/problems/two-sum/

Solution:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        s = {}
        for i, val in enumerate(nums):
            look_for = target - val
            if look_for in s:
                return [i, s[look_for]]
            else:
                s[val] = i
        return False
