"https://leetcode.com/problems/minimum-health-to-beat-game/"

class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        return sum(damage) + 1 - min(max(damage), armor)
