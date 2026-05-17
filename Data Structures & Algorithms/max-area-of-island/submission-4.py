from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def bfs(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visited):
                return 0
            
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            result = 1

            while queue:
                curr_r, curr_c = queue.popleft()

                for dr, dc in DIRS:
                    nr, nc = curr_r + dr, curr_c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        result += 1
            return result




        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and (r, c) not in visited):
                    result = max(result, bfs(r, c))

        return result




        