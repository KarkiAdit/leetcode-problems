# 73. Set Matrix Zeroes

# Unoptimized O(mn) solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols  = len(matrix[0])
        zeros_map = {
            "rows": set(),
            "cols": set(),
        }
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    zeros_map["rows"].add(i)
                    zeros_map["cols"].add(j)
        # Make necessary rows zero
        for i in range(n_rows):
            if i in zeros_map["rows"]:
                for j in range(n_cols):
                    matrix[i][j] = 0
        # Make necessary cols zero
        for j in range(n_cols):
            if j in zeros_map["cols"]:
                for i in range(n_rows):
                    matrix[i][j] = 0

        