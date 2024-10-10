# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elems = set()
        for num in nums:
            if num in elems:
                return True
            else:
                elems.add(num)
        return False
        