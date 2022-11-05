Link : https://leetcode.com/problems/fibonacci-number/description/

Solution:
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1):
            return n

        return self.fib(n-1) + self.fib(n-2)
