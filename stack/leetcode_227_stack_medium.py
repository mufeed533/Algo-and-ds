"https://leetcode.com/problems/basic-calculator-ii/description/"

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operator = "+"
        curr_num = 0

        operators = {"+", "-", "*", "/"}
        numbers = {str(i) for i in range(10)}

        for index in range(len(s)):
            char = s[index]
            if char in numbers:
                curr_num = curr_num * 10 + int(char)
            if char in operators or index == (len(s) - 1):
                if operator == "+":
                    stack.append(curr_num)
                elif operator == "-":
                    stack.append(-curr_num)
                elif operator == "*":
                    stack[-1] *= curr_num
                elif operator == "/":
                    if stack[-1] >=0 :
                        stack[-1] //= curr_num
                    else:
                        stack[-1] = -(-stack[-1]//curr_num)
                curr_num = 0
                operator = char
        return sum(stack)
