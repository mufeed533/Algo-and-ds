"https://leetcode.com/problems/design-an-ordered-stream/description/"

class OrderedStream:

    def __init__(self, n: int):
        self.arr = [0 for i in range(n)]
        self.last_idx = None
        
    def insert(self, idKey, value):
        self.arr[idKey - 1] = value
        if self.last_idx is None:
            i = 0
        else:
            i = self.last_idx + 1
        result = []
        while i < len(self.arr) and self.arr[i] != 0:
            result.append(self.arr[i])
            self.last_idx = i
            i += 1

        return result



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
