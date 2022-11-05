Link : https://leetcode.com/problems/min-stack/description/

Solution: 
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_val = []
    
    def update_min_val(self, val):
        if not self.min_val:
            self.min_val.append(val) 
        else:
            self.min_val.append(min(self.min_val[-1], val))

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.update_min_val(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_val.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val[-1]
