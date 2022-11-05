link : https://leetcode.com/problems/baseball-game/description/

Solution :
class Solution(object):
    def calPoints(self, operations):
        stack = []
        for i in operations:
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == 'C':
                del stack[-1]
            else:
                stack.append(int(i))
        
        return sum(stack)
