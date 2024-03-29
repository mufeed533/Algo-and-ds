"https://leetcode.com/problems/design-a-leaderboard/description/"

import heapq

class Leaderboard:

    def __init__(self):
        self.scores = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = score + self.scores.get(playerId, 0)
        

    def top(self, K):
        return sum(heapq.nlargest(K, self.scores.values()))
        

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
