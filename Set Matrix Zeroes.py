# 73. Set Matrix Zeroes

# Unoptimized O(mn) solution and O(m + n) space
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

# Optimized O(mn) time and O(m + n) space solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols  = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        # Mark corresponding 0th row and 0th col as zero
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_has_zero = True
                    if j == 0:
                        first_col_has_zero = True
                    # Assign corresponding ith row for 0th col and jth col for 0th row as zero
                    matrix[i][0] = matrix[0][j] = 0
        # Assign zero to non-0th row and col
        for i in range(1, n_rows):
            for j in range(1, n_cols):
                # Use the 0th marker
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Handle 0th row
        if first_row_has_zero:
            for j in range(n_cols):
                matrix[0][j] = 0
        # Handle 0th col
        if first_col_has_zero:
            for i in range(n_rows):
                matrix[i][0] = 0
            

        


        