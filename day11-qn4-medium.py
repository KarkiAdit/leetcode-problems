# 3. Longest Substring without Repeating Characters

# Unoptimized O(n) space solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        p1 = 0
        char_in_s = set()
        window_size = 0
        for p2 in range(size):
            curr = s[p2]
            if curr not in char_in_s:
                char_in_s.add(curr)
            else:
                while p1 < size and s[p1] != curr:
                    char_in_s.remove(s[p1])
                    p1 += 1
                p1 += 1
            window_size = max(window_size, p2 - p1 + 1)
        return window_size
            

        