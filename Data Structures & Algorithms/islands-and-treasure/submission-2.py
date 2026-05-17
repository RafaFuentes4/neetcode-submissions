from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == INF):
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))

        