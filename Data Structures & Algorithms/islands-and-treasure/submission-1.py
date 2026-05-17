from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 2147483647 and
                    (nr, nc) not in visited):
                    grid[nr][nc] = dist + 1
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))

        