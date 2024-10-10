# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_map = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        roman_equiv = ""
        a = 10
        b = 5
        c = 1
        while num != 0:
            r = num % 10
            if r >= 1 and r <= 3:
                roman_equiv = symbol_map[c] * r + roman_equiv
            elif r >= 4 and r <= 5:
                roman_equiv = symbol_map[c] * (5 - r) + symbol_map[b] + roman_equiv
            elif r >= 6 and r <= 8:
                roman_equiv = symbol_map[b] + symbol_map[c] * (r % 5)  + roman_equiv
            elif r == 9:
                roman_equiv = symbol_map[c] * (10 - r) + symbol_map[a] + roman_equiv
            a *= 10
            b *= 10
            c *= 10
            num //= 10
        return roman_equiv
            

