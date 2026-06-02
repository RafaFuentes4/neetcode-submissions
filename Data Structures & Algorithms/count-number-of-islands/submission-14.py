from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                current_r, current_c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = current_r + dr, current_c + dc

                    if (0 <= nr < ROWS and
                        0  <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and
                    grid[r][c] == '1'):
                    bfs(r, c)
                    islands += 1
        
        return islands

        