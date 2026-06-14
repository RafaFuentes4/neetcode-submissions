"""
    You are given a 2-D matrix grid. Each cell can have one of three possible values:
     - 0 representing an empty cell
     - 1 representing a fresh fruit
     - 2 representing a rotten fruit
    Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, 
    then the fresh fruit also becomes rotten.

    Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. 
    If this state is impossible within the grid, return -1.

    1. Notes:

        - ¿




"""

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        
        visited = set()
        queue = deque()

        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH:
                    fresh += 1
                elif grid[r][c] == ROTTEN:
                    queue.append((r, c))
                    visited.add((r, c))

        if fresh == 0:
            return 0

        minutes = 0
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRS:
                    nr, nc = dr + r, dc + c

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == FRESH and
                        (nr, nc) not in visited):
                        visited.add((nr, nc))
                        fresh -= 1
                        queue.append((nr, nc))
                
            minutes += 1

        return minutes if fresh == 0 else -1
            




        