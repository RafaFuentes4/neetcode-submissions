from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()
        visited = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    fresh += 1
                elif grid[r][c] == ROTTEN:
                    q.append((r, c))
                    visited.add((r, c))

        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                current_r, current_c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = current_r + dr, current_c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == FRESH and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1

            minutes += 1


        return minutes if fresh == 0 else -1

        

        