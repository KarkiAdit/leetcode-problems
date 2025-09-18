# Consider a rat placed at position (0, 0) in an n x n square matrix mat[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

# The matrix contains only two possible values:

# 0: A blocked cell through which the rat cannot travel.
# 1: A free cell that the rat can pass through.

class Solution:
    di = [+1, 0, 0, -1]
    dj = [0, -1, +1, 0]
    direction_chars = "DLRU"

    def solve(self, m, n, visited, i, j, possible_paths, path_so_far):
        # if we have reached the destination
        if i == n - 1 and j == n - 1:
            possible_paths.append(path_so_far)
            return

        for l in range(4):
            new_i = i + self.di[l]
            new_j = j + self.dj[l]

            # Check if the move is valid
            if (
                0 <= new_i < n
                and 0 <= new_j < n
                and not visited[new_i][new_j]
                and m[new_i][new_j] == 1
            ):
                # Mark the current cell as visited before the recursive call
                visited[i][j] = True
                
                # Recursive call with updated coordinates and path
                self.solve(m, n, visited, new_i, new_j, possible_paths, path_so_far + self.direction_chars[l])
                
                # un-mark the current cell as visited
                visited[i][j] = False

    def findPath(self, m, n):
        possible_paths = []
        visited = [[False] * n for _ in range(n)]
        
        # Check if the start is blocked
        if m[0][0] == 1:
            self.solve(m, n, visited, 0, 0, possible_paths, "")

        if not possible_paths:
            return ["-1"]
        
        possible_paths.sort()
        return possible_paths