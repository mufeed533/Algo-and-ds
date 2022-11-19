"https://leetcode.com/problems/shortest-path-in-binary-matrix/description/"

import collections
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return  -1

        visited = set()
        queue = collections.deque()
        queue.append((0,0, 1))
        visited.add((0,0))

        directions = [[1,0], [-1,0], [0, 1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]

        while queue:
            row, col, shortest_length = queue.popleft()
            for dr, dc in directions:
                r,c = row + dr, col + dc
                if r == ROWS and c == COLS:
                    return shortest_length
                if r in range(ROWS) and c in range(COLS) and not grid[r][c] and (r,c) not in visited:
                    queue.append((r,c, shortest_length+1))
                    visited.add((r,c))
        return -1




