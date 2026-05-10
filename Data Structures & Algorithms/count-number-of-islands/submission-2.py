class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs(i - 1, j) #arriba
            dfs(i + 1, j) #abajo
            dfs(i, j - 1) #izquierda
            dfs(i, j + 1) #derecha


        num_islands = 0

        for i in range(m):
            for j in range(n):
                print(i, j, grid[i][j])
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands

        