# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each string and store in a map
        anagram_map = {}
        for idx in range(len(strs)):
            curr = ''.join(sorted(strs[idx]))
            if curr not in anagram_map:
                anagram_map[curr] = [strs[idx]]
            else:
                anagram_map[curr].append(strs[idx])
        # Loop through the map and construct a return list
        anagram_list = []
        for processed_strs in anagram_map.values():
            anagram_list.append(processed_strs)
        return anagram_list

# Optimized O(m * n) solution

class Solution:
    def equiv_char_tuple(self, s: str) -> tuple:
        # Create a frequency count for each character in the string
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - 97] += 1
        return tuple(char_count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagram_map = {}
        # Loop through the strings and group them by character frequency tuple
        for s in strs:
            s_tupled = self.equiv_char_tuple(s)
            grouped_anagram_map[s_tupled].append(s)

        return list(grouped_anagram_map.values())

