"""
    Given a 2-D grid of characters board and a string word, 
    return true if the word is present in the grid, 
    otherwise return false.
    For the word to be present it must be possible to form it 
    with a path in the board with horizontally or vertically neighboring cells. 
    The same cell may not be used more than once in a word.

    Notes:
        - grid 2D board + str word
        - 4 DIRS
        - same cell cannot be used more than once
    
    Entender el problema:
        - ¿puedo trazar un camino conectando (arriba, abajo, izq, der) cuyas letras
        en orden deletreen word? (sin pisar una celda dos veces)

    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ],
    word = "CAT"

    - word[0] = "C" -> posibles comienzos. 


"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRS = ([-1, 0], [1, 0], [0, -1], [0, 1])
        visited = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            
            if not (0 <= r < ROWS and
                    0 <= c < COLS and
                    board[r][c] == word[i] and
                    (r, c) not in visited):
                    return False
                
            visited.add((r, c))

            for dr, dc in DIRS:
                nr, nc = dr + r, dc + c

                if dfs(nr, nc, i + 1):
                    return True
                
            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False        