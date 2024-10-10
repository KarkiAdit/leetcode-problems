# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        pref = ""
        for j in range(len(strs[0])):
            if j < len(strs[1]) and strs[0][j] == strs[1][j]:
                pref += strs[0][j]
            else:
                break
        for i in range(2, len(strs)):
            curr_pref = ""
            for j in range(len(pref)):
                if j < len(strs[i]) and strs[i][j] == pref[j]:
                    curr_pref += pref[j]
            pref = curr_pref
        return pref

        