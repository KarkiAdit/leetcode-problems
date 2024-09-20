# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        x , y = 0, -1
        direction = 1
        spiraled = []
        while rows > 0 and cols > 0:
            # Move right or left based on the direction
            for _ in range(cols):
                y += direction
                spiraled.append(matrix[x][y])
            # Shrink the height
            rows -= 1
            # Move top or bottom based on the direction
            for _ in range(rows):
                x += direction
                spiraled.append(matrix[x][y])
            # Shrink the width
            cols -= 1
            # Change the direction
            direction *= -1
        return spiraled



            



    
        