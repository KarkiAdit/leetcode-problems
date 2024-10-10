# Valid Palindrome

class Solution:
    def validate_char(self, c):
        return (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57)
    def isPalindrome(self, s: str) -> bool:
        # Lowercase every character in the string
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            char_l = s[left: left + 1] 
            char_r = s[right: right + 1]
            if self.validate_char(char_l) and self.validate_char(char_r):
                if char_l == char_r:
                    left += 1
                    right -= 1
                    continue
                return False
            elif self.validate_char(char_l):
                right -= 1
            else:
                left += 1
        return True
        