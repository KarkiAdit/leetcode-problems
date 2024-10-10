# 76. Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size_s = len(s)
        size_t = len(t)
        if size_s < size_t:
            return ""
        chars_in_t = {}
        map_length = 0
        for char in t:
            if char not in chars_in_t:
                chars_in_t[char] = -1
                map_length += 1
            else:
                chars_in_t[char] -= 1
        p1 = 0
        count = 0
        curr_min_length = float('inf')
        curr_min_window = ""
        for p2 in range(size_s):
            curr = s[p2]
            # Update the character count in the hash map
            if curr in chars_in_t:
                chars_in_t[curr] += 1
                # Update the window count if needed
                if chars_in_t[curr] == 0:
                    count += 1
            # When we hit a valid window
            if count == map_length:
                # Squeeze the window to remove any unnecessary duplicates of p1
                while p1 < p2:
                    curr_p1 = s[p1]
                    if curr_p1 in chars_in_t:
                        if chars_in_t[curr_p1] > 0:
                            chars_in_t[curr_p1] -= 1
                        else:
                            break
                    p1 += 1
                # Update the min window if needed
                if p2 - p1 + 1 < curr_min_length:
                    curr_min_window = s[p1: p2 + 1]
                    curr_min_length = p2 - p1 + 1
                # Move p1 to a valid next start and reduce the window count
                chars_in_t[s[p1]] -= 1
                p1 += 1
                count -= 1
                while p1 < p2 and s[p1] not in chars_in_t:
                    p1 += 1
                
        return curr_min_window
                
                

        