# 14. Longest Common Prefix

class Solution:
    def evaluate_prefix(self, s1: str, s2: str) -> str:
        curr_pref = ""
        idx = 0
        while idx < len(s1) and idx < len(s2) and s1[idx: idx + 1] == s2[idx: idx + 1]:
            curr_pref += s1[idx: idx + 1]
            idx += 1
        return curr_pref

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.evaluate_prefix(prefix, strs[i])
        return prefix

        