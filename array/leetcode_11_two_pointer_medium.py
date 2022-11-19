"https://leetcode.com/problems/container-with-most-water/description/"

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0, len(height) - 1

        max_water_amount = 0

        while l < r:
            max_water_amount = max(max_water_amount, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water_amount





