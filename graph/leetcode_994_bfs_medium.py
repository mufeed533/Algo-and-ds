"https://leetcode.com/problems/rotting-oranges/description/"

import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        fresh_oranges, minutes = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue and fresh_oranges >0:
            for orange in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                        queue.append((r,c))
                        fresh_oranges -= 1
                        grid[r][c] = 2
            minutes += 1
        
        if fresh_oranges:
            return -1

        return minutes
        




