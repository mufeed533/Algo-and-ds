"https://leetcode.com/problems/insert-delete-getrandom-o1/description/"

import random
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        is_exist = val in self.numMap
        if not is_exist:
            self.numList.append(val)
            self.numMap[val] = len(self.numList) - 1
        return not is_exist
        

    def remove(self, val: int) -> bool:
        is_exist = val in self.numMap
        if is_exist:
            idx = self.numMap[val]
            last_val = self.numList[-1]
            self.numList[idx] = last_val
            self.numList.pop()
            self.numMap[last_val] = idx
            del self.numMap[val]

        return is_exist

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
