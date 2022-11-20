"https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/"

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) -1
        min_value = nums[0]

        while l <= r:
            mid = (l+r) // 2
            min_value = min(min_value, nums[mid])

            if nums[r] <= nums[mid]:
                l = mid +1
            else:
                r = mid - 1
        return min_value
