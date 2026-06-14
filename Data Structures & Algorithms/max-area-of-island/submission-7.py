

"""
    1. Notas:

    You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
    An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
    The area of an island is defined as the number of cells within the island.
    Return the maximum area of an island in grid. If no island exists, return 0.

        - grid[i] is either a 0 (representing water) or 1 (representing land)
        - group of 1's connected horizontally or vertically (4 dirs) -> DIRS = ([-1, 0], [1, 0], [0, -1], [0, 1])
        - area = number of cells within the island
            - Return the maximum area of an island in grid
            - If no island exists, return 0
    
    2. Preguntas
        - ¿puedo modificar el grid? no
        - ¿grid vacía? no
        - ¿celdas solo 0 o 1? si
    
    3. Entradas y salidas (Input outputs):

        def max_area_of_island(self, grid: List[List[int]]) -> int:
            Input: grid: matrix of 1s and 0s
            Output: int: maximum area of an island in grid

    4. Ejemplos:

        Ex1: matrix 4 x 5

            0 1 1 0 1
            1 0 1 0 1    [A]
            0 1 1 0 1
            0 1 0 0 0
            
            [A] -> area = 1
            [B] -> area = 6 --- MAX -> return 6
            [C] -> area = 3

        Ex2: all water

            0 0 0 0
            0 0 0 0
            0 0 0 0

            -> return 0

        Ex3: one land cell

            1
        
            -> return 1

    5. Enfoques:

        - DFS recursivo + set visitados. T: O(R x C) S: O(R x C)
        - BFS iterativo + set visitados. T: O(R x C) S: O(R x C)
"""

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def flood(r: int, c: int) -> int:
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visited):
                return 0
            
            visited.add((r, c))

            return 1 + flood(r - 1, c) + flood(r + 1, c) + flood(r, c - 1) + flood(r, c + 1)

        def island_area_bfs(start_r: int, start_c: int) -> int:
            queue = deque()
            queue.append((start_r, start_c))
            visited.add((start_r, start_c))

            area = 0
            while queue:
                r, c = queue.popleft()
                area += 1

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if (nr >= 0 and nr < ROWS and
                        nc >= 0 and nc < COLS and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return area    
            
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, island_area_bfs(r, c))
        return max_area        