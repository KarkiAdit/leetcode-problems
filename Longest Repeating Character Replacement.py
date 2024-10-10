# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        if size == 0:
            return 0
        p1 = 0 
        char_in_s = {}
        curr_max_count = 0
        window_size = 0
        for p2 in range(size):
            curr = s[p2]
            if curr in char_in_s:
                char_in_s[curr] += 1
            else:
                char_in_s[curr] = 1
            curr_max_count = max(curr_max_count, char_in_s[curr])
            # Adjust left pointer and counts if number of replacements exceeds k
            if (p2 - p1 + 1) - curr_max_count > k:
                char_in_s[s[p1]] -= 1
                p1 += 1
            # Update the max length of substring so far
            window_size = max(window_size, p2 - p1 + 1)
        return window_size


            


        