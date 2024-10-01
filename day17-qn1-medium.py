# 79. Word Search

class Solution:
    def find_word_path(self, x, y, idx, visited) -> bool:
        if idx == self.word_length:
            return True
        if not (0 <= x < self.rows) or not (0 <= y < self.cols) or self.board[x][y] != self.chars[idx] or (x, y) in visited:
            return False
        move_factors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for factor in move_factors:
            prev = (x, y)
            visited.add(prev)
            curr_path = self.find_word_path(x + factor[0], y + factor[1], idx + 1, visited)
            if curr_path:
                return True
            visited.remove(prev)
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.word_length = len(word)
        self.chars = list(word)
        visited = set() # A set of tuples
        for x in range(self.rows):
            for y in range(self.cols):
                idx = 0
                if self.find_word_path(x, y, 0, visited):
                    return True
        return False
        