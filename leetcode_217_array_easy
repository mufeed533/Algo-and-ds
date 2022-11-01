Link : https://leetcode.com/problems/contains-duplicate/submissions/834521774/

Solution : 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False
