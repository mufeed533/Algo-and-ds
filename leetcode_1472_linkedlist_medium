Link : https://leetcode.com/problems/design-browser-history/description/
Solution:

class HistoryNode(object):
    def __init__(self, url=None, next=None, prev = None):
        self.url = url,
        self.next = next
        self.prev = prev

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = HistoryNode(url=homepage)
        self.curr = self.head
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        curr_node = self.curr
        self.curr.next = HistoryNode(url=url)
        self.curr = self.curr.next
        self.curr.prev = curr_node
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
        return self.curr.url[0]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.url[0]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
