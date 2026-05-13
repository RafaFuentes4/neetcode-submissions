from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        visited = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1 

        minutes = 0

        while q:
            r, c, mi = q.popleft()

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    grid[nr][nc] == 1 and (nr, nc) not in visited):
                    q.append((nr, nc, mi + 1))
                    visited.add((nr, nc))

                    minutes = max(minutes, mi + 1)
                    fresh -= 1
                
        return minutes if fresh == 0 else -1



        """
            deque
            visited set

            multisource start

        """
        