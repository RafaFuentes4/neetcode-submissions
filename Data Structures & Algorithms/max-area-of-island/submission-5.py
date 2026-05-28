from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        max_area = 0

        def bfs(r, c):
            nonlocal max_area

            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                current_r, current_c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = current_r + dr, current_c + dc

                    if ((nr, nc) not in visited and
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
                
            max_area = max(max_area, area)

        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visited and
                    grid[r][c] == 1):
                    bfs(r, c)
        
        return max_area
        