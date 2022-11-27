"https://leetcode.com/problems/decode-string/description/"

class Solution:
    def decodeString(self, s):
        stack = []

        # numbers can be multiple digit

        for i in s:
            if i == "]":
                char = ""
                while stack:
                    top_char = stack.pop() 
                    if top_char == "[":
                        break
                    char = top_char + char
                counter = ""
                while stack:
                    number = stack.pop() 
                    if not number.isdigit():
                        stack.append(number)
                        break
                    counter = number + counter
                counter = int(counter)
                char = char * counter
                for i in char:
                    stack.append(i)
            else:
                stack.append(i)

        return "".join(stack)
