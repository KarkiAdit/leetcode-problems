# Qn. Smallest Window in a string containing all the characters of another string

class Solution:
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
        p_count = {}
        for char in p:
            if char not in p_count:
                p_count[char] = 1
            else:
                p_count[char] += 1
        start = 0
        min_len = float('inf')
        min_start = 0
        count = 0
        window_count = {}
        for end in range(len(s)):
            char = s[end]
            window_count[char] = window_count.get(char, 0) + 1
            # If the current character is needed in p and we have the right amount, increase count
            if char in p_count and window_count[char] <= p_count[char]:
                count += 1
            # When all characters of p are found in the current window
            while count == len(p):
                # Update the smallest window
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start
                # Try to shrink the window from the left
                left_char = s[start]
                window_count[left_char] -= 1
                # If the left character is in p and now the window lacks enough of it, decrease count
                if left_char in p_count and window_count[left_char] < p_count[left_char]:
                    count -= 1
                start += 1
        # Return the smallest window or -1 if no valid window is found
        if min_len == float('inf'):
            return "-1"
        else:
            return s[min_start:min_start + min_len]