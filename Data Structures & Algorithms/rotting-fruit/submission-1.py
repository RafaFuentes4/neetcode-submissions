from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        visited = set()
        fresh = 0

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                current_r, current_c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = current_r + dr, current_c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            
            minutes += 1

        return minutes if fresh == 0 else -1    
        
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                current_r, current_c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = current_r + dr, current_c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == "1" and (r, c) not in visited):
                    bfs(r, c)
                    islands += 1
        return islands
"""
        
        