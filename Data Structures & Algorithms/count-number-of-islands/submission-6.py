from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        islands = 0
        visited = set()

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            visited.add((start_r, start_c))

            while q:
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                
        return islands


        """
        """
        