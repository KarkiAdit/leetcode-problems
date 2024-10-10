# 200. Number of Islands

# DFS soltuion
class Solution:
    def find_path(self, matrix, indices, x, y):   
        x_cond = 0 <= x < self.rows
        y_cond = 0 <= y < self.cols
        if not x_cond or not y_cond or (x, y) in indices or matrix[x][y] == '0':
            return
        # Update the path indices
        indices.add((x, y))
        arr = [(0,-1), (0,1), (1,0), (-1,0)]
        for each in arr:
             self.find_path(matrix, indices, x + each[0], y + each[1])

    def numIslands(self, grid: List[List[str]]) -> int:
        matrix = grid
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        indices = set() # A set of tuples
        islands = 0
        for x in range(self.rows):
            for y in range(self.cols):
                if matrix[x][y] == '1' and (x, y) not in indices:
                    self.find_path(matrix, indices, x, y)
                    islands += 1
        return islands
        