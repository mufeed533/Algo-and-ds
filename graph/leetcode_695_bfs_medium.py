"https://leetcode.com/problems/max-area-of-island/description/"

import collections

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            area = 1
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))

            directions = [[1,0], [-1,0], [0, 1], [0, -1]]

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col+ dc
                    if (r in range(ROWS) and c in range(COLS)) and (grid[r][c] == 1) and ((r,c) not in visited):
                        area += 1
                        visited.add((r,c))
                        queue.append((r,c))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, bfs(r,c))
        return max_area
