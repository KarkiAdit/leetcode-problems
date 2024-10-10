# 48. Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for x in range(size // 2):
            for y in range(x, size - x - 1):
                curr_pos = matrix[x][y]
                next_x = y
                next_y = size - x - 1
                while next_x != x or next_y != y:
                    temp = matrix[next_x][next_y]
                    matrix[next_x][next_y] = curr_pos
                    curr_pos = temp
                    temp_2 = next_x
                    next_x = next_y
                    next_y = size - temp_2 - 1
                matrix[x][y] = curr_pos
        
