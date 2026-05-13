from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            visited.add((start_r, start_c))
            area = 1

            while q:
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = dr + r, dc + c

                    if(0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1

            return area
                    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
        
        
        
        """
        1. Importo deque.
        2. Identifico los sources (uno o varios).
        3. Inicializo:
        - queue con los sources + distancia 0
        - visited con los sources
        4. Loop:
        while queue:
            saco (pos, dist) con popleft
            si es target → return dist
            para cada vecino válido y no visitado:
                lo marco visited
                lo enqueueo con dist + 1
        5. Si salgo del loop sin return → return -1 (o lo que pida).
        """