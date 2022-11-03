link : https://leetcode.com/problems/climbing-stairs/submissions/835785671/

Solution:
class Solution(object):
    def climbStairs(self, n, mapping=None):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if not mapping:
            mapping = {}
         
        count = 0

        if n >= 1:
            if (n - 1) not in mapping:
                mapping[n-1] = self.climbStairs(n -1, mapping)
            count += mapping.get(n-1)
        if n >= 2:
            if (n - 2) not in mapping:
                mapping[n-2] = self.climbStairs(n -2, mapping)
            count += mapping[n-2]
        return count

Using Fibonacci (true dynamic programming):
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one 
