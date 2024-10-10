# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            # If middle is pointing to correct target
            if nums[middle] == target:
                return middle
            # If target is in left side
            elif target >= nums[0]:
                if nums[middle] < target and nums[middle] >= nums[0]:
                    left = middle + 1
                else:
                    right = middle - 1
            # If target is in right side
            else:
                if nums[middle] > target and nums[middle] < nums[0]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1

                    
                 





        