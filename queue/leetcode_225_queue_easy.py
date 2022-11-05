Link : https://leetcode.com/problems/implement-stack-using-queues/

Solution:

class MyStack(object):

    def __init__(self):
        self.q1 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

        for i in range(len(self.q1) - 1):
            self.q1.append(self.q1.pop(0))
        

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not len(self.q1)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
