# 20. Valid Parenthesis

class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        close_brackets_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for char in s:
            if char == "{" or char == "[" or char == "(":
                open_brackets.append(char)
            elif len(open_brackets) > 0 and close_brackets_map[char] == open_brackets[-1]:
                open_brackets.pop()
            else:
                return False
        if len(open_brackets) == 0:
            return True
        return False

        