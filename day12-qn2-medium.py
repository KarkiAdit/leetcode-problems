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

        