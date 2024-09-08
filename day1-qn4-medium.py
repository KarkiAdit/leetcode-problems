# 7. Reverse Integer

class Solution:
    def check_outside_32bit(self, num: int) -> bool:
        return num < -1 * (2 ** 31) or num > (2 ** 31) - 1

    def reverse(self, x: int) -> int: 
        # Make a positive copy of x
        copy_x = abs(x)
        rev = 0
        while copy_x != 0:
            rev = rev * 10 + copy_x % 10
            copy_x //= 10
        # Choose correct sign to return 
        if x < 0:
            rev *= -1
        # Check if outside 32-bit range
        if self.check_outside_32bit(rev):
            return 0
        else:
            return rev