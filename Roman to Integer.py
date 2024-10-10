# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = roman_map[s[-1]]
        curr = num
        for idx in range(len(s) - 2, -1, -1):
            prev = roman_map[s[idx]]
            if prev < curr:
                num -= prev
            else:
                num += prev
                curr = prev
        return num





        