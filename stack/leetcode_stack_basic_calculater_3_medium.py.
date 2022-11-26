"https://leetcode.com/problems/basic-calculator-iii/"

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        curr_num = 0
        op = "+"
        
        def helper(operator, num):
            if operator == "+":
                stack.append(num)
            elif operator == "-":
                stack.append(-num)
            elif operator == "*":
                stack.append(stack.pop() * num)
            elif operator == "/":
                stack.append(int(stack.pop() / num))
        
        for index in range(len(s)):
            char = s[index]
            if char.isdigit():
                curr_num = curr_num*10 + int(char)
            else:
                if char == "(":
                    stack.append(op)
                    op = "+"
                elif char in ("+", "-", "*", "/", ")"):
                    helper(op, curr_num)
                    if char == ")":
                        curr_num = 0 
                        while isinstance(stack[-1], int):
                            curr_num += stack.pop()
                        op = stack.pop()
                        helper(op, curr_num)
                    op = char
                curr_num = 0
        helper(op, curr_num)
        return sum(stack)
