link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Solution : 

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1

        i = 0
    
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1
