class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return 0

        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, ROWS * COLS - 1

        while left <= right:
            mid = (left + right) // 2

            i = mid // COLS
            j = mid % COLS

            if matrix[i][j] > target:
                right = mid - 1
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                return True
        
        return False


        