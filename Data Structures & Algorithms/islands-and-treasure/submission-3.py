from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        INF = 2147483647

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))

        while q:
            current_r, current_c, current_dist = q.popleft()

            for dr, dc in DIRS:
                nr, nc, n_dist = current_r + dr, current_c + dc, current_dist + 1

                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == INF and
                    (nr, nc) not in visited):
                    grid[nr][nc] = n_dist
                    q.append((nr, nc, n_dist))
                    visited.add((nr, nc))

        

                

        