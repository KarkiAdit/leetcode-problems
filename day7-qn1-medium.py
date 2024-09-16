# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            # Check if middle falls in the lower increasing region
            if nums[middle] <= nums[right]:
                if nums[left] >= nums[right]:
                    if middle - 1 >= 0 and nums[middle - 1] >= nums[right]:
                        return nums[middle]
                    right = middle - 1
                else:
                    return nums[left]
            else:
                if nums[left] >= nums[right]:
                    if middle + 1 < len(nums) and nums[middle + 1] <= nums[right]:
                        return nums[middle + 1]
                    left = middle + 1
                else:
                    return nums[right]
        # Handle array with only one element
        return nums[0]
                