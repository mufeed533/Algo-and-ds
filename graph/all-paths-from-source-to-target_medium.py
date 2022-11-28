"https://leetcode.com/problems/all-paths-from-source-to-target/description/"

from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph):
        queue = deque()
        queue.append([0])
        final = len(graph) - 1
        result = []

        while queue:
            node = queue.popleft()
            if node[-1] == final:
                result.append(node)
            else:
                for i in graph[node[-1]]:
                    queue.append(node + [i])
        
        return result



