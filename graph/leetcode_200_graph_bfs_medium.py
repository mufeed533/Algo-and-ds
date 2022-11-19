"https://leetcode.com/problems/number-of-islands/description/"

import collections

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        island_count = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col+dc
                    if (r in range(ROWS) and c in range(COLS)) and (r,c) not in visited and grid[r][c] == '1':
                        queue.append((r,c))
                        visited.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    island_count += 1        


        return island_count
