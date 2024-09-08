# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Handle when empty list is given
        if not nums:
            return [-1, -1]
        # Map new element from left to right with their index
        elem_map = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in elem_map:
                return[elem_map[diff], idx]
            else:
                elem_map[nums[idx]] = idx
        
        return [-1, -1]

        