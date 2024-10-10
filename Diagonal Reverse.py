# 498. Diagonal Traverse

# Easy solution using O(max(m, n) * max(m, n)) space
class Solution:
    def reverse(self, arr):
        p1 = 0
        p2 = len(arr) - 1
        while p1 < p2:
            temp = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = temp
            p1 += 1
            p2 -= 1


    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        x = len(mat)
        y = len(mat[0])
        diagonal_map = {}
        for i in range(x):
            for j in range(y):
                if i + j not in diagonal_map:
                    diagonal_map[i+j] = []
                diagonal_map[i+j].append(mat[i][j])
        
        # Traverse throught every element in the map and get the array
        diagonaled_arr = []
        for idx_sum in range(0, x + y - 1):
            arr = diagonal_map[idx_sum]
            if idx_sum % 2 == 0:
                self.reverse(arr)
            diagonaled_arr.extend(arr)
        return diagonaled_arr

# Optimized O(1) space solution
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        no_of_rows = len(mat)
        no_of_cols = len(mat[0])
        diagonaled = []
        x = 0
        y = 0
        while x < no_of_rows and y < no_of_cols:
            # For spiral moving up
            while x >= 0 and y < no_of_cols:
                diagonaled.append(mat[x][y])
                x -= 1
                y += 1
            # Change the direction of spiral and adjust start indices
            if y < no_of_cols:
                x += 1
            else:
                x += 2
                y -= 1
            # Check if we have hit the end of matrix
            if x == no_of_rows or y == no_of_cols:
                break
            # For spiral moving down
            while x < no_of_rows and y >= 0:
                diagonaled.append(mat[x][y])
                x += 1
                y -= 1
            # Change the direction of spiral and adjust start indices
            if x < no_of_rows:
                y += 1
            else:
                x -= 1
                y += 2
        return diagonaled
            




        