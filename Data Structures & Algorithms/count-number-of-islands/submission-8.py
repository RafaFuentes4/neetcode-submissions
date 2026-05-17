from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()

                for dr, dc in DIRS:
                    nr, nc = curr_r + dr, curr_c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
        
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == '1' and (r, c) not in visited):
                    bfs(r, c)
                    islands += 1
                
        return islands

        
        