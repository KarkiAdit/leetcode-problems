# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size == 1:
            return s
        max_len = 1
        curr_max_str = s[0]
        for p1 in range(size - 1):
            for p2 in range(p1 + 1, size):
                curr_subs = s[p1: p2 + 1]
                if p2 - p1 + 1 > max_len and curr_subs == curr_subs[::-1]:
                    max_len = p2 - p1 + 1
                    curr_max_str = curr_subs
        return curr_max_str
        