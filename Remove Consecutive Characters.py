# Qn. Remove consecutive characters
# Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        if len(S) == 1:
            return S
        p1 = 0
        non_consecutive_str = ""
        while p1 < len(S):
            p2 = p1 + 1
            while p2 < len(S) and S[p1: p1 + 1] == S[p2: p2 + 1]:
                p2 += 1
            non_consecutive_str += S[p1: p1 + 1]
            p1 = p2
        return non_consecutive_str