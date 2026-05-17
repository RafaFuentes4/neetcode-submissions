from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == '0'):
                return

            visited.add((r, c))

            for dr, dc in DIRS:
                bfs(r + dr, c + dc)

        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and
                    grid[r][c] == '1'):
                    bfs(r, c)
                    islands += 1
        
        return islands

