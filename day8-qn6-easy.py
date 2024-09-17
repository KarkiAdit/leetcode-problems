# 242. Valid Anagram

# Non-optimized
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        unique_char_map = {}
        for char in s:
            if char not in unique_char_map:
                unique_char_map[char] = 1
            else:
                unique_char_map[char] += 1
        for char in t:
            if char not in unique_char_map:
                return False
            else:
                unique_char_map[char] -= 1
                if unique_char_map[char] < 0:
                    return False
        return True
