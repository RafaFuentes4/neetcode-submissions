import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        ROWS, COLS = len(grid), len(grid[0])
        
        q = collections.deque()
        visited = set()

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        while q:
            r, c, distance = q.popleft()
            
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] == 2147483647 and (nr, nc) not in visited):
                    q.append((nr, nc, distance + 1))
                    visited.add((nr, nc))
                    grid[nr][nc] = distance + 1







