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
    
# In O(1) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not equal, it's not an anagram
        if len(s) != len(t):
            return False
        count = [0] * 26
        # Increment counter for s
        for char in s:
            count[ord(char) - ord('a')] += 1
        # Decrement counter for t
        for char in t:
            idx = ord(char) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False    
        return True

