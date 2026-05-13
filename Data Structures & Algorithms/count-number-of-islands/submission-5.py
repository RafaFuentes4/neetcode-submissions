from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0

        def bfs(start_r, start_c):
            q = deque()
            q.append((start_r, start_c))
            visited.add((start_r, start_c))

            while q:
                r, c = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in visited and grid[nr][nc] == "1"):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands


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
        